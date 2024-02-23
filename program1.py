    
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in brackets.values():  # Opening bracket
                stack.append(char)
            elif char in brackets.keys():  # Closing bracket
                if not stack or stack[-1] != brackets[char]:
                    return False
                stack.pop()
            else:
                return False  # Invalid character
        
        return len(stack) == 0  # True if all brackets are matched
        


  

