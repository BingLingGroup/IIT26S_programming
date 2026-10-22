DELIMITER = ","


def collectWords():
    word = input("Insert word(empty stops): ")
    if word:
        result = word
        while True:
            word = input("Insert word(empty stops): ")
            if word:
                result = "{result}{delimiter}{word}".format(
                    result=result, delimiter=DELIMITER,
                    word=word)
            else:
                break
    return result


def analyseWords(result):
    if result:
        word_count = 1
        char_count = 0
        for char in result:
            if char != DELIMITER:
                char_count = char_count + 1
            else:
                word_count = word_count + 1
        avg = char_count / word_count
    else:
        word_count = 0
        char_count = 0
        avg = 0

    print("""- {word_count} Words
- {char_count} Characters
- {avg:.2f} Average word length""".format(
        word_count=word_count,
        char_count=char_count,
        avg=avg))
    return None


def main():
    print("Program starting.")
    analyseWords(collectWords())
    print("Program ending.")
    return None


main()
