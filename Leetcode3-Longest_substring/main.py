# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# =============================================================

s = "abcabcbb"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch = set()
        l = r = 0
        res = 0
        
        while r<len(s):
            
            if s[r] not in ch:
                ch.add(s[r])
                r +=1
                res = max(res, r-l)
            else:
                ch.remove(s[l])
                l +=1
        return res

sol = Solution()

k = sol.lengthOfLongestSubstring(s)


print(f'Output : {k}')
