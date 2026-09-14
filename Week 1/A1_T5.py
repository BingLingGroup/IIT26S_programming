print("Calculate the area of a wall.")
Feed = input("Enter the width in meters: ")

try:
    Width = int(Feed)
except ValueError:
    Width = int(float(Feed))

if Width < 0:
    Width = - Width

Feed = input("Enter the height in meters: ")
Height = int(float(Feed))

try:
    Height = int(Feed)
except ValueError:
    Height = int(float(Feed))

if Height < 0:
    Height = - Height

print("Width is {Width} m and height is {Height} m.".format(Width=Width, Height=Height))

Area = Width * Height
print("The wall will be {Area} square meters.".format(Area=Area))
