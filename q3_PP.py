# alphabet singing

# Examples:
# Input: d Output: db
# Input: g Output: geca

inputLetter = input("enter letter: ")
num = ord(inputLetter)
word = ""

for index in range(num,97-1,-2):
    word = word + chr(index)

print(word)