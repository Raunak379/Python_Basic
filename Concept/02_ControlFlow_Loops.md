# Control Flow & Loops

Control flow decides **which lines of code execute, and how many times**. Python has no braces `{}` — blocks are defined entirely by **indentation** (4 spaces is the convention). Getting indentation wrong is a syntax error, not a style nit.

## if / elif / else
```python
if condition1:
    ...
elif condition2:
    ...
else:
    ...
```
- Python checks conditions **top to bottom** and runs the **first** block whose condition is `True`, then skips the rest entirely (even if a later condition would also be true).
- In `ControlFlow&Loops/if-else.py` (grading program), the order of the `elif` chain matters — if you compare `num > 60` before `num > 90`, a 95 would incorrectly match the `60` branch first. Your code is actually written in *descending* order (90 → 80 → 70 → 60 → 30) which is correct for this pattern.
- `Nestedif.py` shows an **if inside an if** — a vote-eligibility check needs *both* `age >= 18` and `citizen == True`, so the inner `if` only runs after the outer condition passes. This is logically equivalent to `if age >= 18 and citizen:` but demonstrates nesting explicitly.

### Truthiness
Any value can be used as a condition. Falsy values: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`, `False`. Everything else is truthy. So `if citizen:` works directly without writing `if citizen == True:`.

## match-case (structural pattern matching, Python 3.10+)
```python
match day:
    case 1:
        print("Monday")
    case _:
        print("Invalid day")
```
This is Python's version of `switch`. `case _:` is the **wildcard** — it matches anything not caught above, acting like `default`/`else`. Unlike `if/elif`, `match` can also destructure complex data (tuples, lists, objects with specific shapes), which `if/elif` can't do cleanly — your `MatchCase.py` only uses the simple "compare to a literal" form, which is the most common use case (e.g., building a calculator by matching on the operator string `"+"`, `"-"`, etc.).

## for loops
```python
for i in range(1, 6):
    print(i)
```
A `for` loop in Python is really a **"for-each"** — it iterates over any *iterable* (something you can loop over): `range()`, strings, lists, tuples, dicts, sets, files, etc. `range(start, stop, step)`:
- `range(1,6)` → 1,2,3,4,5 (stop is **exclusive**)
- `range(0,20,2)` → 0,2,4,...,18 (step of 2)
- `range(5,-1,-1)` → counts down 5,4,3,2,1,0 (negative step)

### Nested for loops (pattern printing)
```python
for i in range(1, row+1):
    for j in range(i):
        print("*", end="")
    print()
```
The **outer loop controls rows**, the **inner loop controls what's printed in that row**. `end=""` stops `print()` from adding a newline after each `*`, so stars accumulate on one line; the bare `print()` after the inner loop finishes that row and starts a new line. This "outer=row, inner=column" mental model is the key to every pattern/pyramid problem.

## while loops
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```
Runs **as long as the condition stays true**. Unlike `for`, you must manually advance the loop variable (`i += 1`) — forgetting this creates an **infinite loop**.

`while` is the right choice when you don't know the number of iterations in advance. Example from `WhileLoop.py` — counting digits in a number:
```python
count = 0
while number > 0:
    number //= 10   # floor division strips the last digit
    count += 1
```
You can't know ahead of time how many digits a number has, so `for` (which needs a predetermined range) is awkward here; `while` naturally stops once `number` reaches 0.

## break, continue, pass
- **`break`** — exits the loop immediately, skipping all remaining iterations.
- **`continue`** — skips the *rest of the current iteration* only, then moves to the next one.
- **`pass`** — does literally nothing; it's a placeholder where Python's syntax requires a statement (e.g., an empty function body, or "I'll fill this in later").

```python
for i in range(1, 7):
    if i == 3:
        break      # stops entirely at 3 → prints 1, 2
for i in range(1, 7):
    if i == 3:
        continue   # skips only 3 → prints 1,2,4,5,6
```

## How to work with this topic
1. Indentation = block boundaries. Be consistent (spaces, not tabs).
2. For counted/ranged repetition → `for`. For "repeat until a condition changes" → `while`.
3. In nested loops, always ask "what does the outer loop represent, what does the inner loop represent" before writing code.
4. `break` kills the loop; `continue` just skips one lap; `pass` is a no-op placeholder — they're easy to confuse by name but do very different things.
