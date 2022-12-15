# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
#  ======================================================

class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        
        for i in range(len(s)):
            
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                a.append(s[i])
            
            elif s[i] == ')' and len(a)>0 and  a[-1] == '('  :
                a.pop()
            elif s[i] == ']' and len(a)>0 and a[-1] == '[' :
                a.pop()
            elif s[i] == '}' and len(a)>0 and a[-1] == '{':
                a.pop()
            else:
                return False
        
        if a:
            return False
        else:
            return True
            