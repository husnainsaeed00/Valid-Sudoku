# Sudoku Validator

## Problem Description

Given a 9 x 9 Sudoku board, determine if it is valid. Only the filled cells need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

## Example

Input:
[
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]


Output:
true


## Solution

The solution involves iterating over each row, column, and 3 x 3 sub-box of the Sudoku board. For each row, column, or sub-box, we check if the numbers 1-9 appear without repetition. If any repetition is found, the board is considered invalid.

The solution can be implemented using a class `Solution` with the following methods:
- `isValidSudoku(board)`: Checks the validity of the Sudoku board based on the rules mentioned above.
- `isUnique(nums)`: Helper method to check if a list of numbers has unique elements.

The `isValidSudoku` method iterates over each row, column, and sub-box, and uses the `isUnique` method to check for uniqueness. If any of the checks fail, the method returns `False`. If all checks pass, the method returns `True`.

## Usage

1. Create a 9 x 9 Sudoku board in the form of a nested list, where each element represents a cell on the board.
2. Create an instance of the `Solution` class.
3. Call the `isValidSudoku` method on the instance, passing the Sudoku board as an argument.
4. The method will return `True` if the board is valid, and `False` otherwise.

Example code:

```python
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

solution = Solution()
print(solution.isValidSudoku(board))  # Output: True
Complexity Analysis
The time complexity of the solution is O(1) since the board size is fixed (9 x 9).

The space complexity is also O(1) since we are using a constant amount of extra space to store the number set.


Time Complexity: O(1)
Space Complexity: O(1)
License
This project is licensed under the MIT License.
