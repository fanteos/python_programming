#Write a python script that receives two numbers from the user and 
#print the value of the first number divided by the second.


#For the following input: 
    #3
    #4
#The output should be:
    #0.75
    
    

#Receive the numbers
first_number = int(input("Please insert the first number: "))
second_number = int(input("Please insert the second number: "))


#Print the result
print("%.2f" % (first_number / second_number))