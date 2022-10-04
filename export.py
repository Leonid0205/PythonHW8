import json
import csv

def export():
    with open('telephone_directory.json', 'r', encoding='utf-8') as t_d:
        tel_dir = json.load(t_d)
        print(tel_dir)
    with open('telephone_directory.csv', 'w', encoding='utf-8') as t_d_c:
        writer = csv.writer(t_d_c, delimiter=',', lineterminator='\r')
        writer.writerow(['first name', 'last name', 'telephone', 'comment'])
        for i in tel_dir:
            writer.writerow([i['first name'], i['last name'], i['telephone'], i['comment']])
            # writer.writerow(i)
            # writer.writerow(i['first name'])
            # writer.writerow(i['last name'])
            # writer.writerow(i['telephone'])
            # writer.writerow(i['comment'])
            # writer.writerow(i['first name', 'last name', 'telephone', 'comment'])
    print('Export is completed')