class Stack:
    def __init__(self):
        self.list = list()
 
    def push(self, data):
        self.list.append(data)
 
    def pop(self):
        return self.list.pop()
 
class Calculator:
    def __init__(self):
        self.stack = Stack()
 
    def calculate(self, string):
        s = string.split()
        num1 = ''
        num2 = ''
        result = ''
        string_len = len(s)
        for i in range(string_len):
            self.stack.push(s.pop())

        for _ in range(string_len):
            tmp = self.stack.pop()
            if tmp == '+':
                result = num1 + num2
            elif tmp == '-':
                result = num1 - num2
            elif tmp == '*':
                result = num1 * num2
            elif tmp == '/':
                result = num1 / num2
            else:
                if num1 == '':  
                    num1 = int(tmp)
                else:
                    num2 = int(tmp)
            if result != '':
                num1 = int(result)
                result = ''

        return (num1)
        
# Test code
calc = Calculator()
print(calc.calculate('4 6 * 2 / 2 +'))
print(calc.calculate('2 5 + 3 * 6 - 5 *'))