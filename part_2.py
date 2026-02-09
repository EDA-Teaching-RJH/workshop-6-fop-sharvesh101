rover_status = {"Battery": 100,"Heater": "Off","Camera": "Standby"}
print(f"Battey Status: {rover_status["Battery"]}%")

print("Updating Status")
rover_status.update({"Battery": 85})
rover_status.update({"Heater":"On"})

rover_status["Speed"] = 5

print("\nPrinting...")
for data in rover_status:
    print(f"{data}: {rover_status[data]}")

mission_log = [{"Site": "Crater A", "Radiation": "Low", "Water": False},{"Site": "Dune B", "Radiation": "High", "Water": True}]

for log in mission_log:
    print(f"Site [{log["Site"]}] has [{log["Radiation"]}] radiation.")
