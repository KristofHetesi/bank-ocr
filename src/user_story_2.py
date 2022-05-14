from user_story_1 import *


def validate(option,arg):
    letters={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    #main option that uses the first user story to get numbers from a file
    if option=='us1':
        #list to store all numbers and their corresponding results
        validity=[]
        file=arg#"../data/0-9_faulty.txt"#
        #call us1
        numbers=(parse_scan(file))
        #hold one account number at once to deal with
        temp=[]
        for c,val in enumerate(numbers[0]):
           temp.append(val)
           #after 9 digits check validity
           if (c+1)%9==0:
               #adapted to us3
               if '?' not in temp:
                   #comprehesion to reverse list and calculate the components of checksum
                   check=[((x+1)*temp[::-1][x]) if str(temp[::-1][x]).isdigit() else ((x+1)*letters[temp[::-1][x]]) for x in range(len(temp))]
                   #rest of the checksum
                   checksum=sum(check)%11
                   #store validity value with number
                   validity.append([(''.join(list(map(str, temp)))),checksum==0])
                   #print results in case this module is used separately
                   #print(f"Account number {validity[((c+1)//9)-1][0]} validity: {validity[((c+1)//9)-1][1]}")
               else:
                   entry=[(''.join(list(map(str, temp)))),"ILL"]
                   #print(f"Account number {entry[0]} validity: {entry[1]}")
                   validity.append(entry)
               temp=[]
        return validity

    elif option=='num':
        nums=arg
        validity=[]
        if '?' not in nums:
            #comprehesion to reverse list and calculate the components of checksum
            check=[((x+1)*int(nums[::-1][x])) for x in range(len(nums))]
            #rest of the checksum
            checksum=sum(list(map(int,check)))%11
            #store validity value with number
            validity.append((''.join(list(map(str, nums)))))
            validity.append(checksum==0)
        else:
           entry=[(''.join(list(map(str, nums)))),"ILL"]
           #print(f"Account number {entry[0]} validity: {entry[1]}")
           validity=entry

        return validity

    else:
        print("Invalid argument")
        exit(0)


if __name__=="__main__":
    if len(sys.argv) < 3:
        print("""Not enough arguments! Usage: 'user_story_2 us1 <filename>' to use first user story; or user_story_2 num <numbers>''""")
        exit(1)
    else:
        valid_list=validate(sys.argv[1],sys.argv[2])
        if len(valid_list)>=2:
            for i in valid_list:
                print(f"Account number {i[0]} validity: {i[1]}")
        else:
            print(f"Account number {valid_list[0]} validity: {valid_list[1]}")






