#Write a python program that receives one integer number from the user and 
#print if the number is divisible by 3 or by 5.

#For the following input:
#15
#The output should be: 
#The number 15 is divisible by 3 and by 5.

#For the following input: 
#9
#The output should be:
#The number 9 is divisible by 3.

#For the following input:
#2
#The output should be:
#The number 2 is not divisible neither by 3 nor by 5.

#Receive a number
our_number = int(input("Please insert a number: "))

#Check if it is divisible
is_divisible_by_3 = False
if((our_number % 3) == 0):
    is_divisible_by_3 = True

is_divisible_by_5 = False
if((our_number % 5) == 0):
    is_divisible_by_5 = True

#Print the results
if(is_divisible_by_3 and is_divisible_by_5):
    print("The number %d is divisible by 3 and by 5." % our_number)
elif(is_divisible_by_3):
    print("The number %d is divisible by 3." % our_number)
elif(is_divisible_by_5):
    print("The number %d is divisible by 5." % our_number)
else:
    print("The number %d is not divisible neither by 3 nor by 5." % our_number)
    
    
    
    
    
    
    
    