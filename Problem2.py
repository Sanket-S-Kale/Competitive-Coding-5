## Problem 2 https://leetcode.com/problems/valid-sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Time Complexity: O(1) or O(N^2) where N is 9. 
        Since the board is strictly fixed at 9x9, we do a maximum of 81 iterations. 
        Checking and adding to a hash set takes O(1) time on average.
        
        Space Complexity: O(1) or O(N^2). 
        We use three arrays of 9 sets. Each set can hold at most 9 elements. 
        Thus, the maximum space used is bounded by a constant (81 elements * 3 arrays).
        """
        rows = len(board)
        cols = len(board[0])
        
        # Initialize an array of 9 sets to keep track of seen numbers in each row
        setrow = [set() for _ in range(9)]
        # Initialize an array of 9 sets for each column
        setcol = [set() for _ in range(9)]
        # Initialize an array of 9 sets for each 3x3 sub-box
        set33 = [set() for _ in range(9)]

        def helper(r, c):
            # Calculate the 1D index for the 3x3 sub-box (0 to 8)
            # r // 3 maps rows 0-2 to 0, 3-5 to 1, 6-8 to 2
            # c // 3 does the same for columns. Multiplying the row mapping by 3 flattens it.
            set33idx = (3 * (r // 3)) + (c // 3)

            # If the current number already exists in its respective row, column, or 3x3 box, 
            # then it violates the Sudoku rules
            if board[r][c] in setrow[r] or board[r][c] in setcol[c] or board[r][c] in set33[set33idx]:
                return False
            else:
                # Otherwise, record this number as "seen" in the current row, column, and 3x3 box
                setrow[r].add(board[r][c])
                setcol[c].add(board[r][c])
                set33[set33idx].add(board[r][c])
                return True

        result = True
        
        # Iterate through every cell in the 9x9 board
        for r in range(rows):
            for c in range(cols):
                # We only process cells that contain numbers (ignore empty cells marked by '.')
                if board[r][c] != '.':
                    # Check if the current number is valid using the helper function
                    result = result and helper(r, c)
                    
                    # Short-circuit: if a violation is found, immediately return False
                    if not result:
                        return False

        # If we successfully iterate through the board without violations, the board is valid
        return result