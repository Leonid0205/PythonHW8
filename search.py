import json

def search_contact(n):
    with open('telephone_directory.json', 'r', encoding='utf-8') as t_d:
        tel_dir = json.load(t_d)
        search_contact_res = []
        if n == 1:
            first_name = input('Input contact name: ')
            for i in tel_dir:
                if i['first name'] == first_name:
                    search_contact_res.append(i)
            return search_contact_res
        elif n == 2:
            last_name = input('Input contact last name: ')
            for i in tel_dir:
                if i['last name'] == last_name:
                    search_contact_res.append(i)
            return search_contact_res
        elif n == 3:
            telephone = input('Input contact telephone: ')
            for i in tel_dir:
                if i['telephone'] == telephone:
                    search_contact_res.append(i)
            return search_contact_res