# Exception Handling

An **exception** is an error that occurs *while the program is running* (as opposed to a syntax error, which Python catches before running anything at all). If left unhandled, an exception crashes the program and prints a traceback. Exception handling lets you **anticipate specific failures and respond gracefully** instead of crashing.

## try / except — the basic mechanism
```python
try:
    num1 = 10
    num2 = 0
    print(num1 / num2)
except ZeroDivisionError:
    print("cannot divided by zero")
print("program end")
```
How it works:
1. Python runs everything inside `try:` line by line.
2. The moment a line *raises* an exception, Python immediately **stops executing the rest of the `try` block** and jumps to check the `except` clauses.
3. If an `except` clause matches the exception's type, that block runs instead.
4. Execution then **continues normally after the whole try/except** — the program doesn't crash; `"program end"` still prints.

If no `except` clause matches the exception type, it propagates upward (and crashes the program if nothing catches it anywhere).

## Matching specific exception types
Different operations can fail in different ways — Python has a specific exception class for each kind of failure, and your `TryExcept.py` deliberately covers the most common ones:

| Exception | When it happens | Example from your code |
|---|---|---|
| `ZeroDivisionError` | dividing by 0 | `10/0` |
| `ValueError` | converting a value to the wrong type/format | `int("abc")` |
| `IndexError` | accessing a list index that doesn't exist | `num[5]` on a 3-item list |
| `KeyError` | accessing a dict key that doesn't exist | `student["marks"]` when no such key |
| `TypeError` | combining incompatible types | `20 + "20"` (int + str) |

**Why match specific types instead of a bare `except:`?** A bare `except:` catches *everything*, including typos and bugs you didn't anticipate, silently hiding real problems. Matching the exact exception type means you only suppress the *specific* failure you planned for — anything else still surfaces as a crash so you notice it.

## else — runs only if NO exception occurred
```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result =", result)
```
`else` is the **"everything succeeded"** branch — it only executes if the `try` block completed with zero exceptions. This is useful to separate "the risky operation" from "what to do once it worked," rather than cramming the success logic inside `try` itself (where it would be ambiguous whether a later line inside `try` could itself throw).

## finally — always runs, no matter what
```python
try:
    ...
except ValueError:
    ...
else:
    ...
finally:
    print("Program End")
```
`finally` runs **unconditionally** — whether the `try` succeeded, failed and was caught, or even failed and was *not* caught (it still runs before the exception propagates further). It's meant for cleanup that must happen regardless of outcome — closing a file, releasing a lock, closing a network connection.

## Multiple except clauses for one try
```python
try:
    num = int(input("Enter number: "))
    result = 10 / num
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
```
Python checks each `except` in order and runs the **first matching one** — only one `except` block ever runs per exception, even if multiple exist.

## Raising your own exceptions
```python
class InvalidAgeError(Exception):   # custom exception = just a class inheriting from Exception
    pass

age = int(input("Enter your age: "))
if age < 18:
    raise InvalidAgeError("Age must be 18 or above.")
```
`raise` manually triggers an exception — useful for **enforcing business rules** that Python itself has no built-in error for (there's no `TooYoungError` baked into the language). Defining `class InvalidAgeError(Exception): pass` creates a brand-new exception type that behaves exactly like any built-in one — it can be caught with `except InvalidAgeError:` elsewhere, and it carries whatever message you pass to it.

## FileNotFoundError (file merging example)
```python
try:
    file1 = open("file1.txt", "r")
    ...
except FileNotFoundError:
    print("file is not found")
```
Opening a file that doesn't exist raises `FileNotFoundError` — wrapping file operations in `try/except` is standard practice any time you're dealing with the filesystem, since you can never fully guarantee a file exists before trying to open it.

## How to work with this topic
1. Put only the risky line(s) inside `try` — don't wrap your whole program in one giant `try` block, or you lose the ability to tell *which* line failed.
2. Catch the **most specific** exception type you can predict; avoid bare `except:`.
3. Use `else` for "ran successfully" logic, and `finally` for cleanup that must happen either way.
4. Raise custom exceptions for domain rules Python has no built-in error for — it makes the failure self-documenting (`InvalidAgeError` is more meaningful than a generic `ValueError`).
5. The execution order is always: `try` → (if error) matching `except` → (if no error at all) `else` → `finally` (always, last).
