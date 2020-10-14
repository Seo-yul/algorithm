class PriorityQueue:
    def __init__(self):
        self.heap_array = list()
        self.heap_array.append(None)

    def is_empty(self):
        if len(self.heap_array) == 1:
            return True
        else:
            return False

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx][0] < self.heap_array[parent_idx][0]:
            return True
        else:
            return False

    def put(self, data):
        if self.is_empty():
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx
        return True

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        if left_child_popped_idx >= len(self.heap_array):
            return False
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx][0] < self.heap_array[left_child_popped_idx][0]:
                return True
            else:
                return False
        else:
            if self.heap_array[left_child_popped_idx][0] > self.heap_array[right_child_popped_idx][0]:
                if self.heap_array[popped_idx][0] < self.heap_array[left_child_popped_idx][0]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_idx][0] < self.heap_array[right_child_popped_idx][0]:
                    return True
                else:
                    return False

    def get(self):
        if self.is_empty():
            print('get')
            print(p.heap_array)
            return None
        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx][0] < self.heap_array[left_child_popped_idx][0]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
            else:
                if self.heap_array[left_child_popped_idx][0] > self.heap_array[right_child_popped_idx][0]:
                    if self.heap_array[popped_idx][0] < self.heap_array[left_child_popped_idx][0]:
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_popped_idx
                else:
                    if self.heap_array[popped_idx][0] < self.heap_array[right_child_popped_idx][0]:
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = right_child_popped_idx

    def peek(self):
            if self.is_empty():
                return None
            else:
                return self.heap_array[1]

p = PriorityQueue()
x = (20,2)
y = (10,1)
p.put(x)
p.put(y)


print(p.peek())
p.get()
print(p.peek())
p.get()
print(p.peek())