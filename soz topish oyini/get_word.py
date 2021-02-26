import random
from uzword import words

def get_word():
	word = random.choice(words)

	while "-" in word or " " in word:
		word = random.choice(words)

	return word.upper()

