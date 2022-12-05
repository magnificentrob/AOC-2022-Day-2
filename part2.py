import csv
your_move = []
their_move = []

with open('input.txt') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=' ')
	for row in csv_reader:
		if row[0] == 'A':
			their_move.append('Rock')
		if row[0] == 'B':
			their_move.append('Paper')
		if row[0] == 'C':
			their_move.append('Scissors')
		if row[1] == 'X':
			your_move.append('lose')
		if row[1] == 'Y':
			your_move.append('draw')
		if row[1] == 'Z':
			your_move.append('win')

def gameEvaluator(opponent_choice, outcome):
	if outcome == 'draw' and (opponent_choice == 'Rock' or opponent_choice == 'Paper' or opponent_choice == 'Scissors'):
		if opponent_choice == 'Rock':
			return 4
		elif opponent_choice == 'Paper':
			return 5
		else:
			return 6
	if opponent_choice == 'Rock' and outcome == 'win':
		return 8 #Paper
	if opponent_choice == 'Rock' and outcome == 'lose':
		return 3 #Scissors
	if opponent_choice == 'Paper' and outcome == 'win':
		return 9 #Scissors
	if opponent_choice == 'Paper' and outcome == 'lose':
		return 1 #Rock
	if opponent_choice == 'Scissors' and outcome == 'win':
		return 7 #Rock
	if opponent_choice == 'Scissors' and outcome == 'lose':
		return 2 #Paper

your_score = 0

for i in range(len(your_move)):
	your_score += gameEvaluator(their_move[i], your_move[i])
print(your_score)