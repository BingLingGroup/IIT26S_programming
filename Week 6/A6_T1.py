def read_file(filename: str) -> str:
    content = ''
    with open(filename, encoding="utf-8", mode="r") as input_file:
        line = input_file.readline()
        while line != "":
            content += line
            line = input_file.readline()
    return content


def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert filename: ")
    print("#### START \"{filename}\" ####".format(filename=filename))
    print(read_file(filename=filename))
    print("#### END \"{filename}\" ####".format(filename=filename))
    print("Program ending.")


main()