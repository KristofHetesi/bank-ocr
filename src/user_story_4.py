import sys
from user_story_2 import *
from user_story_1 import *


digits={0:[' _ ', '| |', '|_|'],1:['   ','  |', '  |'],2:[' _ ', ' _|', '|_ '], 3:[' _ ', ' _|', ' _|'], 4:['   ','|_|', '  |'],
            5:[' _ ', '|_ ', ' _|'], 6:[' _ ', '|_ ', '|_|'], 7:[' _ ', '  |', '  |'], 8:[' _ ', '|_|', '|_|'], 9:[' _ ', '|_|', '  _|']}

def find_alt_ILL(entries,position,entry):
    symbols=entries[position]
    alt=[]

    for k,v in digits.items():
        same=len([x for x in range(len(symbols)) if symbols[x] == v[x]])
        diff= [[symbols[x],x] for x in range(len(symbols)) if symbols[x] != v[x]]
        pos=diff[0][1]
        diff=diff[0][0]

        if same==2:
            for x in range(3):
                if diff[:x] + '|' + diff[x+1:]==v[pos] or diff[:x] + ' ' + diff[x+1:]==v[pos] or diff[:x] + '_' + diff[x+1:]==v[pos]:
                    alt.append(k)


    if len(alt)==1:
        entry = entry[:position]+str(alt[0])+entry[position+1:]
        new=(validate('num',entry))
        if new[1]=='ILL':
            final=find_alt_ILL(entries,new[0].index("?"),entry)
        else:
            return new

    elif len(alt)==0:
        return [entry,'AMB']

    else:
        return [entry,'ILL']

    return(final)



def error_correction(file,rawfile):

    raw=return_raw(rawfile)

    #open the simple dummy file for reading
    with open(file, 'r') as f:
        #iterate through file
        for c,line in enumerate(f):
                entry=line.strip().split()
                if entry[1]=="ILL":
                    entry[0].index("?")
                    # for i in range(len(entry[0])):
                    #     if entry[0][i]=="?":
                    print(find_alt_ILL(raw[c],entry[0].index("?"),entry[0]))










if __name__=="__main__":
    if len(sys.argv) < 3:
        print("Not enough arguments! Usage: 'user_story_4 <results filename> <unparsed data filename>'")
        exit(1)
    else:
        error_correction(sys.argv[1],sys.argv[2])
