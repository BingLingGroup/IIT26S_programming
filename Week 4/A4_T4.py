print("Program starting.\n")

word_count = 0
char_count = 0
while True:
    word = input("Insert word (empty stops): ")
    if not word:
        break
    else:
        word_count = word_count + 1
        char_count = char_count + len(word)

print("""\nYou inserted:
- {word_count} words
- {char_count} characters""".format(word_count=word_count,
                                    char_count=char_count))
print("\nProgram ending.")
