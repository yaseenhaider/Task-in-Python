# Task in Python

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Practice-Scripts-success)

A curated collection of beginner-friendly Python practice scripts covering list operations, DFS/BFS search, and simple console programs.

## Table of Contents
- [Project Structure](#project-structure)
- [Scripts](#scripts)
- [How to Run](#how-to-run)

## Project Structure

```text
Task-in-Python/
├── basics/
├── console_programs/
├── expert_systems/
├── search_graphs/
└── archive/
```

## Scripts

### `basics/`
- `empty_script.py`  
  Placeholder empty script file.
- `list_slicing_demo.py`  
  Demonstrates slicing ranges, suffixes, and full-copy behavior on a list.
- `dictionary_creation_demo.py`  
  Shows dictionary creation using integer keys and mixed key types.
- `zero_division_error_demo.py`  
  Demonstrates a runtime `ZeroDivisionError`.
- `list_append_vs_extend_demo.py`  
  Compares how `append()` and `extend()` affect list structure.

### `search_graphs/`
- `dfs_maze_solver_recursive.py`  
  Recursive depth-first search maze solver that marks and prints the final path.
- `dfs_maze_solver_stack.py`  
  Stack-based DFS maze traversal using a neighbor helper function.
- `bfs_friends_graph_shortest_path.py`  
  Uses BFS to find a shortest friend-connection path in a small graph.
- `bfs_social_network_path.py`  
  BFS social-network path reconstruction using parent tracking.

### `expert_systems/`
- `medical_expert_system_simple.py`  
  Prints possible diseases, causes, symptoms, and treatments for a symptom category.
- `medical_diagnosis_dfs_symptom_tree.py`  
  Traverses a symptom tree with DFS to collect possible diagnoses.

### `console_programs/`
- `average_trip_distance_calculator.py`  
  Reads trip distances until `0` and reports total and average distance.
- `compound_interest_yearly_balance.py`  
  Calculates and prints year-by-year compound balance growth.
- `borrowed_books_list_operations.py`  
  Demonstrates `append`, `extend`, and `insert` on a borrowed-books list.
- `sales_slicing_examples.py`  
  Uses slicing to show first week, last five days, alternate, and reverse sales views.

### `archive/`
- `Yaseen Haider (SP24-BSE-070).zip` (original user content retained)
- `dsa_practice.dev` (Dev-C++ project metadata retained)

## How to Run

From the repository root:

```bash
python <path_to_script.py>
```

Examples:

```bash
python basics/list_slicing_demo.py
python search_graphs/dfs_maze_solver_recursive.py
python console_programs/sales_slicing_examples.py
```
