# 회문(Palindrome) 검사하기
# - 앞으로부터 읽으나 뒤로부터 읽으나 동일한 스트링
# - 앞쪽 절반은 push, 뒤쪽 절반은 pop을 하면서 확인 
def is_palindrome(s):
    stack = []
    length = len(s)
    mid = length // 2

    # 앞쪽 절반 push
    for i in range(mid):
        stack.append(s[i])

    # 문자열 길이가 홀수 -> 가운데 문자 건너뛰기
    if length % 2 != 0:
        mid += 1

    # 뒤쪽 절반 pop하면서 비교
    for i in range(mid, length):
        if not stack or stack.pop() != s[i]:
            return False

    return True