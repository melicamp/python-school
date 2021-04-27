import menu_module
import number_verify_module


def test_1():
    print("START AUTO TESTU")
    wartosci = ['3', ' ', 'test', "$@#@", '10', '11', '3.21']

    for i in range(0, len(wartosci)):
        podana_liczba = wartosci[i]
        print(wartosci[i])
        i = i + 1
        number_verify_module.number_verify_input_data(podana_liczba)

    if i == len(wartosci):
        print("KONIEC AUTO TESTU \n")
        menu_module.menu_download_decision()
