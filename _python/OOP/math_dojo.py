class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self
    
    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self

math_dojo1 = MathDojo()
x = math_dojo1.add(1, 2).add(3, 4, 5).add(6, 7, 8).result
print(x)

math_dojo2 = MathDojo()
y = math_dojo2.add(300).subtract(10).subtract(20, 30, 40).subtract(50, 60).result
print(y)
