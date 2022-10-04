import json

def delete_contact(list):
    with open('telephone_directory.json', 'r', encoding='utf-8') as t_d:
        tel_dir = json.load(t_d)
    for i in range(len(tel_dir)):
        if tel_dir[i] == list[0]:
            tel_dir.pop(i)
            break                   ###!!!!!!!!!!!!!!!!!!!!!!!!!!
    with open('telephone_directory.json', 'w', encoding='utf-8') as t_d:
        json.dump(tel_dir, t_d, indent=2)
    print('The contact is succesfully deleted')