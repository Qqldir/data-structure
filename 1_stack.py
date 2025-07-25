
# 스택의 개념
# - 한 쪽이 막힌 바구니 형태
# - 후입선출: 넣은 데이터가 아래로 쌓임

'''
ADT STACK
Objects: 0개 이상 n개의 원소를 가진 유한 순서 리스트
Functions:
    Stack CreateStack(Stacksize) : Stacksize 크기의 배열 만들기. TOP 초기화
    Bool is_empty(stack) : stack이 빈 상태인가?
    Bool is_full(stack) : stack이 full 상태인가? 
        -> 해결책: 스택 크기의 resize / 동적할당(realloc)
    Stack push(stack, item) : stack에 item 추가하기
    Element pop(stack) : stack에서 item 하나 가져오기 (제거됨)(가장 위 데이터)
    Element peek(stack) : stack에서 item 하나 가져오기 (유지됨)(top? 없으면 -1)
'''

## 기본 스택 구현

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.__len__() == 0
    
    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")





