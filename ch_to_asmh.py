from Lexer import *
from Syntax import *

"""
This compiles a C header file into its equivalent
ARM Cortex M0+ implementation.
"""

def main():
    """
    This is the main function that calls every other
    function in order to parse a given file to an
    output compiled assembly file.
    """
    
    # Open the files
    nm=open(input("In file: "))
    ou=open(input("Out file: "), "w")
    
    # Call the parser to parse the input to the output
    parser(nm,ou)
    
    # Close the files
    nm.close()
    ou.close()

def parser(nm,ou):
    """
    This takes an input file and and output
    file and parses them.
    
    Inputs:
        nm - The input file
        ou - The output file
    """
    
    # Create a Syntax object
    synt=Syntax()
    
    # Loop around for each line
    for i in nm:
        sp=(' '.join(i.split())).split(" ")
        if sp[0] == '#define':
            val=sp[2]
            if "0x" in val:
                val=val.replace("u","")
            else:
                val=""
            if val != "":
                equ(ou,sp[1],val)

def equ(outFil, val1, val2):
    outFil.write(val1)
    outFil.write(" EQU ")
    outFil.write(val2)
    outFil.write("\n")

main()
