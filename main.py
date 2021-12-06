file = open("input")
halak_strings = file.readline().split(",")
print(halak_strings)
halak = []
for i in halak_strings:
    halak.append(int(i))
print(halak)
halak_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
for i in halak:
    halak_dict[i] = halak_dict[i] + 1


for i in range(1, 257):
    nullas_db = halak_dict[0]
    halak_dict[0] = halak_dict[1]
    halak_dict[1] = halak_dict[2]
    halak_dict[2] = halak_dict[3]
    halak_dict[3] = halak_dict[4]
    halak_dict[4] = halak_dict[5]
    halak_dict[5] = halak_dict[6]
    halak_dict[6] = halak_dict[7]
    halak_dict[7] = halak_dict[8]
    halak_dict[6] = halak_dict[6]+nullas_db
    halak_dict[8] = nullas_db

sum = 0
for i in halak_dict.values():
    sum = sum+i

print(halak_dict)
print("szumma: ", sum)
