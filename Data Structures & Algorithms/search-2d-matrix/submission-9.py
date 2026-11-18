class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        tops, bots = 0 , row -1

        while tops <= bots:
            row = (tops+bots)//2

            if target < matrix[row][0]:
                bots = row -1
            elif target > matrix[row][-1]:
                tops = row +1
            else:
                break
        if not (tops <= bots):
            return False
        
        rows = (tops+ bots) // 2

        l,r = 0, col -1

        while l<=r:
            m = (l+r)//2

            if target < matrix[row][m]:
                r = m -1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
        return False