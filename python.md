- [Basics](#basics)
- [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
- [Advanced Data Structures](#advanced-data-structures)
  - [Implement custom iterators](#implement-custom-iterators)
- [Functional Programming](#functional-programming)
  - [Lambda Functions](#lambda-functions)
  - [Map and Filter](#map-and-filter)
  - [Comprehensions](#comprehensions)
- [Modules and Packages](#modules-and-packages)
  - [Creating your own packages](#creating-your-own-packages)
- [Parallel computing](#parallel-computing)
  - [Multithreading](#multithreading)
  - [Multiprocessing](#multiprocessing)
- [Misc. Topics](#misc-topics)
  - [Decorators](#decorators)
  - [Generators](#generators)
  - [Context Managers](#context-managers)
  - [`asyncio` for non-blocking](#asyncio-for-non-blocking)
- [Advanced Topics and Best Practices](#advanced-topics-and-best-practices)
- [Resources for Learning](#resources-for-learning)

* suggested by chatGPT

# Basics

* Data Types: int, float, str, bool
* Control Flow: if, else, elif, loops (for and while)
* Functions: Defining functions, parameters, return values
* Lists: Creating, slicing, list comprehensions
* Tuples: Immutable sequences
* Dictionaries: Key-value pairs
* Sets: Unordered collections of unique elements
* Strings: Operations, formatting (f-strings, format(), etc.)
* File Handling: Reading and writing files using open() and with statements
* Error Handling: try, except, finally
  ```python
  try:
      x = int(input("Enter a number: "))
  except ValueError:
      print("That's not a number!")
  finally:
      print(f"x is {x}")
  ```

# Object-Oriented Programming (OOP)

* Classes: Defining classes using `class`.
* Inheritance: Subclasses and inheritance hierarchy.
* Polymorphism: Using a single interface to represent different underlying forms.
* Encapsulation: Access modifiers (public, private, protected).
* Abstraction: Using abstract base classes with abc.ABCMeta.

**Practice:**
- Create a simple class hierarchy (e.g., Animal → Dog, Cat).
- Implement polymorphic functions.

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"animal name is {name}")

    def eat(self):
        print(f"animal {self.name} is eating")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def bark(self):
        print(f"dog {self.name} is barking")

    def eat(self, food):
        super().eat()
        print(f"dog {self.name} is eating its {food}")

a=Dog("cute", 4)
a.bark()
a.eat("banana")
Animal(a.name).eat() # actually, here created a new instance of Animal
print(isinstance(a, Dog))
print(isinstance(a, Animal)) # True
```

# Advanced Data Structures

Python has built-in modules and libraries that extend its functionality for data manipulation:

* itertools: For efficient looping and iteration.
* datetime: Working with dates, times, and time zones.
* collections: Specialized container datatypes like deque, Counter, etc.

## Implement custom iterators

```python
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

my_iter = MyIterator([1, 2, 3])
for num in my_iter:
    print(num)
```

# Functional Programming

Functional programming is a paradigm that emphasizes the use of functions to create programs:

* Lambda Functions: Anonymous functions for simple operations.
* Map and Filter: Using map() and filter() for functional programming.
* List Comprehensions: Concise way to create lists based on existing iterables.

## Lambda Functions

```python
add = lambda a, b: a + b
print(add(3, 4))  # Output: 7
```

## Map and Filter

```python
import random
numbers = [random.randint(1,100) for _ in range(20)]

# map() applies a function to each item of an iterable and retuan an iterable
squared = list(map(lambda x: x**2, numbers))

# with multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]

added = map(lambda x, y: x + y, list1, list2)
print(list(added))

# filter() also applies a function to each item of an iterable and only return that item if
# func() return true
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

## Comprehensions

```python
# List comprehension
squares = [x**2 for x in range(6)]

# Dictionary comprehension
d = {i: i**2 for i in range(5)}
```

# Modules and Packages

Python has a vast ecosystem of libraries that you should explore:

* numpy: For numerical computations and arrays.
* pandas: For data manipulation and analysis (e.g., DataFrames).
* matplotlib and seaborn: For data visualization.
* requests: For HTTP requests and APIs.

## Creating your own packages

- Use `__init__.py` to make directories into packages.
- Organize code into logical modules.

```python
├── main.py
└── mypackage
    ├── funcs.py
    ├── __init__.py
    ├── math.py

# main.py
import mypackage as pkg

a=3
b=5
pkg.greet('hello')
print(f"{a} + {b} = {pkg.add(a,b)}")
print(f"{a} * {b} = {pkg.times(a,b)}")

# __init__.py
from .math import add, times
from .funcs import greet

# funcs.py 
def greet(words="you"):
    print(f"Greeting, {words}")
    
#math.py 
def add(x, y):
    return x+y

def times(x, y):
    return x*y%   
```

# Parallel computing

## Multithreading

- Use the `threading` module for threads.

```python
import threading

def worker():
    print(f"Thread {threading.get_ident()} is running")

thread1 = threading.Thread(target=worker)
thread2 = threading.Thread(target=worker)
thread1.start()
thread2.start()
```

## Multiprocessing

- Use the `multiprocessing` module for processes (better for CPU-bound tasks).

```python
import multiprocessing
import time

def square(x):
    return x ** 2

data = [i for i in range(10000000)]

# Using built-in map()
sequential_start = time.time()
squared_sequential = list(map(square, data))
print("Sequential execution time:", time.time() - sequential_start)

# Using multiprocessing's map()
processes_start = time.time()
with multiprocessing.Pool(processes=16) as pool:
    squared_parallel = pool.map(square, data)
print("Parallel execution time:", time.time() - processes_start)
print(squared_parallel[:10])
```

# Misc. Topics

* Decorators: Functions that modify or extend other functions.
* Generators: any function using `yield` becomes a generator
* Context Managers: Using `with` statements for resource management (__enter__ and __exit__ methods).
* Asynchronous Programming: Using `asyncio` for non-blocking code.

## Decorators

* extend the behavior of a function, without change the actual code of func
* essentially a function that takes another function as an argument and returns a new function with enhanced functionality.
* [example](files/conn.py)

```python
def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()  # Output: Something before..., Hello!, Something after...
```

## Generators

* use `yield` to create iterators
 
```python
def fibonacci():
    print("init a and b")
    a, b = 0, 1

    while True:
        print("before yield")
        yield a
        print("after yield, updating a and b")
        a, b = b, a + b
        print("a and b updated. loop again")

fib = fibonacci()
print(type(fib))
for _ in range(4):
    print("calling fib")
    print(next(fib))
    print("done this iteration\n")

calling fib
init a and b
before yield
0
done this iteration

calling fib
after yield, updating a and b
a and b updated. loop again
before yield
1
done this iteration
```

## Context Managers

- Use `with` statements for resource management:

```python
with open('file.txt', 'r') as f:
    content = f.read()
```

- Create custom context managers:

```python
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")

with MyContextManager():
    print("Inside the context")
```

## `asyncio` for non-blocking

```python
import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(2)  # Simulating being blocked and yeilding control
    print("World!")

async def say_goodbye():
    print("Goodbye!")
    await asyncio.sleep(1)
    print("for now!")

# Running the async function
async def main1():
    task1 = asyncio.create_task(say_hello())
    task2 = asyncio.create_task(say_goodbye())

    await task1
    await task2

asyncio.run(main1())
```

* [more](./examples/async.py)

# Advanced Topics and Best Practices

- **Memory Management:** Learn about references, garbage collection, and `sys.getrefcount()`.
- **Performance Optimization:** Use tools like `cProfile` and `timeit`.
- **Testing:** Write unit tests with `unittest` or `pytest`.
- **Code Style:** Follow PEP 8 guidelines for clean code.

# Resources for Learning

* Books:
  * _"Python Crash Course" by Eric Matthes_ – Great for beginners.
  * _"Fluent Python" by Luciano Ramalho_ - covers advanced Python idioms and best practices, for intermediate to advanced learners.
  * _"Automate the Boring Stuff with Python"_ by Al Sweigart (fun and practical projects).
  * _"Python in Depth" by Théotime Coiffet_ – Free online book covering advanced topics.
  * _"Python for Data Analysis" by Wes McKinney_ - for data manipulation with pandas and NumPy.
* Online Courses:
  * [python interview questions](https://www.geeksforgeeks.org/python-interview-questions)
  - [Codecademy's Learn Python 3](https://www.codecademy.com/learn/python)  
  - [Coursera: Introduction to Programming with Python (UC San Diego)](https://www.coursera.org/specializations/introduction-programming-python)
  - edabit: Python Tutorials
- Online Courses:
  - [Real Python](https://realpython.com/) – Tutorials on advanced Python topics.
  - [Sentdex's Advanced Python Playlist](https://www.youtube.com/playlist?list=PLQVjZ6Bl_rIYFnq_kU7-zdh5eC4hJdlvMA) – Excellent for video learners.
- Communities:
  - [Stack Overflow](https://stackoverflow.com/) – Ask questions and learn from others.
  - [Reddit's r/learnpython](https://www.reddit.com/r/learnpython/) – Great for community support.

---
