#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
a_letters = int(input("How many letters would you like in your password?\n")) 
a_symbols = int(input(f"How many symbols would you like?\n"))
a_numbers = int(input(f"How many numbers would you like?\n"))

pw_list = []

for char in range(1, a_letters + 1):
  pw_list.append(random.choice(letters))

for char in range(1, a_symbols + 1):
  pw_list += random.choice(symbols)

for char in range(1, a_numbers + 1):
  pw_list += random.choice(numbers)

print(pw_list)
random.shuffle(pw_list)
print(pw_list)

password = ""
for char in pw_list:
  password += char

print(f"Your password is: {password}")