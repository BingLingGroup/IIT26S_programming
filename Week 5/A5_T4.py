def askDimension(PPrompt: str) -> float:
    Feed = float(input("Insert number: "))
    return Feed


def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    Area = PWidth * PHeight
    return Area


def main():
    print("Program starting.")
    Width = askDimension("width")
    Height = askDimension("height")
    Area = calcRectangleArea(PWidth=Width, PHeight=Height)
    print("")
    print("Area is {Area}²".format(Area=round(Area, 1)))
    print("Program ending.")
    return None


main()
