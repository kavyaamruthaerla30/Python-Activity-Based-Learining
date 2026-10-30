names = ["Asha", "Bala", "Charan"]
marks = []

for name in names:
    row = []
    print("Enter marks for", name)
    for subject in ["Python", "Maths", "English"]:
        mark = float(input(subject + ": "))
        row.append(mark)
    marks.append(row)

averages = []
for i in range(len(marks)):
    average = sum(marks[i]) / len(marks[i])
    averages.append(average)
    print(f"{names[i]} average: {average:.2f}")

top = averages.index(max(averages))
print("Top performer:", names[top])
