from math import sqrt
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def add(a, b): return a + b
def substract(a, b): return a - b
def multiply(a, b): return a * b
def division(a, b): 
    if b == 0:
        raise ValueError('"Division par zéro impossible"')
    return a / b
def modulo(a, b): return a % b
def power(a, b): return a**b
def squart_root(a, _): return sqrt(a)

operation = {
    '+' : add,
    '-': substract,
    '*': multiply,
    '/': division,
    '%': modulo,
    '^':power,
    'sqrt': squart_root
    }

while True:
    a = get_number('Entrez le premier nombre : ')
    op = input("Choisissez l'opérateur (+, -, *, /, %, ^, sqrt) ou 'q' pour quitter : ").lower()
    if op == 'q':
        print("Merci d'avoir utilisé la calculatrice. Au revoir!")
        break
    if op not in operation:
        print("Opérateur non valide.")
        continue
    b = get_number("Entrez le deuxième nombre : ") if op != 'sqrt' else 0
    try:
        result = operation[op](a, b)
        print(f"Le résultat est : {result}")
    except ValueError as e:
        print(f"Erreur : {e}")
    if input("Voulez-vous continuer ? (o/n) : ").lower() != 'o':
        print("Merci d'avoir utilisé la calculatrice. Au revoir!")
        break





