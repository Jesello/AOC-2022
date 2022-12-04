import string

def sum_items(items):
    point = 0
    
    for i in items:
        if i in string.ascii_letters:
            point = point + string.ascii_letters.index(i) + 1
    return point

def part1():
    items = []
    
    with open('input.txt','r') as file:
        for i in file:
            i = i[:-1]
            data = i[:int(len(i)/2)],i[int(len(i)/2):]
                
            for i in data[0]:
                if i in data[1]:
                    items.append(i)
                    break
    

    return sum_items(items)


def part2():
    
    items = []
    lines = []
    count = 0
    
    with open('input.txt','r') as file:
        for i in file:
            i = i[:-1]
            count +=1
            lines.append(i)
            if (count == 3):
                for a in lines[0]:
                    if a in lines[1] and a in lines[2]:
                        items.append(a)
                        break
                lines.clear()
                count = 0
    
    return sum_items(items)

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
