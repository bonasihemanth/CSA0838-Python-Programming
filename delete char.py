input_string = str(input("enter the character:"))
char_to_remove = str(input("enter the character that need to be deleted:"))
newStr = ""
for character in input_string:
    if character != char_to_remove:
        newStr += character
print("The input string is:", input_string)
print("The character to delete is:", char_to_remove)
print("The output string is:", newStr)
