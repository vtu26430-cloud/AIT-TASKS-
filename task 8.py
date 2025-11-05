def is_safe(board, row, col, n):
    """
    Check if placing a queen at (row, col) is safe
    """
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens_util(board, row, n, solutions):
    """
    Recursive utility to place queens row by row
    """
    if row == n:
        # Found a solution, add a copy to solutions
        solutions.append([''.join('Q' if c == 1 else '.' for c in r) for r in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1           # Place queen
            solve_n_queens_util(board, row + 1, n, solutions)  # Recurse for next row
            board[row][col] = 0           # Backtrack

def solve_n_queens(n):
    """
    Solve the N-Queens problem and return all solutions
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

# Example usage
if __name__ == "__main__":
    N = 4
    solutions = solve_n_queens(N)
    print(f"Total solutions for {N}-Queens: {len(solutions)}\n")
    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for row in sol:
            print(row)
        print()
