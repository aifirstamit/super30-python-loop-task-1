# Print even numbers from 1 to 100

for i in range(1, 101):
    if i % 2 == 0:
        print(i)


# I first generate numbers from 1 to 100. For every number, I check the remainder after dividing by 2. 
# If the remainder is zero, it is an even number, so I print it.