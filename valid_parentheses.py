def valid_parentheses(string):
    open_parenthes = 0
    close_parenthes = 0
    for char in string:
        if char == '(':
            open_parenthes += 1
        if char == ')':
            close_parenthes += 1
        if close_parenthes > open_parenthes:
            return False
    if open_parenthes == close_parenthes:
        return True
    return False


if __name__ == '__main__':
    print(valid_parentheses("hi(hi()()"))
