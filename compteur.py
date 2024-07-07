def lecture_du_text():
    with open('comptage.txt', 'r', encoding= 'utf-8') as file:
        content = file.read()
        content_modifie = content.lower().replace('.', '')
    with open('comptage.txt', 'w', encoding='utf-8') as file:
        return file.write(content_modifie)
    #--------------------------# 
def convert_list():
    lecture_du_text()
    with open('comptage.txt', 'r', encoding= 'utf-8') as file:
        content = file.read()
        if ' ' in content:
            lister = content.split(' ')
        return lister
    #---------------------------#
def convert_dict():
    convert_list()
    dictionnaire_de_list = {}
    for i in convert_list():
        if len(i) > 4 and convert_list().count(i)> 1 :
            dictionnaire_de_list[i] = convert_list().count(i) 
    return dictionnaire_de_list

    
for key, value in convert_dict().items():
    print(f'les termes qui se repete sont {key}:{value} fois')
 