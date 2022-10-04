import csv
import json

def import_dir():
    conclusion = []
    with open('telephone_directory.csv', encoding='utf-8') as t_d_c:
        reader = csv.reader(t_d_c, delimiter=',')
        for i in reader:
                dict = {}
                dict['first name'] = i[0]
                dict['last name'] = i[1]
                dict['telephone'] = i[2]
                dict['comment'] = i[3]
                conclusion.append(dict)
    with open('telephone_directory.json', 'w', encoding='utf-8') as t_d:
        json.dump(conclusion, t_d, indent=2)
    print('Import is completed')