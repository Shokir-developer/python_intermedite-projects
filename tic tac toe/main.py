board = [' ' for x in range(10)]

def printBoard(board):
	print(" " + board[1] + " | " + board[2] + " | " + board[3])
	print("-----------")
	print(" " + board[4] + " | " + board[5] + " | " + board[6])
	print("-----------")
	print(" " + board[7] + " | " + board[8] + " | " + board[9])


def isBoardFull(board):
	if board.count(" ") > 1:
		return False
	else:
		return True

def isWinner(bo, le):
	return (bo[1] == le and bo[2] == le and bo[3] == le) or\
		   (bo[4] == le and bo[5] == le and bo[6] == le) or\
		   (bo[7] == le and bo[8] == le and bo[9] == le) or\
		   (bo[1] == le and bo[4] == le and bo[7] == le) or\
		   (bo[2] == le and bo[5] == le and bo[8] == le) or\
		   (bo[3] == le and bo[6] == le and bo[9] == le) or\
		   (bo[1] == le and bo[5] == le and bo[9] == le) or\
		   (bo[3] == le and bo[5] == le and bo[7] == le) 

def insertLetter(letter, pos):
	board[pos] = letter

def spaceIsFree(pos):
	return board[pos] == " "

def playMove():
	run = True
	while run:
		move = input("Please select position of 'X' (1-9): ")
		try:
			move = int(move)
			if all([move > 0, move < 10]):
				if spaceIsFree(move):
					run = False
					insertLetter("x", move)
				else:
					print("Sorry, this space is occupied!")
		except:
			print("Please enter a number")

def compMove():
	possibleMoves = [x for x, letter in enumerate(board) if letter==' ' and x!= 0]
	move = 0
	for let in ['o', 'x']:
		for i in possibleMoves:
			boardCopy = board[:]
			boardCopy[i] = let

			if isWinner(boardCopy, let):
				move = i
				return move

	#This checks if one of the players has a wining move
	cornersOpen = []
	for i in possibleMoves:
		if i in [1, 3, 7, 9]:
			cornersOpen.append(i)

	#This checks for open corners
	if len(cornersOpen)>0:
		move = selectRandom(cornersOpen)
		return move

	if 5 in possibleMoves:
		move = 5
		return move

	edgesOpen = []
	for i in possibleMoves:
		if i in [2, 4, 6, 8]:
			edgesOpen.append(i)

	if len(edgesOpen) > 0:
		move = selectRandom(edgesOpen)

	return move


def selectRandom(li):
#li is the list of open spots.
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def main():
	print("welcome to Tic Tac Toe\n")
	printBoard(board)

	while not(isBoardFull(board)):
		if not(isWinner(board, "o")):
			playMove()
			printBoard(board)
		else:
			print("Sorry this time 'o' won")
			break

		if not(isWinner(board, "x")):
			move = compMove()

			if move == 0:
				print("Tie game")
			else:
				insertLetter("o", move)
				print("Computer placed an 'o' in position", move, ": ")
				printBoard(board)

		else:
			print("X's won this time! Good job")
			break

	if isBoardFull(board):
		print("Tie game")

main()
con = input("It is good game: ")