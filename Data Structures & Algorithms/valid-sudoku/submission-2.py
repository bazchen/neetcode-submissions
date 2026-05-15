class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Solution 2: Hash Map One Pass - O(9**2)
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                char = board[r][c]

                # If char is blank, skip
                if char == '.':
                    continue

                # Check if char already appears in its row, col or square
                elif (char in rows[r] or 
                      char in cols[c] or 
                      char in squares[(r // 3, c // 3)]
                      ):
                    return False

                # If pass, the char is valid so add it as seen to it row, col and square map
                cols[c].add(char)
                rows[r].add(char)
                squares[r // 3, c // 3].add(char)

        return True