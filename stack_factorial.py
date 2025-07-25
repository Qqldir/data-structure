
# 함수/메서드 호출 및 재귀 호출시 콜 스택
def factorial_recursive(n):
    print(f"call factorial({n})")
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)

factorial_recursive(5)

