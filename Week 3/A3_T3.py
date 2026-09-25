print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")

print("""Options:
1 - Print welcome message
0 - Exit""")
choice = int(input("Your choice: "))

if choice == 1:
    print("Welcome {name}!".format(name=name))
elif not choice == 0:
    print("Unknown option.")
else:
    print("Exiting...")

print("\nProgram ending.")
