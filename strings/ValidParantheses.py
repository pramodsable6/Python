# O(n) time | O(n) space

def isValid(s):
    opening_brackets = '[{('
    closing_brackets = ']})'
    pairs = {']': '[', '}': '{', ')': '('}
    stack = []
    
    for i in s:
        if i in closing_brackets:
            if len(stack):
                if stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        elif i in opening_brackets:
            stack.append(i)
    
    return len(stack) == 0

