# Calculate the sum of numbers from 1 to n

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)


# Here I use an accumulator variable called total. 
# It starts at zero, and during every loop iteration I add the current number to total. At the end, total contains the complete sum.