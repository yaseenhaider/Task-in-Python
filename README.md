# Task-in-Python

A collection of beginner-friendly Python practice scripts covering list/dictionary basics, DFS/BFS search, simple expert-system examples, and console input exercises.

## Table of Contents

- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Scripts by Category](#scripts-by-category)
  - [Basics and List Operations](#basics-and-list-operations)
  - [Graph/Search (BFS/DFS)](#graphsearch-bfsdfs)
  - [Expert System / Diagnosis](#expert-system--diagnosis)
  - [Console Input Programs](#console-input-programs)
  - [Other Repository Files](#other-repository-files)
- [Known Issues](#known-issues)

## Project Structure

The repository currently stores scripts directly in the root folder (no subfolders yet). Most files are standalone and can be run individually.

## Requirements

- Python 3.x (Python 3.8+ recommended)
- No third-party dependencies (standard library only)

## How to Run

From the repository root:

```bash
python <script_name>.py
```

Examples:

```bash
python Q1.py
python "DFS assignment.py"
```

## Scripts by Category

### Basics and List Operations

- **Act.py**  
  Empty placeholder file (currently contains no executable code).

- **Act6.py**  
  Demonstrates list slicing with ranges, from-index slicing, and full-list slicing on a character list.

- **act7.py**  
  Shows dictionary creation examples using integer keys and mixed key types.

- **act8.py**  
  Intentionally triggers a `ZeroDivisionError` to demonstrate runtime error behavior.

- **act9.py**  
  Compares `append()` vs `extend()` on lists and prints the difference in resulting list structure.

- **Question4.py**  
  Demonstrates `append`, `extend`, and `insert` operations on a borrowed books list.

- **Question5.py**  
  Uses list slicing to print first-week sales, last 5 days, alternate days, and reverse order.

### Graph/Search (BFS/DFS)

- **Q1.py**  
  Recursive DFS maze solver that finds a path, marks start/goal, and prints the solved maze grid.

- **DFS assignment.py**  
  Stack-based DFS maze traversal with neighbor generation and simple backtracking behavior.

- **Q2.py**  
  BFS shortest-path search in a small friendship graph; returns path between two users.

- **question 2 BFS.py**  
  BFS social-network path reconstruction using parent tracking in a queue-based traversal.

### Expert System / Diagnosis

- **Q3.py**  
  Simple symptom-based medical lookup that prints possible diseases with cause, symptoms, and treatment.

- **Question3.py**  
  DFS-style traversal over a symptom tree to accumulate possible diagnoses from linked symptom nodes.

### Console Input Programs

- **Qustion1.py**  
  Reads trip distances until `0` is entered, then prints total distance and average per trip.

- **Question2.py**  
  Takes principal, annual rate, and years from input and prints year-by-year compound balance.

### Other Repository Files

- **DSA practice.dev**  
  Dev-C++ project configuration file (not a Python script).

- **Yaseen Haider (SP24-BSE-070).zip**  
  Archive file included in repository.

## Known Issues

- In **Question3.py**, `current_symptom = 'Fever'` does not match keys in `symptom_tree` (e.g., `bukhar`, `khansi`), so the script prints an empty diagnosis set.
- In **question 2 BFS.py**, the graph contains `'Sunil'` but the script starts from `'sunil'`, which raises a `KeyError` due to case mismatch.
- Some filenames contain spaces or typos (for example, `DFS assignment.py`, `Qustion1.py`), which can be inconvenient to run and maintain.
