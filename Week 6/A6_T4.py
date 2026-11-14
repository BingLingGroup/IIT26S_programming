import os

HERE = os.path.abspath(os.path.dirname(__file__))


def main():
    print("""Program starting.
This program analyses a list of names from a file.""")
    filename = input("Insert filename to read: ")
    print("Reading names from {filename}.".format(filename=filename))
    print("Analysing names...")
    filename = os.path.join(HERE, filename)
    count = 0
    total_length = 0
    shortest_length = 0
    longest_length = 0
    with open(filename, encoding="utf-8", mode="r") as input_file:
        line = input_file.readline()
        shortest_length = len(line) - 1
        longest_length = shortest_length
        while line != "":
            if line != "\n":
                count = count + 1
                name_length = len(line) - 1
                total_length = total_length + name_length
                if name_length < shortest_length:
                    shortest_length = name_length
                elif name_length > longest_length:
                    longest_length = name_length
            line = input_file.readline()
    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print("Name count - {count}".format(count=count))
    print("Shortest name - {length} chars".format(length=shortest_length))
    print("Longest name - {length} chars".format(length=longest_length))
    print("Average name - {length:.2f} chars".format(
        length=total_length/count))
    print("#### REPORT END ####")
    print("Program ending.")
    return None


main()
