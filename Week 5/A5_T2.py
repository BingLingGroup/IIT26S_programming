def frameWord(PWord):
    padding = "*" * (len(PWord) + 4)
    print(padding)
    print("* {word} *".format(word=PWord))
    print(padding)
    return None

def main():
    print("Program starting.")
    word = input("Insert word: ")
    print()
    frameWord(word)
    print("\nProgram ending.")
    return None
    
main()