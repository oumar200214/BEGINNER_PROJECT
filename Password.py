import random
import string
#get input from the user to generate password or not
def ask_pass(prompt):
    return input(prompt).lower()
#get the length of the password
def ask_size():
    try:
        number = input('What size do you want for your password: ')
        if number.isdigit():
            number = int(number)
            return number
        else: print('Invalide')
    except ValueError:
        print('type number!')
#ask the user if they are something they want to add to the password
def ask_to_add():
    addn = input('What do you want to add to your password: ')
    make = []
    for i in addn:
        make += i
    return make
#generate the code it was so hard for me de developed !
def generator():
    test = []
    for i, k in zip(string.hexdigits, string.punctuation):
        test += i, k
    data1= ''.join(random.choices((test), k= ask_size()))
    return data1
#the main code in a while loop perfect to get multiple password
def main():
    while True:
        password = ask_pass('Do you want to generate you password(y/n): ')

        if password == 'y':
            print(f' you powerfull password is: {generator()}')
        elif password == 'n':
            print('Goodbye')
            break
        else:
            print('Invalide value') 
if __name__ == '__main__':
    main()