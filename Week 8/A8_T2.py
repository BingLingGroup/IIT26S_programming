import myCalculator
import inputChoice


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
    return inputChoice.process_input(min=0, max=4)


def askValue(PPrompt: str):
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
    calculate = getattr(myCalculator, PPrompt)
    try:
        result = calculate(value1, value2)
    except ZeroDivisionError:
        print("Divisor can't be 0.")
        result = None
    return result


if __name__ == "__main__":
    main()
