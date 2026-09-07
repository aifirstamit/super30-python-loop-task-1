# Find the largest number without using max()

numbers = [12, 45, 7, 89, 23, 56]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("Largest number:", largest)


# I cannot use the built-in max function, so I create a variable called largest and initially store the first number. 
# Then I compare every number with largest. 
# Whenever I find a bigger number, I update largest. At the end, largest contains the biggest value.