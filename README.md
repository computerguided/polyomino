# Polyomino Packing Problem Solver


<svg viewBox="0 0 70 60" xmlns="http://www.w3.org/2000/svg">
  <path style="stroke: rgb(0, 0, 0); fill-opacity: 0.8; fill: none; transform-box: fill-box; transform-origin: 50% 50%;" d="M 22.08 47.055 C 22.08 47.762 14.658 17.545 14.658 17.545 L 53.357 25.85 L 22.08 47.055 Z"/>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); transform-box: fill-box; transform-origin: 50% 50%;" cx="14.746" cy="17.81" rx="4.329" ry="4.329"/>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); transform-box: fill-box; transform-origin: 50% 50%;" cx="53.268" cy="25.85" rx="4.329" ry="4.329"/>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); transform-box: fill-box; transform-origin: 50% 50%;" cx="22.08" cy="46.172" rx="4.329" ry="4.329"/>
</svg>

## Overview
This program aims to solve a polyomino packing problem, where the goal is to place a set of predefined shapes onto a matrix without any overlaps or shapes going outside the matrix boundaries. The shapes can be rotated as needed. The solution provides the locations and number of clockwise rotations for each shape.

## Design

### Data Structures

1. **Shapes**: Represented as a list of tuples. Each tuple contains the (row, column) coordinate of a block in the shape relative to the top-left block.

```python
blue    = [(0, 0), (1, 0), (1, 1)]
green   = ...
...
shapes = [blue, green, ...]
```

2. **Matrix**: A 2D list of integers where each block is represented by an integer. Initially, all blocks are set to 0. When a shape is placed, the corresponding blocks are incremented.

### Core Functions

1. ``rotate_shape()``: Rotates a given shape 90 degrees clockwise.

2. ``generate_empty_matrix()``: Generates an empty matrix of the given dimensions.

3. ``place_shape()``: Attempts to place a shape onto the matrix at a given location. Returns `None` if the shape can't be placed.

4. ``remove_shape()``: Removes a shape from the matrix.

5. ``solve()``: The main function that recursively attempts to place each shape onto the matrix, backtracking as necessary.

## Implementation

The primary approach is a depth-first search algorithm. For each shape:

1. Rotate the shape (0 to 3 times) and try to fit it in the current matrix.
2. If the shape fits, proceed with the next shape.
3. If the shape doesn't fit in any rotation, backtrack to the previous shape and continue searching.

The search stops when all shapes are successfully placed or all possibilities are exhausted.

## Usage

1. Define your shapes and initialize the matrix.
2. Call the `solve()` function.
3. If a solution is found, it will be printed with the shape's position and number of rotations.

```python
matrix = create_empty_matrix(5, 5)
result = solve(matrix, shapes)

if result is None:
    print("No solution found.")
else:
    for shape, position, rotation in result:
        print(f"Shape: {shape}, Position: {position}, Rotation: {rotation}")
```
