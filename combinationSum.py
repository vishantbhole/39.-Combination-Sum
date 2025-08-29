# 39. Combination Sum
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if target == total:
                res.append(cur.copy())
                return
            if i >= len(candidates) or target < total:
                return
