# Count vowels in a string

text = input("Enter a string: ")

vowel_count = 0

for i in text.lower():
    if i in "aeiou":
        vowel_count = vowel_count + 1

print("Number of vowels:", vowel_count)



# I start the vowel counter at zero. Then I check every character in the input string. 
# If the character exists inside the string 'aeiou', I increase the counter by one.