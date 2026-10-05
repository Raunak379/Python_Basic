# Variables & Data Types

## What a variable actually is
In Python, a variable is **not a box that holds a value** — it's a *name (label) bound to an object* living in memory. When you write:

```python
x = 10
```

Python first creates an integer object `10` somewhere in memory, then makes the name `x` point to it. You can prove this with `id(x)` (shows the memory address) and `type(x)` (shows the object's type).

This matters because:
- Multiple names can point to the *same* object: `y = x` makes `y` point to the same `10`, it doesn't copy it.
- Reassigning `x = 20` doesn't change the old object — it makes `x` point to a *new* object `20`. The old `10` object still exists until nothing points to it, then Python's garbage collector reclaims it.

## Dynamic typing
Python is **dynamically typed** — a variable has no fixed type; it just points to whatever object was last assigned to it.

```python
x = 10        # x -> int
x = "hello"   # x -> str (completely fine, no error)
```

Contrast with statically typed languages (Java/C++) where a variable's type is fixed at declaration.

## Core built-in data types

| Type | Example | Mutable? | Notes |
|---|---|---|---|
| `int` | `10` | No | Arbitrary precision — doesn't overflow like C's `int` |
| `float` | `10.5` | No | Stored as IEEE-754 double; has precision limits (`0.1 + 0.2 != 0.3`) |
| `str` | `"hello"` | No | Sequence of Unicode characters, immutable |
| `bool` | `True`/`False` | No | Actually a subclass of `int` (`True == 1`) |
| `complex` | `2+3j` | No | Rare in basic scripts |
| `NoneType` | `None` | No | Represents "no value" — like `null` |

**Immutable** means the object's value can't be changed in place — any "modification" actually creates a new object. `int`, `float`, `str`, `bool`, and `tuple` are immutable. `list`, `dict`, and `set` are mutable (covered in the Collections doc).

## Your repo's gotcha: shadowing built-ins
In `Variable&DataType/DataTypes.py`:
```python
int = 10
float = 10.5
str = "hello"
```
This **works**, but it overwrites the built-in `int`, `float`, `str` *functions* with your own values for the rest of that script. After this line, calling `int("5")` would crash with `TypeError: 'int' object is not callable`, because `int` no longer refers to the built-in type — it refers to your variable `10`.

**Rule of thumb:** never name a variable the same as a built-in (`list`, `dict`, `str`, `int`, `float`, `type`, `id`, `sum`, `max`, `min`...). Your `Collection/list.py` and `Collection/Tuples.py` files do this too (`list = [1,2,3,4,5,6]`, `new_list = list[fruits]`), which is why `Tuples.py` actually has a bug — `list[fruits]` is invalid syntax (trying to index the builtin `list` *type* with a tuple) and will throw `TypeError`. It should be `list(fruits)`.

## Type checking & conversion
- `type(x)` → returns the exact type.
- `isinstance(x, int)` → preferred for checks (also respects inheritance).
- Conversion functions: `int("5")`, `float("3.14")`, `str(42)`, `bool(0)` (→ `False`), `bool("")` (→ `False`), `bool([])` (→ `False`).

## f-strings (seen in `operation.py`)
```python
a, b = 5, 10
print(f"Add:{a+b}")
```
`f"..."` is a **formatted string literal** — anything inside `{}` is evaluated as a Python expression and inserted into the string at runtime. It's the modern replacement for `"Add:" + str(a+b)` or `"Add:%d" % (a+b)`.

## How to work with this topic
1. Always ask: "what type of object does this name refer to right now?"
2. Never shadow built-in names.
3. Use f-strings for any string formatting rather than concatenation.
4. Remember immutable vs mutable — it decides whether an operation changes the object in place or creates a new one, which becomes critical once you pass variables into functions (mutable objects can be changed by the function; immutable ones can't).
