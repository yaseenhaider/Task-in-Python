total_distance = 0
trip_count = 0

while True:
    distance = float(input("Enter trip distance in km (0 to stop): "))

    if distance == 0:
        break

    total_distance += distance
    trip_count += 1

if trip_count > 0:
    average_distance = total_distance / trip_count
    print("\nTotal distance covered:", total_distance, "km")
    print("Average distance per trip:", average_distance, "km")
else:
    print("\nNo trips entered!")
