class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for letter in s:
            if letter != '#':
                stack1.append(letter)
            else:
                if stack1:
                    stack1.pop(-1)

        for letter in t:
            if letter != '#':
                stack2.append(letter)
            else:
                if stack2:
                    stack2.pop(-1)

        if stack1 == stack2:
            return True
        else:
            return False
            
            
            
        