
#importer random
import random
#===================================
def nombre_du_des():
    MIN = 1
    MAX = 6
    return random.randint(MIN, MAX)
#===================================
def demande_jeux(prompt):
    while True:
        ask = input(prompt).strip().lower()
        if ask in ['y', 'n']:
            if ask == 'y': return True 
            else: return False
        else: print('il doit etre entre y/n')
#===================================
def nomber_joueur(prompt_2):
    while True:
        joueur = input(prompt_2)
        if joueur.isdigit() and joueur >= '0':
            joueur = int(joueur)
            joue = [0 for _ in range(joueur) if joueur >= 0]
            return joue
        elif joueur.isalpha() or joueur <= '0': 
            print('Fourniser un nombre positive pas une lettre')
            continue
        else: print('Fourniser un nombre')
#===================================
def main():
    score_final = 50
    while True:
        demander_de_jouer = demande_jeux('Voulez vous jouer (y/n): ')
        if demander_de_jouer:
            player = nomber_joueur('quel est le nombre de joueur: ')
            while max(player) < score_final:
                for player_index in range(player.count(player)):
                        print("\nPlayer", player_index +1, "turn has just started!\n")
                        score = 0
                        while True:
                            turn = input('etez vous pret taper (t): ').lower
                            if turn != 't': break
                            else:
                                nombre_du_des()
                                if nombre_du_des() == 6:
                                    print('you done it you win!')
                                    break
                                else : 
                                    score += nombre_du_des()
                                    print(f'votre des est tomber sur {nombre_du_des()}')
                                    print(f'votre score est de, {score}')


                            

        else: 
            print('Merci, et a bientot!')
            break

    










#===================================
if __name__=="__main__":
    main()














def check_winner():...
def score_en_pourcentage():...
def main():...
