import math

print("1. + ")
print("2. - ")
print("3. * ")
print("4. / ")
print("5. EXIT ")

yana = True
while yana:
	command = 4#int(input("Choose command: "))
	result = 0
	aList = []
	if 1 <= command <= 4:
		print("Enter numbers: ")
		print("QUIT = -1")
		while True:
			num = int(input(">>> "))
			if num == -1:
				break
			aList.append(num)

		if command == 1:
			result = sum(aList)

		elif command == 2:
			result = aList[0]
			for x in range(1,len(aList)):
				result -= aList[x]

		elif command == 3:
			result = 1
			for x in aList:
				result *= x
		else:
			result = aList[0]
			for x in range(1,len(aList)):
				result /= aList[x]



	elif command == 5:
		quit()
	else:
		print("Enter correct command")

	print("Result: ", result)
	yana = int(input("Yana ishlaysizmi [ha(1)/yoq(0)]: "))


