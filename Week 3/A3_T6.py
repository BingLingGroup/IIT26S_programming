def common_choices(
        choice):
    """
    Deal with the common choices.
    """
    if not choice == 0:
        print("Unknown option.")
    else:
        print("Exiting...")

    return 0


print("Program starting.")
print("""Welcome to the unit converter program!
Follow the menu instructions below.""")

print("""\nOptions:
1 - Length
2 - Weight
0 - Exit""")
choice = int(input("Your choice: "))

if choice == 1:
    print("""\nLength options:
1 - Meters to kilometers
2 - Kilometers to meters
0 - Exit""")
    choice = int(input("Your choice: "))
    if choice == 1:
        length_in_meters = float(input("Insert meters: "))
        print("{value_1} m is {value_2} km".format(
            value_1=round(length_in_meters, 1), value_2=round(length_in_meters / 1000, 1)))
    elif choice == 2:
        length_in_kms = float(input("Insert kilometers: "))
        print("{value_1} km is {value_2} m".format(
            value_1=round(length_in_kms, 1), value_2=round(length_in_kms * 1000, 1)))
    else:
        common_choices(choice)

elif choice == 2:
    print("""\nWeight options:
1 - Grams to pounds
2 - Pounds to grams
0 - Exit""")
    choice = int(input("Your choice: "))
    if choice == 1:
        weight_in_grams = float(input("Insert grams: "))
        print("{value_1} g is {value_2} lb".format(value_1=round(
            weight_in_grams, 1), value_2=round(weight_in_grams * 0.002204586, 1)))
    elif choice == 2:
        weight_in_pounds = float(input("Insert pounds: "))
        print("{value_1} lb is {value_2} g".format(value_1=round(
            weight_in_pounds, 1), value_2=round(weight_in_pounds / 0.002204586, 1)))
    else:
        common_choices(choice)

else:
    common_choices(choice)

print("\nProgram ending.")
