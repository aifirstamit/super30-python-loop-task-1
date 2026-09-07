# Calculate factorial of a number without using a built-in function

n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("Factorial: ", factorial)


# Unlike the sum program, here I don't add the numbers. I multiply them. 
# I start factorial with 1 because multiplying by 1 doesn't change the result, and then I keep multiplying by every number from 1 to n.