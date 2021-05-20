# Comments after number are my predictions

main_divider = "=========="
print(main_divider)

#1
# Prediction:
# 5

def a():
    return 5
print(a())

print(main_divider)

#2
# Prediction:
# 10

def a():
    return 5
print(a()+a())

print(main_divider)

#3
# Prediction:
# 5

def a():
    return 5
    return 10
print(a())

print(main_divider)

#4
# Prediction:
# 5

def a():
    return 5
    print(10)
print(a())

print(main_divider)

#5
# Prediction:
# 5
# None

def a():
    print(5)
x = a()
print(x)

print(main_divider)

#6
# Prediction:
# 3
# 5
# Error? [Can't add 'None's]

def a(b,c):
    print(b+c)
# This code causes an error ! Comment out to run the code and check outputs!
print(a(1,2) + a(2,3))

print(main_divider)

#7
# Prediction:
# 25

def a(b,c):
    return str(b)+str(c)
print(a(2,5))

print(main_divider)

#8
# Prediction:
# 100
# 10

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

print(main_divider)

#9
# Prediction:
# 7
# 14
# 21

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

print(main_divider)

#10
# Prediction:
# 8

def a(b,c):
    return b+c
    return 10
print(a(3,5))

print(main_divider)

#11
# Prediction:
# 500
# 500
# 300
# 500

b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

print(main_divider)

#12
# Prediction:
# 500
# 500
# 300
# 500

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print

print(main_divider)

#13
# Prediction:
# 500
# 500
# 300
# 300

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

print(main_divider)

#14
# Prediction:
# 1
# 3
# 2

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

print(main_divider)

#15
# Prediction:
# 1
# 3
# 5
# 10

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

print(main_divider)

