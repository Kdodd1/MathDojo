#Create flexible functions that take n amount of arguments
class mathDojo:
    def __init__(self):
        self.total = 0
        
    def add(self, *args):
        for val in args:
            self.total += val
        return self
    def subtract(self, *args):
        for val in args:
            self.total -= val
        return self
    def result(self):
        print(self.total)

#Example
md = mathDojo()
md.add(2,4,5).add(1,2).subtract(4).result()