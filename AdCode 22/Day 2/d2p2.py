#the first few lines are boilerplate code for opening txt files
f = open("Day 2/d2i.txt", "r")
lines = f.readlines()
overall_score = 0
#we're using dictionaries again but this time we're doing something clever
#write out the list of possibilities to get clarity in the dictionary
score_dict = {'A X': 3, 'A Y': 1, "A Z": 2, 'B X': 1, 'B Y': 2, "B Z": 3, 'C X': 2, 'C Y': 3, "C Z": 1}
#since XYZ is our results (lose/tie/win) we just assign that value
end_dict = {"X": 0, "Y": 3, "Z": 6}
for line in lines:
    round_score = 0
    #clear trailing whitespace
    line = line.rstrip()
    played_line = line.split()
    round_end = played_line[1]
    #so just add it back up
    round_score = score_dict[line] + end_dict[round_end]
    overall_score = overall_score + round_score
print(overall_score)