import my_calculator


def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        if choice == 1:
            print("{value:.1f}".format(value=askValue("add")))
        elif choice == 2:
            print("{value:.1f}".format(value=askValue("subtract")))
        elif choice == 3:
            print("{value:.1f}".format(value=askValue("multiply")))
        elif choice == 4:
            result = askValue("divide")
            if result:
                print("{value:.1f}".format(value=result))
        elif choice == 0:
            print("Exiting program.\n")
            break
        else:
            print("Unknown option!")
        print()
    print("Program ending.")
    return None


def showOptions() -> None:
    print("Program starting.")
    print("""Options:
1 - Add
2 - Subtract
3 - Multiply
4 - Divide
0 - Exit""")
    print("Program ending.")
    return None


def askChoice() -> int:
    choice_str = input("Your choice: ")
    try:
        choice = int(choice_str)
        if choice > 4 or choice < 0:
            choice = -1
    except ValueError:
        choice = -1
    return choice


def askValue(PPrompt: str) -> float:
    if PPrompt == "add":
        value1 = float(input("Insert first addend value: "))
        value2 = float(input("Insert second addend value: "))
        print("{value1:.1f} + {value2:.1f} = ".format(value1=value1,
                                                      value2=value2), end="")
    elif PPrompt == "subtract":
        value1 = float(input("Insert first minuend value: "))
        value2 = float(input("Insert second subtrahend value: "))
        print("{value1:.1f} - {value2:.1f} = ".format(value1=value1,
                                                      value2=value2), end="")
    elif PPrompt == "multiply":
        value1 = float(input("Insert first multiplicand value: "))
        value2 = float(input("Insert multiplier value: "))
        print("{value1:.1f} * {value2:.1f} = ".format(value1=value1,
                                                      value2=value2), end="")
    else:
        value1 = float(input("Insert first dividend value: "))
        value2 = float(input("Insert divisor value: "))
        print("{value1:.1f} / {value2:.1f} = ".format(value1=value1,
                                                      value2=value2), end="")
    calculate = getattr(my_calculator, PPrompt)
    try:
        result = calculate(value1, value2)
    except ZeroDivisionError:
        print("Divisor can't be 0.")
        result = None
    return result


if __name__ == "__main__":
    main()
