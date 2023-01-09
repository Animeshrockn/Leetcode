# 875. Koko Eating Bananas

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.


# ===========================================


import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r

        while l<=r:
            
            mid = (l+r)//2
            hours = 0
            for item in piles:
                hours += math.ceil(item / mid)
            
            if hours <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res


piles = [3,6,7,11]
h = 8

sol = Solution()
result = sol.minEatingSpeed(piles,h)

print(f'Output is : {result}')



