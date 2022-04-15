#Write a python program that receives two integer numbers from the user and print 
#the absolute value of the first number minus the second number.

#For the following input:
#4
#12

#The output should be: 
#The absolute value of (4 - 12) is 8.

#Receive the numbers
first_number = int(input("Please insert the first number: "))
second_number = int(input("Please insert the second number: "))

#Compute the absolute value of the difference
result = abs(first_number - second_number)

#Show the result
print("The absolute value of (%d - %d) is %d." % (first_number, second_number, result))