class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        a = []
        def f(i, c, t):
            if t == target:
                a.append(c.copy())
                return
            if t > target or i == len(candidates):
                return
            f(i, c + [candidates[i]], t + candidates[i])
            f(i + 1, c, t)
        f(0, [], 0)
        return a