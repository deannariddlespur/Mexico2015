#/Users/deannariddlespur/Github/Mexico2015
# python ex15.py ex15_sample.txt
# 1. Above each line, write out in English what that line does.

# 
#from sys import argv Says: From the module named sys (which, if it were in a file would be in a file named 'sys.py') import the thing named 'argv' into the current name context. That makes it possible to refer to 'argv' without having to mention the module it came from
from sys import argv

#??????
script, filename = argv

# sets the variable text to open the file
txt = open(filename)

#prints the text file with the name of the file in the output
print "Here's your file %r:" % filename

#file.read(n) - This method reads n number of characters from the file, or if n is blank it reads the entire file. 
print txt.read()
# prints the text following the print statement
print "Type the text filename again:"
# asks the user to put the name of the text tile in  and stores it in the file_ again variable
file_again = raw_input("> ")
#assigns the variable txt_again the contents of the file_again variable
txt_again = open(file_again)
# prints the contents of the txt_again variable which is the contents of the .txt file created
print txt_again.read()