import menu_module
import test_1_module


# stringi
back_literal = ('lub cofnij do menu wisując "BACK"')
end_literal = ('Dziękuje za skorzystanie z programu')
error_literal = (
    "Coś ty wpisał? \nTo nie jest liczba, tylko coś ze znakami specjalnymi. \nHieroglifów Ci nie zweryfikuje.")
error_litera2 = (
    'Chcesz mnie oszukać spacją/tabulatorem?? \nNie ładnie kłamczuszku :P')
error_litera3 = (
    "Coś ty wpisał? \nTo nie jest liczba. \nOperujesz na systemie rzymskim wpisując litery??")
float_literal = (
    'Wiem że liczba jest zmiennoprzecinkowa, ale nie umiem określić czy jest parzysta')
nr_input = ("Podaj liczbę")
negative_literal = ('Liczba X jest nieparzysta')  # [:6], [-16:]
next_number_error = ('Podaj tym razem liczbę.')
next_number = ("Podaj kolejną cyfrę.")
null_literal = ("Nic nie wpisałeś.")
positive_literal = ('Liczba x jest parzysta')  # [:6], [-13:]
return_literal = ('Spróbuj jeszcze raz.')
welcome_literal = ('To jest program sprawdzający liczby')


def number_welcome():
    print(welcome_literal)
    number_input_data()


def number_input_data():
    print(nr_input, back_literal)
    podana_liczba = input('')
    number_verify_input_data(podana_liczba)


def number_verify_input_data(podana_liczba):

    while True:
        try:
            if podana_liczba == (""):
                print(null_literal)
                print(return_literal, next_number_error, back_literal, '\n')
            elif podana_liczba.isspace():
                print(error_litera2)
                print(return_literal, next_number_error, back_literal, '\n')
            elif podana_liczba.upper() == ("BACK"):
                print(end_literal, '\n')
                menu_module.menu_download_decision()
            elif podana_liczba.isalpha():
                print(error_litera3, '\n')
                print(return_literal, next_number_error, back_literal, '\n')
            else:
                wynik = float(podana_liczba) % 2
                number_input_data_calc(podana_liczba, wynik)
        except ValueError:
            print(error_literal, '\n')
            print(return_literal, next_number_error, back_literal, '\n')

        return


def number_input_data_calc(podana_liczba, wynik):

    if wynik == 0:
        print(positive_literal[0:6], podana_liczba,
              positive_literal[-13:], '\n')
        print(return_literal)
        print(next_number, back_literal, '\n')
    elif wynik == 1:
        print(negative_literal[:6], podana_liczba,
              negative_literal[-16:], '\n')
        print(return_literal)
        print(next_number, back_literal, '\n')
    else:
        print(float_literal, '\n')
        print(return_literal)
        print(next_number, back_literal, '\n')
