class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for number in nums:
            self.result += number   
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for number in nums:
            self.result -= number
        return self
# create an instance:
md = MathDojo()
# Test 1:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x) # should print 5

# Test 2:
md.result = 0 # reset the result property to 0 for starting a new test
x = md.add(1,2,3,4,5).result
print(x) # should print 15

# Test 3:
# We use the result value saved in Test 2

x = md.subtract(1,2,3).result
print(x) # should print 9

# Test 4:
md.result = 0 # reset the result property to 0 for starting a new test
x = md.subtract(1,2,3,4,5).result
print(x) # should print -15