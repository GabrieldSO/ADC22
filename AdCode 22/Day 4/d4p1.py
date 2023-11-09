#the first few lines are boilerplate code for opening txt files
f = open("Day 4/d4i.txt", "r")
lines = f.readlines()
containment_counter = 0
for line in lines:
    #clear trailing whitespace
    line = line.rstrip()
    #so we need to parse this into 4 options per line
    range_1, range_2 = line.split(",")
    range_1_start, range_1_end = range_1.split("-")
    range_2_start, range_2_end = range_2.split("-")
    #typecasting
    r1_start = int(range_1_start)
    r2_start = int(range_2_start)
    r1_end = int(range_1_end)
    r2_end = int(range_2_end)
    if(r1_start >= r2_start and r1_end <= r2_end):
        containment_counter += 1
    elif(r2_start >= r1_start and r2_end <= r1_end):
        containment_counter += 1
    
print(containment_counter)

    