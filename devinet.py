import random

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

def get_userInput(prompt):
    return input(prompt).strip().lower()
def check_userInput(get_user, full_answer):
    return get_user == full_answer

def main():
    score = 0
    question_number = 7
    question_to_ask = random.sample(list(questions.items()), question_number)
    for acronyme, full_answer in question_to_ask:
        get_user = get_userInput(f'what is the {acronyme}: ')
        if check_userInput(get_user, full_answer):
            print("Correct!")
            score += 1
        else: print(f'Incorrect!, the good response is {full_answer} ')
    print(f'le jeu est termine est votre score est de {score}/{question_number}')
    pourcentage = (score/question_number) * 100
    print(f'your result is {pourcentage:.2f}%')
    if pourcentage == 100:
        print(f'you are a genius!')
    elif pourcentage >= 80:
        print(f'pas mal pour un debutant!')
    elif pourcentage >= 60:
        print("Bon travail, mais il y a encore place à l'amélioration.")
    else:
        print("Continuez à pratiquer, vous vous améliorerez!")


if __name__ == "__main__":
    main()