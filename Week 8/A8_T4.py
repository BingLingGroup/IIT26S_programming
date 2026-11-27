import os
import datetime as dt
from datetime import datetime
import inputChoice

HERE = os.path.abspath(os.path.dirname(__file__))

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)


def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    filename = os.path.join(HERE, PFilename)
    with open(filename, encoding="utf-8", mode="r") as input_file:
        lines = input_file.readlines()
        for line in lines:
            content = line.strip()
            if content:
                PTimestamps.append(datetime.strptime(content, "%Y-%m-%dT%H:%M"))
        return None


def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    count = 0
    for timestamp in PTimestamps:
        if timestamp.year == PYear:
            count = count + 1
    return count


def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    count = 0
    for timestamp in PTimestamps:
        if MONTHS[timestamp.month - 1] == PMonth:
            count = count + 1
    return count


def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    count = 0
    for timestamp in PTimestamps:
        if WEEKDAYS[timestamp.weekday()] == PWeekday:
            count = count + 1
    return count


def showOptions() -> None:
    print("""Options:
1 - Calculate amount of timestamps during year
2 - Calculate amount of timestamps during month
3 - Calculate amount of timestamps during weekday
0 - Exit""")
    return None


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    datetimeList = []
    readTimestamps(PFilename=filename, PTimestamps=datetimeList)
    while True:
        showOptions()
        choice = inputChoice.process_input(min=0, max=3)
        if choice == 1:
            PYear = int(input("Insert year: "))
            print("Amount of timestamps during year '{PYear}' is {count}".format(PYear=PYear, count=calculateYears(PYear=PYear, PTimestamps=datetimeList)))
        elif choice == 2:
            PMonth = input("Insert month: ")
            print("Amount of timestamps during month '{month}' is {count}".format(month=PMonth, count=calculateMonths(PMonth=PMonth, PTimestamps=datetimeList)))
        elif choice == 3:
            PWeekday = input("Insert weekday: ")
            print("Amount of timestamps during weekday '{weekday}' is {count}".format(weekday=PWeekday, count=calculateWeekdays(PWeekday=PWeekday, PTimestamps=datetimeList)))
        else:
            print("Exiting program.\n")
            break
        print()
    print("Program ending.")
    return


if __name__ == "__main__":
    main()
