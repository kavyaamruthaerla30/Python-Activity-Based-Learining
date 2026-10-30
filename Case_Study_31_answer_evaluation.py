key = input("Enter answer key (e.g. ABCD): ").upper().replace(" ", "")
answers = input("Enter student answers (use - for blank): ").upper().replace(" ", "")

if len(key) != len(answers):
    print("Answer count must match the answer key")
else:
    correct = wrong = blank = 0
    for i in range(len(key)):
        if answers[i] == "-":
            blank += 1
        elif answers[i] == key[i]:
            correct += 1
        else:
            wrong += 1
    score = correct - 0.25 * wrong
    print("Correct:", correct)
    print("Incorrect:", wrong)
    print("Unanswered:", blank)
    print(f"Final score: {score:.2f} out of {len(key)}")
