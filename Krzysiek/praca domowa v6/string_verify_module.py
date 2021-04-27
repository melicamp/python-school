import menu_module

# stringi
back_literal = ('lub cofnij do menu wisując "BACK"')
end_literal = ('Dziękuje za skorzystanie z programu')
input_text = ('Podaj tekst')
null_literal = ("Nic nie wpisałeś.")
verify_1 = ("    - Weryfikowany tekst to       :")
verify_2 = ("    - Długość tekstu              :")
verify_3 = ("    - male litery                 :")
verify_4 = ("    - DUŻE LITERY                 :")
verify_5 = ("    - cyfry                       :")
verify_6 = ("    - puste znaki (spacja/tab)    :")
verify_7 = ("    - inne znaki (np. @%&$^)      :")
welcome_literal = ('To jest program do zliczania znaków w stringu')


def liczenie_znaków():
    print(welcome_literal, '\n')
    print(input_text, back_literal)
    text = input()
    liczenie_znaków_logika(text)


def liczenie_znaków_logika(text):

    # Zerowanie liczników
    male_litery = 0
    duze_litery = 0
    cyfry = 0
    puste_znaki = 0
    inne_znaki = 0

    if text == (''):
        print(null_literal)

    elif text.upper() == ('BACK'):
        print(end_literal, "\n")
        menu_module.menu_download_decision()

    for i in range(0, len(text)):
        if text[i].islower():
            male_litery = male_litery + 1
            i = i + 1
        elif text[i].isupper():
            duze_litery = duze_litery + 1
            i = i + 1
        elif text[i].isspace():
            puste_znaki = puste_znaki + 1
            i = i + 1
        elif text[i].isdigit():
            cyfry = cyfry + 1
            i = i + 1
        else:
            inne_znaki = inne_znaki + 1

    print(verify_1, text)
    print(verify_2, len(text))
    print(verify_3, male_litery)
    print(verify_4, duze_litery)
    print(verify_5, cyfry)
    print(verify_6, puste_znaki)
    print(verify_7, inne_znaki)
    print('')

    return
