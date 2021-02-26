import random

def son_top(x=10):
	print("Keling son topish o'yinini o'ynaymiz.")
	print("1 dan {} gacha son o'yladim topa olasizmi?".format(x))

	count = 0
	person_guess = 0
	computer_guess = 0
	
	computer_guess = random.randint(1, x)

	while True:
		print("Taxminingizni kiriting.")
		person_guess = int(input())

		count += 1
		if person_guess == computer_guess:
			print("TOPDINGIZ! Men {} sonini o'ylagan edim. Siz {} urinishda topdingiz!".format(computer_guess,count))
			break
		elif person_guess < computer_guess:
			print("Xato men o'ylagan son bundan kattaroq. Yana harakat qilib ko'ring.")
		elif person_guess > computer_guess:
			print("Xato men o'ylagan son bundan kichikroq. Yana harakat qilib ko'ring")

	return count