total = int(input("Total classes conducted: "))
attended = int(input("Classes attended: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details")
else:
    percentage = attended / total * 100
    future = 0
    while (attended + future) / (total + future) * 100 < 75:
        future += 1
    print(f"Current attendance: {percentage:.2f}%")
    print(f"Consecutive classes to attend: {future}")
