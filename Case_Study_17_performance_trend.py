subjects = ["Python", "Maths", "English"]
old_marks = []
new_marks = []

for subject in subjects:
    old_marks.append(float(input(f"Previous marks in {subject}: ")))
    new_marks.append(float(input(f"Latest marks in {subject}: ")))

for i in range(len(subjects)):
    change = new_marks[i] - old_marks[i]
    if change > 0:
        status = "Improved"
    elif change < 0:
        status = "Declined"
    else:
        status = "No change"
    print(f"{subjects[i]}: {status} by {abs(change):.1f} marks")

weakest = new_marks.index(min(new_marks))
print("Weakest subject in latest exam:", subjects[weakest])
