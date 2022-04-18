#Write a python program with a function that will receive any quantity of
#integer numbers from the user. The function will stop receiving numbers
# when the user insert the number zero. The function will return all the
#numbers received as a list.


# =============================================================================
# The function
# =============================================================================
def receive_inputs():
    our_list = []
    
    while(True):
        current_number = int(input("Please insert a number (zero to stop): "))

        if(current_number == 0):
            return our_list
        
        our_list.append(current_number)



# =============================================================================
# The main
# =============================================================================
l = receive_inputs()
print(l)