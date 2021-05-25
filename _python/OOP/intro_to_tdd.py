import unittest, re

def reverseList(list):
    for i in range(len(list) // 2):
        list[i], list[len(list) - i - 1] = list[len(list) - i - 1], list[i]
    return list

def isPalindrome(string):
    # Strip string of non-alphanumerics; set all to lowercase
    s = re.sub(r'[^a-zA-Z]', '', string).lower()

    # Compare to its opposite index counterpart
    for i in range(len(s) // 2):
        if not s[i] == s[len(s) - i - 1]:
            return False
    return True

def coins(change):
    coins = []

    # Count quarter amount
    coins.append(change // 25)
    change %= 25
    
    # Count dime amount
    coins.append(change // 10)
    change %= 10
    
    # Count nickels and penny
    coins.append(change // 5)
    coins.append(change % 5)
    return coins

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

class ReverseListTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([0,1,2,3]), [3,2,1,0])
    
    def testTwo(self):
        self.assertEqual(reverseList([0,2,4,6,8]), [8,6,4,2,0])
    
    def testThree(self):
        self.assertEqual(reverseList([0]), [0])

class IsPalindromeTests(unittest.TestCase):
    def testOne(self):
        self.assertTrue(isPalindrome("racecar"))
    
    def testTwo(self):
        self.assertFalse(isPalindrome("ayo"))

    def testThree(self):
        self.assertTrue(isPalindrome("reviver"))

    # Allows for strings that contain non-alphanumeric chars
    def testFour(self):
        self.assertTrue(isPalindrome("A man, a plan, a canal - Panama."))

    def testFive(self):
        self.assertTrue(isPalindrome("Mr. Owl ate my metal worm."))

class CoinsTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(coins(87), [3,1,0,2])
    
    def testTwo(self):
        self.assertEqual(coins(52), [2,0,0,2])

    def testThree(self):
        self.assertEqual(coins(19), [0,1,1,4])
    
    def testFour(self):
        self.assertEqual(coins(41), [1,1,1,1])

    def testFive(self):
        self.assertEqual(coins(94), [3,1,1,4])

class FactorialTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(factorial(5), 120)

    def testTwo(self):
        self.assertEqual(factorial(0), 1)

    def testThree(self):
        self.assertEqual(factorial(10), 3628800)

class FibonacciTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fibonacci(5), 5)

    def testTwo(self):
        self.assertEqual(fibonacci(10), 55)

    def testThree(self):
        self.assertEqual(fibonacci(15), 610)

if __name__ == "__main__":
    unittest.main()