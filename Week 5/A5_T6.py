def showOptions():
    print("""Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit""")
    return None


def askChoice():
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    else:
        return None


def main():
    print("Program starting.")
    count = 0
    while True:
        showOptions()
        choice = askChoice()
        if choice is not None:
            if choice == 1:
                print("Current count - {count}".format(count=count))
            elif choice == 2:
                count = count + 1
                print("Count increased!")
            elif choice == 3:
                count = 0
                print("Cleared count!")
            elif choice == 0:
                print("Exiting program.")
                break
            else:
                print("Unknown option!")
        else:
            print("Unknown option!")
        print()
    print("\nProgram ending.")
    return None


main()
