def common_choices(
        choice):
    """
    Deal with the common choices.
    """
    if not choice == 0:
        print("Unknown option.")
    else:
        print("Exiting...")

    return 0


print("""Program starting.
Testing decision structures.""")
value = int(input("Insert an integer: "))
print("""Options:
1 - In one multi-branched decision
2 - In multiple independent if-statements
0 - Exit""")
choice = int(input("Your choice: "))

if choice == 1:
    if value >= 400:
        value = value + 44
    elif value >= 200:
        value = value + 22
    elif value >= 100:
        value = value + 11
    print("Using one multi-branched decision structure.")
    print("Result is {value}".format(value=value))
elif choice == 2:
    if value >= 400:
        value = value + 44
    if value >= 200:
        value = value + 22
    if value >= 100:
        value = value + 11
    print("Using multiple independent if-statements.")
    print("Result is {value}".format(value=value))
else:
    common_choices(choice)

print("\nProgram ending.")