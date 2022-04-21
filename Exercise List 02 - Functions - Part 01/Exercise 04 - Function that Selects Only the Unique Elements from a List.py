#Write a python program with a function that receives a list A
#of integer numbers and return a new list containing only one 
#occurrence of each element from A.

#For the following input: [2, 5, 6, 3, 8, 3, 6, 3, 4, 5, 1]

#The function should return: [2, 5, 6, 3, 8, 4, 5, 1]


# =============================================================================
# The functions
# =============================================================================
def unique_elements(input_list):
    #first way
    #unique_list = set(input_list)
    #unique_list = list(unique_list)
    
    #second way
    unique_list = list([])
    for i in input_list:
        if(not i in unique_list):
            unique_list.append(i)
    
    return unique_list




# =============================================================================
# The main
# =============================================================================
test = [2, 5, 6, 3, 8, 3, 6, 3, 4, 5, 1]
unique = unique_elements(test)
print(unique)