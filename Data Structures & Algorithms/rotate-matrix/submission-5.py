class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        #reverse
        
        for i in range(rows//2):
            matrix[i], matrix[rows - i - 1] = matrix[rows - i - 1], matrix[i]

        #transpose
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
