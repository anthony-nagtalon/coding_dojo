class Underscore:
    def map(self, iterable, callback):
        arr = []
        for i in iterable:
            arr.append(callback(i))
        return arr
    
    def find(self, iterable, callback):
        for i in iterable:
            if callback(i):
                return i

        # Return None if no values pass
        return None 

    def filter(self, iterable, callback):
        arr = []
        for i in iterable:
            if callback(i):
                arr.append(i)
        return arr

    def reject(self, iterable, callback):
        arr = []
        for i in iterable:
            if not callback(i):
                arr.append(i)
        return arr

_ = Underscore() 
print(_.map([1,2,3], lambda x: x*2)) # should return [2,4,6]
print(_.find([1,2,3,4,5,6], lambda x: x>4)) # should return the first value that is greater than 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # should return [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # should return [1,3,5]