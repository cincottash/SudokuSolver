from puzzles import *

def printPuzzle(puzzle):
	for i in range(9):
		print(puzzle[i])

#checks if the puzzle is sovled or not
def solved(puzzle):
	for i in range(9):
		for j in range(9):
			if(puzzle[i][j] == 0):
				return True
	return False

#checks if a placed number has a duplicate in the row
def checkRow(puzzle, row, num):
	for i in puzzle[row]:
		if(i == num):
			return True
	return False

#checks if a placed number has a duplicate in the col
def checkCol(puzzle, col, num):
	for row in range(9):
		if(puzzle[row][col] == num):
			return True
			
	return False

#checks if a number exists within its corresponding triplet certain triplet
def checkTriplet(puzzle, row, col, num):
	#row/colStart always return the top left of the triplet
	rowStart = (row//3)*3
	colStart = (col//3)*3

	for i in range(3):
		for j in range(3):
			if(puzzle[i+rowStart][j+colStart] == num):
				return True

	return False

#checks if we can place a number at the requested spot
def canPlace(puzzle, row, col, num):
	if(not checkTriplet(puzzle, row, col, num) and not checkCol(puzzle, col, num) and not checkRow(puzzle, row, num)):
		return True
	else:
		return False

def findNextEmptySpot(puzzle, current):
	for i in range(9):
		for j in range(9):
			if(puzzle[i][j] == 0):
				current[0] = i
				current[1] = j
				return True
	return False

def solve(puzzle):

	#current controls which square we're currently working on
	current = [0,0]

	#if there are no more empty spots we have solved the puzzle
	if(not findNextEmptySpot(puzzle, current)):
		return True

	row = current[0]
	col = current[1]

	for num in range(1, 10):
		if(canPlace(puzzle, row, col, num)):
			puzzle[row][col] = num

			if(solve(puzzle)):
				return True

			puzzle[row][col] = 0
	return False


def main():
	print("Starting board:")
	printPuzzle(hardTest)
	print("\n")

	if(solve(hardTest)):
		print("Solved board:")
		printPuzzle(hardTest)
	else:
		print("No solution exists")
	


if __name__ == "__main__":
	main()