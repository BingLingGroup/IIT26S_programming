print("Program starting.\n")

input_list = []
while True:
    word = input("Insert word (empty stops): ")
    if not word:
        break
    else:
        input_list.append(word)

print("""You inserted:
- {word_count} words
- {char_count} characters""".format(word_count=len(input_list),
                                    char_count=len("".join(input_list))))
print("\n\nProgram ending.")
