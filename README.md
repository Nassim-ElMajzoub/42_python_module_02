*This project has been created as part of the 42 curriculum by nel-majz.*

# Garden Guardian: Data Engineering for Smart Agriculture

## Description

**Garden Guardian** is a Python project focused on mastering exception handling and building resilient data pipelines for agricultural systems. The project's goal is to learn how to write robust, fault-tolerant code that gracefully handles errors and unexpected situations without crashing.

Starting with basic try/except blocks and progressing through custom exceptions, finally blocks, and error raising, this project builds a complete garden management system that demonstrates professional error handling practices.

**Project Goals:**
- Master Python's exception handling mechanisms
- Build fault-tolerant systems that handle failures gracefully
- Learn to create custom exception types for domain-specific errors
- Understand resource cleanup with finally blocks
- Practice defensive programming and input validation
- Develop skills in building resilient data pipelines

The project consists of 5 exercises (0-4) that progressively introduce error handling concepts, from basic sensor validation to a comprehensive agricultural monitoring system.

---

## Instructions

### Requirements

- **Python 3.10+**
- **flake8** linter (for code style validation)
- **mypy** (for static type checking)

### Installation

```bash
pip3 install flake8 --break-system-packages
pip3 install mypy --break-system-packages
```

### Execution

Each exercise can be run independently:
```bash
# Exercise 0: Basic exception handling
python3 ex0/ft_first_exception.py

# Exercise 1: Agricultural data validation pipeline
python3 ex1/ft_raise_exception.py

# Exercise 2: Different types of problems
python3 ex2/ft_different_errors.py

# Exercise 3: Custom error types
python3 ex3/ft_custom_errors.py

# Exercise 4: Finally block - always clean up
python3 ex4/ft_finally_block.py
```

### Code Validation

```bash
# Check code style
flake8 ex0/ft_first_exception.py

# Check type hints
mypy ex0/ft_first_exception.py
```

---

## Exercise Breakdown

### Exercise 0: Agricultural Data Validation
**Concepts:** Basic try/except blocks, ValueError exception, input validation, graceful error handling

**Key Learning:** Programs shouldn't crash on bad input - catch exceptions and handle them gracefully. Error handling belongs in the caller, not the function itself.

### Exercise 1: Agricultural Data Validation Pipeline
**Concepts:** The `raise` keyword, input range validation, defensive programming, meaningful error messages

**Key Learning:** Functions should validate inputs and raise appropriate exceptions. Detect problems early and raise errors with clear messages.

### Exercise 2: Different Types of Problems
**Concepts:** Multiple exception types (ValueError, ZeroDivisionError, FileNotFoundError, TypeError), catching multiple exceptions in one block

**Key Learning:** Python has different exception types for different problems. You can catch multiple types together using a tuple syntax.

### Exercise 3: Making Your Own Error Types
**Concepts:** Custom exceptions, exception inheritance, domain-specific errors, exception hierarchies

**Key Learning:** Create custom exception classes to make errors more meaningful. Use inheritance to organize error families — catching a parent catches all its children.

### Exercise 4: Finally Block - Always Clean Up
**Concepts:** try/except/finally structure, try/finally without except, guaranteed cleanup, resource management

**Key Learning:** The `finally` block always executes, ensuring cleanup happens even when errors occur or when returning early.

---

## Key Programming Principles Demonstrated

### 1. **Defensive Programming**
- Validate inputs before processing
- Check preconditions and raise errors early
- Never assume data is valid

### 2. **Graceful Degradation**
- Programs continue running despite errors
- Errors are caught and handled appropriately
- Systems recover and provide meaningful feedback

### 3. **Resource Management**
- Always clean up resources (files, connections, hardware)
- Use `finally` blocks for guaranteed cleanup
- Prevent resource leaks

### 4. **Exception Hierarchy**
- Organize errors by category (GardenError → PlantError, WaterError)
- Catch specific errors or entire families
- Use inheritance to model error relationships

### 5. **Separation of Concerns**
- Functions detect and raise errors
- Callers catch and handle errors
- Clear responsibility boundaries

---

## Exception Handling Patterns

### Basic Try/Except
```python
try:
    risky_operation()
except ValueError:
    handle_error()
```

### Catching Multiple Together
```python
try:
    operation()
except (ValueError, TypeError, FileNotFoundError) as e:
    print(f"Caught {type(e).__name__}: {e}")
```

### Try/Finally Without Except
```python
try:
    do_something()
finally:
    cleanup()  # Always runs, even on return
```

### Try/Except/Finally
```python
try:
    open_resource()
    use_resource()
except Exception:
    handle_error()
finally:
    close_resource()  # Always runs
```

### Raising Errors
```python
def validate(data: str) -> int:
    if not data:
        raise ValueError("Data cannot be empty!")
    return int(data)
```

### Custom Exceptions
```python
class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="A plant is experiencing problems"):
        super().__init__(message)
```

---

## Technical Skills Acquired

- ✅ Basic exception handling with try/except
- ✅ Understanding different exception types
- ✅ Catching multiple exceptions in one block
- ✅ Creating custom exception classes
- ✅ Exception inheritance and hierarchies
- ✅ Resource cleanup with finally blocks
- ✅ try/finally without except
- ✅ Raising exceptions with meaningful messages
- ✅ Input validation and defensive programming
- ✅ Static type checking with mypy
- ✅ Code style validation with flake8

---

## Resources

### Official Documentation
- [Python Exceptions Documentation](https://docs.python.org/3/tutorial/errors.html) - Official Python exception handling guide
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html) - Complete list of Python's built-in exceptions
- [PEP 8 – Style Guide](https://peps.python.org/pep-0008/) - Official Python style guide

### Exception Handling Concepts
- [Real Python - Exception Handling](https://realpython.com/python-exceptions/) - Comprehensive exception handling tutorial
- [GeeksforGeeks - Exception Handling](https://www.geeksforgeeks.org/python-exception-handling/) - Clear explanations with examples
- [Python Exception Handling Best Practices](https://realpython.com/the-most-diabolical-python-antipattern/) - Common mistakes to avoid

### Specific Topics
- [Custom Exceptions in Python](https://realpython.com/python-custom-exceptions/) - Creating domain-specific exceptions
- [Context Managers and Cleanup](https://realpython.com/python-with-statement/) - Advanced resource management
- [mypy Documentation](https://mypy.readthedocs.io/en/stable/) - Static type checker documentation

### Tools
- [flake8 Documentation](https://flake8.pycqa.org/en/latest/) - Linting tool documentation
- [mypy Documentation](https://mypy.readthedocs.io/en/stable/) - Type checking tool documentation

---

## AI Usage

AI (Claude by Anthropic) was used as an **interactive learning assistant** throughout this project, following the 42 curriculum's AI guidelines.

### Tasks AI Assisted With:

#### 1. **Concept Explanation**
- **What:** Understanding try/except blocks, exception types, finally blocks, raise keyword, mypy
- **How:** Interactive Q&A to understand exception handling fundamentals
- **Which parts:** All exercises - conceptual understanding before implementation

#### 2. **Syntax Clarification**
- **What:** Correct Python exception handling syntax
- **How:** Learning proper try/except/finally structure and type hint usage
- **Which parts:** All exercises - ensuring proper Python syntax

#### 3. **Debugging Guidance**
- **What:** Identifying logic errors in exception handling
- **How:** Understanding where to place try/except blocks, when to use finally
- **Which parts:** Exercises 1, 4 - proper exception handling flow

#### 4. **Design Pattern Discussion**
- **What:** When to use different exception handling approaches
- **How:** Understanding when to catch specific vs general exceptions, when to create custom exceptions
- **Which parts:** Exercises 2, 3 - system architecture decisions

#### 5. **Code Review**
- **What:** Feedback on exception handling implementation
- **How:** Identifying issues like catching exceptions in the wrong place, output formatting
- **Which parts:** All exercises - ensuring correct patterns

### What AI Did NOT Do:

❌ **Write complete solutions** - All code was written by me
❌ **Copy-paste implementations** - Every line was typed and understood by me
❌ **Make design decisions** - I chose implementation approaches after understanding options
❌ **Debug code without my analysis** - I identified issues before discussing solutions

### Learning Approach:

The AI was used as a **tutor, not a solution provider**. For each exercise:
1. AI explained the concept
2. I asked clarifying questions until I understood
3. I implemented the solution myself
4. I reviewed my work with AI to catch issues
5. I understood and could explain every line of code

This approach ensured **genuine learning** while leveraging AI as an **educational tool**, fully aligned with 42's philosophy of peer learning and deep understanding.

### Key Principle Followed:

> *"Only use AI-generated content that you fully understand and can take responsibility for."*

Every piece of code submitted represents my understanding and ability to implement exception handling independently.

---

## Reflection

This project demonstrated the critical importance of exception handling in building reliable software systems. Starting from basic error catching and progressing through custom exceptions, resource cleanup, and error raising, each exercise built the foundation for professional-grade error handling.

The agricultural theme made abstract concepts concrete: sensors that fail (ValueError), resources that need cleanup (finally blocks), and domain-specific problems (custom exceptions). By the final exercise, the watering system handles errors gracefully, maintains data integrity, and provides clear feedback — all while ensuring cleanup always happens.

**Key Takeaway**: Exception handling isn't just about preventing crashes — it's about building systems that are resilient, maintainable, and provide excellent user experience even when things go wrong. Professional software anticipates failure and handles it with grace.

The skills acquired here are fundamental to any real-world application, from web services to IoT systems to data pipelines. Every production system needs robust error handling, and this project provided the foundation to build it correctly.

---

## Author

Nassim El Majzoub - 42 Student

*Project completed as part of the 42 programming curriculum*