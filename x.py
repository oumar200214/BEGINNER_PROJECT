import random

CHOICES = ['Pierre', 'Papier', 'Ciseaux']

def get_user_choice(prompt):
    while True:
        choice = input(prompt).capitalize()
        if choice in CHOICES:
            return choice
        print(f"Choix invalide. Veuillez choisir parmi : {', '.join(CHOICES)}")

def get_computer_choice():
    return random.choice(CHOICES)

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return 'Égalité'
    winning_combinations = [('Pierre', 'Ciseaux'), ('Ciseaux', 'Papier'), ('Papier', 'Pierre')]
    if (choice1, choice2) in winning_combinations:
        return 'Joueur 1'
    return 'Joueur 2'

def play_round(player1, player2):
    choice1 = player1()
    choice2 = player2()
    print(f"Joueur 1 : {choice1}")
    print(f"Joueur 2 : {choice2}")
    winner = determine_winner(choice1, choice2)
    print(f"Résultat : {winner}")
    return winner

def update_scores(scores, winner):
    if winner == 'Égalité':
        scores['Joueur 1'] += 1
        scores['Joueur 2'] += 1
    elif winner == 'Joueur 1':
        scores['Joueur 1'] += 3
    else:
        scores['Joueur 2'] += 3

def play_game():
    scores = {'Joueur 1': 0, 'Joueur 2': 0}
    player_count = get_player_count()
    
    while True:
        if player_count == 1:
            winner = play_round(lambda: get_user_choice("Votre choix : "), get_computer_choice)
        else:
            winner = play_round(lambda: get_user_choice("Choix du Joueur 1 : "), 
                                lambda: get_user_choice("Choix du Joueur 2 : "))
        
        update_scores(scores, winner)
        
        if not continue_playing():
            break
    
    print("\nScores finaux :")
    for player, score in scores.items():
        print(f"{player} : {score}")

def get_player_count():
    while True:
        try:
            count = int(input("Nombre de joueurs (1 ou 2) : "))
            if count in [1, 2]:
                return count
            print("Veuillez entrer 1 ou 2.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def continue_playing():
    return input("Voulez-vous continuer à jouer ? (oui/non) : ").lower().startswith('o')

if __name__ == '__main__':
    play_game()