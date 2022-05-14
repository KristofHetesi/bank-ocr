import sys
from user_story_3 import *


digits={0:[' _ ', '| |', '|_|'],1:['   ','  |', '  |'],2:[' _ ', ' _|', '|_ '], 3:[' _ ', ' _|', ' _|'], 4:['   ','|_|', '  |'],
            5:[' _ ', '|_ ', ' _|'], 6:[' _ ', '|_ ', '|_|'], 7:[' _ ', '  |', '  |'], 8:[' _ ', '|_|', '|_|'], 9:[' _ ', '|_|', '  _|'],
            'A':[' _ ', '|_|', '| |'],'B':[' _ ', '|_\\', '|_/'],'C':[' _ ', '|  ', '|_ '],'D':[' _ ', '| \\', '|_/'],
             'E':[' _ ', '|_ ', '|_ '],'F':[' _ ', '|_ ', '|  ']}

#function to deal with ILL labeled entries
def find_alt_ILL(entries,position,entry):
    #store the 3 digit parts for altering
    symbols=entries[position]
    #store alterations solutions
    alt=[]
    #iterate digits dictionary
    for k,v in digits.items():
        #get the number of parts that match in the dictionary item and the item we want to alter
        same=len([x for x in range(len(symbols)) if symbols[x] == v[x]])
        #get the part that is different between the two
        diff= [[symbols[x],x] for x in range(len(symbols)) if symbols[x] != v[x]]

        #in case there is only one part that is different, we can try and alter it
        if same==2:
            #position of the part inside the symbols
            pos=diff[0][1]
            #the part itself to be altered
            diff=diff[0][0]
            #we have three position we change inside one part
            for x in range(3):
                #try all three positions with all three possible symbols and see if they match the last missing part for a correct number
                if diff[:x] + '|' + diff[x+1:]==v[pos] or diff[:x] + ' ' + diff[x+1:]==v[pos] or diff[:x] + '_' + diff[x+1:]==v[pos] or \
                       diff[:x] + '\\' + diff[x+1:]==v[pos] or diff[:x] + '/' + diff[x+1:]==v[pos] :
                    #add to possible alterations
                    alt.append(k)



    # only one good option, then validate our newly created numbers
    if len(alt)==1:
        entry = entry[:position]+str(alt[0])+entry[position+1:]
        new=(validate('num',entry))
        #we may still have some illegible digits in there
        if new[1]=='ILL':
            #call recursively the function again to deal with all ?s one by one
            return find_alt_ILL(entries,new[0].index("?"),entry)
        else:
            return new

    #multiple options -> starts a series of recursive calls
    elif len(alt)>1:
        #iterate options
        for opt in alt :
            #evaluate new numbers
            entr = entry[:position]+str(opt)+entry[position+1:]
            new=validate('num',entr)
            #if there are still ? after this
            if new[1]=='ILL':
                #call recursively the function again to deal with all ?s one by one
                final=find_alt_ILL(entries,new[0].index("?"),entr)
                #at the end of the recursion see if the final numbers have a valid checksum if not then delete first option
                if final[1]==False:
                    alt.remove(opt)

    #after the iterations we need to check again if we have only one valid option
    if len(alt)==1:
        entry = entry[:position]+str(alt[0])+entry[position+1:]
        new=(validate('num',entry))
        #we may still have some illegible digits in there
        if new[1]=='ILL':
            #call recursively the function again to deal with all ?s one by one
            final=find_alt_ILL(entries,new[0].index("?"),entry)
        else:
            return new

    #still multiple options remaining-> send back to later evaluation
    elif len(alt)>1:
        return [entry,'AMB']
    #no options, return original
    else:
        return [entry,'ILL']

    return(final)


#function to correct numbers with ERR label
def find_alt_ERR(numbers):
    #all the possible alternatives to each number
    alternatives={0:[8],1:[7],2:[],3:[9],4:[],5:[6,9,'E'],6:[5,8],7:[1],8:[0,6,9,'A'],9:[3,5,8],'A':[8],'B':['D'],'C':['E'],'D':['B'],
                  'E':[6,'C','F'],'F':['E']}
    alts=[]
    #iterate numbers
    for c,dig in enumerate(numbers):
        if dig.isdigit():
            dig=int(dig)
        #iterate possible alternatives to digit
        for x in alternatives[dig]:
            #check validity with new numbers
            new = validate('num',numbers[:c]+str(x)+numbers[c+1:])
            if new[1] == True:
                alts.append(new)
    if len(alts)==1:
        return alts[0]
    elif len(alts)>1:
        return [numbers,"AMB"]

    else:
        return [numbers,False]

#function to correct ILL and ERR labeled entries
def error_correction(file,rawfile):

    raw=return_raw(rawfile)
    new_entries=[]
    #open the simple dummy file for reading
    with open(file, 'r') as f:
        #iterate through file
        for c,line in enumerate(f):
            new_entry=[]
            entry=line.strip().split()
            if entry[1]=="ILL":
                new_entry=find_alt_ILL(raw[c],entry[0].index("?"),entry[0])
                #after correcting the ILL its still possible to have invalid checksum
                if  new_entry[1] == False:
                    new_entry=find_alt_ERR(new_entry[0])

            elif entry[1]=="ERR":
                new_entry=find_alt_ERR(entry[0])

            new_entries.append(new_entry)
    make_results(f"{file}_final",new_entries)



if __name__=="__main__":
    if len(sys.argv) < 3:
        print("Not enough arguments! Usage: 'user_story_4 <results filename> <unparsed data filename>'")
        exit(1)
    else:

        error_correction(sys.argv[1],sys.argv[2])
