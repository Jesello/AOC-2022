index = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

def part1():
    with open('input.txt','r') as file:
        point = 0
        for i in file:
            data = i.split(" ")
            data[1] = data[1][:1]
            
            
            lose = ["AZ" , "BX" , "CY"]
            draw = ["AX", "BY", "CZ"]
            win = ["AY", "BZ" , "CX"]
    
            if data[0] + data[1] in lose:
                point = point + 0 + index[data[1]]
            elif data[0] + data[1] in draw:
                point = point + 3 + index[data[1]]
            elif data[0] + data[1] in win:
                point = point + 6 + index[data[1]]
    return point

def part2():
    with open('input.txt','r') as file:
        point = 0
        for i in file:
            data = i.split(" ")
            data[1] = data[1][:1]


            lose = {
                "A" : "Z",
                "B" : "X",
                "C" : "Y"
            }

            win = {
                "A" : "Y",
                "B" : "Z",
                "C" : "X"
            }

            draw = {
                "A" : "X",
                "B" : "Y",
                "C" : "Z"
            }

            if (data[1] == "Y"):
                point = point + index[draw[data[0]]] + 3
            elif (data[1] == "X"):
                point = point + index[lose[data[0]]] + 0
            elif (data[1] == "Z"):
                point = point + index[win[data[0]]] + 6
    return point
            
print(part1())
print(part2())
