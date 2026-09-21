print("Program starting.")
print("Estimate how many minutes you spent on programming...\n")

time_list = []
i = 0
sum = 0
average = 0

while i < 7:
    time_list.append(int(input("A1_T{num}: ".format(num=i + 1))))
    sum = sum + time_list[i]
    i = i + 1

average = sum / i
print("\nIn total you spent {sum} minutes on programming.".format(sum=sum))
print("Average per task was {average} min and same rounded to the nearest integer {rounded} min.\n".format(average=round(average, 2), rounded=round(average)))
print("Program ending.")
