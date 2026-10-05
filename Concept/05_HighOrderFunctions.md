# Higher-Order Functions: map, filter, reduce, sorted, lambda

A **higher-order function** is a function that takes another function as an argument (or returns one). This is possible in Python because **functions are objects** — you can pass them around just like a number or a string.

## Functions recap (`HighOrder/Function.py`)
```python
def add(a, b):
    sum = a + b
    print(sum)
add(5, 10)
```
- `def` declares a function. Code inside only runs when the function is **called** (`add(5,10)`), not when it's defined.
- Parameters (`a`, `b`) are local names bound to whatever arguments are passed in.
- `return` sends a value back to the caller; a function with no `return` implicitly returns `None`. (Your `add()` only `print`s — it doesn't `return` the sum, so `add(5,10)` can't be used in an expression like `x = add(5,10) + 1`. Fine for a quick script, but worth knowing the difference between "printing a result" and "returning a result.")

## lambda — anonymous, throwaway functions
```python
lambda x: x > 20
```
A `lambda` is a function with no name, restricted to a **single expression** (no multiple statements, no loops). It's used when a function is needed briefly, usually as an argument to another function, and naming it with `def` would be overkill.

```python
def is_even(x):      # equivalent, named version
    return x % 2 == 0
is_even_lambda = lambda x: x % 2 == 0
```

## filter(function, iterable) → keeps elements where function returns True
```python
list(filter(lambda x: x > 20, [10, 25, 30, 15, 40]))   # [25, 30, 40]
```
`filter` calls the function on every element and **keeps only the ones that return a truthy value**. It returns a `filter` object (a lazy iterator), so you wrap it in `list(...)` to see the actual results. `Filter.py` covers: evens, "greater than 20," negatives, strings starting with `"P"`, and (intentionally inverted logic, worth noting) a function literally named `empty` that returns `True` for empty strings — used with `filter`, this *keeps* only the empty strings, which is the opposite of the exercise's stated goal ("remove all empty strings"). To actually remove them you'd filter with `lambda x: x != ""` instead.

## map(function, iterable) → transforms every element
```python
list(map(lambda x: x.upper(), ["python", "java"]))   # ['PYTHON', 'JAVA']
```
Unlike `filter` (keep/drop), `map` **transforms every single element** and returns the same number of elements you started with. `Map.py` also shows `map()` with **two iterables at once**:
```python
list(map(lambda x, y: x + y, [1,2,3], [4,5,6]))   # [5, 7, 9]
```
Here the lambda takes two arguments, and `map` pulls one value from each list per call, pairing them up by position.

## reduce(function, iterable) → collapses to a single value
```python
from functools import reduce
reduce(lambda x, y: x + y, [5, 10, 15, 20])   # 50
```
`reduce` is **not a builtin** — it lives in `functools` and must be imported. It works by repeatedly applying a two-argument function: first to elements 1 & 2, then to that result & element 3, then to that result & element 4, and so on, until one value remains.
```
reduce(f, [5,10,15,20])
= f(f(f(5,10),15),20)
```
This is why `reduce` is perfect for "largest/smallest/sum/product/concatenate" — anything where you combine a running result with the next item. `Reduce.py`'s `largest = lambda x,y: x if x>y else y` keeps the bigger of two values each step, so by the end only the overall largest survives.

## sorted(iterable, key=..., reverse=...) → new sorted list
```python
sorted([15, 2, 30, 8, 21])                      # ascending
sorted([15, 2, 30, 8, 21], reverse=True)        # descending
sorted(["cat","elephant","dog"], key=len)       # sort by a derived value, not the value itself
sorted(students, key=lambda x: x[1])            # sort tuples by their 2nd element (marks)
```
**`key=` is the single most important concept here.** It doesn't sort by that value directly — it tells `sorted()` **what to compute for each element**, then sorts the *original elements* based on those computed values. `sorted(number, key=lastDigit)` sorts actual numbers like `25, 12, 43` but orders them according to each one's last digit, not the number's own size.

`sort()` (list method, in-place, returns `None`) vs `sorted()` (builtin function, returns a *new* list, leaves the original untouched) — `list.py` uses `.sort()`, `sort.py` uses `sorted()`; know which one you're calling.

## How these four connect
| Function | Input → Output | Mental model |
|---|---|---|
| `map` | n elements → n elements | "transform each" |
| `filter` | n elements → ≤n elements | "keep some" |
| `reduce` | n elements → 1 value | "combine all into one" |
| `sorted` | n elements → n elements, reordered | "arrange by some rule" |

## How to work with this topic
1. Reach for `map`/`filter`/`reduce`/`sorted` instead of writing a manual `for` loop once you're comfortable — they express *intent* more clearly ("transform," "keep," "combine," "order").
2. `lambda` is for short, one-off, single-expression functions passed inline; use a normal `def` once the logic needs more than one line or you want to reuse it elsewhere.
3. Always double check the *direction* of a `filter` condition — "keep if True" is easy to accidentally write backwards (as in the empty-string example above).
4. `reduce` requires `from functools import reduce` — it's the one of these four not built into the global namespace.
