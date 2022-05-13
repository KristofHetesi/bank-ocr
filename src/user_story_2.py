from user_story_1 import *

def validate(option):
    #main option that uses the first user story to get numbers from a file
    if option=='us1':
        #list to store all numbers and their corresponding results
        validity=[]
        file="../data/0-9_horiz.txt"#input("Filepath: ")
        #call us1
        numbers=(parse_scan(file))
        #hold one account number at once to deal with
        temp=[]
        for c,val in enumerate(numbers):
           temp.append(val)
           #after 9 digits check validity
           if (c+1)%9==0:
               #comprehesion to reverse list and calculate the components of checksum
               check=[((x+1)*temp[::-1][x]) for x in range(len(temp))]
               #rest of the checksum
               checksum=sum(check)%11
               #store validity value with number
               validity.append([(''.join(list(map(str, temp)))),checksum==0])
               #print results in case this module is used separately
               print(f"Account number {validity[((c+1)//9)-1][0]} validity: {validity[((c+1)//9)-1][1]}")
               temp=[]
        return validity

    elif option=='num':
        nums=(input("Numbers: "))
        validity=[]
        #comprehesion to reverse list and calculate the components of checksum
        check=[((x+1)*int(nums[::-1][x])) for x in range(len(nums))]
        #rest of the checksum
        checksum=sum(list(map(int,check)))%11
        #store validity value with number
        validity.append((''.join(list(map(str, nums)))))
        validity.append(checksum==0)
        print(f"Account number {validity[0]} validity: {validity[1]}")
        return validity

    else:
        print("Invalid argument")
        exit(0)


if __name__=="__main__":
    if len(sys.argv) < 2:
        print("""Not enough arguments! Usage: 'user_story_2 <option>' ; options: 'us1' to use numbers from the first components freshly parsed
        or 'num' to input your own numbers as a single entry for test purposes""")
        exit(1)
    else:
        validate(sys.argv[1])





