import json
import checks

def contact_change(list):
    with open('telephone_directory.json', 'r', encoding='utf-8') as t_d:
        tel_dir = json.load(t_d)
    for i in range(len(tel_dir)):
        if tel_dir[i] == list[0]:
            print('What you want to change: \n'
                'First name - 1\n'
                'Last name - 2\n'
                'Telephone - 3\n'
                'Comment - 4')
            change = checks.check(4)
            if change == 1:

                tel_dir.pop(i)
                list[0]['first name'] = checks.check_length('first name')
                tel_dir.append(list[0])
                break
            if change == 2:
                tel_dir.pop(i)
                list[0]['last name'] = checks.check_length('last name')
                tel_dir.append(list[0])
                break
            if change == 3:
                tel_dir.pop(i)
                list[0]['telephone'] = checks.check_phone()
                tel_dir.append(list[0])
                break
            if change == 4:
                tel_dir.pop(i)
                list[0]['comment'] = checks.check_length('comment')
                tel_dir.append(list[0])
                break
    with open('telephone_directory.json', 'w', encoding='utf-8') as t_d:
        json.dump(tel_dir, t_d, indent=2)
    print('The contact is changed')