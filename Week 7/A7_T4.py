import os

HERE = os.path.abspath(os.path.dirname(__file__))
DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturnday", "Sunday",)


class TIMESTAMP:
    def __init__(self, row: str) -> None:
        row_list = row.split(DELIMITER)
        self.weekday = row_list[0]
        self.hour = int(row_list[1])
        self.consumption = float(row_list[2])
        self.price = float(row_list[3])
        self.total = self.consumption * self.price


def readTimestamps(p_filename: str, p_rows: list[TIMESTAMP]) -> None:
    """
    0. Clear PRows list just in case
    1. Open filehandle
    2. Read filehandle line-by-line
    2.1. Skip first line (header row)
    2.2. Check if line is empty '\n'
    2.3. Add non empty datarow without newline at the end.
    3. Close filehandle
    """
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


def displayTimestamps(p_rows: list[TIMESTAMP]) -> None:
    """
    Iterate results and print for the user
    """
    print("Electricity usage:")
    for row in p_rows:
        print(" - {weekday} {hour:02d}:00, price {price:.2f}, consumption {consumption:.2f} kWh, total {total:.2f} €".format(
            weekday=row.weekday, 
            hour=row.hour, 
            price=row.price, 
            consumption=row.consumption, 
            total=row.total))
    return None


def main() -> None:
    """
    1. Initialise
    1.1. Initialise rows list
    1.2. Initialise results list
    2. Operate
    2.1. Ask user to define filename
    2.2. Read file
    2.3. Analyse rows
    2.3. Display results
    3. Cleanup
    3.1. Clear lists
    """
    print("Program starting.")
    p_filename = input("Insert filename: ")
    p_rows = []
    readTimestamps(p_filename=p_filename, p_rows=p_rows)
    displayTimestamps(p_rows)
    p_rows.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
