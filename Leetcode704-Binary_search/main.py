# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# ===========================================

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l = 0
        r = len(nums)-1

        while(l<=r):
            mid = (l+r) //2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
            
        return -1


nums = [-1,0,3,5,9,12]
target = 9


sol = Solution()

result = sol.search(nums,target)

print(f'Output is : {result}')