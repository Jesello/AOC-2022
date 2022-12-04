def part1():
    file = open("input.txt","r")
    point = 0
    for i in file:
        data = i[:-1].split(",")

        data[0] = data[0].split("-")
        data[1] = data[1].split("-")

        g1 = []
        g2 = []
        

        for i in range(int(data[0][0]),int(data[0][1])+1):
            g1.append(i)
            
        for i in range(int(data[1][0]),int(data[1][1])+1):
            g2.append(i)

        b1 = True
        for i in g1:
            if i in g2:
                pass
            else:
                b1 = False

        b2 = True
        for i in g2:
            if i in g1:
                pass
            else:
                b2 = False

        if (b1 == True or b2 == True):
            point += 1
    file.close()
    return point


def part2():
    file = open("input.txt","r")
    point = 0
    for i in file:
        data = i[:-1].split(",")

        data[0] = data[0].split("-")
        data[1] = data[1].split("-")

        g1 = []
        g2 = []
        

        for i in range(int(data[0][0]),int(data[0][1])+1):
            g1.append(i)
            
        for i in range(int(data[1][0]),int(data[1][1])+1):
            g2.append(i)

        b1 = False
        for i in g1:
            if i in g2:
                b1 = True
            else:
               pass

        b2 = False
        for i in g2:
            if i in g1:
                b1 = True
            else:
                pass

        if (b1 == True or b2 == True):
            point += 1
    file.close()
    return point

    
        
        
print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
