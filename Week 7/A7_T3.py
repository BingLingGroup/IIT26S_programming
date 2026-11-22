import os

HERE = os.path.abspath(os.path.dirname(__file__))

WEEKDAYS = ("Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturnday", "Sunday",)


def read_file(p_filename: str, p_rows: list[str]) -> None:
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
                p_rows.append(content)
    return None


def analyse_timestamps(p_rows: list[str], p_results: list[str]) -> None:
    """
    Append results to the PResults list
    Initialise helper list
    WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]
    Iterate rows with i
    Iterate WEEKDAYS with j
    Check if the row starts with the weekday name
    Count the day in proper place
    Iterate WEEKDAYS with i and append the daily results
    Clear the helper list
    """
    print("Analysing timestamps.")
    amount_list = [0, 0, 0, 0, 0, 0, 0]
    for row in p_rows:
        row_list = row.split(";")
        j = WEEKDAYS.index(row_list[0])
        amount_list[j] = amount_list[j] + 1
    i = 0
    while i < len(amount_list):
        p_results.append(" - {weekday} {amount} stamps".format(weekday=WEEKDAYS[i], amount=amount_list[i]))
        i = i + 1
    amount_list.clear()
    return None


def display_results(p_results: list[str]) -> None:
    """
    Iterate results and print for the user
    """
    print("""Displaying results.
### Timestamp analysis ###""")
    for result in p_results:
        print(result)
    print("### Timestamp analysis ###")
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
    p_results = []
    read_file(p_filename=p_filename, p_rows=p_rows)
    analyse_timestamps(p_rows=p_rows, p_results=p_results)
    display_results(p_results)
    p_rows.clear()
    p_results.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
