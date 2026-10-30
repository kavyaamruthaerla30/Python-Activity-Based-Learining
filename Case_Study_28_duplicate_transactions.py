ids = input("Enter transaction IDs separated by spaces: ").split()
amount_text = input("Enter matching amounts separated by spaces: ").split()

if len(ids) != len(amount_text):
    print("Enter the same number of IDs and amounts")
else:
    amounts = [float(value) for value in amount_text]
    seen = []
    for i in range(len(ids)):
        if ids[i] in seen:
            print("Duplicate transaction ID:", ids[i])
        else:
            seen.append(ids[i])
        if amounts[i] > 5000:
            print("High-value transaction:", ids[i], "Rs.", amounts[i])
    print("Audit completed")
