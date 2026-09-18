print("Program starting.\n")
word_1 = input("Insert a closed compound word: ")
print("The word you inserted is '{word_1}' and in reverse it is '{word_r}'.".format(
    word_1=word_1, word_r=word_1[::-1]))
print("The inserted word length is {length}".format(length=len(word_1)))
print("Last character is '{char}'\n".format(char=word_1[-1]))
print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))

print("\nThe word '{word_1}' sliced to the defined substring is '{word_s}'.".format(
    word_1=word_1, word_s=word_1[start:end:step]))
print("Program ending.")
