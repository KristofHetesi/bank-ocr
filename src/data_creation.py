import random

numbers=[''' _ 
| |
|_|''']

digits={0:[' _ ', '| |', '|_|'],1:['   ','  |', '  |'],2:[' _ ', ' _|', '|_ '], 3:[' _ ', ' _|', ' _|'], 4:['   ','|_|', '  |'],
            5:[' _ ', '|_ ', ' _|'], 6:[' _ ', '|_ ', '|_|'], 7:[' _ ', '  |', '  |'], 8:[' _ ', '|_|', '|_|'], 9:[' _ ', '|_|', ' _|'],
            'A':[' _ ', '|_|', '| |'],'B':[' _ ', '|_\\', '|_/'],'C':[' _ ', '|  ', '|_ '],'D':[' _ ', '| \\', '|_/'],
             'E':[' _ ', '|_ ', '|_ '],'F':[' _ ', '|_ ', '|  ']}

#create a mass of test cases without specific test goal
#give number of entries as input
def create_entries_mass(pc,file):
    filetowrite=file
    toprint=[]
    for i in range(pc*9):
        toprint.append((random.choices((list(digits.items())))[0]))
    entries=[x[0] for x in toprint]
    symbols=[x[1] for x in toprint]
    chunked = [symbols[i:i+9] for i in range(0, len(symbols), 9)]
    f = open(filetowrite, "w")

    random_weights= [0] * 14 + [1] * 1
    for x in range(len(chunked)):

        for i in range(3):

            line=""
            new=""
            for y in range(len(chunked[x])):
                messup=random.choice(random_weights)
                if messup==1:
                    new=chunked[x][y][i][:-1]+' '
                else:
                    new=chunked[x][y][i]
                line+=new
            # if messup==1:
            #     line=line[:-2]
            f.write(line+'\n')

        f.write('\n')

    f.close()
    return [entries,symbols]

if __name__=="__main__":
    create_entries_mass(500,"../data/test_mass.txt")











