class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        a = []
        for i in range(numRows):
            b = [1] * (i + 1)
            for j in range(1, i):
                b[j] = a[i - 1][j - 1] + a[i - 1][j]
            a.append(b)
        return a