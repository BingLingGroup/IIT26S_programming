import os
import inputChoice

HERE = os.path.abspath(os.path.dirname(__file__))


def showOptions() -> None:
    print("""Options:
1 - Read values
2 - Amount of values
3 - Calculate sum of values
4 - Calculate average of values
0 - Exit""")
    return None


def readValues(filename: str, values_list: list):
    filename = os.path.join(HERE, filename)
    with open(filename, encoding="utf-8", mode="r") as input_file:
        lines = input_file.readlines()
        for line in lines:
            content = line.strip()
            if content:
                values_list.append(float(content))
        return None


def main():
    print("Program starting.")
    valuesList = []
    while True:
        showOptions()
        choice = inputChoice.process_input(min=0, max=4)
        if choice == 1:
            filename = input("Insert filename: ")
            if len(valuesList) == 0:
                readValues(filename=filename, values_list=valuesList)
            else:
                valuesList = []
                readValues(filename=filename, values_list=valuesList)
        elif choice == 2:
            print("Amount of values {count}".format(count=len(valuesList)))
        elif choice == 3:
            print("Sum of values {sum}".format(sum=round(sum(valuesList), 1)))
        elif choice == 4:
            print("Average of values {average}".format(
                average=round(sum(valuesList)/len(valuesList), 1)))
        else:
            print("Exiting program.\n")
            break
        print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
