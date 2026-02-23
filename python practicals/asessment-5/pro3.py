color = input("Enter traffic light color (Red/Yellow/Green): ")

if color.lower() == "red":
    print("Stop")
elif color.lower() == "yellow":
    print("Wait")
elif color.lower() == "green":
    print("Go")
else:
    print("Invalid color")