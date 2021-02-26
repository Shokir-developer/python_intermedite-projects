import random

def son_top_pc(x=10):
	print("Keling son topish o'yinini yana o'ynaymiz.")
	input("1 dan {} gacha son o'ylang men topishga harakat qilaman.O'ylagan bo'lsangiz ixtiyoriy tugmani bosing".format(x))

	count = 0

	quyi = 1
	yuqori = 10

	while True:
		count += 1

		if quyi != yuqori:
			taxmin = random.randint(quyi, yuqori)
		else:
			taxmin = quyi

		javob = input("Siz {} soni o'yladingiz.To'g'ri(t), katta(+), kichik(-):".format(taxmin))

		if javob == '+':
			quyi = taxmin + 1
		elif javob == '-':
			yuqori = taxmin - 1
		else:
			break
	print("Topdim")
	print("Men {} ta urinishda topdim".format(count))
	return count

