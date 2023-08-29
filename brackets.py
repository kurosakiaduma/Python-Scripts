class Solution():
    def brackets(inp:str):
        stack = []
        for i in inp:
            if i == "(":
                stack.append(i)
            elif i == "{":
                stack.append(i)
            elif i == "[":
                stack.append(i)
            elif i == "}":
                try:
                    assert(stack[-1] == "{")
                    stack.pop()
                except:
                    return False
            elif i == "]":
                try:
                    assert(stack[-1] == "[")
                    stack.pop()
                except:
                    return False
            elif i == ")":
                try:
                    assert(stack[-1] == "(")
                    stack.pop()
                except:
                    return False
        if stack:
            return False
        else:
            return True
 