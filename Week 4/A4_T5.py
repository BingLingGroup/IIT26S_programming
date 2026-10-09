print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))

print()

loop_condition = True

if start >= stop:
    loop_condition = False
    print("Starting point value must be less than the stopping point value.")

if inspection > stop or inspection < start:
    loop_condition = False
    print("Inspection value must be within the range of start and stop.")

if loop_condition:
    print("First loop - inspection with break:")
    i = start
    output_list = []
    while loop_condition and i < stop:
        if i == inspection:
            break
        output_list.append("{value}".format(value=i))
        i = i + 1
    if output_list:
        print(" ".join(output_list))
    else:
        print()

    print("Second loop - inspection with continue:")
    i = start
    output_list = []
    while loop_condition and i < stop:
        if i == inspection:
            i = i + 1
            continue
        output_list.append("{value}".format(value=i))
        i = i + 1
    if output_list:
        print(" ".join(output_list))
    else:
        print()

print("\nProgram ending.")
