print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")

print("""Options:
1 - Print welcome message
2 - Print the name backwards
3 - Print the first character
4 - Show the amount of characters in the name
0 - Exit""")
choice = int(input("Your choice: "))

if choice == 1:
    print("Welcome {name}!".format(name=name))
elif choice == 2:
    print("Your name backwards is \"{NameBackwards}\"".format(
        NameBackwards=name[::-1]))
elif choice == 3:
    print("The first character in name \"{Name}\" is \"{FirstChar}\"".format(
        Name=name, FirstChar=name[0]))
elif choice == 4:
    print("There are {NameLength} characters in the name \"{Name}\"".format(
        NameLength=len(name), Name=name))
elif not choice == 0:
    print("Unknown option.")
else:
    print("Exiting...")

print("\nProgram ending.")
