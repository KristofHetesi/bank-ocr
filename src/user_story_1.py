import sys

def read_file(filename):
    #list to store the lines from the files; one string is one line
    lines_as_string=[]

    #open the simple dummy file for reading
    with open(filename, 'r') as f:
        #iterate through file
        for c,val in enumerate(f):
                lines_as_string.append(val) #add line to string
                lines_as_string[-1]=lines_as_string[-1][0:-1] #get rid of the new line character at the end of every line without using strip
                #if strip is used the starting spaces also vanish
                if len(lines_as_string[-1])==1 or len(lines_as_string[-1])==0: #if the line is too short
                    #delete every fourth line (empty lines)
                    lines_as_string=lines_as_string[:-1]
    return(lines_as_string)

def make_entries(lines):
    #create lists to parse the data
    entries= []
    entry_as_nested_list=[]
    #iterate over the lines
    for c in range(len(lines)):
        #make every three character into one cohesive element
        #every three character in a line represents a third of the whole digit
        #store in a temporary variable
        separate_digit_parts = ["".join([lines[c][x-3],lines[c][x-2],lines[c][x-1]])
                for x in range(1,(len(lines[c])+1)) if x%3==0]

        #store digit parts as lists in a second temporary variable used later
        entry_as_nested_list.append(separate_digit_parts)

        #reset the first temporary variable since next iteration is dealing with another entry that is handeld separately
        separate_digit_parts=[]

        #every third iteration means that with the third line we have a whole entry stringified and put into lists by line
        if (c+1)%3==0:
            #place the lists as one entry for each three line
            entries.append(entry_as_nested_list)
            #restart temporary variable to allow new entry to be added
            entry_as_nested_list=[]

        #at the end we have a three leveled nested list
        #inner levels represent one line in wich each digit part is a string
        #second level is one entry aka three lines
    return entries


def give_numbers(entries):
    #transpose the inner parts of the nested list
    #reorders them so one inner list is know represents the three parts of a digit
    digit_parts=[list(map(list, zip(*x))) for x in entries]

    #digits represented as their three parts
    digits={0:[' _ ', '| |', '|_|'],1:['   ','  |', '  |'],2:[' _ ', ' _|', '|_ '], 3:[' _ ', ' _|', ' _|'], 4:['   ','|_|', '  |'],
            5:[' _ ', '|_ ', ' _|'], 6:[' _ ', '|_ ', '|_|'], 7:[' _ ', '  |', '  |'], 8:[' _ ', '|_|', '|_|'], 9:[' _ ', '|_|', '  _|']}

    #get dictionary indexes
    key_list = list(digits.keys())
    val_list = list(digits.values())

    #identify a digit by its three parts, modified to work with user story 3
    numbers=[key_list[val_list.index(digit_parts[x][y])] if digit_parts[x][y] in digits.values()  else '?' for x in range(len(digit_parts))  for y in range(len(digit_parts[x])) ]
    #numbers=[key_list[val_list.index(digit_parts[x][y])] for x in range(len(digit_parts)) for y in range(len(digit_parts[x]))]
    return [numbers,digit_parts]

def parse_scan(filename):
    lines=read_file(filename)
    entries=make_entries(lines)
    numbers=give_numbers(entries)
    return numbers


def return_raw(filename):
    lines=read_file(filename)
    entries=make_entries(lines)
    numbers=give_numbers(entries)
    return numbers[1]

if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Not enough arguments! Usage: user_story_1 <filename>")
        exit(1)
    else:
       numbers=(parse_scan(str(sys.argv[1])))
       temp=[]
       for c,val in enumerate(numbers[0]):
           temp.append(val)
           if (c+1)%9==0:
               print(f"Account num: {''.join(list(map(str, temp)))}")
               temp=[]


