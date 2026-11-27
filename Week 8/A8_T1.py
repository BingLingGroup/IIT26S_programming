from time import sleep
import inputChoice


def print_options():
    print("""Options:
1 - Set pause duration
2 - Activate pause
0 - Exit""")
    return None


def main():
    print("Program starting.")
    duration = None
    while True:
        print_options()
        choice = inputChoice.process_input(min=0, max=2)
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
