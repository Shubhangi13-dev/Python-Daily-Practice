# if Statement
'''
age = 18

if age >= 18:
    print("you can vote")'''

# if-else Statement
'''
number = 5

if number > 0:
    print("Positive number")
else:
    print("Not positive")'''

# if-elif-else
'''
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")'''


# Nested if
'''
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("enter allowed")'''

# Suppose a customer wants to purchase a product. the application needs to check whether:
'''
is_logged_in = True
product_available = True
cart_total = 1500
wallet_balance = 1000    # 2000

if not is_logged_in:
    print("Please log in to continue")

elif not product_available:
    print("Product is out of stock")

elif wallet_balance < cart_total:
    print("Insufficient balance")

else:
    print("Order placed successfully")'''


# Applications often have different roles, such as admin, manager, and user.
'''
role = input("enter your role: ").lower()

if role == "admin":
    print("you can manage users and settings")

elif role == "manager":
    print("you can view reports and manage tasks")

elif role == "user":
    print("you can access your own profile")

else:
    print("Invalid role")'''


username = input("enter username: ")
password = input("enter password: ")
account_active = True

if username == "admin" and password == "python123" and account_active:
    print("login successful")
else:
    print("login failed")