import random as ran
from string import punctuation
#Siyanda
class user_information:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def user_info_(self):
        return f"Welcome {self.name} {self.surname}"
i = True

def error_correcting(username_error, user_surname_error, user_age_error):
    try:
        return True
    except SyntaxError:
        print("Syntax Error occurred")
    except ZeroDivisionError:
        print("Error")
    except ValueError:
        print('Value Error')
    except:
        print("Error has occurred")


def length_of_name_validator(name_value):
    if len(name_value) > 50:
        print("You have entered invalid name")
        return True
    return False

def length_of_surname_vaildator(surname_value):
    if len(surname_value)>60:
        print("Your surname is invaild")
        return True
    return  False

def invalid_characters_checker(invalid_char):
    symbols = set(punctuation)
    if any(char in symbols for char in invalid_char):
        print(("Invaild symbols please try again"))
        return True
    return False

def creating_bank_account(bank_details):
    id_number = input("Enter valid SA ID number:")
    r = ran.randint(1000000, 9999999)

    def is_valid_sa_id(id_number):
        if len(id_number) != 13:
            print("Invalid SA ID number length")
            return False

        try:
            year = int(id_number[0:2])
            month = int(id_number[2:4])
            day = int(id_number[4:6])

            if month < 1 or month > 12 or day < 1 or day > 31:
                print("Invalid date components in SA ID number")
                return False

            citizenship_digit = int(id_number[6])
            if citizenship_digit < 0 or citizenship_digit > 8 or (citizenship_digit > 4 and citizenship_digit != 5):
                print("Invalid citizenship digit in SA ID number")
                return False

            gender_digit = int(id_number[7])
            if gender_digit < 0 or gender_digit > 9 or (gender_digit > 4 and gender_digit != 9):
                print("Invalid gender digit in SA ID number")
                return False
            return True
        except ValueError:
            print("Invalid SA ID number format")
            return False

    while not is_valid_sa_id(id_number):
        id_number = input("Please re-enter valid SA ID number: ")

    try:
        print("Which account type would you like to create?")
        print("1. Savings Account\n2. Cheque Account\n3. Free-Account")
        account_type = int(input("Enter your choice: "))

        if account_type == 1 or "Savings Account" == str(account_type).upper():
            print("You have created a Savings account")
            print(f"{new_user.user_info_()} \n Your account number is {r} \n You have a Savings Account with {bank_details}")
        elif account_type == 2:
            print("You have created a Cheque account")
            print(f"{new_user.user_info_()} \n Your account number is {r} \n You have a Cheque Account with {bank_details}")
        elif account_type == 3:
            print("You have created a Free-account")
            print(f"{new_user.user_info_()} \n Your account number is {r} \n You have a Free Account with {bank_details}")
        else:
            while True:
                return "Invalid Choice made, please retype your choice"
                return "Which account type would you like to create?"
                return "1. Savings Account\n2. Cheque Account\n3. Free-Account"
                account_type = int(input("Enter your choice: "))
    except Exception as e:
        return f"Following error occurred: {e}"
    except SyntaxError:
        raise SyntaxError
    except ZeroDivisionError:
        raise ZeroDivisionError

username = input("Enter Name: ")
user_surname = input("Enter Surname: ")
user_age = int(input("Enter Age: "))

try:
    user_age_reference = user_age
except ValueError:
    print("Value Error")

while invalid_characters_checker(username):
    username = input("Please re-enter name:")
while(invalid_characters_checker(user_surname)):
    user_surname = input("Please re-enter surname: ")

while length_of_name_validator(username):
    username = input("Please Re-enter name:")
while length_of_surname_vaildator(user_surname):
    user_surname = input("Please re-enter surname: ")

error_correcting(username, user_surname, user_age)
new_user = user_information(username, user_surname, user_age)
new_user.user_info_()

if user_age >= 18:
    print("Which bank would you like to make an account in?")
    print("\n 1.FNB \n 2.Nedbank \n 3.Standard Bank")
    try:
        user_options = input("Enter your options (type C to cancel)")
        user_cap = user_options.upper()
        if user_cap == "C":
            print("Loading...")
            print("Okay, canceled")
        elif user_cap == "FNB" or int(user_options) == 1:
            bank_detail = creating_bank_account("Fnb")
            print(f"Alrighty {username}, you have chosen FNB")
            print(f"{bank_detail}")
        elif user_cap == "NEDBANK" or int(user_options) == 2:
            bank_detail_nedbank = creating_bank_account("Nedbank")
            print(f"Alrighty {username}, you have chosen Nedbank")
            print(f"{bank_detail_nedbank}")
        elif user_cap == "STANDARD BANK" or int(user_options) == 3:
            bank_detail_standard = creating_bank_account("Standard Bank")
            print(f"Alrighty {username}, you have chosen Standard Bank")
            print(f"{bank_detail_standard}")
        else:
            while True:
                if user_cap == "C":
                    break
            print("Invalid choice")
            print("Which bank would you like to make an account in?")
            print("1.FNB \n 2.Nedbank \n 3.Standard Bank")
            user_options = input("Enter your options (type C to cancel)")
    except SyntaxError:
        raise SyntaxError
    while i is True:
        if user_cap == "C":
          break
          print("Error")
          print("Which bank would you like to make an account in?")
          print("1.FNB \n 2.Nedbank \n 3.Standard Bank")
          user_options = input("Enter your options (type C to cancel)")


elif user_age <= 17:
    print("Sorry, you're too young to sign up on your own >:")
    print("Enter relationship:\n Mom\n Dad\n other")

    young_user_parent_choice = input("Enter choice: ")

    def info_process(guardian_first_names, guardian_last_names):
        print("Information processing...")
        print(
            f"Hello, {guardian_first_names} {guardian_last_names}, what bank would you like {username} {user_surname} to have")
        print("\nFnb\n Nedbank\nStandard Bank")

    def parent_choice(options):
        try:
            if young_user_parent_choice.upper() == "MOM" or young_user_parent_choice == "1":
                print("Loading..")
                guardian_first_name = input("Enter Mother's fist name: ")
                while length_of_name_validator(guardian_first_name):
                    print("You entered invalid name, please try again")
                    guardian_first_name = input("Re-enter Mother's name: ")

                guardian_last_name = input("Enter Mother's last name")
                while length_of_surname_vaildator(guardian_last_name):
                    print("You entered invalid name, please try again")
                    guardian_last_name = input("Re-enter Mother's last name")

                info_process(guardian_first_name, guardian_last_name)
                guardian_choice = input("Enter Choice: ")

            elif young_user_parent_choice.upper() == "DAD" or young_user_parent_choice == "2":
                print("Loading..")
                guardian_first_name = input("Enter Father's fist name: ")
                while length_of_name_validator(guardian_first_name):
                    print("You entered invalid name, please try again")
                    guardian_first_name = input("Re-enter Father's name: ")

                guardian_last_name = input("Enter Father's last name")
                while length_of_surname_vaildator(guardian_last_name):
                    print("You entered invalid name, please try again")
                    guardian_last_name = input("Re-enter Father's last name")

                info_process(guardian_first_name, guardian_last_name)
                guardian_choice = input("Enter Choice: ")

            elif young_user_parent_choice.upper() == "OTHER" or young_user_parent_choice == "3":
                other_option = input("Enter your guardian status: ")
                guardian_first_name = input(f"Enter {other_option}'s first name: ")

                while length_of_name_validator(guardian_first_name):
                    print("You entered invalid name, please try again")
                    guardian_first_name = input(f"Re-enter {other_option}'s name: ")

                guardian_last_name = input(f"Enter {other_option}'s last name")
                while length_of_surname_vaildator(guardian_last_name):
                    print("You entered invalid name, please try again")
                    guardian_last_name = input(f"Re-enter {other_option}'s last name")

                info_process(guardian_first_name, guardian_last_name)
                guardian_choice = input("Enter Choice: ")

            try:
                if guardian_choice.upper() == "C":
                    print("Loading...")
                    print("Okay, canceled")

                elif guardian_choice.upper() == "FNB" or guardian_choice == "1":
                    bank_detail = creating_bank_account("Fnb")
                    print(f"{guardian_first_name} {guardian_last_name}, has chosen FNB for you")
                    print(f"{bank_detail}")

                elif guardian_choice.upper() == "NEDBANK" or guardian_choice == "2":
                    bank_detail_nedbank = creating_bank_account("Nedbank")
                    print(f"{guardian_first_name} {guardian_last_name}, has chosen Nedbank for you")
                    print(f"{bank_detail_nedbank}")

                elif guardian_choice.upper() == "STANDARD BANK" or guardian_choice == "3":
                    bank_detail_standard = creating_bank_account("Standard Bank")
                    print(f"{guardian_first_name} {guardian_last_name}, has chosen Standard Bank for you")
                    print(f"{bank_detail_standard}")

                else:
                    while True:
                        if guardian_choice.upper() == "C":
                            break

                    print("Invalid choice")
                    print("Which bank would you like to make an account in?")
                    print("1.FNB \n 2.Nedbank \n 3.Standard Bank")
                    user_options = input("Enter your options (type C to cancel)")

            except SyntaxError:
                raise SyntaxError

            except ValueError:
                raise ValueError

            except KeyboardInterrupt:
                raise f"Sorry, Keyboard Interrupted: {KeyboardInterrupt}"

        except SyntaxError:
            raise SyntaxError

    parent_choice(young_user_parent_choice)

