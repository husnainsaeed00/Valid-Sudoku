class Solution:
    def isValidSudoku(self, board):
        # Check each row
        for row in board:
            if not self.isUnique(row):
                return False

        # Check each column
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.isUnique(column):
                return False

        # Check each sub-box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
                if not self.isUnique(sub_box):
                    return False

        return True

    def isUnique(self, nums):
        num_set = set()
        for num in nums:
            if num == '.':
                continue
            if num in num_set:
                return False
            num_set.add(num)
        return True
