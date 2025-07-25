# 큐의 개념
# - 관의 형태로 뚫린 자료구조
# - 선입선출
# - 서로 다른 속도로 실행되는 두 프로세스 간의 상호작용 조화시키는 버퍼 역할


'''
- 시뮬레이션의 대기열(공항의 비행기, 은행의 대기열)
- 통신에서의 데이터 패킷들의 모델링
- 프린터와 컴퓨터 사이의 버퍼링
- 많은 알고리즘에서 사용
- CPU의 태스크 스케줄링(Task Scheduling)
- 다양한 이벤트 구동 방식(Event-driven) 컴퓨터 시뮬레이션
- 콜 센터의 전화 서비스 처리 등
- 이진 트리의 레벨 순회(Level-order Traversal)
- 그래프에서 너비우선탐색(BFS) 
'''

'''
ADT QUEUE
Objects: 0개 이상 n개의 원소를 가진 유한 순서 리스트
Functions:
    Queue CreateQueue(Queuesize) : Queuesize 크기의 배열 만들기
    Bool is_emptyQ(queue) : queue가 빈 상태인가?
    Bool is_fullQ(queue) : queue가 Full 상태인가?
    Queue AddQ(queue, item) : queue에 item 추가하기 (rear)
    Element DeleteQ(queue) : queue에서 item 하나 가져오기 (제거됨)
    fromt(공백 -> -1) rear
'''

# 1. 선형 큐
# - 삽입 위해서 요소들 이동시켜야 함
# - 문제 많아서 사용 x

# 2. 원형 큐
# - 배열을 원형으로 사용
# - front: 첫 번째 요소 하나 앞의 인덱스 , [1]부터 채워
# - rear: 마지막 요소의 인덱스

# 문제점
# - empty와 full 구별 안 됨 -> 하나 걍 비워둬


########## QUE의 기본 형태 ##########
MAX_QSIZE = 10

class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % MAX_QSIZE

    def clear(self):
        self.front = self.rear

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item
        else:
            print("큐가 꽉 찼습니다.")

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QSIZE
            return self.items[self.front]
        else:
            print("큐가 비어 있습니다.")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]
        else:
            print("큐가 비어 있습니다.")
            return None

    def display(self):
        if self.isEmpty():
            print("큐가 비어 있습니다.")
            return

        if self.front < self.rear:
            out = self.items[self.front + 1 : self.rear + 1]
        else:
            out = self.items[self.front + 1 : MAX_QSIZE] + self.items[0 : self.rear + 1]
        print(f"[f={self.front}, r={self.rear}] -> {out}")



########## DEQUE(double-ended queue) ##########
# - front와 rear에서 모두 삽입과 삭제가 가능한 큐
# - 최적화된 연산 속도(vs list)
'''
ADT DEQUE
Objects: n개의 elment형으로 구성된 요소들의 순서 있는 모임
Functions:
    create() ::= 덱을 생성
    is_empty(dq) ::= 덱이 공백상태인지를 검사
    is_full(dq) ::= 덱이 포화상태인지를 검사
    add_front(dq, e) ::= 덱의 앞에 요소를 추가  
    add_rear(dq, e) ::= 덱의 뒤에 요소를 추가
    delete_front(dq) ::= 덱의 앞에 있는 요소를 반환한 다음 삭제
    delete_rear(dq) ::= 덱의 뒤에 있는 요소를 반환한 다음 삭제
    get_front(q) ::= 덱의 앞에서 삭제하지 않고 앞에 있는 요소를 반환
    get_rear(q) ::= 덱의 뒤에서 삭제하지 않고 뒤에 있는 요소를 반환
'''

from collections import deque
array = [1, 2]
item = 0
num = 3

deque = deque()
deque = deque(maxlen = 5) # 자동 제거됨 

deque.append(item) # item을 데크의 오른쪽 끝에 삽입
deque.appendleft(item) # item을 데크의 왼쪽 끝에 삽입
deque.pop() # 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제
deque.popleft() # 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제
deque.extend(array) # 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가
deque.extendleft(array) # 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가
deque.remove(item) # item을 데크에서 찾아 삭제
deque.rotate(num) # 데크를 num만큼 회전(양수면 오른쪽, 음수면 왼쪽)


# 회문검사
def is_palindrome(s):
    dq = deque(s)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False


# 너비 우선 탐색(BFS)
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}
bfs(graph, 'A')  # 출력: A B C D


