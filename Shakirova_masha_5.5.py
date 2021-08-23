src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

rezult = {a: 0 for a in src}
print(rezult)

for a in src:
    if a in rezult:
        rezult[a] += 1
print(rezult)
print([a for a in rezult if rezult[a] == 1])
