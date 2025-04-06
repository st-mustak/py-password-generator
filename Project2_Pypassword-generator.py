#PyPassword Generator
import random
print("Welcome to PyPassword Generator.")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+']

user_letters = int(input("How many letters would you like in your password: \n"))
user_numbers = int(input("How many numbers would you like in your password: \n"))
user_symbols = int(input("How many symbols would you like in your password: \n"))

# Easy-Level
# password = ""
# for char in range(0,user_letters):
#     password +=random.choice(letters)
#
# for char in range(0,user_numbers):
#     password +=random.choice(numbers)
#
# for char in range(0,user_symbols):
#     password +=random.choice(symbols)
# print(password)

#Hard Level
password_list = []
for char in range(0,user_letters):
    password_list.append(random.choice(letters))

for char in range(0,user_numbers):
    password_list.append(random.choice(numbers))

for char in range(0,user_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password+=char

print(f"Your password is: {password}")




