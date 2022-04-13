#Write a script to compute and show the maximum and minimum of three given integer numbers


#receive the three numbers
first_number = int(input("Please insert the first integer number: "))
second_number = int(input("Please insert the second integer number: "))
third_number = int(input("Please insert the third integer number: "))


#compute the maximum and minimum
#our_max = max(first_number, second_number, third_number)

our_max = first_number
if(second_number > our_max):
    our_max = second_number
if(third_number > our_max):
    our_max = third_number
    
    
#our_min = min(first_number, second_number, third_number)


our_min = first_number
if(second_number < our_min):
    our_min = second_number
if(third_number < our_min):
    our_min = third_number
    
    
print("The minimum is %d." % our_min)
print("The maximum is %d." % our_max)