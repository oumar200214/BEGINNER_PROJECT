import random
import string

def ask_user(prompt):
    """Ask the user a yes/no question."""
    while True:
        response = input(prompt).lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("Veuillez répondre par 'y' ou 'n'.")

def get_password_length():
    """Get the desired password length from the user."""
    while True:
        try:
            length = int(input("Quelle longueur souhaitez-vous pour votre mot de passe ? "))
            if length > 0:
                return length
            print("La longueur doit être un nombre positif.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

def get_custom_characters():
    """Get custom characters from the user to include in the password."""
    if ask_user("Voulez-vous ajouter des caractères personnalisés à votre mot de passe ? (y/n): "):
        return input("Entrez les caractères que vous souhaitez ajouter : ")
    return ""

def generate_password(length, custom_chars=""):
    """Generate a password of the specified length, including any custom characters."""
    character_set = string.ascii_letters + string.digits + string.punctuation + custom_chars
    password = ''.join(random.choice(character_set) for _ in range(length))
    
    # Ensure the password contains at least one character from each category
    categories = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    for category in categories:
        if not any(char in category for char in password):
            random_pos = random.randint(0, length - 1)
            password = password[:random_pos] + random.choice(category) + password[random_pos + 1:]
    
    return password

def main():
    """Main function to run the password generator."""
    print("Bienvenue dans le générateur de mot de passe sécurisé!")
    
    while True:
        if ask_user("Voulez-vous générer un nouveau mot de passe ? (y/n): "):
            length = get_password_length()
            custom_chars = get_custom_characters()
            password = generate_password(length, custom_chars)
            print(f"Votre mot de passe sécurisé est : {password}")
        else:
            print("Merci d'avoir utilisé notre générateur de mot de passe. Au revoir!")
            break

if __name__ == '__main__':
    main()