from bisect import bisect_right
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)

        dp = [(0, 0)]

        for s, e, p in jobs:

            i = bisect_right(dp, (s, float('inf'))) - 1
            curr_profit = dp[i][1] + p


            if curr_profit > dp[-1][1]:
                dp.append((e, curr_profit))

        return dp[-1][1]
