import random
import os

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
characters = "'!@#$%^&*()_+-=[]{}|;:,.<>?/'"

def password(length):
    password = ''
    for _ in range(length):
        char_type = random.choice(['letter', 'number', 'character'])
        if char_type == 'letter':
            password += random.choice(letters)
        elif char_type == 'number':
            password += random.choice(numbers)
        else:
            password += random.choice(characters)

    def save_password(password):        
        try:
            outputfile=input("Enter the output file name (default is 'password.txt'): ") or 'password.txt'
        except EOFError:
            outputfile = 'password.txt'

        script_dir = os.path.dirname(os.path.abspath(__file__))
        outputdir=os.path.join(script_dir, outputfile) 
        with open(outputdir, 'a') as file:
            file.write(password + '\n')

    save_password(password)
    return password

if __name__ == '__main__':
    length = int(input("Enter the desired password length: "))
    generated_password = password(length)
    print(f"Generated Password: {generated_password}")