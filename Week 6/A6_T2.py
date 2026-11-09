import os

HERE = os.path.abspath(os.path.dirname(__file__))


def main():
    print("Program starting.")
    first_name = input("Insert first name: ")
    last_name = input("Insert last name: ")
    filename = input("Insert filename: ")
    with open(os.path.join(HERE, filename), encoding="utf-8", mode="w") as output_file:
        output_file.write("{first_name}\n{last_name}\n".format(
            first_name=first_name, last_name=last_name))
    print("Program ending.")


main()
