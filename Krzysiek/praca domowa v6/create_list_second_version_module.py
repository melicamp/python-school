import menu_module

# stringi
back_literal_2 = ('Podaj element, lub cofnij do menu wisując "BACK"')
back_literal_3 = (
    'Podaj kolejny element, lub wyświetl wynik "RESULT", lub cofnij do menu wisując "BACK"')
orginal_list_literal = ('Twoja lista w oryginale:')
ready_list_literal = ('Lista elementów jest gotowa')
reverse_list_literal_1 = ('Twoja lista po przyłożeniu lusterka:')
sort_list_literal_2 = ('Lista posortowana')
welcome_literal = ('To jest program do tworzenia listy elementów')


def item_list_version_2():
    print(welcome_literal, '(WERSJA 2)')
    item_list_input_data_version_2()


def item_list_input_data_version_2():
    print(back_literal_2)
    lista = []
    element = input()
    item_list_create(element, lista)


def item_list_create(element, lista):
    while True:
        if element.upper() == ('RESULT'):
            print("\n", ready_list_literal, "\n")
            print("    ", orginal_list_literal)
            print("        ", lista, '\n')

            print("    ", reverse_list_literal_1, 'odwrócona poprzez pętle ;)')
            reverse_list_loop(lista)

            print('    Sortowanie listy')
            sort_list_loop(lista)

            print('NOWA LISTA')
            item_list_input_data_version_2()

        elif element.upper() == ('BACK'):
            menu_module.menu_download_decision()

        else:
            lista.append(element)
            # print (lista, '\n')        #wyświetla listę elementów po każdym dodaniu nowego wpisu
            print(back_literal_3)
            element = input()


def reverse_list_loop(lista):
    lista_reverse = lista
    length_list = len(lista_reverse)
    i = length_list - 1
    p = 0
    while i >= p:
        element_tymczasowy = lista_reverse[i]
        lista_reverse[i] = lista[p]
        lista_reverse[p] = element_tymczasowy
        i = i - 1
        p = p + 1

    print('        ', lista_reverse, '\n')


def sort_list_loop(lista):
    lista_sortowana = lista
    print('    Jak posortować? UP - rosnąco, DOWN - malejąco?')
    sort_decision = input()

    if sort_decision.upper() != "UP" and sort_decision.upper() != "DOWN":
        while True:
            print('Nie rozpoznano dyspozycji')
            sort_decision = input()
    else:
        zamiana = True
        while zamiana:
            zamiana = False
            for i in range(0, len(lista)-1):
                if (sort_decision.upper() == "UP" and lista_sortowana[i] > lista_sortowana[i+1]) or (sort_decision.upper() == "DOWN" and lista_sortowana[i] < lista_sortowana[i+1]):
                    tymczasowy_element = lista_sortowana[i]
                    lista_sortowana[i] = lista_sortowana[i+1]
                    lista_sortowana[i+1] = tymczasowy_element
                    zamiana = True
        print("    ", sort_list_literal_2)
        print('        ', lista_sortowana, '\n')
