# Print multiplication table from 1 to 20

n = int(input("Enter a number: "))

for i in range(1, 21):
    print(n, "x", i, "=", n * i)


# First I take a number from the user and convert it to an integer. 
# Then I run a loop from 1 to 20. During every iteration, I multiply the user's number by the current loop value.