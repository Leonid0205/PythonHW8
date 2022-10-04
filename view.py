import json
from checks import check_phone
from checks import check_length

def get_value():
    tel_dir = {}
    tel_dir['first name'] = check_length('first name')
    tel_dir['last name'] = check_length('last name')
    tel_dir['telephone'] = check_phone()
    tel_dir['comment'] = check_length('comment')
    return tel_dir
def show_tel_contact(list):
    for n, i in enumerate(list):
        print(f'{n + 1} Contact\n'
              f'first name: {i["first name"]}\n'
              f'last name: {i["last name"]}\n'
              f'telephone: {i["telephone"]}\n'
              f'comment: {i["comment"]}\n')
def show_tel_dir():
    with open('telephone_directory.json', 'r', encoding='utf-8') as t_d:
        tel_dir = json.load(t_d)
        print()
        print('The following contacts found: ')
        for n, i in enumerate(tel_dir):
            print(f'{n + 1} Contact\n'
              f'first name: {i["first name"]}\n'
              f'last name: {i["last name"]}\n'
              f'telephone: {i["telephone"]}\n'
              f'comment: {i["comment"]}\n')