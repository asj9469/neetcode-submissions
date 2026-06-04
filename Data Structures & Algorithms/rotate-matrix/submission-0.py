class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # matrix rotation = same thing as reversing and then transposing

        # reverse
        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]

        # transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return

        