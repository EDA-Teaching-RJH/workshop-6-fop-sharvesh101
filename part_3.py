speed = input("Enter Motor Speed: ")
try:
    speed = int(speed)
except ValueError:
    print("Error: Corrupted Signal. Maintaining current speed.")

def get_coordinate():
        while True:
            x_coords = input("Enter X-coordinate (integer): ")
            try:
                x_coords = int(x_coords)
            except:
                 print("\nInvalid coordinate")
            if type(x_coords) == int and x_coords in range(-100,101):
                    break
            else:
                 print("\nCoordinate out of range")
                 print("Enter Coordinate Between -100 to 100\n")

get_coordinate()