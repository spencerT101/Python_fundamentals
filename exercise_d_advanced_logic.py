# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

even_integ = []

for even_number in numbers:
    if even_number % 2 == 0:
        even_integ.append(even_number)

print(even_integ)



# 2. Print the difference between the largest and smallest value:

# create function to invoke the list, numbers
# use max and min key words to work define empty variable

def b_difference(list):
     difference= max(list) - min(list)
     return difference

    



print(b_difference(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.


#this code only checks for duplicates doesnt fulfil task

# def check_duplicates(numbers):

#     for duplicates in numbers:
#         if numbers.count(duplicates) > 1:
#             return True
        
#         return False

# print(check_duplicates(numbers))



# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 







