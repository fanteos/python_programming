#Write a python program with a function that receives a string 
#of characters and check if the string is a palindrome. 
#A palindrome is a sequence of characters or numbers which can 
#be read forward or backwards with the same meaning. 
#Examples of palindromes are: madam, ana and otto. 
#The function must return a boolean containing either True 
#if the word is a palindrome or False otherwise. 

#For the following input: 
    #otto

#The function should return: 
    #True

# =============================================================================
# Function
# =============================================================================
def verify_palindrome(string):
    flag = False
    
    string_reversed = string[::-1]
    
    if(string == string_reversed):
        flag = True
    
    return flag



# =============================================================================
# Main
# =============================================================================
test1 = "otto"
print(verify_palindrome(test1))

test2 = "3otto3"
print(verify_palindrome(test2))

test3 = "ottio"
print(verify_palindrome(test3))

