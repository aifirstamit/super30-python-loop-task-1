# Iterate through a dictionary and print every key and value

student = {
    "name": "Rahul",
    "age": 22,
    "course": "Data Science",
    "city": "Bangalore"
}

for key, value in student.items():
    print(key, ":", value)



# When working with a dictionary, I want both the key and value. So I use the items method. 
# In every iteration, key stores the dictionary key and value stores the corresponding value.