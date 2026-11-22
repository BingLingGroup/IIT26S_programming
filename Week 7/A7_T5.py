import os

HERE = os.path.abspath(os.path.dirname(__file__))
DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday",)


class TIMESTAMP:
    def __init__(self, row: str) -> None:
        row_list = row.split(DELIMITER)
        self.weekday = row_list[0]
        self.hour = int(row_list[1])
        self.consumption = float(row_list[2])
        self.price = float(row_list[3])
        self.total = self.consumption * self.price


class DAY_USAGE:
    def __init__(self) -> None:
        self.usage = 0.0
        self.total = 0.0

    def add_up(self, timestamp: TIMESTAMP) -> None:
        self.usage = self.usage + timestamp.consumption
        self.total = self.total + timestamp.total


def readTimestamps(p_filename: str, p_rows: list[TIMESTAMP]) -> None:
    p_rows.clear()
    print("Reading file \"{filename}\".".format(filename=p_filename))
    p_filename = os.path.join(HERE, p_filename)
    with open(p_filename, encoding="utf-8", mode="r") as input_file:
        lines = input_file.readlines()[1:]
        for line in lines:
            content = line.strip()
            if content:
                new_timestamp = TIMESTAMP(content)
                p_rows.append(new_timestamp)
    return None


def analyseTimestamps(p_rows: list[TIMESTAMP], p_results: list[str]) -> None:
    print("Analysing timestamps.")
    day_list = [DAY_USAGE() for _ in range(7)]
    for timestamp in p_rows:
        j = WEEKDAYS.index(timestamp.weekday)
        day_list[j].add_up(timestamp)
    i = 0
    while i < len(day_list):
        p_results.append(" - {weekday} usage {amount:.2f} kWh, cost {total:.2f} €".format(weekday=WEEKDAYS[i], amount=day_list[i].usage, total=day_list[i].total))
        i = i + 1
    day_list.clear()
    return None


def displayResults(p_results: list[str]) -> None:
    """
    Iterate results and print for the user
    """
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for result in p_results:
        print(result)
    print("### Electricity consumption summary ###")
    return None


def main() -> None:
    print("Program starting.")
    p_filename = input("Insert filename: ")
    p_rows = []
    p_results = []
    readTimestamps(p_filename=p_filename, p_rows=p_rows)
    analyseTimestamps(p_rows=p_rows, p_results=p_results)
    displayResults(p_results=p_results)
    p_rows.clear()
    p_results.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
