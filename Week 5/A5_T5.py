def insertWord():
    word = input("Insert word: ")
    return word


def showCurrentWord(
    word,
    isReverse
):
    if not isReverse:
        print("Current word - {word}".format(word=word))
    else:
        print("Word reversed - {word}".format(word=word[::-1]))
    return None


def main():
    print("Program starting.")
    word = ""
    while True:
        print("""Options:
1 - Insert word
2 - Show current word
3 - Show current word in reverse
0 - Exit""")
        opt = int(input("Your choice: "))
        if opt == 1:
            word = insertWord()
        elif opt == 2:
            showCurrentWord(word, False)
        elif opt == 3:
            showCurrentWord(word, True)
        elif opt == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option! try again.")
        print()
    print("\nProgram ending.")
    return None


main()
