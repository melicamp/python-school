import sys
import number_verify_module
import string_verify_module
import create_list_first_version_module
import create_list_second_version_module
import test_1_module
import test_2_module


# stringi
welcome_literal = ('To jest program COMBO trzy w jednym')
menu_present1 = ('Umiem robić kilka rzeczy')
end_literal = ('Dziękuje za skorzystanie z programu')
first_decision_literal = ('''Co chcesz zrobić?:
        1 - Określić czy liczba jest parzysta
        2 - Stworzyć liste elementów (wersja 1)
        3 - Stworzyć liste elementów (wersja 2)
        4 - Przeanalizować wpisany string pod kątem ilośći liter, znaków i cyfr

        5 - "PSEUDO TEST AUTOMATYCZNY" - określania parzystości liczby
        6 - "PSEUDO TEST AUTOMATYCZNY" - analiza string pod kątem ilośći liter, znaków i cyfr

        CLOSE - Zakończyć program''')

validation_input_1 = ('Nie rozpoznano dyspozycji.')
validation_input_corect_1 = (
    '      Podaj swoją decyzję (1-6) lub zakończ program (CLOSE)')


def menu_download_decision():
    print(welcome_literal)
    print(menu_present1)
    print(first_decision_literal)

    user_decision = input()
    print()

    menu_check_decision(user_decision)


def menu_check_decision(user_decision):
    while True:
        if user_decision.upper() == ("CLOSE"):
            print(end_literal)
            sys.exit()
        elif user_decision == ("1"):
            number_verify_module.number_welcome()
        elif user_decision == ("2"):
            create_list_first_version_module.item_list_input_data_version_1()
        elif user_decision == ("3"):
            create_list_second_version_module.item_list_version_2()
        elif user_decision == ("4"):
            string_verify_module.liczenie_znaków()
        elif user_decision == ("5"):
            test_1_module.test_1()
        elif user_decision == ("6"):
            test_2_module.test_2()
        else:
            print(validation_input_1)
            print(validation_input_corect_1)
            user_decision = input()
            print()

    return
