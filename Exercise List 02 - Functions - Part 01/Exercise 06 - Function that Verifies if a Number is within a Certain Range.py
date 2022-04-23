#Write a python program with a function that receives a number 
#and check if the number is within the range [0, 55]. 
#The function must return a boolean containing either True 
#if the number is within the range or False otherwise.

#For the following input: 
    #7

#The function should return: 
    #True
    
# =============================================================================
# Function
# =============================================================================
def verify_interval(number, interval = [0, 55]):
    flag = False
    
    if((number >= interval[0]) and (number <= interval[1])):
        flag = True
        
    return flag


# =============================================================================
# Main
# =============================================================================
print(verify_interval(7))

print(verify_interval(7, [0, 6]))

print(verify_interval(55))