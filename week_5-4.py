"""
HashTable 클래스는 문자열을 key로 입력받는 해쉬 테이블 자료구조를 구현한 것이다.
HashTable 클래스는 단순한 해쉬 함수로 인해, 해쉬 충돌이 빈번히 발생한다.
이 단점을 개선하기 위해, Chaining 기법으로 ChainedHashTable을 구현하고자 한다.
HashTable을 상속하여 해쉬 충돌이 발생해도 정상적으로 동작하는 ChainedHashTable을 완성하시오.
"""
class HashTable:
    def __init__(self):
        self.table = [None]*10
 
    @staticmethod
    def hash_func(key):
        return ord(key[0]) % 10
 
    def set(self, key, value):
        self.table[hash_func(key)] = value
 
    def get(self, key):
        return self.table[hash_func(key)]
 
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
 
class ChainedHashTable(HashTable):
    def __init__(self):
        ht = HashTable()
        self.table = ht.table
    
    def set(self, key, value):
        hash_key = super().hash_func(key)

        if self.table[hash_key] != None:
            for index in range(len(self.table[hash_key])):
                if self.table[hash_key][index][0] == key:
                    self.table[hash_key][index][1] = value
                    return True
            self.table[hash_key].append([key, value])
        else:
            self.table[hash_key] = [[key, value]]
            return True

        
    def get(self, key):
        hash_key = super().hash_func(key)
        if self.table[hash_key] != 0:
            for index in range(len(self.table[hash_key])):
                if self.table[hash_key][index][0] == key:
                    return self.table[hash_key][index][1]
            return None
        else:
            return None
 
# Test code 
ht = ChainedHashTable()
ht.set('hello', 1)
ht.set('hello2', 2)
ht.set('hello3', 3)
ht.set('hello4', 4)
 
print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')
print()
 
ht.set('hello2', 5)
 
print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')