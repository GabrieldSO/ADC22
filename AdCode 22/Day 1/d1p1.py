f = open("d1p1i.txt", "r")
lines = f.readlines()
elf_list = []
elf_calorie_counter = 0
for line in lines:
    if line != "\n":
        elf_calorie_counter = elf_calorie_counter + int(line)
    else:
        elf_list.append(elf_calorie_counter)
        elf_calorie_counter = 0
print(max(elf_list))