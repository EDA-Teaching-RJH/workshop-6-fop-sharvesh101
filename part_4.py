travel_log = []

while True:
    slope_angle = input("Sensor Reading (Slope Angle): ")
    try:
        slope_angle = int(slope_angle)
    except:
        print("Sensor Glitch")
    if type(slope_angle) == int:
        if slope_angle > 45:
            print("\nCRITICAL TILT! HALTING.")
            break
        else:
            travel_log.append(slope_angle)
            print("Path Stable. Moving forward.")
    
print("Mission Terminated.")
print(f"Total steps taken: {len(travel_log)}")
print(travel_log)