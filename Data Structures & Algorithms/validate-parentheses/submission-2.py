class Solution:
    def isValid(self, s: str) -> bool:
        
        n = len(s)
        if n%2==1:
            return False
        lst = []
        for i in list(s):

            if i == '[' or i == '{' or i == '(':
                lst.append(i)
            else:
                if len(lst)==0:
                    return False
                else:
                    top = lst.pop()
                    if i == ']' and top!='[':
                        return False
                    elif i == '}' and top!='{':
                        return False
                    elif i == ')' and top!='(':
                        return False
                    
        return len(lst) == 0
