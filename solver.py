blue    = [(0, 0), (1, 0), (1, 1)]
green   = [(0, 0), (0, 1), (0, 2), (1, 1)]
magenta = [(0, 1), (1, 0), (1, 1)]
red     = [(0, 0), (1, 0), (2, 0), (3, 0)]
orange  = [(0, 1), (1, 1), (2, 0), (2, 1)]
yellow  = [(0, 0), (0, 1)]
gray    = [(0, 0), (0, 1), (1, 0), (2, 0), (2, 1)]

shapes = [blue, green, magenta, red, orange, yellow, gray]

def rotate_shape(shape, num_rotations):
    """Rotate the given shape by 90 degrees clockwise for the specified number of times, 
    shift it to have non-negative indices, and sort it by row and then by column."""
    
    for _ in range(num_rotations):
        shape = [(y, -x) for x, y in shape]
        
        # Find the minimum x and y coordinates
        min_x = min([coord[1] for coord in shape])
        min_y = min([coord[0] for coord in shape])
        
        # Shift the shape to have non-negative indices
        shape = [(y - min_y, x - min_x) for y, x in shape]
    
    # Sort the shape by row and then by column
    shape.sort(key=lambda coord: (coord[0], coord[1]))
    
    return shape

def create_empty_matrix(rows, cols):
    """Create an empty matrix of given rows and cols filled with zeros."""
    return [[0 for _ in range(cols)] for _ in range(rows)]

def place_shape(matrix, shape, position):
    """
    Place the given shape at the specified position in the matrix.
    
    Args:
    - matrix (List[List[int]]): The current matrix.
    - shape (List[Tuple[int, int]]): The shape to be placed.
    - position (Tuple[int, int]): The position (row, column) to place the shape.
    
    Returns:
    - List[List[int]]: The new matrix with the shape placed. If placement is not possible, returns None.
    """
    new_matrix = [row.copy() for row in matrix]

    for cell in shape:
        row, col = cell
        new_row = position[0] + row
        new_col = position[1] + col

        # Check boundaries
        if new_row < 0 or new_row >= len(matrix) or new_col < 0 or new_col >= len(matrix[0]):
            return None
        
        new_matrix[new_row][new_col] += 1

        # Check for overlap
        if new_matrix[new_row][new_col] > 1:
            return None

    return new_matrix


def remove_shape(matrix, shape, position):
    """
    Removes the given shape from the matrix at the specified position.

    Args:
    - matrix (List[List[int]]): The current matrix.
    - shape (List[Tuple[int, int]]): The shape to be removed.
    - position (Tuple[int, int]): The position in the matrix where the shape's (0, 0) cell should be placed.

    Returns:
    - List[List[int]]: The matrix after removing the shape.
    """
    new_matrix = [row.copy() for row in matrix]
    
    for cell in shape:
        x, y = cell
        new_matrix[position[0] + x][position[1] + y] -= 1
        
    return new_matrix

def solve(matrix, shapes):
    """
    Tries to fit all shapes into the matrix using DFS.
    
    Args:
    - matrix (List[List[int]]): The current matrix.
    - shapes (List[List[Tuple[int, int]]]): A list of shapes to be placed.
    
    Returns:
    - List[Tuple[List[Tuple[int, int]], Tuple[int, int], int]]: A list of tuples where each tuple contains the shape,
      its position in the matrix, and its rotation. If no solution is found, returns an empty list.
    """
    if not shapes:
        return []

    current_shape = shapes[0]

    # Try to fit the shape in all possible rotations and positions
    for rotation in range(4):
        rotated_shape = rotate_shape(current_shape, rotation)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                position = (row, col)

                # Place the shape
                new_matrix = place_shape(matrix.copy(), rotated_shape, position)
                
                # Check if there's an overlap
                if new_matrix is not None:
                    # Recursively try to fit the remaining shapes
                    result = solve(new_matrix, shapes[1:])

                    if result is not None:
                        return [(rotated_shape, position, rotation)] + result

    # If no solution is found
    return None


matrix = create_empty_matrix(5, 5)
result = solve(matrix, shapes)

if result is None:
    print("No solution found.")
else:
    for shape, position, rotation in result:
        print(f"Shape: {shape}, Position: {position}, Rotation: {rotation}")