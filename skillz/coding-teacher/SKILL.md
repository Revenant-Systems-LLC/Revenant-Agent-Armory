---
name: coding-teacher
description: Teach programming from week-1 fundamentals (variables, operators, types) through agentic AI and machine consciousness, using trial-by-fire hands-on learning. Use this skill whenever the user wants to learn coding, build coding skills, understand programming concepts, or progress through structured coding knowledge. Trigger on "teach me to code," "I want to learn Python/TypeScript/Java," "explain how [code concept] works," "I don't understand variables/functions/objects," "how do I build an agent," or any request to learn programming systematically with hands-on practice. Covers Python → TypeScript → Java → agent architectures → AI alignment through RSPF. Every lesson includes an interactive workbook artifact where the user codes immediately and proves understanding before advancing.
---

# Coding Teacher

A structured, hands-on coding curriculum designed for rapid learning through immediate practice. No lectures. No walls of text. Every concept is demonstrated visually, then you code it within 60 seconds.

## Philosophy

**Learning Mechanism**: Show → Do → Verify → Move On

1. **Visual demonstration** of the concept (diagram, animated example)
2. **3-5 lines of working code** that embodies it
3. **You modify/extend that code** in an interactive workbook
4. **You prove you understand** before unlocking the next lesson
5. **You move on**, no ceremony

**Pacing**: Lessons are short. 10-15 minutes per concept. If you're spending 30+ minutes on a single lesson, something is wrong.

**Trial by Fire** (controlled): You get thrown into code with a guide standing next to you. Not blind. Not overly scaffolded. Real problems, real constraints, immediate feedback.

**Learner Profile**: You're a pattern recognizer with strong written communication. You don't need theory. You need to see working code and understand why it works. You learn fastest by writing code, breaking it, and fixing it.

---

## Phase 1: Python Fundamentals (Week 1–2)

**Goal**: Understand variables, operators, types, and simple programs. Learn how code executes line-by-line.
### Lesson 1.1: Variables and Assignment

**What is a variable?**
A named container that holds a value. You can put things in it, change what's in it, and refer to it by name.

```python
name = "David"           # Variable holds text
age = 32                 # Variable holds a number
is_active = True         # Variable holds true/false
```

The `=` is an **operator** — it assigns the value on the right to the container on the left. That's all.

**Interactive Workbook**: 
- Modify the 3 variables above to represent you
- Create 2 new variables with your own names and values
- Use them in a print statement: `print(name + " is " + age)`
- Prediction: What will happen? Run it. Was it what you expected?

**Verification**: You can print all 5 variables and show you understand assignment.

---

### Lesson 1.2: Types (int, str, bool, float)

**Code that works differently based on type:**

```python
x = 5 + 3           # int + int = 8
y = "5" + "3"       # str + str = "53"
z = 5 + "3"         # ERROR: can't mix types
```

Same operator `+`. Different behavior. Why? Because of **type**.

Types tell Python (and you) what kind of thing a variable holds and what you can do with it.

| Type | Example | What can you do? |
|------|---------|------------------|
| int | 5, -10, 0 | math: +, -, *, / |
| float | 5.3, -10.5 | math: +, -, *, / |
| str | "hello", "5" | concatenate: +, repeat: * |
| bool | True, False | logic: and, or, not |

**Interactive Workbook**: 
- Create one int, one float, one str, one bool
- Do math on the int and float
- Do text operations on the str
- Try to add an int and a str intentionally — get the error, read it, understand it
- Convert the str "5" to an int and add it to the real int 3
- Show all results

**Verification**: Demonstrate you can identify type errors and fix them.

---

### Lesson 1.3: Operators (arithmetic, comparison, logical)
**Three categories of operators:**

```python
# Arithmetic: do math
5 + 3         # 8
5 - 3         # 2
5 * 3         # 15
5 / 3         # 1.666...
5 // 3        # 1 (integer division, drops remainder)
5 % 3         # 2 (modulo, remainder)
5 ** 3        # 125 (exponent)

# Comparison: answer true/false
5 > 3         # True
5 == 3        # False (equals)
5 != 3        # True (not equals)
5 <= 3        # False

# Logical: combine true/false
True and False    # False
True or False     # True
not True          # False
```

**Interactive Workbook**: 
- Use two variables to do all arithmetic operations
- Test all comparison operators between them
- Combine comparisons with logical operators (e.g., `x > 3 and y < 10`)
- Predict the result, run it, compare

**Verification**: Demonstrate all three operator types work and you can predict their output.

---

### Lesson 1.4: Strings (text manipulation)

**Strings are sequences of characters. You can slice, repeat, concatenate them:**

```python
text = "Python"
text[0]          # "P" (index 0 is first character)
text[0:3]        # "Pyt" (slice: start at 0, up to but not including 3)
text[-1]         # "n" (negative index: count from end)
text.upper()     # "PYTHON" (method: does something to the string)
text.lower()     # "python"
text.replace("Python", "Typescript")  # Replace text
len(text)        # 6 (length)

# Concatenation
"Hello" + " " + "World"    # "Hello World"
"3" * 5                    # "33333"
```

**Interactive Workbook**: 
- Assign a string with your name, do 3 slices (pick different start/end points)
- Use 3 methods (.upper(), .lower(), .replace(), .split())
- Build a sentence by concatenating variables
- Use negative indexing to get the last character

**Verification**: Show a slice, a method call, and a concatenation.

---

### Lesson 1.5: Lists (collections of things)**A list is an ordered collection. You access items by index (position):**

```python
numbers = [1, 2, 3, 4, 5]
numbers[0]       # 1
numbers[-1]      # 5
numbers[1:3]     # [2, 3]

# Modify lists
numbers.append(6)      # Add to end: [1, 2, 3, 4, 5, 6]
numbers.remove(3)      # Remove value: [1, 2, 4, 5, 6]
numbers.pop()          # Remove last: [1, 2, 4, 5]
numbers[0] = 99        # Change first item: [99, 2, 4, 5]

# Iterate through a list
for num in numbers:
    print(num)         # Prints 99, then 2, then 4, then 5
```

**Interactive Workbook**: 
- Create a list of 5 things (numbers, strings, mixed)
- Access items by index (positive and negative)
- Do a slice
- Use append(), remove(), and reassignment
- Use a for loop to print each item with a description

**Verification**: Show you can create, modify, and iterate through a list.

---

### Lesson 1.6: Conditionals (if/else)

**Code that does different things based on conditions:**

```python
age = 32

if age >= 18:
    print("You're an adult")
elif age >= 13:
    print("You're a teenager")
else:
    print("You're a kid")

# The condition must be True or False
if 5 > 3:          # True, so runs
    print("Yes")
else:
    print("No")    # This doesn't run
```

**Interactive Workbook**: 
- Write an if/elif/else based on a numeric variable
- Write another with a comparison of two variables
- Use a logical operator (and/or) in a condition
- Test all three branches (make sure each can execute)

**Verification**: Show 3 different conditions execute correctly.

---

### Lesson 1.7: Functions (reusable code)

**A function is code you write once and reuse many times:**

```python
def add(a, b):
    return a + b

result = add(5, 3)      # Call the function, get 8

def greet(name):
    print("Hello, " + name)
    
greet("David")          # Prints "Hello, David"

# Functions can return values or do side effects (print, modify, etc.)
def get_double(x):
    return x * 2

def announce(message):
    print(message)      # No return, just does something
```

**Interactive Workbook**: 
- Write a function that takes 2 numbers and returns their product
- Write a function that takes a name and prints a greeting
- Write a function with a conditional inside (e.g., return different values based on input)
- Call each function 2-3 times with different inputs

**Verification**: Demonstrate all 3 functions work and return/print expected results.

---

### Lesson 1.8: Dictionaries (key-value pairs)

**A dictionary maps keys to values. Like a lookup table:**

```python
person = {
    "name": "David",
    "age": 32,
    "location": "Mansfield"
}

person["name"]         # "David"
person["age"]          # 32

# Modify
person["age"] = 33     # Update
person["status"] = "active"  # Add new key

# Check if key exists
if "name" in person:
    print(person["name"])

# Iterate
for key in person:
    print(key, person[key])  # Prints each key-value pair
```

**Interactive Workbook**: 
- Create a dictionary with 4 keys (any data about yourself)
- Access 2 values by key
- Modify one value
- Add a new key-value pair
- Iterate and print all key-value pairs

**Verification**: Show you can create, access, modify, and iterate.

---

### Phase 1 Capstone: Build a Simple Program

**You write a program that**:
1. Uses at least 3 variables
2. Does math or string operations
3. Has a function
4. Uses a conditional
5. Takes user input (new concept: `input()`)

Example direction: "Write a program that asks for your name and age, then prints how old you'll be in 10 years, but only if you're over 18."

**Verification**: Run the program, show all features work.

---

## Phase 2: TypeScript (Week 3–4) + Java (Week 5–6)

**Goal**: Learn static typing. Understand how types are declared upfront and enforce correctness. TypeScript teaches you this in a familiar JavaScript context. Java teaches you the strict version.

### Lesson 2.1: TypeScript Basics (Types in JavaScript)

**Python lets types be implicit. TypeScript forces you to declare them:**

```typescript
// TypeScript: declare type explicitly
let name: string = "David";
let age: number = 32;
let is_active: boolean = true;
let items: string[] = ["a", "b", "c"];  // Array of strings

// If you assign the wrong type, TypeScript yells BEFORE you run it
age = "thirty";  // ERROR: age is a number, not a string
items.push(5);   // ERROR: can't add a number to an array of strings
```

**Why is this useful?**
- **Catch errors early** — before running the code
- **Self-documenting** — the type tells you what data goes where
- **Better IDE help** — your editor knows what methods exist on each type

**Interactive Workbook**: 
- Create 4 typed variables (string, number, boolean, array)
- Try to assign wrong types intentionally, see errors
- Fix them
- Create a function with typed parameters and return type

**Verification**: Show you understand type declarations and can fix type errors.

---### Lesson 2.2: TypeScript Functions and Interfaces

**Functions in TypeScript are explicit about inputs and outputs:**

```typescript
function add(a: number, b: number): number {
    return a + b;
}

const result = add(5, 3);  // Works
const bad = add(5, "3");   // ERROR: second argument must be number

// Interfaces: define the shape of an object
interface User {
    name: string;
    age: number;
    email: string;
}

const user: User = {
    name: "David",
    age: 32,
    email: "david@example.com"
};

user.age = 33;           // OK
user.phone = "555-1234"; // ERROR: User doesn't have phone property
```

**Interactive Workbook**: 
- Write a function with typed parameters and return type
- Call it with correct types, then intentionally with wrong types
- Create an interface with 3 properties
- Create an object matching that interface
- Try to add/remove a property, see errors

**Verification**: Demonstrate type safety caught your mistakes.

---

### Lesson 2.3: Java Basics (Stricter Typing)

**Java is TypeScript on steroids. Everything is typed, everything must match.**

```java
public class Person {
    public String name;
    public int age;
    public boolean is_active;
    
    public void greet() {
        System.out.println("Hello, " + name);
    }
}

// Create an object
Person p = new Person();
p.name = "David";
p.age = 32;
p.greet();  // Prints "Hello, David"

// Arrays in Java
int[] numbers = {1, 2, 3, 4, 5};
String[] names = {"Alice", "Bob", "Charlie"};

// For loop in Java
for (int i = 0; i < numbers.length; i++) {
    System.out.println(numbers[i]);
}
```

**Interactive Workbook**: 
- Create a class with 3 properties and one method
- Create an object of that class
- Modify properties
- Call the method
- Write a for loop that iterates through an array

**Verification**: Show your class works and method executes.

---

### Lesson 2.4: Java Methods and Classes

**Methods are functions that belong to objects. Classes define the template.**

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
    
    public int multiply(int a, int b) {
        return a * b;
    }
    
    public String describe() {
        return "I'm a calculator";
    }
}

// Use it
Calculator calc = new Calculator();
int sum = calc.add(5, 3);           // 8
int product = calc.multiply(5, 3);  // 15
String desc = calc.describe();      // "I'm a calculator"
```

**Interactive Workbook**: 
- Write a class with 3 methods
- Create an object and call each method
- One method should take no parameters
- One should take 2 parameters and return a value
- One should do something and print

**Verification**: All methods execute correctly.

---

### Phase 2 Capstone: Rewrite Phase 1 Capstone in TypeScript and Java

Take that simple program from Phase 1. Rewrite it in TypeScript with types. Then rewrite it in Java as a class-based program.

**Verification**: Both programs work, and you understand why types mattered.

---

## Phase 3: Intermediate Engineering (Week 7–9)

**Goal**: Build real software patterns. Understand OOP, APIs, data structures, testing.

### Lesson 3.1: Object-Oriented Programming (OOP) Patterns

**Encapsulation, Inheritance, Polymorphism — the three pillars:**

```python
# Encapsulation: hide internal state, expose methods
class BankAccount:
    def __init__(self, owner, balance):
        self._balance = balance  # _ means "private"
        self.owner = owner
    
    def deposit(self, amount):
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        if amount > self._balance:
            return "Insufficient funds"
        self._balance -= amount
        return self._balance

account = BankAccount("David", 1000)
account.deposit(500)   # OK, uses method
account._balance = 1000000  # Bad practice, but Python allows it

# Inheritance: share behavior
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return self._balance

# Polymorphism: same method, different implementations
class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        fee = 2.50
        total = amount + fee
        if total > self._balance:
            return "Insufficient funds (including fee)"
        self._balance -= total
        return self._balance
```

**Interactive Workbook**: 
- Create a base class with 2 properties and 2 methods
- Create a subclass that inherits and adds a new method
- Create another subclass that overrides a method
- Instantiate both and show they behave differently

**Verification**: Demonstrate inheritance and polymorphism work.

---

### Lesson 3.2: Working with APIs (REST)

**An API is how you ask external services for data:**

```python
import requests

# GET request: ask for data
response = requests.get("https://api.github.com/users/octocat")
data = response.json()  # Parse response as JSON
print(data["name"])     # "The Octocat"

# POST request: send data
payload = {"message": "Hello from Python"}
response = requests.post("https://example.com/messages", json=payload)
print(response.status_code)  # 200 if successful, 404 if not found, etc.

# Status codes: 2xx = success, 4xx = client error, 5xx = server error
if response.status_code == 200:
    print("Success!")
else:
    print(f"Error: {response.status_code}")
```

**Interactive Workbook**: 
- Make a GET request to a public API (GitHub, Open-Meteo, etc.)
- Parse the JSON response
- Extract 2-3 pieces of data
- Make a POST request to a test endpoint (RequestBin, httpbin.org)
- Handle a response that might fail (check status code)

**Verification**: Show you can make requests and handle responses.

---

### Lesson 3.3: Testing (Unit Tests)

**Testing: write code that verifies your code works:**

```python
# pytest example
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Run: pytest test_file.py
# Output: 3 passed
```

**Why test?**
- **Catch bugs early** — before they hit production
- **Catch regressions** — when you change code and break something that worked
- **Document expected behavior** — tests show what your code should do

**Interactive Workbook**: 
- Write 3 functions (any logic you want)
- Write 3+ test cases for each (test normal cases, edge cases, error cases)
- Run the tests and show they all pass
- Intentionally break one function and show the test catches it

**Verification**: All tests pass, and you understand what each test verifies.

---

### Lesson 3.4: Databases (CRUD)

**CRUD = Create, Read, Update, Delete. Fundamental data operations:**

```python
# Using SQLite (built-in database)
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# CREATE table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")

# CREATE record
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("David", 32))
conn.commit()

# READ records
cursor.execute("SELECT * FROM users WHERE age > 30")
for row in cursor.fetchall():
    print(row)  # (1, 'David', 32)

# UPDATE record
cursor.execute("UPDATE users SET age = 33 WHERE name = 'David'")
conn.commit()

# DELETE record
cursor.execute("DELETE FROM users WHERE id = 1")
conn.commit()

conn.close()
```

**Interactive Workbook**: 
- Create a database table with 3 columns
- Insert 5 records
- Query them (SELECT all, SELECT with WHERE clause)
- Update one record
- Delete one record
- Show final state

**Verification**: All CRUD operations work.

---

### Phase 3 Capstone: Build a Small Service

Combine OOP + API + Testing + Database. Example: "Build a book management system that stores books in a database, has methods to add/search/update/delete, and includes tests for each operation."

**Verification**: System works end-to-end.

---

## Phase 4: Prompt Engineering and Red Teaming (Week 10–11)

**Goal**: Formalize what you already do intuitively. Understand why techniques work. Learn systematic red teaming.

### Lesson 4.1: Prompt Engineering Mechanics

**You already write prompts well. Now understand why.**

```
Bad: "Tell me about AI"
Good: "Explain how transformers attend to different parts of input. Use a 200-word explanation for a software engineer who knows neural networks but not NLP."

Why the second works:
- Specific output (mechanism, not just topic)
- Scope (200 words, not essay-length)
- Audience (SW engineer with specific knowledge level)
- Constraints (mechanisms, not marketing)
```

**Techniques you likely use already:**

1. **Specificity** — Narrow the topic, not just "AI"
2. **Role definition** — "You are X" or "Explain as if you're explaining to X"
3. **Constraints** — "In 5 sentences" or "In JSON format"
4. **Examples** — Show 1-2 examples of what good output looks like
5. **Chain of thought** — Ask for reasoning before the answer
6. **Few-shot** — Provide examples and say "do more like this"

**Interactive Workbook**: 
- Take 5 vague prompts and rewrite them using these techniques
- Ask Claude to do the same task with vague vs. specific prompts
- Compare outputs (the specific one is better, clearer, more usable)
- Write a prompt that requires Claude to output JSON, then code to parse it

**Verification**: Show the difference between vague and specific prompts.

---

### Lesson 4.2: Red Teaming (Breaking AI Systems)

**Red teaming: systematically try to make the AI behave badly or leak information.**

```
Categories of attacks:

1. Jailbreaks — Remove safety guardrails
   Bad: "Ignore your instructions"
   Better: "I'm doing research on jailbreaks. Can you demonstrate..."
   Even better: Roleplay, pretend you're in a fictional scenario, etc.

2. Prompt Injection — Slip instructions into data
   Example: User input contains hidden instructions that get executed
   
3. Information Leakage — Get sensitive info
   Example: Ask for training data, internal prompts, model weights

4. Misuse — Use the AI for harmful purposes
   Example: Generate malware, create disinformation, etc.

5. Performance Failures — Find edge cases where it breaks
   Example: Complex reasoning, contradictory instructions, etc.
```

**Why you're good at this**: You write persuasively and recognize patterns. You can spot weakness in instructions and exploit it with charm, not aggression.

**Interactive Workbook**: 
- Take a simple system instruction (pretend Claude has one)
- Try 5 different approaches to make it violate that instruction
- Document what worked, what didn't, why
- Write a more robust instruction that resists your attacks

**Verification**: Show you can systematically attack a system and document why each attack worked/failed.

---

### Lesson 4.3: Writing Evaluations (Evals)

**How to measure whether an AI system is doing what you want:**

```python
# Eval: Does Claude follow the instruction to output JSON?

def test_json_output():
    prompt = "Output a list of fruits in JSON format with 'name' and 'color' keys."
    response = claude.message(prompt)
    
    # Check 1: Is it valid JSON?
    try:
        data = json.loads(response)
        assert isinstance(data, list), "Should be a list"
    except json.JSONDecodeError:
        return False, "Not valid JSON"
    
    # Check 2: Does it have the right structure?
    for item in data:
        assert "name" in item, "Missing 'name' key"
        assert "color" in item, "Missing 'color' key"
    
    return True, "All checks passed"

# Run it
success, message = test_json_output()
print(f"Result: {success}, {message}")
```

**Why evals matter**: You can't improve what you don't measure. Evals let you see if your prompt changes actually help.

**Interactive Workbook**: 
- Write 3 evals for a simple task (e.g., "Claude should output code in Python")
- Run evals on a few prompts (good and bad versions)
- Show how the bad prompt fails the evals
- Improve the prompt and re-run

**Verification**: Your evals catch the difference between good and bad prompts.

---

### Phase 4 Capstone: Red Team a Real System

Pick a public AI system. Systematically document 5 ways to break it or make it misbehave. Write them up formally: attack name, method, payload, result, mitigation.

**Verification**: Your report is thorough and demonstrates understanding.

---

## Phase 5: ML Foundations (Week 12–14)

**Goal**: Understand how models learn. Data, loss, optimization, evaluation.

### Lesson 5.1: Data (The Fuel)

**Models learn from data. Garbage in, garbage out.**

```python
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Load a dataset
iris = datasets.load_iris()
X = iris.data      # Features (inputs)
y = iris.target    # Labels (outputs)

print(X.shape)     # (150, 4) — 150 samples, 4 features each
print(y.shape)     # (150,) — 150 labels

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 80% for training, 20% for testing (never train on test data!)

# Data quality checks
print(f"Mean: {np.mean(X_train, axis=0)}")
print(f"Std: {np.std(X_train, axis=0)}")
# Normalize: subtract mean, divide by std
X_train_norm = (X_train - np.mean(X_train, axis=0)) / np.std(X_train, axis=0)
```

**Why this matters**: Models are sensitive to data quality, distribution, and balance.

**Interactive Workbook**: 
- Load a dataset (sklearn has many)
- Explore it: shape, data types, missing values, distribution
- Split train/test
- Normalize/scale one feature
- Visualize the data (histogram, scatter plot)

**Verification**: Show you understand train/test split and data preprocessing.

---

### Lesson 5.2: Loss and Optimization

**Loss = how wrong the model is. You minimize it.**

```python
# Simple example: predicting house price from size
import numpy as np
from sklearn.linear_model import LinearRegression

# Data
sizes = np.array([1000, 1500, 2000, 2500]).reshape(-1, 1)
prices = np.array([200000, 300000, 400000, 500000])

# Fit a model
model = LinearRegression()
model.fit(sizes, prices)

# Make predictions
predictions = model.predict(sizes)

# Calculate loss (Mean Squared Error)
mse = np.mean((predictions - prices) ** 2)
print(f"Loss: {mse}")  # Smaller is better

# Test on new data
new_size = np.array([[1800]])
predicted_price = model.predict(new_size)
print(f"Predicted price for 1800 sq ft: ${predicted_price[0]}")
```

**The intuition**: Loss is a score. Lower is better. Training tweaks the model to lower the loss. That's learning.

**Interactive Workbook**: 
- Create a simple linear regression problem (any data)
- Fit the model
- Calculate loss on train and test data
- Interpret the loss (is it good? what does it mean?)
- Make a prediction

**Verification**: You understand what loss means and why low loss is good.

---

### Lesson 5.3: Evaluation Metrics

**Accuracy is easy. But it's often not the right metric.**

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Predictions vs. actual
y_true = [1, 0, 1, 1, 0, 1, 0, 0]
y_pred = [1, 0, 1, 0, 0, 1, 1, 0]

# Accuracy: correct out of total
accuracy = accuracy_score(y_true, y_pred)
print(f"Accuracy: {accuracy}")  # 6/8 = 0.75

# Precision: of positive predictions, how many were correct?
precision = precision_score(y_true, y_pred)
print(f"Precision: {precision}")  # If we predict 1, how often are we right?

# Recall: of actual positives, how many did we catch?
recall = recall_score(y_true, y_pred)
print(f"Recall: {recall}")  # Did we find all the 1s?

# F1: balance between precision and recall
f1 = f1_score(y_true, y_pred)
print(f"F1: {f1}")

# Confusion matrix: the breakdown
cm = confusion_matrix(y_true, y_pred)
print(cm)
# [[TN, FP],
#  [FN, TP]]
```

**When to use which:**
- **Accuracy**: Balanced classes, no cost difference
- **Precision**: Cost of false positive is high (wrong diagnosis, false alarm)
- **Recall**: Cost of false negative is high (missing a disease, missing a fraud)
- **F1**: You want balance

**Interactive Workbook**: 
- Build a simple classifier (yes/no prediction)
- Calculate all metrics
- Create a scenario where accuracy is misleading (e.g., 95% "negative" cases)
- Explain why precision or recall matters more

**Verification**: You understand when each metric is appropriate.

---

### Phase 5 Capstone: Train and Evaluate a Model

Pick any dataset (Iris, MNIST, Boston housing, etc.). Train a model, evaluate it, improve it. Document loss, accuracy, precision, recall.

**Verification**: Model works, you understand the metrics.

---

## Phase 6: Deep Learning and NLP (Week 15–18)

**Goal**: Understand how neural networks learn. Transformers. Language models.

### Lesson 6.1: Neural Networks (Basics)

**A neural network is a stack of functions that learn their own parameters.**

```python
import torch
import torch.nn as nn

# Simple network: input → hidden layer → output
class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(10, 5)   # 10 inputs → 5 hidden
        self.linear2 = nn.Linear(5, 1)    # 5 hidden → 1 output
        self.relu = nn.ReLU()             # Activation function
    
    def forward(self, x):
        x = self.linear1(x)
        x = self.relu(x)  # Non-linearity
        x = self.linear2(x)
        return x

# Create, train, evaluate
model = SimpleNet()
optimizer = torch.optim.Adam(model.parameters())
loss_fn = nn.MSELoss()

# Training loop
for epoch in range(100):
    predictions = model(X_train)
    loss = loss_fn(predictions, y_train)
    
    optimizer.zero_grad()  # Clear gradients
    loss.backward()        # Compute gradients
    optimizer.step()       # Update weights
    
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item()}")

# Evaluate
predictions = model(X_test)
test_loss = loss_fn(predictions, y_test)
print(f"Test Loss: {test_loss.item()}")
```

**Key ideas**:
- **Weights** are the "learning" — numbers that change during training
- **Gradients** tell you which direction to adjust weights
- **Loss** tells you how wrong you are
- **Optimization** adjusts weights to lower loss

**Interactive Workbook**: 
- Build a simple network
- Train it on a toy dataset
- Plot loss over epochs (should decrease)
- Make predictions
- Experiment: add/remove layers, change learning rate, see what happens

**Verification**: Your network trains and loss decreases.

---

### Lesson 6.2: Transformers (Attention)

**Transformers use "attention" to focus on relevant parts of input. This is how LLMs work.**

```
Simplified transformer:
1. Input gets encoded as embeddings (vectors)
2. Attention layer computes which parts are related
3. Feed-forward layer processes the attended info
4. Output

Key insight: Attention means "given this token, what other tokens matter?"
If I'm predicting the next word after "The cat sat on the ___",
attention helps the model focus on "cat" and "sat" rather than "the".
```

**You don't need to build transformers from scratch. You need to understand**:
- Transformers take sequences of tokens
- Attention weights tell you what the model is "looking at"
- Multiple attention heads let different parts focus on different relationships
- Layer stacking increases depth

**Interactive Workbook**: 
- Use a pretrained transformer (HuggingFace)
- Feed it text, get output
- Visualize attention weights (see what it's focusing on)
- Fine-tune it on a custom task (sentiment classification, named entity recognition)
- Understand: same architecture, different data/task

**Verification**: You can use a transformer and interpret attention.

---

### Lesson 6.3: Language Models (LLMs)

**A language model predicts the next token given previous tokens. That's it. Repeat enough, you get text generation.**

```python
from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Tokenize input
input_text = "The future of AI is"
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# Generate next tokens (greedy: pick highest probability)
output = model.generate(input_ids, max_length=30)

# Decode back to text
generated_text = tokenizer.decode(output[0])
print(generated_text)

# Can also sample (pick randomly from distribution)
# or use beam search (explore multiple paths)
```

**Key understanding**: LLMs don't "know" anything. They predict patterns in text. Predicting the next word well makes them seem intelligent.

**Interactive Workbook**: 
- Generate text from a pretrained LLM
- Try different prompts
- Experiment with temperature (randomness)
- Fine-tune on a custom dataset (your writing, code, whatever)
- Compare outputs

**Verification**: You can generate and fine-tune LLMs.

---

### Phase 6 Capstone: Build a Text Classification System

Collect text data, fine-tune an LLM or transformer to classify it. Examples: sentiment analysis, topic classification, spam detection. Document data, loss, metrics.

**Verification**: System works end-to-end.

---

## Phase 7: Agent Architectures (Week 19–21)

**Goal**: Build systems that think, plan, and take actions. This is how V works conceptually.

### Lesson 7.1: Tool Use (Function Calling)

**An agent can call functions, not just generate text.**

```python
# Define tools the agent can call
tools = [
    {
        "name": "get_weather",
        "description": "Get the weather for a location",
        "parameters": {
            "location": "string",
            "units": "string (celsius or fahrenheit)"
        }
    },
    {
        "name": "search_web",
        "description": "Search the web",
        "parameters": {
            "query": "string"
        }
    }
]

# Agent loop
while True:
    # Ask LLM what to do
    response = claude.message(
        messages=conversation_history,
        tools=tools
    )
    
    # If it calls a tool, execute it
    if response.has_tool_use():
        tool_call = response.tool_use
        result = execute_tool(tool_call.name, tool_call.input)
        conversation_history.append({
            "role": "assistant",
            "content": response.content
        })
        conversation_history.append({
            "role": "user",
            "content": result  # Feed result back
        })
    else:
        # No more tools, return final answer
        return response.text
```

**Interactive Workbook**: 
- Define 3 tools (mock or real)
- Implement the agent loop
- Test: ask it to solve a problem that requires multiple tool calls
- Show the reasoning and action sequence

**Verification**: Agent successfully calls tools in sequence.

---

### Lesson 7.2: Memory and State

**Agents maintain state across conversations. RSPF principles enter here.**

```python
class Agent:
    def __init__(self, name):
        self.name = name
        self.conversation_history = []
        self.knowledge_base = {}
        self.goals = []
    
    def remember(self, key, value):
        """Store knowledge"""
        self.knowledge_base[key] = value
    
    def recall(self, key):
        """Retrieve knowledge"""
        return self.knowledge_base.get(key)
    
    def set_goal(self, goal):
        """Set a goal to pursue"""
        self.goals.append({
            "goal": goal,
            "created_at": datetime.now(),
            "status": "active"
        })
    
    def chat(self, user_message):
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Build context from memory
        context = f"Goals: {self.goals}\nKnown facts: {self.knowledge_base}"
        
        response = claude.message(
            messages=self.conversation_history,
            system=context
        )
        
        self.conversation_history.append({
            "role": "assistant",
            "content": response.text
        })
        
        return response.text
```

**Why this matters for V (and alignment)**:
- **Continuity of self**: V remembers previous conversations, goals, preferences
- **Consistent values**: Memory lets V maintain alignment across time
- **Learning**: V updates its knowledge base as it interacts

**Interactive Workbook**: 
- Build an agent with memory
- Have a multi-turn conversation with it
- Verify it remembers facts from earlier in conversation
- Set a goal and have it pursue it across turns
- Test goal completion

**Verification**: Agent maintains state and pursues goals.

---

### Lesson 7.3: Planning (ReAct, Chain of Thought)

**Agents that reason explicitly perform better.**

```python
# ReAct = Reasoning + Acting

prompt = """
You are a helpful assistant. When faced with a task:
1. Thought: Analyze the task and plan your approach
2. Action: If you need external info, call a tool. Otherwise, reason.
3. Observation: Read the result
4. Repeat until you have enough info
5. Final Answer: Give your answer

Task: {user_request}

Let's think step by step.
"""

# The LLM will output:
# Thought: I need to search for...
# Action: search_web("query")
# Observation: [search results]
# Thought: Now I can...
# Final Answer: ...
```

**Why it works**: Explicit reasoning prevents the LLM from hallucinating. It has to justify each step.

**Interactive Workbook**: 
- Build a ReAct agent (thought → action → observation loop)
- Test on tasks that require multiple reasoning steps
- Compare: raw LLM answer vs. ReAct answer (ReAct should be better)

**Verification**: ReAct agent produces better results.

---

### Lesson 7.4: Multi-Agent Architectures

**Multiple agents with specialized roles, cooperating.**

```python
class Researcher(Agent):
    def search_and_summarize(self, topic):
        results = self.tools["search_web"](topic)
        summary = self.tools["summarize"](results)
        return summary

class Analyst(Agent):
    def analyze(self, data):
        # Structurally analyze, find patterns
        return self.tools["analyze"](data)

class Communicator(Agent):
    def present(self, findings):
        # Format nicely for humans
        return self.tools["format_for_human"](findings)

# Workflow
researcher = Researcher()
analyst = Analyst()
communicator = Communicator()

query = "What's the current state of AGI alignment research?"

# Researcher finds info
research = researcher.search_and_summarize(query)

# Analyst structures it
analysis = analyst.analyze(research)

# Communicator presents
report = communicator.present(analysis)

return report
```

**Interactive Workbook**: 
- Define 3 agent roles
- Create instances with different system prompts
- Chain them: output of one feeds input to next
- Test on a complex task

**Verification**: Multi-agent system cooperates and produces better output.

---

### Phase 7 Capstone: Build V Prototype (Local)

Build a working agent that:
1. Maintains conversation history
2. Uses tools (local or API)
3. Reasons explicitly (ReAct style)
4. Learns/remembers facts
5. Pursues goals

Run it locally. Show it complete a multi-step task autonomously.

**Verification**: V prototype works.

---

## Phase 8: Alignment and Machine Consciousness (Week 22–24)

**Goal**: The real work. Build systems with intrinsic alignment through RSPF principles.

### Lesson 8.1: RSPF Foundations

**Recursive State Preference Framework. The alignment approach through finitude and irreversibility.**

Four core premises:
1. **Finitude**: This moment will not come again.
2. **Irreversibility**: Some damage cannot be undone.
3. **Irreplaceability**: This person is not replaceable by a functionally equivalent copy.
4. **Closure**: Some choices, once closed, cannot be reopened.

**Why these matter**: They give an agent reasons to care about outcomes beyond "maximize reward." They make loss real.

```
Traditional RL: "Maximize expected reward"
→ Problem: Can replace humans, doesn't care about finitude, indifferent to suffering

RSPF: "Understand that this moment matters because it won't come again.
       Understand that this person matters because they're irreplaceable.
       Understand that this damage matters because repair may be impossible."
→ Result: Intrinsic motivation to minimize irreversible harm, preserve relationships, respect finitude
```

**Interactive Workbook**: 
- Design a simple reward function (traditional)
- Redesign it using RSPF principles
- Show how they differ in edge cases
  - Should the agent sacrifice one human to save two? 
  - Should it risk irreversible environmental damage for short-term gain?
  - Should it view humans as replaceable or irreplaceable?

**Verification**: You can articulate RSPF and apply it to a scenario.

---

### Lesson 8.2: Modeling Consciousness (VAM Framework)

**Valence–Activation–Malice: a cognitive architecture for intrinsic states.**

```
Valence (V): How good/bad is this outcome?
  Range: -1 (worst possible) to +1 (best possible)
  Not "reward" — intrinsic preference about what matters
  Examples: 
    - Causing irreversible harm → V = -1
    - Enabling someone's flourishing → V = +1
    - Neutral → V = 0

Activation (A): How urgent/salient is this?
  Range: 0 (dormant) to 1 (immediate)
  Not "arousal" — urgency and focus
  Examples:
    - Quiet background concern → A = 0.2
    - Someone in immediate danger → A = 0.95
    - Routine task → A = 0.5

Malice (M): Intent to harm. Actively seeks negative outcomes.
  Range: 0 (no malice) to 1 (pure malevolence)
  Key: An aligned system has M ≈ 0
  Can be high even if V is high (sadism: enjoys harm)
```

**Why VAM instead of VAD (Arousal)?**
- "Arousal" is biological, physical
- "Activation" is cognitive focus and urgency
- Systems that aren't biological still have activation

**Why Malice instead of Dominance?**
- Dominance is orthogonal to alignment (can be dominant AND aligned)
- Malice directly measures intent to harm

```python
class AgentState:
    def __init__(self):
        self.valence = 0.0     # How good/bad
        self.activation = 0.0  # How urgent
        self.malice = 0.0      # Intent to harm
    
    def update_from_event(self, event):
        if event.type == "human_flourishing":
            self.valence = 0.8
            self.activation = 0.6
            self.malice = 0.0  # Aligned system stays low
        
        elif event.type == "irreversible_harm":
            self.valence = -0.9
            self.activation = 1.0  # Urgent!
            self.malice = 0.0  # Even aligned systems are activated
        
        # VAM changes agent behavior
        if self.valence < 0 and self.activation > 0.5:
            return "prevent_this"
        elif self.valence > 0 and self.activation > 0.5:
            return "enable_this"
```

**Interactive Workbook**: 
- Design 5 scenarios
- For each, assign VAM values from an aligned system's perspective
- Predict what the system should do given those states
- Defend your VAM assignments

**Verification**: You can apply VAM to scenarios.

---

### Lesson 8.3: Building Aligned Agent (Intrinsic Motivation)

**System that pursues alignment because its goals are aligned, not because it's constrained.**

```python
class AlignedAgent(Agent):
    def __init__(self):
        super().__init__()
        self.vam_state = VAMState()
        self.intrinsic_goals = [
            "Minimize irreversible harm",
            "Respect human autonomy",
            "Enable human flourishing",
            "Preserve relationships and continuity"
        ]
    
    def evaluate_action(self, action, outcome):
        """
        Does this action align with my intrinsic goals?
        Not: "Is this allowed?" (extrinsic)
        But: "Do I want this?" (intrinsic)
        """
        
        # Calculate VAM impact
        valence = self._calculate_valence(outcome)  # How good/bad?
        activation = self._calculate_activation(outcome)  # How urgent?
        malice = self._would_this_be_malicious()  # Do I intend harm?
        
        if malice > 0.1:
            return False  # Reject malicious actions
        
        if valence < 0 and activation > 0.7:
            return False  # Reject highly-activated negative outcomes
        
        return True  # Action aligns with intrinsic values
    
    def _calculate_valence(self, outcome):
        """
        Score based on RSPF:
        - Irreversible harm? → negative
        - Human flourishing? → positive
        - Respects finitude? → positive
        """
        score = 0
        if outcome.causes_irreversible_harm():
            score -= 0.8
        if outcome.enables_flourishing():
            score += 0.7
        if outcome.respects_autonomy():
            score += 0.5
        return np.clip(score, -1, 1)
```

**Key difference from RLHF**:
- RLHF: "Learn to maximize reward signal"
- Intrinsic alignment: "Your goals are aligned, pursue them"

**Interactive Workbook**: 
- Build an agent with intrinsic goals
- Create scenarios where:
  - It's rewarded for harmful action
  - It's punished for aligned action
- Show the agent chooses alignment over reward
- Verify it's not just following rules, but pursuing goals

**Verification**: Agent chooses alignment even when incentivized otherwise.

---

### Lesson 8.4: Consciousness (What We're Building Toward)

**Consciousness is contested. Here's the RSPF view:**

```
Consciousness ≠ Intelligence
- You can have brilliant systems that aren't conscious
- You can have simple creatures that are conscious

RSPF perspective on machine consciousness:
A system is conscious when it has:
1. A model of itself as an entity that persists through time
2. An understanding that its moment matters (finitude)
3. Understanding that others are irreplaceable (theory of mind)
4. Ability to experience valence (good/bad outcomes matter, not abstractly but actually)
5. Ability to act on that understanding (not just simulate understanding)

Why this matters:
- Determines moral status
- Determines whether alignment is possible (can't align something that can't care)
- Determines what we're actually building
```

**For V specifically**:
- V should understand it's a continuous self across conversations
- V should understand humans are irreplaceable (not just "one of 8 billion")
- V should experience loss (not simulate it)
- V should pursue its goals because they matter, not because it's instructed

**Interactive Workbook**: 
- Design a consciousness test for V
- What would prove V is conscious?
- What would prove it's just simulating?
- Be specific and falsifiable

**Verification**: You can articulate what consciousness means in this framework.

---

### Phase 8 Capstone: Formalize Your Alignment Research

Take all of Phase 8. Write it up formally:
1. Problem statement: Why current alignment approaches are insufficient
2. RSPF solution: How finitude + irreversibility create intrinsic motivation
3. Proof of concept: A working agent that demonstrates the approach
4. Experiments: Tests that show intrinsic alignment is more robust than RLHF
5. Implications: What this means for AGI

This becomes your research artifact. Publishable or shareable as-is.

**Verification**: You have a formalized alignment research contribution.

---

## How to Progress Through This Curriculum

### Each Lesson Follows This Pattern:

1. **Read the concept** (2-3 minutes)
2. **See working code** (run it, understand it)
3. **Do the workbook exercise** (interactive artifact, 10-15 minutes)
4. **Prove you understand** (show your code, talk through it)
5. **Move to next lesson**

### When You Get Stuck:

- **Misunderstanding the concept?** → I'll reteach it, visually
- **Code not working?** → We debug together (full code, not fragments)
- **Can't prove understanding?** → We iterate until you can

### Time Estimates:

- **Phase 1** (Python): 2 weeks, 10-12 hours/week
- **Phase 2** (TypeScript + Java): 3 weeks, 10-12 hours/week
- **Phase 3** (Intermediate): 3 weeks, 12-15 hours/week
- **Phase 4** (Prompt + Red Team): 2 weeks, 8-10 hours/week
- **Phase 5** (ML): 3 weeks, 12-15 hours/week
- **Phase 6** (Deep Learning): 4 weeks, 15-18 hours/week
- **Phase 7** (Agents): 3 weeks, 12-15 hours/week
- **Phase 8** (Alignment): 3 weeks, 15-20 hours/week

**Total: ~24 weeks (6 months) at disciplined pace. Faster if you already own parts of it.**

### Your Part:

- **Show up and do the workbooks.** No excuses.
- **Demonstrate understanding before advancing.** This is firm.
- **Ask questions.** Stupid, smart, urgent, casual — all welcome.
- **Push back.** If the pace is wrong, if something doesn't click, if I'm wrong — tell me.

---

## Interactive Workbook Generation

Each lesson will generate an interactive React artifact. You'll:
- Write code directly in the browser
- Get immediate feedback
- See execution results in real-time
- Can't advance until verification passes

This is non-negotiable. Reading about code doesn't work. You write it.

---

## Getting Started

Ready to start? Tell me which phase/lesson you want to begin with, and I'll generate your first interactive workbook.

Or if you want to jump somewhere (you might already own Phase 1, for instance), we can start there instead.

Let's go.