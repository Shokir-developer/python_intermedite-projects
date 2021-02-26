import random
from son_top_odam import son_top
from son_top_pc import son_top_pc

def play(x=10):
	yana = True

	while yana:
		taxmin_odam = son_top(x)
		taxmin_pc = son_top_pc(x)

		if taxmin_odam < taxmin_pc:
			print(f"Siz yutdingiz! Player: {taxmin_odam}, Computer:{taxmin_pc}")
		elif taxmin_odam > taxmin_pc:
			print(f"Men yutdim! Player: {taxmin_odam}, Computer:{taxmin_pc}")
		else:
			print(f"Durrang! Player: {taxmin_odam}, Computer:{taxmin_pc}")

		yana = int(input("Yana o'ynaysizmi: ha(1), yoq(0): "))

play()
