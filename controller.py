import view
import change_contact
import checks
import create
import delete
import export
import import_j
import logger
import search
import reception


def button_click():
    while True:
        reception.reception()
        press = checks.check(6)
        if press == 1:
            tel_dir = view.get_value()
            create.create_telephone_directory(tel_dir)
            logger.create_contact_log(tel_dir)
        elif press == 2:
            if checks.check_empty_dir():
                reception.search_option()
                search_press = checks.check(3)
                result = search.search_contact(search_press)
                if len(result) != 0:
                    view.show_tel_contact(result)
                else:
                    print('Sorry there is no such contact')
                if len(result) == 1:
                    press_action = reception.action()
                    if press_action == 1:
                        change_contact.contact_change(result)
                        logger.change_contact_log(result[0])
                    if press_action == 2:
                        delete.delete_contact(result)
                        logger.delete_contact_log(result[0])
                    if press_action == 3:
                        continue
                    if press_action == 4:
                        exit()
                    
            else:
                continue
        elif press == 3:
            if checks.check_empty_dir():
                view.show_tel_dir()
        elif press == 4:
            import_j.import_dir()
            logger.import_log()
        elif press == 5:
            export.export()
            logger.export_log()
        else: 
            break