# 1. Print numbers from 1 to 10

for i in range(1, 11):
    print(i)

# 2. Print numbers from 10 to 1

for i in range(10, 0, -1):
    print(i)

# 3. Print even numbers from 1 to 20

for i in range(2, 21, 2):
    print(i)

# 4. Print odd numbers from 1 to 20

for i in range(1, 21, 2):
    print(i)

# 5. Sum of numbers from 1 to 10

total = 0

for i in range(1, 11):
    total += i

print(total)

# 6. Multiplication table

num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 7. Print each character in a string

name = "Python"

for ch in name:
    print(ch)

# 8. Count characters in a string using a loop

text = "Python"
count = 0

for ch in text:
    count += 1

print(count)


# 9. Print each item from a list

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# 10. Find the sum of list elements

numbers = [10, 20, 30, 40]
total = 0

for num in numbers:
    total += num

print(total)

# 11. Find the largest number in a list

numbers = [12, 45, 8, 67, 23]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)

# 12. Count even numbers in a list

numbers = [1, 2, 4, 7, 8, 10]
count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print(count)

# 13. Print squares of numbers

for i in range(1, 6):
    print(i ** 2)

# 14. Print cubes of numbers

for i in range(1, 6):
    print(i ** 3)

# 15. Calculate factorial

num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print(fact)

# 16. Print a star pattern

for i in range(1, 6):
    print("*" * i)

# 17. Print a reverse star pattern

for i in range(5, 0, -1):
    print("*" * i)

# 18. Print index and value using enumerate()

names = ["Asha", "Ravi", "Neha"]

for index, name in enumerate(names):
    print(index, name)

# 19. Loop through a dictionary

student = {"name": "Asha", "marks": 85}

for key, value in student.items():
    print(key, value)

# 20. Check whether a number is prime

num = 7
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
print(is_prime)

# 21. Print a list with index

names = ["Asha", "Ravi", "Neha"]
for i in range(len(names)):
    print(i, names[i])

# 22. Find the smallest number

nums = [18, 6, 25, 3, 12]
smallest = nums[0]

for n in nums:
    if n < smallest:
        smallest = n

print(smallest)

# 23. Count vowels in a word

word = "education"
count = 0

for ch in word:
    if ch in "aeiou":
        count += 1

print(count)

# 24. Print each word in a sentence

sentence = "Python is easy to learn"
for word in sentence.split():
    print(word)

# 25. Check which numbers are above 50

nums = [25, 60, 45, 80, 10]

if n in nums:
    if n > 50:
        print(n)


# while Loop -- 15 examples
# 26. Print 1 to 10

i = 1

while i <= 10:
    print(i)
    i += 1

# 27. Print 10 to 1

i = 10

while i >= 1:
    print(i)
    i -= 1

# 28. Print even numbers

i = 2

while i <= 20:
    print(i)
    i += 2

# 29. Sum numbers from 1 to 10

i = 1
total = 0

while i <= 10:
    total += i 
    i += 1

print(total)

# 30. Multiplication table using while 

num = 4 
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

# 31. Count digits in a number

num = 12345
count = 0

while num > 0:
    count += 1
    num //= 10

print(count)

# 32. Reverse a number

num = 1234
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print(reverse)

# 33. Sum digits of a number

num = 1234
total = 0

while num > 0:
    total += num % 10
    reverse = reverse * 10 + digit
    num //= 10

print(total)

# 34. Check palindrome number

num = 121
original = num 
reverse = 0

while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not palindrome")

# 35. Keep asking for a positive number

num = int(input("enter a positive number:"))

while num <= 0:
    num = int(input("Try again: "))

print("Accepted")

# 36. Password retry example

password = ""

while password != "python123":
    password = input("enter password: ")

print("Access granted")

# 37. print Multiples of 3

i = 3 
while i <= 30:
    print(i)
    i += 3

# 38. Calculate factorial using while

num = 5 
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print(fact)

# 39. Fibonacci sequence 

a = 0
b = 1
count = 0

while count < 8 :
    print(a)
    a, b = b, a + b
    count += 1

# 40. Menu-driven calculator

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "3":
        break
    elif choice == "1":
        print(10 + 5)
    elif choice == "2":
        print(10 - 5)
    else:
        print("Invalid choice")

# 41. Print multiples of 5 up to 50

n = 5
while n <= 50:
    print(n)
    n += 5

# 42. Print a number until it reaches 100

n = 10
while n >= 0:
    print(n)
    n -= 2

# 43. Find the number greater than 100 divisible  by 9

n = 101
while n % 9 != 0:
    n += 1

print(n)

# 44. Calculate the sum of digits until number becomes 0

n = 2468
total = 0

while n > 0:
    total += n % 10
    n //= 10

print(total)

# 45. Keep doubling a number until it exceeds 500

n = 3
while n <= 500:
    print(n)
    n *= 2

# 46. Print a sequence of odd numbers

n = 1
while n <= 25:
    print(n)
    n += 2

# 47. Find how many times 2 fits into a number

n = 64
count = 0

while n >= 2:
    n //= 2
    count += 1

print(count)

# 48. Remove digits from a number one by one 

n = 9876

while n > 0:
    print(n % 10)
    n //= 10

# 49. Print a simple menu until user chooses exit

choice = ""

while choice != "3":
    print("1. Say Hello")
    print("2. Say Welcome")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        print("Hello!")
    elif choice == "z":
        print("welcome!")

# 50. Count down by 2

n = 20
while n >= 0:
    print(n)
    n -= 2

 