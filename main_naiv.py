file = open("input")
halak_strings = file.readline().split(",")
print(halak_strings)
halak = []
for i in halak_strings:
    halak.append(int(i))
print(halak)
kov_halak = []
for i in range(1, 257):
    for hal in halak:
        if hal > 0:
            kov_halak.append(hal - 1)
        else:
            kov_halak.append(6)
            kov_halak.append(8)
    halak = kov_halak.copy()
    print(str(i) + " nap: ")
    kov_halak = []

print(len(halak))