
from itertools import repeat
numbers=[]
let=0
with open('../data/0-9_horiz.txt', 'r') as f:

    for c,val in enumerate(f):

            numbers.append(val)


            numbers[-1]=numbers[-1][0:-1]
                #print(" ",end="")



            #el
            if len(numbers[-1])==1 or len(numbers[-1])==0:
                numbers=numbers[:-1]

            #numbers[-1][-1]=''

            #print(line.strip())
        # else:
        #     numbers.append(line)
        #c += 1
        #print([x.split(' ')[1] for x in open(f).readlines()])


numbers2= []
temp=[]
temp2=[]

for c in range(len(numbers)):
    # if c==17:
    #     continue

    for x in range(1,(len(numbers[c])+1)):
        if x%3==0:
            temp.append("".join([numbers[c][x-3],numbers[c][x-2],numbers[c][x-1]]))
            # numbers2[c].append("".join([numbers[c][x-3],numbers[c][x-2],numbers[c][x-1]]))
            # print('nums',numbers2)


    # if c==len(numbers)-1:
    #     temp.append("".join([numbers[c][-3],numbers[c][-2],numbers[c][-1]]))
    #     print("hhata",temp)
    temp2.append(temp)

    temp=[]
    if (c+1)%3==0:
        numbers2.append(temp2)
        print("temp2",temp2)
        temp2=[]
        print("num2",numbers2)



    #numbers2.append()
print(numbers2)
numbers3=[]

for x in numbers2:
    numbers3.append(list(map(list, zip(*x))))

print("num3",numbers3)

numbers4=[]
digits={0:[' _ ', '| |', '|_|'],1:['   ','  |', '  |'],2:[' _ ', ' _|', '|_ '], 3:[' _ ', ' _|', ' _|'], 4:['   ','|_|', '  |'],
        5:[' _ ', '|_ ', ' _|'], 6:[' _ ', '|_ ', '|_|'], 7:[' _ ', '  |', '  |'], 8:[' _ ', '|_|', '|_|'], 9:[' _ ', '|_|', '  _|']}
key_list = list(digits.keys())
val_list = list(digits.values())
for x in range(len(numbers3)):
    for y in range(len(numbers3[x])):
        numbers4.append(key_list[val_list.index(numbers3[x][y])])


print(numbers4)
