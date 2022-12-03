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
print(j[len(j)-1])
print(sum(j[-3:]))
