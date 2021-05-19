
# we will store the current greatest number here
max = -9999999

# get the first value
number = int(input("Enter value or -1 to stop"))

#if the number is not equal to -1 we will continue
while number != -1:

    # is the number greater than max
    if number > max:

        # yes - update max
        max = number

    # get next number
    number = int(input("Enter value pr -1 to stop"))

# print the largest number
print("The largest number is" ,max)
