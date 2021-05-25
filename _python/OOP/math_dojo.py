import unittest

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

class MathDojoTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(self.math_dojo1.add(1, 2).add(3, 4, 5).add(6, 7, 8).result, 36)

    def testTwo(self):
        self.assertEqual(self.math_dojo2.add(300).subtract(10).subtract(20, 30, 40).subtract(50, 60).result, 90)

    def testThree(self):
        self.assertEqual(self.math_dojo3.add(9).subtract(6).add(160).subtract(20).result, 143)

    def setUp(self):
        self.math_dojo1 = MathDojo()
        self.math_dojo2 = MathDojo()
        self.math_dojo3 = MathDojo()

if __name__ == "__main__":
    unittest.main()