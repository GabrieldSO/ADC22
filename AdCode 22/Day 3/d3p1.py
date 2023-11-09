from collections import defaultdict
#so we have a string that we'll split in two
def find_matching_character(string_1, string_2):
    #defaultdict(int) starts a dictionary with everything keyed to 0
    dict_s1 = defaultdict(int)
    dict_s2 = defaultdict(int)
    # then we iterate over the string
    for char in string_1:
        #and now we look in the dictionary and add +1 to whatever is already stored in the key associated with the digit
        dict_s1[char] += 1
    for char in string_2:
        dict_s2[char] += 1
    #there's a messy bit of code here that needs to be explained
    #what this does is a) dict_s1.keys() & dict_s2.keys() - & is the intersect operand
    #so this gives us a set of the keys that exist in both
    #list()[0] is syntatic manipulation to get it in list form so we can access by index and pull the value from the inside
    return list(dict_s1.keys() & dict_s2.keys())[0]

def character_value(character_input):
    #the point of this is to convert a character into a number and give us a solid output, it's otherwise pretty unremarkable
    mod = 0
    #we now determine how much we need to subtract to get our desired values
    if(character_input.isupper()):
        # the ASCII mod that gives us A = 27 through Z = 52
        mod = 38
    else:
        #the ASCII mod that gives us a = 1 through z = 26
        mod = 96
    return ord(character_input) - mod

#could we not have done this as a function? could I not have extensively coded this out?
#yes, but why?

#the first few lines are boilerplate code for opening txt files
f = open("Day 3/d3i.txt", "r")
lines = f.readlines()
total_priority = 0
for line in lines:
    #clear trailing whitespace
    line = line.rstrip()
    #yay for list indexes!
    string_1, string_2 = line[:len(line)//2], line[len(line)//2:]
    matching_char = find_matching_character(string_1, string_2)
    char_priority = character_value(matching_char)
    total_priority += char_priority
    
print(total_priority)
    