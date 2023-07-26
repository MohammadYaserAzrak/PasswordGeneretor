# Modules imported
import string
import random

# Starting point
if __name__ == "__main__":
    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    # Input correct password length
    password_length = input(
        "How many characters do you want for the password? "
    ).strip()
    while True:
        try:
            password_length = int(password_length)
            if not 6 <= password_length <= 20:
                print("You need 6 <= characters <= 20")
                password_length = input("Enter the number again: ").strip()
            else:
                break
        except:
            print("Please enter numbers only")
            password_length = input(
                "How many characters do you want for the password? "
            ).strip()

    # Shuffle string lists
    random.shuffle(lower_case)
    random.shuffle(upper_case)
    random.shuffle(digits)
    random.shuffle(punctuation)

    # Divide the percentages
    letters_part = round(password_length * (30 / 100))
    others_part = round(password_length * (20 / 100))

    password = []
    for i in range(letters_part):
        password.append(lower_case[i])  # 30% uppercase
        password.append(upper_case[i])  # 30% lowercase

    for i in range(others_part):
        password.append(digits[i])  # 20% digits
        password.append(punctuation[i])  # 20% punctuation

    random.shuffle(password)
    print("".join(password))
