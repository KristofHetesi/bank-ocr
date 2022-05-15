# Bank-OCR python portfolio work
## Goal
The purpose of the project is to build a small application to interpret scanned bar accounts given as input in a certain format.
Additionally, to offer some error detection/correcting capabilities

## Project constraints
The project should be done in 2 weeks with (optimally) maximum 20 hours of work.

## Project scope
The project will be done using python with a limited number of libraries.
The main files will consist of one file for each user story as a module.
However, when a user story only adds more functionality to an existing process,
it will be contained in the same file. All the modules should be able to communicate via a caller file, but should be capable of functioning by themselves.

## Results
The project is completely working, however due to the time constraints there is no real error handling implemented,
so the program expects a flawless user,flawless files and flawless inputs to work. Also, the time ran out to implement unit tests
properly so only manual testing was done. The structure could also be improved for more clarity. Further optimization
of the processes would also be required

Since I could not implement proper testing in time, I created a python script to generate a huge number of entries randomly, so hopefully
a lot of possible entries prove more or less that the system works as intended.

## Usage 
### Separately
#### user_story_1
Run the file from the command line. Takes 1 argument: the name of the file with the scanned numbers
#### user_story_2
Run the file from the command line. Has two options. If you give 'us1' as the first argument,
you need to have the name of the scanned file as a second argument, to validate numbers from a file.
If you give 'num' as the first argument,
you need to have a 9 digit number as a second argument, to validate the number.
#### user_story_3
Run the file from the command line. Takes 2 arguments: name of the file you want your results to be written in and the name
of the file with the raw scanned numbers.
#### user_story_4
Run the file from the command line. Takes the file name that contains the results of the validation and the file name of the raw, scanned entries.

### Together
Run main with 2 arguments: name of the file you want your results to be written in and the name
of the file with the raw scanned numbers.

The final solutions are visible clearly in the final_<yourfile>.txt file after running the scripts.


### Comment
To see the code working, generate a text file using data_creation, which randomly creates 5000 entries to a txt file, or use the test.txt.

## Files
### structure
The files are separated into 3 folders. scr is the code folder, data is for the text files, which were used to
manually test the code.
The test folder contains the tests (work in progress due to time issues)
### main
Used to execute all the components

### user_story_1.py

#### read_file
This function gets a filename as an input, then reads the contents and returns a list, containing all the lines,
a line as one consecutive string of characters

#### make_entries
This function continues the work of the read_files. Takes a list of strings as an input, and through a series of
transformation return a multiple nested list (three cahracters representing a third of the digit inside a list
of the characters in one line.)

#### give_numbers
Continues the work of the previous function, takes a nested list as input, transposes it to make a nested list 
where each digit is inside a list as the three parts of it (top,bottom,middle). Then it identifies which number belongs
to a batch of characters and returns it.

#### parse_scan
The driver to execute all the previous functions in order. Takes the filename as input returns the account numbers
and the final matrix of scanned characters

#### return_raw
Returns only the raw formatted characters

### user_story_2

#### validate
If the user input was us1 it works with a file and uses the first user case, if the input was num it validates a 
single entry, but the functionality is almost completely the same in both parts.

This function calculates a checksum and returns all account numbers paired with the checksum value.

### user_story_3

#### make_results
This function takes a filename to write to and the filename of the raw entries to format and write the results using the first two user stories.

### user_story_4

#### error_correction
Takes as argument the file name with the results from validation and the raw numbers file name.
Then it executes the two other functions in the file to try and correct  entries with labels ILL or ERR. Then returns the final results.

#### find_alt_ERR
This function tries to correct entries with label ERR-invalid checksum. Takes an entry as an input and finds all possible combinations of numbers.
In case of one possible solution it returns the solution, in case there are multiple solutions appends the label AMB and in case
there is no possible combination with valid checksum it returns ERR.

#### find_alt_ILL
This function tries to correct entries with label ILL-illegible digit. Takes an entry as raw format, the position of the illegible character and the entry itself as an input and finds all possible digits to replace the illegible one.
It has multiple recursions to deal with validating the entry again if it has another ?

This function should be simplified in the future. Due to time constraints I used my first complex solution at the end.




