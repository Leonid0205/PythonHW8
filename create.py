import json

def create_telephone_directory(list):
    try:
        with open('telephone_directory.json', 'r', encoding='utf-8') as t_d:
            telephone_dir = json.load(t_d)
    except:
            telephone_dir = []
    telephone_dir.append(list)
    with open('telephone_directory.json', 'w', encoding='utf-8') as t_d:
        json.dump(telephone_dir, t_d, indent = 2)
        print('Contact is successfully added')