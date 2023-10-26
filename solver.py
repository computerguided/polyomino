def bounding_box(shape):
    return (max([p[0] for p in shape]) - min([p[0] for p in shape]) + 1,
            max([p[1] for p in shape]) - min([p[1] for p in shape]) + 1)

def can_place(shape, x, y, grid):
    box_width, box_height = bounding_box(shape)
    if x + box_width > len(grid) or y + box_height > len(grid[0]):
        return False
    
    for dx, dy in shape:
        if x + dx >= len(grid) or y + dy >= len(grid[0]) or grid[x+dx][y+dy] != 0:
            return False
    return True

def place_shape(shape, x, y, grid, value):
    for dx, dy in shape:
        grid[x + dx][y + dy] = value

def rotate_shape(shape):
    return [(y, -x) for x, y in shape]

shapes = [
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (1, 0)]
]

# Sort shapes by size (largest first)
shapes.sort(key=lambda s: -len(s))

def solve(grid, shapes, shape_idx):
    if shape_idx == len(shapes):
        return True

    for rotation in range(4):
        shape = shapes[shape_idx]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if can_place(shape, x, y, grid):
                    place_shape(shape, x, y, grid, shape_idx + 1)
                    if solve(grid, shapes, shape_idx + 1):
                        return True
                    place_shape(shape, x, y, grid, 0)  # Reset the grid
        shapes[shape_idx] = rotate_shape(shape)  # Try the next rotation

    return False

grid = [[0 for _ in range(5)] for _ in range(5)]

if solve(grid, shapes, 0):
    for row in grid:
        print(' '.join(map(str, row)))
else:
    print("No solution found")
