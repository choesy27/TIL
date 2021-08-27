from collections import deque

balanced_parentheses_string = "()))((()"

# 올바른 괄호 문자열인지 확인
def is_correct_parentheses(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0

def reverse_parentheses(string):
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ')'
        else:
            reversed_string += '('

    return reversed_string

def seperate_to_u_v(string):
    # 2. (, )의 개수가 같아야 한다.
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while queue:
        char = queue.popleft()
        u += char

        if char == '(':
            left += 1
        else:
            right += 1

        if left == right:
            break

    v = ''.join(list(queue))

    return u, v

def change_to_correct_parentheses(string):
    # 1. 빈 문자열일 경우, 빈 문자열을 그대로 반환
    if string == "":
        return ""

    u, v = seperate_to_u_v(string)

    # 3. 올바른 괄호 문자열 -> 재귀?
    if is_correct_parentheses(u):
        return u + change_to_correct_parentheses(v)

    # 4. 문자열 u가 올바른 괄호 문자열이 아니라면
    else:
        return "(" + change_to_correct_parentheses(v) + ")" + reverse_parentheses(u[1:-1])

def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parentheses(balanced_parentheses_string)

print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!