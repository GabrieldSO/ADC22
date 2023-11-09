#the first few lines are boilerplate code for opening txt files
f = open("Day 2/d2i.txt", "r")
lines = f.readlines()
overall_score = 0
#we're using a pair of dictionaries here
#the idea is that we're going to read the re
score_dict = {'A X': 3, 'A Y': 6, "A Z": 0, 'B X': 0, 'B Y': 3, "B Z": 6, 'C X': 6, 'C Y': 0, "C Z": 3}
#the score is then determined by what you played - since XYZ is RPS then we just assign the those values
player_dict = {"X": 1, "Y": 2, "Z": 3}
for line in lines:
    round_score = 0
    #clean trailing whitespace
    line = line.rstrip()
    #get the player's line
    player_line = line.split()
    player_line = player_line[1]
    #determine score by verifying the line played and what you played against the dictionary
    round_score = score_dict[line] + player_dict[player_line]
    #add it all back up
    overall_score = overall_score + round_score
print(overall_score)