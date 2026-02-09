command_batch = [
    "MOVE 10",
    "TURN LEFT",
    "MOVE 5",
    "MOVE five",    # Corrupted: 'five' is text, not a number
    "DIG",
    "MOVE 20",
    "XÆA-12",       # Corrupted: Unknown command
    "RETURN",
    "MOVE 15"
]

rover_state = {"x": 0, "y": 0, "samples": 0}

for command in command_batch:
    parts = command.split()
    if parts[0] == "MOVE" and len(parts) > 1:
        try:
            parts[1] = int(parts[1])
        except:
            print("Error in the command_batch for move")
            continue
        distance = rover_state["y"] + parts[1]
        rover_state.update({"y":distance})
    elif parts[0] == "TURN":
        print("Turing...")
    elif parts[0] == "DIG":
        print("Digging...")
        sample = rover_state["samples"] + 1
        rover_state.update({"samples":sample})
    elif parts[0] == "RETURN":
        print("Returing...")
    else:
        print("Error Invalid command")

print(rover_state)
