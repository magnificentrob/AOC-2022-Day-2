import csv
your_move = []
their_move = []
total = 0
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
			your_move.append('Rock')
		if row[1] == 'Y':
			your_move.append('Paper')
		if row[1] == 'Z':
			your_move.append('Scissors')


your_score = 0

for i in range(len(your_move)):
	if their_move[i] == your_move[i]:
		if your_move[i] == 'Rock':
			your_score += 4
		elif your_move[i] == 'Paper':
			your_score += 5
		else:
			your_score += 6
	elif their_move[i] == 'Paper' and your_move[i] == 'Rock':
		your_score +=1
	elif their_move[i] == 'Rock' and your_move[i] == 'Paper':
		your_score +=8
	elif their_move[i] == 'Scissors' and your_move[i] == 'Paper':
		your_score+=2
	elif their_move[i] == 'Paper' and your_move[i] == 'Scissors':
		your_score+=9
	elif their_move[i] == 'Rock' and your_move[i] == 'Scissors':
		your_score+= 3
	else:
		your_score+= 7
print(your_score)