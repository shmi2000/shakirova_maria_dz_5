def odd_nums(num):
    for num in range(1, num + 1, 2):
        yield num


for a in odd_nums(int(input())):
    print(a)
