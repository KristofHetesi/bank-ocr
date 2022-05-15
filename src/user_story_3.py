try:
    from user_story_1 import *
    from user_story_2 import *
except:pass

def make_results(tof,fromf):
    if __name__!="user_story_3":
        results=validate('us1',fromf)
    else:
        results=fromf
    with open(tof, 'w') as f:
        for entry in results:
            if entry[1]==True:
                formatted=f"{entry[0]}\n"
            elif entry[1]==False:
                formatted=f"{entry[0]} ERR\n"
            else:
                formatted=f"{entry[0]} {entry[1]}\n"
            f.write(formatted)



if __name__=="__main__":
    if len(sys.argv) < 3:
        print("Not enough arguments! Usage: 'user_story_3 <filenameto> <filenamefrom>'")
        exit(1)
    else:
        make_results(sys.argv[1],sys.argv[2])
