x = 0
y = 0
j = []

with open("input.txt","r") as file:
    for i in file:
        if (i == "\n"):
            if (y > x):
                j.append(y)
            y = 0
        else:
            y += int(i)

j.sort()
print(f'Part1: {j[len(j)-1]}')
print(f'Part2: {sum(j[-3:])}')
