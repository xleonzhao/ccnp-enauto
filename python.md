- [Basics](#basics)
- [Advanced](#advanced)
  - [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
  - [Advanced Data Structures](#advanced-data-structures)
  - [Functional Programming](#functional-programming)
  - [Modules and Libraries](#modules-and-libraries)
  - [Advanced Topics](#advanced-topics)
    - [decorator](#decorator)
  - [Practice with Real-World Projects](#practice-with-real-world-projects)
- [Resources for Learning](#resources-for-learning)
- [Deekseek-R1](#deekseek-r1)
  - [**1. Build a Strong Foundational Knowledge**](#1-build-a-strong-foundational-knowledge)
  - [**2. Advanced Topics in Python**](#2-advanced-topics-in-python)
    - [**a. Object-Oriented Programming (OOP)**](#a-object-oriented-programming-oop)
    - [**b. Advanced Data Structures**](#b-advanced-data-structures)
    - [**c. Functional Programming**](#c-functional-programming)
    - [**d. Modules and Packages**](#d-modules-and-packages)
    - [**e. Error Handling**](#e-error-handling)
    - [**f. Multithreading and Multiprocessing**](#f-multithreading-and-multiprocessing)
    - [**g. Decorators**](#g-decorators)
    - [**h. Context Managers**](#h-context-managers)
    - [**i. Iterators and Generators**](#i-iterators-and-generators)
  - [**3. Advanced Topics and Best Practices**](#3-advanced-topics-and-best-practices)
  - [**4. Resources for Advanced Learning**](#4-resources-for-advanced-learning)
  - [**5. Build Projects to Apply What You Learn**](#5-build-projects-to-apply-what-you-learn)

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

- **Generators:** Use `yield` to create iterators.
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

# Functional Programming

Functional programming is a paradigm that emphasizes the use of functions to create programs:

* Lambda Functions: Anonymous functions for simple operations.
* Map and Filter: Using map() and filter() for functional programming.
* List Comprehensions: Concise way to create lists based on existing iterables.

- **Lambda Functions:** Short anonymous functions.
  ```python
  add = lambda a, b: a + b
  print(add(3, 4))  # Output: 7
  ```

- **Map and Filter:** Apply functions to iterables.
  ```python
  import random
  numbers = [random.randint(1,100) for _ in range(20)]

  # map() applies a function to each item of an iterable and retuan an iterable
  squared = list(map(lambda x: x**2, numbers))
  
  # filter() also applies a function to each item of an iterable and only return that item if
  # func() return true
  evens = list(filter(lambda x: x % 2 == 0, numbers))
  ```
- **Comprehensions:** Lists, dictionaries, and generators.
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

- Importing modules:
  ```python
  import math
  from math import sqrt
  ```

- Creating your own packages:
  - Use `__init__.py` to make directories into packages.
  - Organize code into logical modules.

**Practice:**

- Create a simple package with multiple modules.
- Use existing packages like NumPy or Pandas for data manipulation.

### **e. Error Handling**


### **f. Multithreading and Multiprocessing**

- Use the `threading` module for threads.
- Use the `multiprocessing` module for processes (better for CPU-bound tasks).

  ```python
  import threading

  def worker():
      print(f"Thread {threading.get_ident()} is running")

  thread1 = threading.Thread(target=worker)
  thread2 = threading.Thread(target=worker)
  thread1.start()
  thread2.start()
  ```

### **g. Decorators**

- Enhance functions with decorators:

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

### **h. Context Managers**

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

### **i. Iterators and Generators**

- Implement custom iterators:

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

---

## **3. Advanced Topics and Best Practices**

- **Memory Management:** Learn about references, garbage collection, and `sys.getrefcount()`.
- **Performance Optimization:** Use tools like `cProfile` and `timeit`.
- **Testing:** Write unit tests with `unittest` or `pytest`.
- **Code Style:** Follow PEP 8 guidelines for clean code.

**Practice:**
- Build small projects (e.g., a calculator, to-do list app).
- Contribute to open-source Python projects.

---

## **4. Resources for Advanced Learning**

* https://www.geeksforgeeks.org/python-interview-questions

---

## **5. Build Projects to Apply What You Learn**
The best way to master Python is by building projects:
- Create a script to automate repetitive tasks (e.g., data entry).
- Build a simple web app using Flask or Django.
- Analyze data with Pandas and NumPy.



# Advanced Topics

## Advanced Topics

* Decorators: Functions that modify or extend other functions.
* Generators: Using `yield` to create iterators.
* Context Managers: Using `with` statements for resource management (__enter__ and __exit__ methods).
* Error Handling: Custom `exceptions` and handling specific errors.
* Asynchronous Programming: Using asyncio for non-blocking code.

### decorator

* extend the behavior of a function, without change the actual code of func
* essentially a function that takes another function as an argument and returns a new function with enhanced functionality.
* [example](files/conn.py)

## Practice with Real-World Projects

To solidify your understanding, work on projects that apply Python's advanced features:

* Build a simple web scraper using requests and BeautifulSoup.
* Create a data analysis pipeline using pandas and numpy.
* Implement an asynchronous script to handle I/O-bound tasks.
* Write a small application using OOP principles.


# Resources for Learning

Here are some resources to help you learn Python:

* Books:
  * _"Python Crash Course" by Eric Matthes_ – Great for beginners.
  * _"Fluent Python" by Luciano Ramalho_ - covers advanced Python idioms and best practices, for intermediate to advanced learners.
  * _"Automate the Boring Stuff with Python"_ by Al Sweigart (fun and practical projects).
  * _"Python in Depth" by Théotime Coiffet_ – Free online book covering advanced topics.
  * _"Python for Data Analysis" by Wes McKinney_ - for data manipulation with pandas and NumPy.

* Online Courses:
  - [Codecademy's Learn Python 3](https://www.codecademy.com/learn/python)  
  - [Coursera: Introduction to Programming with Python (UC San Diego)](https://www.coursera.org/specializations/introduction-programming-python)
  - edabit: Python Tutorials
- **Online Courses:**
  - [Real Python](https://realpython.com/) – Tutorials on advanced Python topics.
  - [Sentdex's Advanced Python Playlist](https://www.youtube.com/playlist?list=PLQVjZ6Bl_rIYFnq_kU7-zdh5eC4hJdlvMA) – Excellent for video learners.
- **Communities:**
  - [Stack Overflow](https://stackoverflow.com/) – Ask questions and learn from others.
  - [Reddit's r/learnpython](https://www.reddit.com/r/learnpython/) – Great for community support.

---
