```
import re
def check_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."

    if not re.search(r"[0-9]", password):
        return "Password must contain at least one number."

    if not re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
        return "Password must contain at least one special character."

    return "Password is strong!"

while True:
    password = input("\nEnter your password (or type 'exit' to stop): ")

    if password.lower() == "exit":
        print("Program stopped.")
        break

    print(check_password(password))
```
