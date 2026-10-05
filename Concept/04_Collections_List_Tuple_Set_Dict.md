# Collections: List, Tuple, Set, Dictionary

Python has four built-in "container" types. The most important mental model is: **which are ordered, which allow duplicates, which are mutable, and what's each one actually for.**

| Type | Syntax | Ordered | Duplicates | Mutable | Lookup |
|---|---|---|---|---|---|
| `list` | `[1,2,3]` | Yes | Yes | Yes | by index (fast), by value (slow, O(n)) |
| `tuple` | `(1,2,3)` | Yes | Yes | **No** | by index (fast) |
| `set` | `{1,2,3}` | No* | **No** | Yes | by value (fast, O(1) hash-based) |
| `dict` | `{"k":"v"}` | Yes (insertion order, 3.7+) | Keys: No. Values: Yes | Yes | by key (fast, O(1) hash-based) |

*sets have no guaranteed order — don't rely on iteration order.

## List — the general-purpose, mutable, ordered container
```python
Fruits = ["apple", "banana", "orange"]
Fruits[3] = "kiwi"          # modify in place (mutable!)
Fruits.append("Watermelon") # add to end
Fruits.insert(2, "grapes")  # add at specific index
Fruits[::-1]                # reversed copy
Fruits.sort()               # in-place ascending sort
Fruits.sort(reverse=True)   # in-place descending sort
```
Because lists are mutable, `.append()`/`.insert()`/`.sort()` **change the original list** and return `None` — this trips people up (`x = Fruits.sort()` makes `x` be `None`, not the sorted list). Use `sorted(Fruits)` if you want a *new* sorted list without touching the original.

### Manual algorithms practiced in `list.py`
- **Largest/smallest without `max()`/`min()`**: start with the first element as a running "best," compare every other element, replace when a bigger/smaller one appears. This O(n) linear scan is the basis of basically every "find X in an unsorted collection" problem.
- **Second largest**: needs two tracking variables (`large`, `Seclarge`) — one bug to watch for in your code: inside the first loop you assign to `larg` (a typo-different variable from `large`), so `large` itself never updates. The intended fix is to use one consistent variable name throughout.
- **Removing duplicates** — three escalating techniques:
  1. Manual nested loop: for each element, scan the "unique so far" list to check if it's already there (what `in` does internally, done by hand).
  2. Same idea, using the `in` operator directly — `if numbers[i] not in unique`.
  3. **The idiomatic one-liner**: `list(dict.fromkeys(lst))` — builds a dict from the list (dict keys are automatically deduplicated) then converts back to a list. This also preserves original order, unlike converting to a `set`.
- **Sum of all elements via `reduce`**: `reduce(add, num)` repeatedly applies `add(x,y)` across the list, collapsing it to a single value — this is the functional-programming way to total a list instead of a manual loop with an accumulator.

## Tuple — immutable, ordered
```python
fruits = ("apple", "Banana", "mango")
```
Once created, you can **never** change, add, or remove elements (`fruits[0] = "x"` → `TypeError`). Use a tuple when the data shouldn't change — e.g., fixed coordinates `(x, y)`, or when you want a dict key (lists can't be dict keys because they're mutable — a key's hash must never change; tuples *can* be keys because they're immutable).

- **Unpacking**: `a, b, c, d = (1,2,3,4)` assigns each element to a variable in one line — extremely common for returning multiple values from a function.
- **Nested tuples**: `num[1][1]` — first index picks the inner tuple, second index picks an element inside it. Same rule applies to nested lists.
- `Tuples.py` has a bug: `new_list = list[fruits]` should be `new_list = list(fruits)` — `list[fruits]` tries to subscript the `list` *type itself* with a tuple, which raises `TypeError: type 'list' is not subscriptable with ...` in this context (and is further confused because `list` may already be shadowed elsewhere in the repo).

## Set — unordered, unique, hash-based
```python
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set1 | set2   # union        → all elements from both
set1 & set2   # intersection → elements in both
set1 - set2   # difference   → in set1 but not set2
(set1-set2) | (set2-set1)   # symmetric difference → in exactly one of the two
```
Sets exist to answer two questions **extremely fast**: "is this value in here?" and "what does this collection have in common with that one?" They're backed by a hash table, so membership checks (`x in my_set`) are O(1) on average, versus O(n) for a list.

- **Deduplicating a list via a set**: `set(num)` — since a set can't hold duplicates, converting drops them automatically. (Your code uses `set(dict.fromkeys(num))`, which works but is redundant — `dict.fromkeys` already dedupes, so wrapping it in `set()` again is unnecessary; plain `set(num)` is simpler. The tradeoff: a plain `set(num)` loses original order entirely, while `dict.fromkeys(num)` preserves order — so pick based on whether order matters.)
- **Subset / disjoint checks**: `A.issubset(B)` (is every element of A also in B), `A.isdisjoint(B)` (do A and B share zero elements).

## Dictionary — key/value store
```python
dict = {"name": "Raunak", "age": 21, "city": "Siwan"}
dict.get("name")      # safe lookup — returns None (or a default) instead of crashing if missing
dict["name"] = "x"    # modify existing key
dict["course"] = "bca" # add new key
dict.pop("name")       # remove a key (and return its value)
for key in dict: ...               # iterates over KEYS by default
for value in dict.values(): ...    # iterates over values
for key, value in dict.items(): ...# iterates over pairs — the most common pattern
"age" in dict          # membership check — checks KEYS, not values
```
Keys must be **immutable & hashable** (strings, numbers, tuples) — this is exactly why lists can't be dict keys but tuples can.

### Patterns from `Dictionaries.py`
- **Character frequency counter**:
  ```python
  frequency = {}
  for char in text:
      if char in frequency:
          frequency[char] += 1
      else:
          frequency[char] = 1
  ```
  This "if key exists, increment; else, initialize to 1" pattern is one of the most common dict idioms. (It can be simplified with `frequency[char] = frequency.get(char, 0) + 1`, or with `collections.Counter(text)`.)
- **Finding the max value's key**: manual linear scan (`method 1`) vs. the idiomatic `max(marks, key=marks.get)` (`method 2`) — the `key=` argument tells `max()` *what to compare* (here, each name's mark) while still returning the *name*, not the mark. This `key=` pattern reappears constantly in Python (`sorted()`, `min()`, `max()`).
- **Merging dicts**: `dict1.update(dict2)` merges `dict2` into `dict1` in place; on key collisions, `dict2`'s values win.
- **Reversing keys/values**: swapping `{k: v}` → `{v: k}` only works safely if values are unique and hashable — if two keys share a value, one entry silently overwrites the other.

## How to work with this topic
1. Need order + duplicates + the ability to change it later → **list**.
2. Need order + duplicates but it must never change → **tuple**.
3. Need fast membership tests / set algebra / automatic dedup, don't care about order → **set**.
4. Need to look things up by a meaningful label instead of a numeric position → **dict**.
5. Before writing a manual loop, ask "does Python already have a built-in/method for this?" (`max`, `min`, `sorted`, `dict.fromkeys`, `Counter`) — your repo deliberately practices both the manual and idiomatic approach, which is the right way to *learn* the concept, but production code should default to the idiomatic one.
