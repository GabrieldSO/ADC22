#the first few lines are boilerplate code for opening txt files
f = open("Day 5/d5i.txt", "r")
lines = f.readlines()
containment_counter = 0
input_string = "        [C] [B] [H]                "
for char in input_string:
    print(char)