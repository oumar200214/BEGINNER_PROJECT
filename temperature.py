def split_string(input_str):
    num_part = ''
    char_part = ''
    for char in input_str:
        if char.isdigit():
            num_part += char
        else:
            char_part += char
    
    return [float(num_part), char_part]

def collect_CorForK():
    global result
    if result[1] == 'C':
        convert = input('What do you want between (F/K): ').upper()
        if convert == 'F':
            resultat_ferh = f'The conversion in Fahrenheit is {(result[0]*9/5) + 32} F'
            return resultat_ferh
        elif convert == 'K':
            resultat_kelvin = f'The conversion in Fahrenheit is {(result[0]+ 273.15)} K'
            return resultat_kelvin
    #----------------
    elif result[1] == 'F':
        convert = input('What do you want between (C/K): ').upper()
        if convert == 'F':
            resultat_cel = f'The conversion in Celsius is {(result[0] - 32) * 5/9} C'
            return resultat_cel
        elif convert == 'K':
            resultat_kelvin_fer = f'The conversion in Fahrenheit is {(((result[0] - 32) * 5/9 )+ 273.15)} K'
            return resultat_kelvin_fer
    #------------------
    elif result[1] == 'K':
        convert = input('What do you want between (F/C): ').upper()
        if convert == 'F':
            resultat_ferh_kel = f'The conversion in Fahrenheit is {(result[0] - 459.67)} F'
            return resultat_ferh_kel
        elif convert == 'K':
            resultat_kelvin_cel = f'The conversion in Celsius is {(result[0] - 273.15)} C'
            return resultat_kelvin_cel
    else:
        print('Invalide type')
    


while True:
    try:
        get_temperature = input("Veuillez saisir une chaîne de caractères (par exemple, '45C') : ").upper()
        result = split_string(get_temperature)
        print(collect_CorForK())
    except ValueError:
        print("Please type like this exemple '45c'")
    if input('do you want to continue(y/n): ') == 'n': 
        break  
    else: 
        continue

#print("Partie numérique :", result[0])
#print("Partie alphabétique :", result[1])

