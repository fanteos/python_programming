#Receive an integer number and check if the number is either even or odd



#receive an integer number
our_number = int(input("Please insert an integer number: "))


#check if it is even or odd and print the result
if((our_number % 2) == 0):
    print("The number (%d) is even." % our_number)
else:
    print("The number (%d) is odd." % our_number)