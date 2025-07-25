# 중위표기법(Infix Notation) 수식의 후위표기법 변환
# - 피연산자 순서 동일
# - 연산자 순서 다르니, 우선 순위 적용 -> 연산자만 스택 저장출력
# - 피연산자 만나며 그대로 출력
# - 연산자를 만나면 스택에 저장, 스택 top보다 우선 순위가 낮은 연산자가 나오면 그때 출력
# - 왼쪽 괄호는 우선 순위가 가장 낮은 연산자
# - 오른쪽 괄호가 나오면 스택에서 왼쪽 괄호 위에 쌓여있는 모든 연산자를 출력
def infix_to_postfix(expression):
    def precedence(op):
        if op == '(':
            return 0 
        elif op in '+-':
            return 1
        elif op in '*/':
            return 2
        return -1

    output = []
    stack = []

    for token in expression:
        if token.isalnum():  # 피연산자면 바로 출력
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            # 왼쪽 괄호 전까지 연산자 모두 출력
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # 왼쪽 괄호 제거
        else:  # 연산자일 경우
            while stack and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)

    # 남은 연산자 모두 출력
    while stack:
        output.append(stack.pop())

    return ''.join(output)

# 예시
expr = "중위식"
print("중위식:", expr)
print("후위식:", infix_to_postfix(expr))  