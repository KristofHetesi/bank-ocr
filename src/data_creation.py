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
        toprint.append((random.choices((list(digits.values())))[0]))
    chunked = [toprint[i:i+9] for i in range(0, len(toprint), 9)]
    f = open(filetowrite, "a")


    for x in range(len(chunked)):
        for i in range(3):
            line=""
            for y in range(len(chunked[x])):
                print(chunked[x][y][i])
                line+=chunked[x][y][i]
            f.write(line+'\n')
        f.write('\n')

    f.close()

if __name__=="__main__":
    inp=input("File: ")
    create_entries_mass(500,inp)











