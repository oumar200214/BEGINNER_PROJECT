import random

def lancer_de():
    """Simule le lancer d'un dé à 6 faces."""
    return random.randint(1, 6)

def demander_joueur(prompt):
    """Demande à l'utilisateur s'il veut jouer."""
    while True:
        reponse = input(prompt).strip().lower()
        if reponse in ['o', 'n']:
            return reponse == 'o'
        print("Veuillez répondre par 'o' pour oui ou 'n' pour non.")

def obtenir_nombre_joueurs():
    """Demande et valide le nombre de joueurs."""
    while True:
        try:
            nombre = int(input("Quel est le nombre de joueurs ? "))
            if nombre > 0:
                return nombre
            print("Le nombre de joueurs doit être positif.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

def jouer_tour(numero_joueur):
    """Simule le tour d'un joueur."""
    score_tour = 0
    print(f"\nTour du joueur {numero_joueur}")
    while True:
        input("Appuyez sur Entrée pour lancer le dé...")
        resultat = lancer_de()
        print(f"Vous avez obtenu un {resultat}")
        if resultat == 1:
            print("Vous perdez tous vos points pour ce tour!")
            return 0
        score_tour += resultat
        print(f"Score actuel du tour : {score_tour}")
        if not demander_joueur("Voulez-vous continuer à lancer ? (o/n) "):
            return score_tour

def main():
    SCORE_GAGNANT = 50
    scores = []
    
    if not demander_joueur("Voulez-vous jouer au jeu de dés ? (o/n) "):
        print("Merci et à bientôt !")
        return

    nombre_joueurs = obtenir_nombre_joueurs()
    scores = [0 for _ in range(nombre_joueurs)]

    tour = 1
    while max(scores) < SCORE_GAGNANT:
        print(f"\n--- Tour {tour} ---")
        for i in range(nombre_joueurs):
            score_tour = jouer_tour(i + 1)
            scores[i] += score_tour
            print(f"Score total du joueur {i + 1} : {scores[i]}")
            if scores[i] >= SCORE_GAGNANT:
                print(f"\nLe joueur {i + 1} a gagné avec un score de {scores[i]} !")
                return
        tour += 1

if __name__ == "__main__":
    main()