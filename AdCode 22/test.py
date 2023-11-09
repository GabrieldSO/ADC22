line = "6-6,4-6"
range_1, range_2 = line.split(",")
range_1_start, range_1_end = range_1.split("-")
range_2_start, range_2_end = range_2.split("-")
#typecasting
range_1_start = int(range_1_start)
range_2_start = int(range_2_start)
range_1_end = int(range_1_end)
range_2_end = int(range_2_end)
#and the checks!
r1s_contains_r2s = bool(range_1_start <= range_2_start)
r1e_contains_r2e = bool(range_1_end >= range_2_end)
print(not(r1s_contains_r2s ^ r1e_contains_r2e))