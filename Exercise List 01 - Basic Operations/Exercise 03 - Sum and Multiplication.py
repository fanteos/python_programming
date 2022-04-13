#Write a script to compute and show the sum and multiplication of the two integer numbers



#receive two integer numbers
first_number = int(input("Please input the first integer number: "))
second_number = int(input("Please input the second integer number: "))


#compute the sum and multiplication
#our_sum = sum(first_number, second_number)

our_sum = first_number + second_number

our_mult = first_number * second_number



#print the results
print("The sum of %d and %d is %d." % (first_number, second_number, our_sum))
#print("The sum of ", first_number, " and ", second_number, " is ", our_sum, ".", sep="")

print("The multiplication of %d and %d is %d." % (first_number, second_number, our_mult))