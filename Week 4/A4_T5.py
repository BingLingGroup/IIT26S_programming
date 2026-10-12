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
    if i != inspection:
        print(i, end="")
        i = i + 1
        while i < stop:
            if i == inspection:
                break
            print(" {value}".format(value=i), end="")
            i = i + 1

    print("\nSecond loop - inspection with continue:")
    i = start
    if i != inspection:
        print(i, end="")
    else:
        i = i + 1
        print(i, end="")
    i = i + 1
    while i < stop:
        if i == inspection:
            i = i + 1
            continue
        print(" {value}".format(value=i), end="")
        i = i + 1
    print()

print("\nProgram ending.")
