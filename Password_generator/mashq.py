import random
from string import digits, punctuation, ascii_letters

password_list = []
yana = True

while yana:
	length = int(input("Choose length of password: "))

	all_sym = digits + punctuation + ascii_letters

	password = ''.join(random.sample(all_sym, length))
	print(password)
	password_list.append(password)

	yana = int(input("Yana parol kerakmi: [1/0]: "))

print("You have such as password: ", password_list)