def is_empty(x):
    if not x:
        return True
    for i in x:
        if i != ' ':
            return False
    return True
    
def part1():
    packages = ['' for i in range(9)]
    stacks = []
    output = ''
    file = open('input.txt','r')
    
    get_package = False
    
    for i in file:
        if (i[:-1] == '\n'):
            i = i[:-1]
        
        if (i.startswith(' 1')):
            for b in enumerate(packages):
                packages[b[0]] = packages[b[0]][::-1]
            get_package = True
            for stack in packages:
                stacks.append(list(stack))
            
        
        if (get_package == False):
            count = 0
            for a in range(0,len(i),4):
                if (is_empty(i[a:a+4][1])):
                    count += 1
                    continue
                else:
                    packages[count] += i[a:a+4][1]
                    count += 1
                    
        if (i.startswith('move')):
            i = i.split(' ')
            data = [int(i[1]),int(i[3])-1,int(i[5])-1]
            for _ in range(data[0]):
                stacks[data[2]].append(stacks[data[1]].pop())
    for i in stacks:
        output += i[-1]
    
    return output
        
    
            
    

def part2():
    packages = ['' for i in range(9)]
    output = ''
    file = open('input.txt','r')
    
    get_package = False
    
    for i in file:
        if (i[:-1] == '\n'):
            i = i[:-1]
        
        if (i.startswith(' 1')):
            for b in enumerate(packages):
                packages[b[0]] = packages[b[0]][::-1]
            get_package = True
            
        
        if (get_package == False):
            count = 0
            for a in range(0,len(i),4):
                if (is_empty(i[a:a+4][1])):
                    count += 1
                    continue
                else:
                    packages[count] += i[a:a+4][1]
                    count += 1
                    
        if (i.startswith('move')):
            i = i.split(' ')
            data = [int(i[1]),int(i[3])-1,int(i[5])-1]
            
            packages[data[2]] = packages[data[2]] + packages[data[1]][-data[0]:]
            packages[data[1]] = packages[data[1]][:-data[0]]
            
    for i in packages:
        output += i[-1]
    
    return output




print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
