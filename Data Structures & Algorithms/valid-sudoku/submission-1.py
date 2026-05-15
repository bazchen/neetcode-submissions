class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Solution 1: Brute Force
        print(board)

        # Check each row - O(1)
        for row in range(9):
            seen = set()
            for col in range(9):
                char = board[row][col]
                if char == '.':
                    continue
                elif char in seen:
                    return False
                seen.add(board[row][col])

        # Check each col - O(81 = 1)
        for col in range(9):
            seen = set()
            for row in range(9):
                char = board[row][col]
                if char == '.':
                    continue
                elif char in seen:
                    return False
                seen.add(board[row][col])

        # Check each square - O(81 = 1)
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    char = board[row][col]
                    if char == '.':
                        continue
                    elif char in seen:
                        return False
                    seen.add(board[row][col])

        return True