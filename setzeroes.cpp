class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        coords=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    coords.append([i,j])
        for i in coords:
            for _ in range(len(matrix)):
                for __ in range(len(matrix[0])):
                    if _==i[0] or __==i[1]:
                        matrix[_][__]=0
        
