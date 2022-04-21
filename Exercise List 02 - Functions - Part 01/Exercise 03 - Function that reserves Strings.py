#Write a python program with a function that receives a string of 
#characters and return the reversed string.

#For the following input: Input String

#The function should return:gnirtS tupnI

# =============================================================================
# Functions
# =============================================================================
def reverse_string(input_string):
    #first way
    #reversed_string = input_string[::-1]
    
    #second way
    #reversed_string = list(input_string)
    #reversed_string.reverse()
    #reversed_string = str().join(reversed_string)
    
    #third way
    reversed_string = ""
    for i in range(len(input_string)):
        reversed_string = reversed_string +  \
            input_string[len(input_string) -i -1]
            
    return reversed_string


# =============================================================================
# Main
# =============================================================================
string_example = "Input String"
print("%s" % reverse_string(string_example))
