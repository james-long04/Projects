import random
import string

def is_valid(password):
    if len(password) < 10:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in string.punctuation for char in password):
        return False
    return True
def strengthen_password(password):
    original_password = password
    # python
    
    if len(password) < 10:
        
        password += random.choice(string.ascii_letters)
        
        
        x = random.choice(string.ascii_letters), k = 10 - len(password)
        
        # x -> ["a", "g", "5"]
        "*".join(x) -> "a" + "*" + "g" + "*" + "5"
        
        password += ''.join(random.choice(string.ascii_letters), k = 10 - len(password))
        
        password += ''.join(random.choices(string.ascii_letters + string.digits, k=10 - len(password)))   
    if not any(char.isdigit() for char in password):
        password += random.choice(string.digits)   
    if not any(char.isupper() for char in password):
        password += random.choice(string.ascii_uppercase)   
    if not any(char in string.punctuation for char in password):
        password += random.choice(string.punctuation)   
    return password if password != original_password else original_password
while True:
    password = input("Enter a password (or 'exit' to quit): ")
    if password.lower() == 'exit':
        break      
    if is_valid(password):
        print("Your password is valid.")
    else:
        strengthened = strengthen_password(password)
        print(f"Your password was strengthened to: {strengthened}")

