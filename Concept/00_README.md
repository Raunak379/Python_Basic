# Concept Notes — Index

Deep-dive explanations for every topic practiced in this repository. Each file explains **what the concept is, how it actually works under the hood, and how it connects to the exercises already written** in the corresponding source folder — plus any bugs/gotchas spotted along the way.

| File | Covers | Source folder |
|---|---|---|
| [01_Variables_DataTypes.md](01_Variables_DataTypes.md) | Variables as name-bindings, dynamic typing, mutability, f-strings | `Variable&DataType/` |
| [02_ControlFlow_Loops.md](02_ControlFlow_Loops.md) | if/elif/else, match-case, for/while, break/continue/pass | `ControlFlow&Loops/` |
| [03_Strings_Collections.md](03_Strings_Collections.md) | String indexing & slicing, sequence rules | `String&collection/` |
| [04_Collections_List_Tuple_Set_Dict.md](04_Collections_List_Tuple_Set_Dict.md) | list, tuple, set, dict — mutability, ordering, use cases | `Collection/` |
| [05_HighOrderFunctions.md](05_HighOrderFunctions.md) | functions, lambda, map, filter, reduce, sorted | `HighOrder/` |
| [06_OOP.md](06_OOP.md) | Classes/objects, encapsulation, inheritance, polymorphism, abstraction, class vs instance attributes | `ObjectOrientedProgram/` |
| [07_ExceptionHandling.md](07_ExceptionHandling.md) | try/except/else/finally, custom exceptions | `Exception_Handling/` |
| [08_FileHandling.md](08_FileHandling.md) | File modes (r/w/a), reading, writing, copying, searching | `FileHandling/` |
| [09_DSA.md](09_DSA.md) | Array, Stack, Queue, Circular Queue, Deque, Linked List, BST, Tree Traversal, Graph, Recursion | `DSA/` |

## Suggested reading order
1-5 build the language fundamentals (data, control flow, collections, functional tools). 6-8 build real program structure (OOP, error handling, I/O). 9 is the capstone — it reuses almost every earlier concept (classes from OOP, recursion, loops, lists) to build real data structures.

## How these notes were made
Each file was written by reading the actual `.py` exercises in this repo and explaining the concept the way it's used there — including a few bugs spotted along the way (e.g. an empty `DSA/Queue.py`, an unfinished `printGraph` in `DSA/Graph.py`, a `list[fruits]` typo in `Collection/Tuples.py`, and `DSA/Recursion.py` currently holding commented-out linked-list code instead of recursion examples). Treat those call-outs as a punch list if you want the repo fully clean.
