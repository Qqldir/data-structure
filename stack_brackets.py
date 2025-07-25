
# 컴파일러의 괄호 짝 맞추기
# - 왼쪽 괄호의 개수와 오른쪽 괄호의 개수를 같게
# - 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 
# - 여는 괄호 -> 스택 추가 / 닫는 괄호 -> 스택에서 끄집어내서 닫는 괄호와 같은 쌍인지 체크
def check_brackets(expr):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for ch in expr:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack:
                return "오류: 닫는 괄호과 같은 여는 괄호가 없음"
            open_ch = stack.pop()
            if bracket_pairs[ch] != open_ch:
                return f"오류: {open_ch} 와 {ch} 는 짝이 맞지 않음"

    if stack:
        return "오류"

    return "성공"
