from checks import check

def reception():
    print('\nHello')
    print('\nYou can:\n'
          '1 - Create a contact\n'
          '2 - Find a contact\n'
          '3 - Show all contacts\n'
          '4 - Import of contacts\n'
          '5 - Export of contacts\n'
          '6 - Exit')
def search_option():
    print('Serch by:\n'
          '1 - First name\n'
          '2 - Last name\n'
          '3 - Phone')
def action():
    print('What you want to do with contact:\n'
          '1 - Change\n'
          '2 - Delete\n'
          '3 - Exit to the main menu\n'
          '4 - Exit the program')
    return check(4)