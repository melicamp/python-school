import menu_module


def start_program():
    print (' testowy literał do pull requesta')
    print('Podaj imię')
    user_name = input("")

    print('\nCześć %s' % (user_name))
    menu_module.menu_download_decision()


start_program()
