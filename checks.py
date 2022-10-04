import json

def check(n):
    while True:
        try:
            item = int(input('Input an item of a menu: '))
            if 0 < item <= n:
                break
            else: 
                print('There is no such item in the menu')
                continue
        except:
            print('Incorrect value was inputed')
    return item
def check_empty_dir():
    try:
        with open('telephone_directory.json', 'r', encoding='utf-8') as t_d:
            tel_dir = json.load(t_d)
            return True
    except:
        print('Telephone directory is empty')
        return False
def check_phone():
    while True:
        try:
            phone = int(input('Input telephone ten digits length: '))
            if len(str(phone)) == 10:
                break
            else:
                print('Telephone format is ten digits 9991112233')
        except:
            print('Incorrect value was inputed')
    return str(phone)
def check_length(str):
    while True:
        try:
            result = input(f'Input {str} (length of {str} needs to be less than 20 symbols): ')
            if len(result) < 20:
                break
            else:
                print(f'{str} length needs to be less than 20 symbols')
        except:
            print('Incorrect value was inputed')
    return result