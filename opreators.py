a = int(input("Enter a first no :"))
b = int(input("Enter a 2nd no :"))

print()

#Calculate total price

total_price = 5 * 140
print(total_price)

#Calculate remaining balance
balance = 1350 - 1000
print(balance)

#Calculate area of lenght
lenght = 50
width = 8
area = lenght + width
print(area)


#Divide 57 chocolates equality among 6 students
quotient = 57 // 6
remainder = 57 % 6

print("Quotient:", quotient)
print("Remainder:", remainder)

#Calculate the square and cube of a number
number = 5
square = number ** 2
cube = number ** 3
print("Square:", square)
print("Cube", cube)

#Convert 135 minutes into hours and remaining minutes
minutes = 135
hours = minutes // 60
remaining_minutes = minutes % 60
print("Hours:", hours)
print("Remaining minutes:", remaining_minutes)

#Calculate the average of three numbers
a = 10
b = 20
c = 30
average = (a + b + c) / 3
print(average) 


a = 15 // 4
b = 15 % 4
print(a, b)

x = -15 // 4
y = -15 % 4
print(x, y)

res = 2 ** 3 ** 2
print(res)

p = 10 + 3 * 2 ** 2 - 4 / 2
print(p)

val = 10.0 % 3
print(type(val), val)

a = 7
b = 2.0
print(a // b)

x = 5.5 + 4.5 * 2 // 3
print(x)

print(10 == 10.0)

print("apple" > "Apple")

print([1, 2] < [1, 2, 0])

print(True == 1, False == 0)

a = 5
print(1 < a < 10)

print(10 != 10.0)

x = 0 and 10
y = 5 and 20
print(x, y)

a = "Hello" or ""
b = "" or "World"
print(a, b)

print(not [] and not "0")

res = 10 or 1 / 0
print(res)

x = [] or [0] or False
print(x)

print(not (5 > 2 and 3 < 1))

a = True
b = False
print(a and not b or b)

a = 10
a += 5 * 2
print(a)

x = 8
x //= 3
print(x)

lst = [1, 2]
lst += [3, 4]
print(lst)

a = 5
a **= 2
print(a)

if (n := len("Python")) > 5:
    print(n)

x = 12
x %= 5
print(x)

a = 5  # 0101
b = 3  # 0011
print(a & b, a | b)

a = 5 # 0101
b = 3 # 0011
print(a ^ b)

x = 10
print(-x)

print(-(-5))

x = 3 # 0011
print(x << 2)

x = 16 # 10000
print(x >> 3)

a = 1
print((a << 3) - 1)

s = "y" in "Python"
print(s)

d = {"a": 1, "b": 2}
print(1 in d, "a" in d)

print(1 not in [1, 2, 3])

t = (1, (2, 3))
print(2 in t)

print("th" not in "python")

st = (1, 2, 3)
print(3 in st)

a = [1, 2]
b = [1, 2]
print(a is b, a == b)

x = 256
y = 256
print(x is y)

m = "hello"
n = "hello"
print(m is n)

a = None
print(a is None)

p = [10]
q = p
print(p is not q)

x = True
y = 1
print(x is y)

a = 10 
b = 20 
c = 30
print(a < b and b < c or a > c)

x = 5
print(x & 1 == 0)

a = [1, 2]
b = a
b += [3]
print(a is b, a)

a = [1, 2]
b = a
b = b + [3]
print(a is b, a)

x = 10
y = 5
z = x > y and x & y or x ^ y
print(z)

