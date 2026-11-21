def main():
    print("Program starting.")
    input_string = input("Insert comma separated integers: ")
    input_list = input_string.split(",")
    i = 0
    int_list = []
    value = 0
    while i < len(input_list):
        try:
            value = int(input_list[i])
        except ValueError:
            print("Invalid value '{value}' detected.".format(value=input_list[i]))
            i = i + 1
            continue
        int_list.append(value)
        i = i + 1
    if len(int_list) > 0:
        print("There are {count} integers in the list.".format(count=len(int_list)))
        value_sum = sum(int_list)
        if value_sum & 1:
            print("Sum of the integers is {sum} and it's odd".format(sum=value_sum))
        else:
            print("Sum of the integers is {sum} and it's even".format(sum=value_sum))
    else:
        print("No values to analyse.")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
