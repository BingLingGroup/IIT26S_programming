def askName():
    name = input("Insert name: ")
    return name


def greetUser(PName):
    print("Hello {PName}!".format(PName=PName))
    return None


def main():
    print("Program starting.")
    greetUser(askName())
    print("Program ending.")
    return None


main()
