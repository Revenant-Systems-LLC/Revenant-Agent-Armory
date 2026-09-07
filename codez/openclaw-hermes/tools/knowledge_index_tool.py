"""
Knowledge Index Tool - Runtime integration of INDEX.md knowledgebase

Provides three main classes:
1. IndexMetadataParser - Parses INDEX.md and generates JSON cache
2. IndexSearchEngine - Implements FTS keyword search
3. SemanticRanker - Intent-based ranking via Claude Haiku

Main API: knowledge_index(action, query, context, limit)
"""

import json
import sqlite3
import re
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class IndexItem:
    """Single item in INDEX (skill, agent, tool, etc.)"""
    name: str
    path: str
    directory: str
    description: str = ""
    category: Optional[str] = None
    file_count: Optional[int] = None
    role: Optional[str] = None


class IndexMetadataParser:
    """Parses INDEX.md and generates INDEX_metadata.json cache"""

    def __init__(self, index_path: str):
        self.index_path = Path(index_path)
        self.metadata = {
            "version": datetime.now().isoformat(),
            "directories": {},
            "search_index": {"keywords": {}, "triggers": {}}
        }

    def parse(self) -> Dict[str, Any]:
        """Parse INDEX.md and return metadata structure"""
        if not self.index_path.exists():
            raise FileNotFoundError(f"INDEX.md not found at {self.index_path}")

        with open(self.index_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract Directory Overview table first to get file counts
        dir_overview = self._extract_directory_overview(content)

        # Parse each directory section
        dir_sections = self._split_directory_sections(content)

        for dir_name, section_content in dir_sections.items():
            dir_info = dir_overview.get(dir_name, {})
            items = self._parse_directory_section(dir_name, section_content)

            self.metadata["directories"][dir_name] = {
                "description": dir_info.get("description", ""),
                "file_count": dir_info.get("file_count", len(items)),
                "purpose": dir_info.get("purpose", ""),
                "items": items
            }

            # Build search index for this directory
            self._build_search_index(dir_name, items)

        return self.metadata

    def _extract_directory_overview(self, content: str) -> Dict[str, Dict[str, Any]]:
        """Extract the Directory Overview table"""
        overview = {}

        # Find the Directory Overview section
        overview_match = re.search(
            r'## Directory Overview\s*\n\s*\|\s*Directory.*?\n(.*?)\n\n---',
            content,
            re.DOTALL
        )

        if not overview_match:
            return overview

        table_content = overview_match.group(1)

        # Parse table rows (skip header separator)
        rows = [r.strip() for r in table_content.split('\n') if r.strip() and not r.startswith('|---')]

        for row in rows:
            # Parse: | dirname/ | count | purpose |
            parts = [p.strip() for p in row.split('|')[1:-1]]
            if len(parts) >= 3:
                dir_name = parts[0]
                try:
                    file_count = int(parts[1].replace(',', ''))
                except (ValueError, IndexError):
                    file_count = 0
                purpose = parts[2] if len(parts) > 2 else ""

                overview[dir_name] = {
                    "file_count": file_count,
                    "purpose": purpose
                }

        return overview

    def _split_directory_sections(self, content: str) -> Dict[str, str]:
        """Split content into directory sections"""
        sections = {}

        # Find all ## dirname/ sections
        pattern = r'## ([a-z0-9\-_.]+/)\n\n(.*?)(?=\n## |\Z)'
        matches = re.finditer(pattern, content, re.DOTALL)

        for match in matches:
            dir_name = match.group(1)
            section_content = match.group(2)
            sections[dir_name] = section_content

        return sections

    def _parse_directory_section(self, dir_name: str, content: str) -> List[Dict[str, str]]:
        """Parse items from a directory section"""
        items = []

        # Skip the description line (e.g., "**92 files** — Agent...")
        content_lines = content.split('\n')

        # Find tables and lists
        in_table = False
        table_rows = []

        for line in content_lines:
            line = line.strip()

            # Table markers
            if line.startswith('|') and not line.startswith('|---'):
                in_table = True
                table_rows.append(line)
            elif in_table and line.startswith('|---'):
                continue
            elif in_table and (line.startswith('|') or line == ''):
                if line.startswith('|'):
                    table_rows.append(line)
            else:
                if table_rows:
                    items.extend(self._parse_table_rows(table_rows, dir_name))
                    table_rows = []
                    in_table = False

                # Parse backtick-delimited lists (e.g., `item1`, `item2`, ...)
                if '`' in line:
                    items.extend(self._parse_backtick_list(line, dir_name))

        if table_rows:
            items.extend(self._parse_table_rows(table_rows, dir_name))

        return items

    def _parse_table_rows(self, rows: List[str], dir_name: str) -> List[Dict[str, str]]:
        """Parse items from table rows"""
        items = []

        # Skip header rows - look for separator and header content
        start = 0
        for i, row in enumerate(rows):
            if '|---' in row:
                start = i + 1
                break
            first_parts = [p.strip().lower() for p in row.split('|')[1:-1]]
            if any(h in first_parts for h in ['directory', 'agent', 'file', 'category', 'item', 'name', 'file', 'items']):
                start = i + 1

        for row in rows[start:]:
            if not row.strip():
                continue

            parts = [p.strip() for p in row.split('|')[1:-1]]

            if len(parts) >= 1:
                item_name = parts[0].strip('`').strip()
                description = parts[1].strip('`').strip() if len(parts) > 1 else ""

                # Filter out artifacts and empty names
                if item_name and item_name not in ['.md', '.py', '.json', '.txt', '.docx'] and not item_name.startswith('|'):
                    items.append({
                        "name": item_name,
                        "path": f"{dir_name}{item_name}",
                        "directory": dir_name,
                        "description": description
                    })

        return items

    def _parse_backtick_list(self, line: str, dir_name: str) -> List[Dict[str, str]]:
        """Parse items from backtick-delimited list (e.g., `item1`, `item2`)"""
        items = []

        # Find all `item` patterns
        pattern = r'`([^`]+)`'
        matches = re.finditer(pattern, line)

        for match in matches:
            item_name = match.group(1)
            items.append({
                "name": item_name,
                "path": f"{dir_name}{item_name}",
                "directory": dir_name,
                "description": ""
            })

        return items

    def _build_search_index(self, dir_name: str, items: List[Dict[str, str]]):
        """Build search index (keywords and triggers) for items"""
        for item in items:
            name = item.get("name", "").lower()
            description = item.get("description", "").lower()

            # Add keywords
            for word in (name + " " + description).split():
                word = re.sub(r'[^\w\-]', '', word)
                if len(word) > 2:
                    if word not in self.metadata["search_index"]["keywords"]:
                        self.metadata["search_index"]["keywords"][word] = []
                    self.metadata["search_index"]["keywords"][word].append(item["path"])

            # Add triggers (common discovery patterns)
            if dir_name == "skills/":
                for trigger in name.split('-'):
                    if trigger and len(trigger) > 2:
                        self.metadata["search_index"]["triggers"][trigger] = item["path"]

    def save_to_json(self, output_path: str) -> str:
        """Save metadata to JSON file"""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2)

        return str(output_file)


class IndexSearchEngine:
    """Full-text search engine using SQLite FTS5"""

    def __init__(self, metadata: Dict[str, Any]):
        self.metadata = metadata
        self.db_path = ":memory:"
        self.conn = None
        self._init_fts_index()

    def _init_fts_index(self):
        """Initialize FTS5 index in memory"""
        self.conn = sqlite3.connect(self.db_path)
        cursor = self.conn.cursor()

        # Create FTS5 virtual table - simplified structure
        cursor.execute("""
            CREATE VIRTUAL TABLE index_fts USING fts5(
                name,
                path,
                directory,
                description
            )
        """)

        # Populate with all items
        for dir_name, dir_info in self.metadata.get("directories", {}).items():
            for item in dir_info.get("items", []):
                cursor.execute("""
                    INSERT INTO index_fts(name, path, directory, description)
                    VALUES (?, ?, ?, ?)
                """, (
                    item.get("name", ""),
                    item.get("path", ""),
                    item.get("directory", ""),
                    item.get("description", "")
                ))

        self.conn.commit()

    def search(self, query: str, limit: int = 10) -> List[Dict[str, str]]:
        """Search using FTS5 keyword search"""
        cursor = self.conn.cursor()

        # Escape FTS special characters
        query = re.sub(r'["\-*:]', '', query).strip()

        # Split query into terms and search
        terms = query.split()
        fts_query = " OR ".join(f'"{term}"' for term in terms if term)

        try:
            cursor.execute(f"""
                SELECT path, name, directory, description, rank(index_fts) as relevance
                FROM index_fts
                WHERE index_fts MATCH ?
                ORDER BY relevance ASC
                LIMIT ?
            """, (fts_query, limit))

            results = []
            for row in cursor.fetchall():
                if row[0]:  # Only include valid results
                    results.append({
                        "path": row[0],
                        "name": row[1] if row[1] else "",
                        "directory": row[2] if row[2] else "",
                        "description": row[3] if row[3] else "",
                        "relevance_score": abs(float(row[4])) if row[4] else 0.5
                    })

            return results
        except Exception as e:
            # Fall back to simple LIKE search
            try:
                cursor.execute("""
                    SELECT path, name, directory, description
                    FROM index_fts
                    WHERE name LIKE ? OR description LIKE ? OR path LIKE ?
                    ORDER BY name
                    LIMIT ?
                """, (f"%{query}%", f"%{query}%", f"%{query}%", limit))

                results = []
                for row in cursor.fetchall():
                    if row[0]:
                        results.append({
                            "path": row[0],
                            "name": row[1] if row[1] else "",
                            "directory": row[2] if row[2] else "",
                            "description": row[3] if row[3] else "",
                            "relevance_score": 0.5
                        })

                return results
            except Exception:
                return []

    def browse(self, directory: Optional[str] = None) -> Dict[str, Any]:
        """Browse directory or list all directories"""
        if directory is None:
            # Return all directories
            return {
                "directories": list(self.metadata.get("directories", {}).keys()),
                "total_directories": len(self.metadata.get("directories", {}))
            }

        # Return items in a specific directory
        dir_info = self.metadata.get("directories", {}).get(directory, {})
        return {
            "directory": directory,
            "description": dir_info.get("description", ""),
            "file_count": dir_info.get("file_count", 0),
            "items": dir_info.get("items", [])
        }

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()


class CatalogUnifier:
    """Unifies search results from INDEX and catalog.json"""

    def __init__(self, catalog_path: Optional[str] = None):
        self.catalog_path = catalog_path or Path(__file__).parent.parent / "data" / "catalog.json"
        self.catalog = self._load_catalog()

    def _load_catalog(self) -> Dict[str, Any]:
        """Load catalog.json"""
        try:
            if self.catalog_path and Path(self.catalog_path).exists():
                with open(self.catalog_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception:
            pass
        return {"skills": []}

    def merge_results(self, index_results: List[Dict[str, str]], limit: int = 10) -> List[Dict[str, str]]:
        """
        Merge INDEX results with catalog skills, deduplicating and ranking.
        Returns merged list up to limit.
        """
        seen = set()
        merged = []

        # Add INDEX results first (higher priority as INDEX is the canonical source)
        for result in index_results:
            key = (result.get("name", "").lower(), result.get("directory", ""))
            if key not in seen:
                merged.append(result)
                seen.add(key)

        # Find related skills from catalog
        if self.catalog.get("skills"):
            for skill in self.catalog["skills"]:
                skill_name = skill.get("name", "").lower()
                # Check if this skill is already in merged results
                if not any(skill_name in r.get("name", "").lower() for r in merged):
                    # Check if skill matches any of the INDEX result names
                    for idx_result in index_results:
                        idx_name = idx_result.get("name", "").lower()
                        if any(word in skill_name for word in idx_name.split('-') if len(word) > 2):
                            merged.append({
                                "name": skill.get("name", ""),
                                "path": skill.get("path", ""),
                                "directory": "skills/",
                                "description": skill.get("description", ""),
                                "category": skill.get("category", ""),
                                "tags": skill.get("tags", []),
                                "source": "catalog"
                            })
                            seen.add((skill_name, "skills/"))
                            break

        return merged[:limit]


class SemanticRanker:
    """Intent-based ranking using Claude Haiku for semantic understanding"""

    def __init__(self, metadata: Dict[str, Any]):
        self.metadata = metadata

    def rank_by_intent(self, candidates: List[Dict[str, str]], intent: str) -> List[Dict[str, str]]:
        """
        Rank candidates by user intent using Claude Haiku semantic understanding.
        Returns candidates sorted by relevance to the user's intent.
        Falls back to original order if API call fails.
        """
        if not candidates or not intent:
            return candidates

        try:
            import anthropic

            # Format candidates for ranking
            candidate_text = "\n".join([
                f"{i+1}. {c.get('name', '')} ({c.get('directory', '')}) - {c.get('description', '')}"
                for i, c in enumerate(candidates[:10])  # Limit to top 10 for API efficiency
            ])

            prompt = f"""You are a knowledge base assistant. Given a user's intent and a list of available tools/agents/skills, rank the candidates by relevance to the intent.

User Intent: {intent}

Available Items:
{candidate_text}

Return ONLY a comma-separated list of item numbers (1-based) in order of relevance. Example: "3,1,5,2,4"
Do not explain, do not include names, just the numbers."""

            client = anthropic.Anthropic()
            message = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=100,
                messages=[{"role": "user", "content": prompt}]
            )

            # Parse ranking from response
            ranking_str = message.content[0].text.strip()
            ranking = [int(x.strip()) - 1 for x in ranking_str.split(',') if x.strip().isdigit()]

            # Reorder candidates based on ranking
            ranked = []
            for idx in ranking:
                if 0 <= idx < len(candidates):
                    ranked.append(candidates[idx])

            # Add any candidates not in ranking (fallback)
            for i, candidate in enumerate(candidates):
                if i not in ranking and candidate not in ranked:
                    ranked.append(candidate)

            return ranked

        except Exception:
            # Fallback: return candidates as-is if API call fails
            return candidates


def knowledge_index(
    action: str,
    query: Optional[str] = None,
    context: Optional[str] = None,
    limit: int = 10,
    metadata_path: Optional[str] = None
) -> Dict[str, Any]:
    """
    Main API for knowledge index access.

    Actions:
    - browse: List categories or items in a category
    - search: Keyword search across INDEX
    - suggest: Intent-based suggestions (Phase 2)
    - detail: Get full description for an item
    - discover: Explore related capabilities

    Args:
        action: One of browse, search, suggest, detail, discover
        query: Search query or directory name
        context: Optional context for intent-based suggestions
        limit: Max results to return
        metadata_path: Path to INDEX_metadata.json (if None, will parse INDEX.md)

    Returns:
        Dictionary with results for the requested action
    """

    # Determine metadata path
    if metadata_path is None:
        # Try to load from default location, otherwise parse INDEX.md
        default_metadata = Path(__file__).parent.parent / "data" / "INDEX_metadata.json"
        if default_metadata.exists():
            with open(default_metadata, 'r') as f:
                metadata = json.load(f)
        else:
            # Parse INDEX.md
            index_file = Path(__file__).parent.parent / "INDEX.md"
            parser = IndexMetadataParser(str(index_file))
            metadata = parser.parse()
            # Save for future use
            default_metadata.parent.mkdir(parents=True, exist_ok=True)
            parser.save_to_json(str(default_metadata))
    else:
        with open(metadata_path, 'r') as f:
            metadata = json.load(f)

    # Initialize search engine and unifier
    engine = IndexSearchEngine(metadata)
    unifier = CatalogUnifier()

    try:
        if action == "browse":
            return engine.browse(query)

        elif action == "search":
            if not query:
                return {"error": "query required for search action"}
            results = engine.search(query, limit)
            # Merge with catalog results for unified discovery
            merged = unifier.merge_results(results, limit)
            return {
                "action": "search",
                "query": query,
                "result_count": len(merged),
                "results": merged
            }

        elif action == "detail":
            if not query:
                return {"error": "query required for detail action"}
            results = engine.search(query, limit=1)
            if results:
                return {
                    "action": "detail",
                    "item": results[0]
                }
            return {"error": f"Item '{query}' not found"}

        elif action == "suggest":
            # Intent-based suggestions using semantic ranking
            if not query:
                return {"error": "query required for suggest action"}
            results = engine.search(query, limit)
            # Merge with catalog for comprehensive suggestions
            merged = unifier.merge_results(results, limit)
            # Rank by intent using Claude Haiku
            ranker = SemanticRanker(metadata)
            ranked = ranker.rank_by_intent(merged, query)
            return {
                "action": "suggest",
                "intent": query,
                "result_count": len(ranked),
                "suggestions": ranked
            }

        elif action == "discover":
            # Find related capabilities across INDEX and catalog
            if not query:
                return {"error": "query required for discover action"}
            results = engine.search(query, limit)
            merged = unifier.merge_results(results, limit)
            return {
                "action": "discover",
                "seed": query,
                "related": merged
            }

        else:
            return {"error": f"Unknown action: {action}"}

    finally:
        engine.close()
