# Basic
print("== Basic ====")
for val in range(150):
    print(val)
print()

# Multiples of Five
print("== Multiples of Five ====")
for val in range(1001):
    if val % 5 == 0:
        print(val)

print()

# Alternatively, for less iterations:
print("== Multiples of Five (Alt.) ====")
for val in range(5, 1001, 5):
    print(val)

print()

# Counting the Dojo Way
print("== Counting the Dojo Way ====")
for val in range(1, 101):
    if(val % 10 == 0):
        print("Coding Dojo")
    elif(val % 5 == 0):
        print("Coding")
    else:
        print(val)

print()

# Whoa. That Sucker's Huge
print("== Whoa. That Sucker's Huge ====")
sum = 0
for val in range(500001):
    sum += val
print("Sum:", sum)

print()

# Countdown by Fours
# 0 is not a positive number!
print("== Countdown by Fours ====")
for val in range(2018, 0, -4):
    print(val)

print()

# Flexible Counter
print("== Flexible Counter ====")
lowNum = 2
highNum = 9
mult = 3
for val in range(lowNum, highNum + 1):
    if(val % mult == 0):
        print(val)

print()
