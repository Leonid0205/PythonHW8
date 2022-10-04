from datetime import datetime as dt

def create_contact_log(list):
    time = dt.now().strftime('%H:%M')
    with open ('log.txt', 'a') as log:
        log.write('New contact created: {} {}\n'
                  .format(list, time))
def delete_contact_log(list):
    time = dt.now().strftime('%H:%M')
    with open ('log.txt', 'a') as log:
        log.write('Contact was deleteed: {} {}\n'
                  .format(list, time))
def change_contact_log(list):
    time = dt.now().strftime('%H:%M')
    with open ('log.txt', 'a') as log:
        log.write('Contact was changed: {} {}\n'
                  .format(list, time))
def import_log():
    time = dt.now().strftime('%H:%M')
    with open ('log.txt', 'a') as log:
        log.write('Import all contacts: {}\n'
                  .format(time))
def export_log():
    time = dt.now().strftime('%H:%M')
    with open ('log.txt', 'a') as log:
        log.write('Export all contacts: {}\n'
                  .format(time))