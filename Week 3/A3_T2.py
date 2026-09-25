print("Program starting.")
print("String comparisons")
str_1 = input("Insert first word: ")
char_1 = input("Insert a character: ")

if char_1 in str_1:
    print("Word \"{str}\" contains character \"{char}\"".format(
        str=str_1, char=char_1))
else:
    print("Word \"{str}\" doesn't contain character \"{char}\"".format(
        str=str_1, char=char_1))

str_2 = input("Insert second word: ")

if str_1 < str_2:
    print("The first word \"{str_1}\" is before the second word \"{str_2}\" alphabetically.".format(
        str_1=str_1, str_2=str_2))
elif str_2 < str_1:
    print("The second word \"{str_2}\" is before the first word \"{str_1}\" alphabetically.".format(
        str_1=str_1, str_2=str_2))
else:
    print(
        "Both inserted words are the same alphabetically, \"{str}\"".format(str=str_1))

print("Program ending.")
