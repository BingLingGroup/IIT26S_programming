import string

print("Program starting.\n")
hex_string = input("Insert a hex color: ")
if len(hex_string) == 7 and all(char in string.hexdigits for char in hex_string[1:]):
    print("""\nColors
- Red {red}
- Green {green}
- Blue {blue}""".format(red=hex_string[1:3], green=hex_string[3:5], blue=hex_string[5:7]))
print("\nProgram ending.")
