rover_status = {"Power": 100, "Samples": 0}
inventory = []

while True:
    print("\n1 Dig for Sample")
    print("2 Report Status")
    print("3 Emergency Stop")
    choice = int(input("\nEnter Choice: "))
    if choice == 1:
        sample = input("Enter Sample: ")
        inventory.append(sample)
        power = rover_status["Power"] - 10
        rover_status.update({"Power":power})
    elif choice == 2:
        for data in rover_status:
            print(f"{data}: {rover_status[data]}")
        if inventory == []:
            print("\nThere are NO items in inventory")
        else:
            num_items = len(inventory)
            rover_status.update({"Samples":num_items})
            for item in inventory:
                print(f"[{item}]",end=" ")
            print("\nThese items are in the inventory")
    elif choice ==  3:
        break
    else:
        print("\nENTER PROPER CHOICE\n")