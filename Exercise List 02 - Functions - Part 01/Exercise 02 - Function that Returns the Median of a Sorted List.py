#Write a python program with a function that receives a sorted list L of 
#integer numbers. The function then returns the median of L.

#For the following input:
#[1, 3, 7, 12, 15, 17, 19]

#The function should return:
#12

# =============================================================================
# Our Function
# =============================================================================
def calculate_median(l):
    median = 0
    
    if((len(l) % 2) == 0):
        median = l[int(len(l) / 2)]
        median += l[int(len(l) / 2)-1]
        median = median / 2
    else:
        median = l[int(len(l) / 2)]
        
    return median


# =============================================================================
# Our main
# =============================================================================
test1 = [1, 3, 7, 12, 15, 17, 19]
print("%f" % calculate_median(test1))



test2 = [1, 3, 7, 12, 13, 15, 17, 19]
print("%f" % calculate_median(test2))






