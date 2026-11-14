from string import ascii_uppercase as UPPER_ALPHABETS
from string import ascii_lowercase as LOWER_ALPHABETS
import os

HERE = os.path.abspath(os.path.dirname(__file__))


# CAESAR_CIPHER_UPPER = {
#     "A": "N",
#     "B": "O",
#     "C": "P",
#     "D": "Q",
#     "E": "R",
#     "F": "S",
#     "G": "T",
#     "H": "U",
#     "I": "V",
#     "J": "W",
#     "K": "X",
#     "L": "Y",
#     "M": "Z",
#     "N": "A",
#     "O": "B",
#     "P": "C",
#     "Q": "D",
#     "R": "E",
#     "S": "F",
#     "T": "G",
#     "U": "H",
#     "V": "I",
#     "W": "J",
#     "X": "K",
#     "Y": "L",
#     "Z": "M"
# }

# CAESAR_CIPHER_LOWER = {
#     "a": "n",
#     "b": "o",
#     "c": "p",
#     "d": "q",
#     "e": "r",
#     "f": "s",
#     "g": "t",
#     "h": "u",
#     "i": "v",
#     "j": "w",
#     "k": "x",
#     "l": "y",
#     "m": "z",
#     "n": "a",
#     "o": "b",
#     "p": "c",
#     "q": "d",
#     "r": "e",
#     "s": "f",
#     "t": "g",
#     "u": "h",
#     "v": "i",
#     "w": "j",
#     "x": "k",
#     "y": "l",
#     "z": "m"
# }
#
#
# def get_ciphered_text(text: str) -> str:
#     ciphered_text = ""
#     for c in text:
#         if c.isalpha():
#             if c.isupper():
#                 ciphered_text = ciphered_text + CAESAR_CIPHER_UPPER[c]
#             else:
#                 ciphered_text = ciphered_text + CAESAR_CIPHER_LOWER[c]
#         else:
#             ciphered_text = ciphered_text + c
#     return ciphered_text


def shiftCharacter(
        char: str,
        alphabets: str) -> str:
    if alphabets == LOWER_ALPHABETS:
        offset = ord(char) - ord("a")
        result = chr((offset + 13) % 26 + ord("a"))
    elif alphabets == UPPER_ALPHABETS:
        offset = ord(char) - ord("A")
        result = chr((offset + 13) % 26 + ord("A"))
    else:
        result = char
    return result


def rot13(text: str) -> str:
    ciphered_text = ""
    for c in text:
        if c in UPPER_ALPHABETS:
            ciphered_text = ciphered_text + shiftCharacter(
                char=c,
                alphabets=UPPER_ALPHABETS)
        elif c in LOWER_ALPHABETS:
            ciphered_text = ciphered_text + shiftCharacter(
                char=c,
                alphabets=LOWER_ALPHABETS)
        else:
            ciphered_text = ciphered_text + c
    return ciphered_text


def writeFile(filename: str, content: str) -> None:
    with open(filename, "w", encoding="UTF-8") as output_file:
        output_file.write(content)
    return None


def main():
    print("Program starting.\n")
    print("Collecting plain text rows for ciphering.")
    row = input("Insert row(empty stops): ")
    text_list = []
    ciphered_list = []
    while row != "":
        text_list.append(row)
        row = input("Insert row(empty stops): ")
    print("\n#### Ciphered text ####")
    for row in text_list:
        ciphered = rot13(row)
        print(ciphered)
        ciphered_list.append(ciphered)
    result = "\n".join(ciphered_list)
    print("\n#### Ciphered text ####")
    filename = input("Insert filename to save: ")
    writeFile(filename=filename, content=result)
    print("Ciphered text saved!")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
