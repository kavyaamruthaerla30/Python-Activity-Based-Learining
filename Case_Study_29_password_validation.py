password = input("Enter a sample password: ")
errors = []

if len(password) < 8:
    errors.append("Use at least 8 characters")
if not any(ch.isupper() for ch in password):
    errors.append("Include an uppercase letter")
if not any(ch.islower() for ch in password):
    errors.append("Include a lowercase letter")
if not any(ch.isdigit() for ch in password):
    errors.append("Include a digit")
if not any(not ch.isalnum() for ch in password):
    errors.append("Include a special character")

if errors:
    print("Password does not meet the policy:")
    for error in errors:
        print("-", error)
else:
    print("Password meets the sample policy")
