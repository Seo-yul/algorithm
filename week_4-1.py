import itertools
class PrimeNumberGenerator:    
    def __init__(self, max_iter):
        self.max_iter = max_iter
    
    def __iter__(self):
        tmp = itertools.count(1, 1)
        for i in range(self.max_iter):
            while True:
                ok = True
                num = next(tmp)
                for j in range(2, num) :
                    if num % j == 0 :
                        ok = False
                        break
                if ok:
                    yield num
                    break
        return
        
# Test code
gen = PrimeNumberGenerator(10)
for x in gen:
    print(x)


