from get_word import get_word
from display_word import display

def play():
	word = get_word()

	word_letters = set(word)

	user_letters = ""
	print(f"Men {len(word)} xonali so'z o'yladim. Topa olasizmi.")

	while len(word_letters) > 0:
		print(display(user_letters, word))

		if len(user_letters) > 0:
			print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")

		print()
		letter = input("Xarf kiriting: ").upper()

		if letter in user_letters:
			print("Bu harfni avval kiritgansiz. Boshqa harf kiritng.")
			continue
		elif letter in word:
			word_letters.remove(letter)
			print(f"{letter} harfi to'g'ri.")
		else:
			print("Bunday harf yo'q.")

		user_letters += letter

	print(f"Tabriklayman {word} so'zini {len(user_letters)} urinishda topdingiz.")


play()