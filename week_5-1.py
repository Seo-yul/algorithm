"""
Linked Queue의 특징
Linked Queue는 Doubly Linked List를 기반으로 만들어진 Queue이다.
Linked Queue의 모든 동작은 O(1)의 시간복잡도로 동작한다.
Linked Queue에 정의된 동작은 아래와 같다.
is_empty(): Queue가 비어있으면 True, 비어있지 않으면 False를 출력한다.
put(): Queue의 rear에 새로운 데이터를 입력한다.
get(): Queue의 front에서 데이터를 출력한다. 출력한 데이터는 Queue에서 삭제한다. 더이상 출력할 데이터가 없는 경우 None을 출력한다.
peek(): Queue의 front에서 데이터를 출력한다. 출력한 데이터는 Queue에 그대로 유지한다. 더이상 출력할 데이터가 없는 경우 None을 출력한다.
"""
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
 
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
 
    def is_empty(self):
        if self.front == None and self.rear == None:
            return True
        return False
 
    def put(self, data):
        new_node = Node(data,self.rear)
        if not self.front:
            self.front = new_node
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
 
    def get(self):
        if not self.front:
            self.rear = None
            return None
        result = self.front.data
        self.front = self.front.next
        return result
 
    def peek(self):
        if not self.front:
            return None
        result = self.front.data
        return result
 
# Test code
queue = LinkedQueue()
 
print(queue.is_empty())
for i in range(10):
    queue.put(i)
print(queue.is_empty())
 
for _ in range(11):
    print(queue.get(), end=' ')
print()
 
for i in range(20):
    queue.put(i)
print(queue.is_empty())
 
for _ in range(5):
    print(queue.peek(), end=' ')
print()
 
for _ in range(21):
    print(queue.get(), end=' ')
print()
print(queue.is_empty())