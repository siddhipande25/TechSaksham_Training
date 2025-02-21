# Python Basics

## Python Introduction

Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

## Variables and Data Types

### Variables
A variable is used to store data in Python. Unlike other languages, Python does not require explicit declaration of variables.

**Example:**
```python
x = 10        # Integer
name = "John" # String
pi = 3.14     # Float
is_valid = True  # Boolean
```
## Data Types in Python

Python has several built-in data types:

### 1. Numeric Types
Used to store numeric values.
- `int` – Integer numbers (e.g., `10`, `-5`)
- `float` – Floating-point numbers (e.g., `3.14`, `-2.5`)
- `complex` – Complex numbers (e.g., `3 + 4j`)

### 2. Sequence Types
Used to store ordered collections of items.
- `list` – Mutable, ordered collection (e.g., `[1, 2, 3]`)
- `tuple` – Immutable, ordered collection (e.g., `(4, 5, 6)`)
- `range` – Represents an immutable sequence of numbers (e.g., `range(1, 10)`)

### 3. Text Type
Used to store text data.
- `str` – String data type (e.g., `"Hello, World!"`)

### 4. Boolean Type
Represents `True` or `False` values.
- `bool` – Boolean values (`True` or `False`)

### 5. Set Types
Used to store unordered, unique items.
- `set` – Mutable, unordered collection with unique elements (e.g., `{1, 2, 3}`)
- `frozenset` – Immutable version of a set (e.g., `frozenset({4, 5, 6})`)

### 6. Mapping Type
Used to store key-value pairs.
- `dict` – Dictionary that holds key-value pairs (e.g., `{"name": "Alice", "age": 25}`)

### 7. Binary Types
Used for handling binary data.
- `bytes` – Immutable binary data (e.g., `b"hello"`)
- `bytearray` – Mutable binary data (e.g., `bytearray(5)`)
- `memoryview` – Allows memory-efficient access to binary data.


## Data Structures in Python

### 1. List

A list is an ordered, mutable collection that can store elements of different types.

**Example:**

```python
my_list = [1, 2, 3, "apple", "banana"]
print(my_list[0])  # Output: 1
```

### 2. Tuple

A tuple is an ordered, immutable collection.

**Example:**

```python
my_tuple = (10, 20, 30, "hello")
print(my_tuple[1])  # Output: 20
```

### 3. Dictionary

A dictionary is an unordered, mutable collection of key-value pairs.

**Example:**

```python
my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])  # Output: Alice
```

## Operators in Python

Operators in Python are used to perform operations on variables and values. Python supports several types of operators:

### 1. Arithmetic Operators
Used to perform mathematical operations.

| Operator | Description  | Example |
|----------|-------------|---------|
| `+` | Addition | `5 + 3  # Output: 8` |
| `-` | Subtraction | `10 - 4  # Output: 6` |
| `*` | Multiplication | `2 * 3  # Output: 6` |
| `/` | Division | `10 / 2  # Output: 5.0` |
| `%` | Modulus (Remainder) | `10 % 3  # Output: 1` |
| `**` | Exponentiation | `2 ** 3  # Output: 8` |
| `//` | Floor Division | `10 // 3  # Output: 3` |

### 2. Comparison Operators
Used to compare values and return a boolean result (`True` or `False`).

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal to | `5 == 5  # Output: True` |
| `!=` | Not equal to | `5 != 3  # Output: True` |
| `>` | Greater than | `10 > 5  # Output: True` |
| `<` | Less than | `5 < 10  # Output: True` |
| `>=` | Greater than or equal to | `8 >= 8  # Output: True` |
| `<=` | Less than or equal to | `7 <= 10  # Output: True` |

### 3. Logical Operators
Used to combine conditional statements.

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | Returns `True` if both statements are true | `(5 > 3 and 10 > 5)  # Output: True` |
| `or` | Returns `True` if one of the statements is true | `(5 > 3 or 10 < 5)  # Output: True` |
| `not` | Reverses the result | `not(5 > 3)  # Output: False` |

### 4. Assignment Operators
Used to assign values to variables.

| Operator | Example | Equivalent To |
|----------|---------|---------------|
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 2` | `x = x - 2` |
| `*=` | `x *= 4` | `x = x * 4` |
| `/=` | `x /= 2` | `x = x / 2` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 2` | `x = x ** 2` |
| `//=` | `x //= 3` | `x = x // 3` |

### 5. Bitwise Operators
Used to perform operations on binary numbers.

| Operator | Description | Example |
|----------|-------------|---------|
| `&` | Bitwise AND | `5 & 3  # Output: 1` |
| `|` | Bitwise OR | `5 | 3  # Output: 7` |
| `^` | Bitwise XOR | `5 ^ 3  # Output: 6` |
| `~` | Bitwise NOT | `~5  # Output: -6` |
| `<<` | Left shift | `5 << 1  # Output: 10` |
| `>>` | Right shift | `5 >> 1  # Output: 2` |

---

## Conditional Statements

### `if`, `elif`, `else`

Used to execute different blocks of code based on conditions.

**Example:**

```python
x = 10
if x > 0:
    print("Positive number")
elif x < 0:
    print("Negative number")
else:
    print("Zero")
```

## Looping Constructs

### `for` Loop

Used to iterate over sequences like lists and ranges.

**Example:**

```python
for i in range(5):
    print(i)  # Outputs: 0 1 2 3 4
```

---

## Functions in Python

Functions in Python are reusable blocks of code that perform a specific task. They help in code organization, reusability, and modularity.

### 1. Defining a Function
A function is defined using the `def` keyword.

**Syntax:**
```python
def function_name(parameters):
    # Function body
    return value  # Optional
```
**Example:**
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```
### 2. Function with Multiple Parameters
Functions can take multiple parameters.

**Example:**
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```
### 3. Default Parameter Values
Functions can have default values for parameters.

**Example:**

```python
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())        # Output: Hello, Guest!
print(greet("John"))  # Output: Hello, John!
```
### 4. Keyword Arguments
You can specify arguments by name.

**Example:**

```python
def person_info(name, age):
    print(f"Name: {name}, Age: {age}")

person_info(age=25, name="Alice")
```
### 5. Arbitrary Arguments (*args)
Used when the number of arguments is unknown.

**Example:**

```python
def sum_numbers(*numbers):
    return sum(numbers)

print(sum_numbers(1, 2, 3, 4))  # Output: 10
```

### 6. Arbitrary Keyword Arguments (**kwargs)
Used when the number of keyword arguments is unknown.

**Example:**

```python
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
```

### 7. Lambda Functions
A lambda function is a small anonymous function.

**Syntax:**

```python
lambda arguments: expression
```

**Example:**

```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

## Exception Handling in Python

Exception handling in Python is used to manage and respond to runtime errors, preventing crashes and ensuring smooth execution of programs.

### 1. What is an Exception?
An exception is an error that occurs during the execution of a program. Common Python exceptions include:
- `ZeroDivisionError` – Division by zero
- `TypeError` – Incorrect type of operation
- `ValueError` – Invalid value passed to a function
- `IndexError` – Accessing an invalid index in a sequence
- `KeyError` – Accessing a non-existent key in a dictionary

### 2. Handling Exceptions using `try` and `except`
We use `try` and `except` blocks to handle exceptions.

**Example:**

```python
try:
    x = 10 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Output: Cannot divide by zero!
```
### 3. Catching Multiple Exceptions
You can handle multiple exceptions in one try block.

**Example:**

```python
try:
    num = int("hello")  # This will raise ValueError
except (ValueError, TypeError):
    print("Invalid input!")  # Output: Invalid input!
```

### 4. Using else with try-except
The else block runs if no exception occurs.

**Example:**

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")  # Output: Division successful!
```

### 5. Using finally
The finally block executes regardless of whether an exception occurs or not.

**Example:**

```python
try:
    file = open("test.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing resources...")  # This will always execute
```

### 6. Raising Exceptions with raise
You can manually raise an exception using raise.

**Example:**

```python
x = -1
if x < 0:
    raise ValueError("Negative value is not allowed!")
```

## File Handling in Python

File handling in Python allows reading and writing files, which is essential for data storage and manipulation.

### 1. Opening a File
Files are opened using the open() function.

**Example:**

```python
file = open("example.txt", "r")  # Open file in read mode
content = file.read()
print(content)
file.close()
```

### 2. Writing to a File
You can write data to a file using the w mode.

**Example:**

```python
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()
```

### 3. Appending to a File
Use a mode to append content to an existing file.

**Example:**

```python
file = open("example.txt", "a")
file.write("\nAppended text.")
file.close()
```

### 4. Using with Statement
Using with ensures files are properly closed after execution.

**Example:**

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```
## Object-Oriented Programming (OOP) Concepts in Python

Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code efficiently.

### 1. Defining a Class and Object
A class is a blueprint for objects.

**Example:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 25)
print(person1.greet())  # Output: Hello, my name is Alice and I am 25 years old.
```

### 2. Inheritance
Inheritance allows a class to inherit attributes and methods from another class.

**Example:**

```python
class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title
    
    def work(self):
        return f"{self.name} is working as a {self.job_title}."

employee1 = Employee("Bob", 30, "Software Engineer")
print(employee1.greet())  # Output: Hello, my name is Bob and I am 30 years old.
print(employee1.work())   # Output: Bob is working as a Software Engineer.
```

### 3. Encapsulation
Encapsulation restricts direct access to some data fields by making them private.

**Example:**

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable
    
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

account = BankAccount(1000)
print(account.deposit(500))  # Output: 1500
```

### 4. Polymorphism
Polymorphism allows different classes to use the same method name.

**Example:**

````python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Output: Woof! Meow!
```
### End of Python Basics 🚀
