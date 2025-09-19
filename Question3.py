
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))

average = (m1 + m2 + m3) / 3

if average >= 85:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print(f"\nAverage Marks = {average:.2f}")
print(f"Grade = {grade}")
