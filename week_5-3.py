"""
다음은 linkedlist를 구현한 것이다. 이때 linked list는 양방향이 연결된 double linked list이다.
원하는 데이터 노드의 전/후에 노드를 추가하는 insert_before()와 insert_after() 메소드를 완성하시오.

아래 테스트 코드에서 에러 없이 동작을 해야 한다.
예를 들어, node_mgmt = NodeMgmt(0)을 통해 인스턴스를 생성한 후, insert_before(200, 0)메소드를 실행시키면 200 다음 0 이 차례로 출력되어야 한다.
"""

class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next
 
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert_before(self, data, before_data):
        node = self.tail
        while node.data != before_data:
            node = node.prev
            if node == None:
                return False
        new = Node(data)
        if node.prev == None:
            node.prev = new
            new.next = node
            self.head = new
            return True
        else:
            new.next = node
            new.prev = node.prev
            node.prev = new
            node.prev.next = new
            return True

    def insert_after(self, data, after_data):
        if self.head == None:
            self.head = Node(data)
            return True            
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node == None:
                    return False
            new = Node(data)
            after_new = node.next
            new.next = after_new
            new.prev = node
            node.next = new
            if new.next == None:
                self.tail = new
            return True
 
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new
 
    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next
 
# Test Code
node_mgmt = NodeMgmt(0)
for data in range(1, 5):
    node_mgmt.insert(data)
 
node_mgmt.insert_before(200, 0)
node_mgmt.insert_after(100, 2)
node_mgmt.desc()