# 후위표기법(Postfix Notation) 수식 계산하기
# - 수식 왼쪽에서 오른쪽으로 스캔해서
# - 피연산자 -> 스택 저장
# - 연산자 -> 필요한 수만큼의 피연산자를 스택에서 꺼내 연산을 실행 & 연산 결과 다시 스택에 저장
def evaluate_postfix(expression):
    stack = []

    for item in expression.split():
        if item.isdigit():  # 피연산자이면
            stack.append(int(item))
        else:  # 연산자이면
            second = stack.pop()
            first = stack.pop()
            if item == '+':
                result = first + second
            elif item == '-':
                result = first - second
            elif item == '*':
                result = first * second
            elif item == '/':
                result = first / second  # 실수 나눗셈
            else:
                return "오류: 지원하지 않는 연산자"
            stack.append(result)

    if len(stack) != 1:
        return "오류: 표현식이 잘못됨"
    
    return stack.pop()

postfix_expr = "후위표기식"  
print("결과:", evaluate_postfix(postfix_expr))