import menu_module
import string_verify_module


def test_2():
    print("START AUTO TESTU")
    wartosci = ['abcd', 'ABCD', '123', "$@#@", 'AB CD',
                'ab     cd', 'ABCD_EFG_hijk 12345    789']

    for i in range(0, len(wartosci)):
        text = wartosci[i]
        print(wartosci[i])
        i = i + 1
        string_verify_module.liczenie_znaków_logika(text)

    if i == len(wartosci):
        print("KONIEC AUTO TESTU \n")
        menu_module.menu_download_decision()
