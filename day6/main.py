def part1():
    file = open('input.txt','r').read()

    for i in range(4,len(file)):
        if len(set(file[i-4:i])) == 4:
            return i

def part2():

    file = open('input.txt','r').read()

    for i in range(14,len(file)):
        if len(set(file[i-14:i])) == 14:
            return i
     
print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
