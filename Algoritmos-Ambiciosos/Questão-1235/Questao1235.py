from bisect import bisect_right
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [(0, 0)]

        for s, e, p in jobs:
            i = bisect_right(dp, (s, float('inf'))) - 1
            curr_profit = dp[i][1] + p

            if curr_profit > dp[-1][1]:
                dp.append((e, curr_profit))

        return dp[-1][1]

if __name__ == "__main__":
    test_cases = [
        {
            "startTime": [1, 2, 3, 3],
            "endTime": [3, 4, 5, 6],
            "profit": [50, 10, 40, 70],
            "expected": 120
        },
        {
            "startTime": [1, 2, 3, 4, 6],
            "endTime": [3, 5, 10, 6, 9],
            "profit": [20, 20, 100, 70, 60],
            "expected": 150
        },
        {
            "startTime": [1, 1, 1],
            "endTime": [2, 3, 4],
            "profit": [5, 6, 4],
            "expected": 6
        }
    ]

    sol = Solution()
    for i, test in enumerate(test_cases, 1):
        result = sol.jobScheduling(test["startTime"], test["endTime"], test["profit"])
        print(f"Teste {i}: resultado = {result} | esperado = {test['expected']}")