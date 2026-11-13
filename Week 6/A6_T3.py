def read_file(filename: str) -> str:
    with open(filename, encoding="utf-8", mode="r") as input_file:
        return input_file.read()


def write_file(filename: str, content: str) -> None:
    with open(filename, encoding="utf-8", mode="w") as output_file:
        output_file.write(content)
    return None


def main():
    print("Program starting.")
    print("This program can copy a file.")
    src_name = input("Insert source filename: ")
    dst_name = input("Insert destination filename: ")
    print("Reading file '{filename}' content.".format(filename=src_name))
    content = read_file(src_name)
    print("File content ready in memory.")
    print("Writing content into file '{filename}'.".format(filename=dst_name))
    write_file(filename=dst_name, content=content)
    print("Copying operation complete.")
    print("Program ending.")
    return None


main()
