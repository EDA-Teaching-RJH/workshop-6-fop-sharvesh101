sample_bay = ["Basalt","Silica","Iron","Dust"]
print("First Item collected:",sample_bay[0])
print("Last Item collected:",sample_bay[-1])
print("Total number of samples in the bay:",len(sample_bay))

for sample in sample_bay:
    print(f"Transmitting data for: [{sample}]")
print()

new_findings = []
times = 3
while times != 0:
    rock_name = input("Enter the Name of the rock: ")
    new_findings.append(rock_name)
    times -= 1
for item in new_findings:
    print(f"The Item: [{item}]")
print("Are in the new_finding list\n")

for the_item in sample_bay:
    if the_item == "Dust" or the_item == "dust":
        sample_bay.remove(the_item)
        print("Item found")
        print("\"Dust\" is Removed from the list")