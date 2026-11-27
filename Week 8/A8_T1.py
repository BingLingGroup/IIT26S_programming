from time import sleep


def print_options():
    print("""Options:
1 - Set pause duration
2 - Activate pause
0 - Exit""")
    return None


def process_input():
    choice_str = input("Your choice: ")
    try:
        choice = int(choice_str)
        if choice > 2 or choice < 0:
            choice = -1
    except ValueError:
        choice = -1
    return choice


def main():
    print("Program starting.")
    duration = None
    while True:
        print_options()
        choice = process_input()
        if choice == 1:
            duration = float(input("Insert pause duration (s): "))
        elif choice == 2:
            if duration:
                print("Pausing for {duration} seconds.".format(
                    duration=duration))
                sleep(duration)
                print("Unpaused.")
            else:
                print("""Pause is not set.
Set pause first.""")
        elif choice != 0:
            print("Unknown option!")
        else:
            print()
            break
        print()
        
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
