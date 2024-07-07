import random

# Dictionnaire contenant les questions et réponses
questions = {
    "CPU": "central processing unit",
    "RAM": "random access memory",
    "GPU": "graphics processing unit",
    "HDD": "hard disk drive",
    "SSD": "solid state drive",
    "OS": "operating system",
    "LAN": "local area network",
    "IP": "internet protocol",
    "USB": "universal serial bus",
    "BIOS": "basic input/output system"
}

def get_user_input(prompt):
    """Obtenir l'entrée de l'utilisateur et la nettoyer."""
    return input(prompt).lower().strip()

def check_answer(user_answer, correct_answer):
    """Vérifier si la réponse de l'utilisateur est correcte."""
    return user_answer == correct_answer

def play_game():
    """Fonction principale pour jouer au jeu."""
    score = 0
    total_questions = 5  # Nombre de questions à poser
    
    # Sélectionner des questions aléatoires
    selected_questions = random.sample(list(questions.items()), total_questions)
    
    print("Bienvenue dans le jeu de devinettes informatiques!")
    print(f"Vous allez répondre à {total_questions} questions.\n")
    
    for acronym, full_form in selected_questions:
        user_answer = get_user_input(f"Que signifie {acronym} ? ")
        if check_answer(user_answer, full_form):
            print("Correct!")
            score += 1
        else:
            print(f"Désolé, la réponse correcte était : {full_form}")
        print()  # Ligne vide pour la lisibilité
    
    print(f"Jeu terminé! Votre score est de {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Pourcentage de réussite : {percentage:.2f}%")
    
    if percentage == 100:
        print("Parfait! Vous êtes un expert!")
    elif percentage >= 80:
        print("Excellent travail!")
    elif percentage >= 60:
        print("Bon travail, mais il y a encore place à l'amélioration.")
    else:
        print("Continuez à pratiquer, vous vous améliorerez!")

if __name__ == "__main__":
    play_game()