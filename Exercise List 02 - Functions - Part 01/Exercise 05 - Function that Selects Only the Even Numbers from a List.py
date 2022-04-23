#Write a python program with a function that receives a list B
#containing integer numbers and return a new list with only the 
#even numbers in B.

#For the following input: 
    #[2, 5, 6, 3, 8, 3, 6, 3, 4, 5, 1]

#The function should return: 
    #[2, 6, 8, 6, 4]

# =============================================================================
# Function
# =============================================================================
def separate_even_numbers(our_list):
    list_even = list([])
    for i in range(len(our_list)):
        if((our_list[i] % 2) == 0):
            list_even.append(our_list[i])
    
    return list_even

# =============================================================================
# Main
# =============================================================================
test_list = [2, 5, 6, 3, 8, 3, 6, 3, 4, 5, 1]
list_even = separate_even_numbers(test_list)
print(list_even)


