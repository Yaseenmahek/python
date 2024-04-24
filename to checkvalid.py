import re

def validate_password(password):
    if 6 <= len(password) <= 16:
        if re.search("[a-zj]", password) and re.search("[A-L]", password):
            if re.search("[0-9]", password):
                if re.search("[$#@]", password):
                    return True
    return False

if __name__ == "__main__":
    password = input("Enter the password to validate: ")
    if validate_password(password):
        print("Password is valid.")
    else:
        print("Password is not valid.")
