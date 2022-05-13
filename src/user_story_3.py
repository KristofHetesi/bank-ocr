from user_story_1 import *
from user_story_2 import *

def make_results(tof):
    results=validate('us1')
    with open(tof, 'a') as f:
        for entry in results:
            if entry[1]==True:
                formatted=f"{entry[0]}\n"
            elif entry[1]==False:
                formatted=f"{entry[0]} ERR\n"
            else:
                formatted=f"{entry[0]} {entry[1]}\n"
            f.write(formatted)

if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Not enough arguments! Usage: 'user_story_3 <filenameto>'")
        exit(1)
    else:
        make_results(sys.argv[1])
