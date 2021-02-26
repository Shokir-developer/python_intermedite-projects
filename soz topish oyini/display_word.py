def display(user_letters, word):
	display_letters = ""

	for letter in word:
		if letter in user_letters.upper():
			display_letters += letter
		else:
			display_letters += "-"

	return display_letters

