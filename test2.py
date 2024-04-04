def is_valid(board, row, col, n):
    # Check if L-shaped piece can be placed at position (row, col)
    return (
        row >= 0 and row < n - 1 and col >= 0 and col < n - 1 and
        board[row][col] == 0 and board[row][col + 1] == 0 and board[row + 1][col] == 0
    )

def tile_util(board, row, col, n):
    # Base case: If all squares are filled
    if row == n:
        return True

    next_row = 0
    next_col = 0

    # Move to next row and column
    if col == n - 1:
        next_row = row + 1
        next_col = 0
    else:
        next_row = row
        next_col = col + 1

    # If the current square is not empty, move to the next square
    if board[row][col] == 1:
        return tile_util(board, next_row, next_col, n)

    # Try placing L-shaped piece at (row, col)
    if is_valid(board, row, col, n):
        board[row][col] = board[row][col + 1] = board[row + 1][col] = 1
        if tile_util(board, next_row, next_col, n):
            return True
        # Backtrack
        board[row][col] = board[row][col + 1] = board[row + 1][col] = 0

    # Try placing L-shaped piece at the next square
    if tile_util(board, next_row, next_col, n):
        return True

    return False

def tile_square(n, removed_square):
    board = [[0]*n for _ in range(n)]

    # Mark removed square as filled
    for row, col in removed_square:
        board[row][col] = 1

    if tile_util(board, 0, 0, n):
        print("Tiling Possible:")
        for row in board:
            print(row)
    else:
        print("Tiling Not Possible")

# Example usage
n = 4
removed_square = [(1, 1)]
tile_square(n, removed_square)
