import sys

def main(raw_file,writeto):

    validity=validate('us1',raw_file)
    make_results(writeto,validity)
    print(f"Your results have been saved to {writeto}")
    res=error_correction(writeto,raw_file)
    print(f"Your results have been corrected and saved to final_{writeto}")
    return res


if __name__=="__main__":
    if len(sys.argv) < 3:
        print("Not enough arguments! Usage: 'user_story_3 <filenametowrite> <filenamefromread>'")
        exit(1)
    else:
        from user_story_4 import *
        from user_story_3 import *
        main(sys.argv[2],sys.argv[1])

