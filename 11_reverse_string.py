# Reverse a string using a for loop without using [::-1] or reversed()

text = input("Enter a string: ")

reversed_text = ""

for i in text:
    reversed_text = i + reversed_text

print("Reversed string:", reversed_text)



# The important idea here is that I add each new character to the beginning of the existing string. 
# Because every new character comes before the previous characters, the final string becomes reversed.