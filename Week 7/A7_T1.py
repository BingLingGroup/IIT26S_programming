def main():
    print("Program starting.")
    print("Collect positive integers.")
    value = int(input("Insert positive integer(negative stops): "))
    value_list = []
    while value >= 0:
        value_list.append(value)
        value = int(input("Insert positive integer(negative stops): "))
    print("""Stopped collecting positive integers.
Displaying {count} integers:""".format(count=len(value_list)))
    i = 0
    for item in value_list:
        print("- Index {index} => Ordinal {ordinal} => Integer {value}".format(
            index=i, ordinal=i + 1, value=item))
        i = i + 1
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
