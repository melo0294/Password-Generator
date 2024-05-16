#IMPORTING MODULES
import string
import random

#FUNCTION TO GENERATE PASSWORDS
def generate_password(size, special_characters):
    #IF USER WANTS SPECIAL CHARACTERS IN THE PASSWORD
    if special_characters:
        #PASSWORD MAY HAVE LETTER, NUMBERS AND SPECIAL CHARACTERS
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        #PASSWORD MAY HAVE ONLY LETTERS AND NUMBERS
        characters = string.ascii_letters + string.digits

    #GENERATING THE PASSWORD
    password = ''.join(random.choice(characters) for _ in range(size))
    return password

def main():
    #ASKING USER ABOUT PASSWORD SIZE
    size = int(input("How many characters does your password must have? (limit 20 characters)\n"))
    size = min(size, 20)

    #ASKING USER IF THE PASSWORD MUST HAVE SPECIAL CHARACTERS
    answer = input("Do you want letter, numbers and special characters? (yes or not)\n")
    special_characters = answer.lower() == 'yes'

    #ASKING USER THE AMOUNT TO GENERATE
    amount = int(input("How many passwords do you want to generate? (limit 10)\n"))
    amount = min(amount, 10)

    #GENERATING AND PRINTING THE PASSWORDS
    for _ in range(amount):
        print(generate_password(size, special_characters))

if __name__ == "__main__":
    main()
