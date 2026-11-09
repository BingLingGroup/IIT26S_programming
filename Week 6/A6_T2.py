def write_file(filename: str, content: str) -> None:
    with open(filename, encoding="utf-8", mode="w") as output_file:
        output_file.write(content)


def main():
    print("Program starting.")
    first_name = input("Insert first name: ")
    last_name = input("Insert last name: ")
    filename = input("Insert filename: ")
    write_file(filename=filename,
               content="{first_name}\n{last_name}\n".format(
                   first_name=first_name, last_name=last_name))
    print("Program ending.")


main()
