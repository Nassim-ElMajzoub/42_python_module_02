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

The project consists of 6 exercises (0-5) that progressively introduce error handling concepts, culminating in a comprehensive garden management system with complete exception handling integration.

---

## Instructions

### Requirements

- **Python 3.10+**
- **flake8** linter (for code style validation)


### Execution

Each exercise can be run independently:
```bash
# Exercise 0: Basic exception handling
python3 ex0/ft_first_exception.py

# Exercise 1: Multiple exception types
python3 ex1/ft_different_errors.py

# Exercise 2: Custom exceptions
python3 ex2/ft_custom_errors.py

# Exercise 3: Finally blocks
python3 ex3/ft_finally_block.py

# Exercise 4: Raising errors
python3 ex4/ft_raise_errors.py

# Exercise 5: Complete system (final integration)
python3 ex5/ft_garden_management.py
```

---

## Exercise Breakdown

### Exercise 0: Agricultural Data Validation Pipeline
**Concepts:** Basic try/except blocks, ValueError exception, input validation, graceful error handling

**Key Learning:** Programs shouldn't crash on bad input - catch exceptions and handle them gracefully.

### Exercise 1: Different Types of Problems
**Concepts:** Multiple exception types (ValueError, ZeroDivisionError, FileNotFoundError, KeyError), catching multiple exceptions, exception specificity

**Key Learning:** Python has different exception types for different problems. You can catch them separately or together.

### Exercise 2: Making Your Own Error Types
**Concepts:** Custom exceptions, exception inheritance, domain-specific errors, exception hierarchies

**Key Learning:** Create custom exception classes to make errors more meaningful and specific to your application domain.

### Exercise 3: Finally Block - Always Clean Up
**Concepts:** try/except/finally structure, guaranteed cleanup, resource management

**Key Learning:** The `finally` block always executes, ensuring cleanup happens even when errors occur.

### Exercise 4: Raising Your Own Errors
**Concepts:** The `raise` keyword, input validation, defensive programming, helpful error messages

**Key Learning:** Detect problems early and raise errors with clear messages. Functions should validate inputs and raise appropriate exceptions.

### Exercise 5: Garden Management System
**Concepts:** Integration of all concepts - custom exceptions, multiple error types, finally blocks, error raising, class-based design

**Key Learning:** Combine all exception handling techniques to build robust, fault-tolerant systems that recover from errors gracefully.

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

### Multiple Exception Types
```python
try:
    operation()
except ValueError:
    handle_value_error()
except TypeError:
    handle_type_error()
```

### Catching Multiple Together
```python
try:
    operation()
except (ValueError, TypeError, KeyError):
    handle_any_of_these()
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
def validate(data):
    if not data:
        raise ValueError("Data cannot be empty!")
    return data
```

### Custom Exceptions
```python
class CustomError(Exception):
    pass

raise CustomError("Something specific went wrong")
```

---

## Technical Skills Acquired

- ✅ Basic exception handling with try/except
- ✅ Understanding different exception types
- ✅ Creating custom exception classes
- ✅ Exception inheritance and hierarchies
- ✅ Resource cleanup with finally blocks
- ✅ Raising exceptions with meaningful messages
- ✅ Input validation and defensive programming
- ✅ Error recovery and fault tolerance
- ✅ Building resilient systems
- ✅ Professional error handling practices

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
- [Defensive Programming](https://en.wikipedia.org/wiki/Defensive_programming) - Programming philosophy

### Tools
- [flake8 Documentation](https://flake8.pycqa.org/en/latest/) - Linting tool documentation

---

## AI Usage

AI (Claude by Anthropic) was used as an **interactive learning assistant** throughout this project, following the 42 curriculum's AI guidelines.

### Tasks AI Assisted With:

#### 1. **Concept Explanation**
- **What:** Understanding try/except blocks, exception types, finally blocks, raise keyword
- **How:** Interactive Q&A to understand exception handling fundamentals
- **Which parts:** All exercises - conceptual understanding before implementation

#### 2. **Syntax Clarification**
- **What:** Correct Python exception handling syntax
- **How:** Learning proper try/except/finally structure
- **Which parts:** All exercises - ensuring proper Python syntax

#### 3. **Debugging Guidance**
- **What:** Identifying logic errors in exception handling
- **How:** Understanding where to place try/except blocks, when to use finally
- **Which parts:** Exercises 3-5 - proper exception handling flow

#### 4. **Design Pattern Discussion**
- **What:** When to use different exception handling approaches
- **How:** Understanding when to catch specific vs general exceptions, when to create custom exceptions
- **Which parts:** Exercises 2, 5 - system architecture decisions

#### 5. **Code Review**
- **What:** Feedback on exception handling implementation
- **How:** Identifying issues like catching exceptions in the wrong place
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

The agricultural theme made abstract concepts concrete: sensors that fail (ValueError), resources that need cleanup (finally blocks), and domain-specific problems (custom exceptions). By the final exercise, I created a comprehensive system that handles errors gracefully, maintains data integrity, and provides clear feedback - all while continuing to operate.

**Key Takeaway**: Exception handling isn't just about preventing crashes - it's about building systems that are resilient, maintainable, and provide excellent user experience even when things go wrong. Professional software anticipates failure and handles it with grace.

The skills acquired here are fundamental to any real-world application, from web services to IoT systems to data pipelines. Every production system needs robust error handling, and this project provided the foundation to build it correctly.

---

## Author

Nassim El Majzoub - 42 Student

*Project completed as part of the 42 programming curriculum*