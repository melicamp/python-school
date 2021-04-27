import menu_module

# stringi
auto_score = ('Element {i} z {podana_dlugosc_listy} z listy')
# [:6] [11] [-13:]
back_literal = ('lub cofnij do menu wisując "BACK"')
below_zero_validation = ("Jak mam zrobić ujemną ilość elementów??")
# [:7], [12] [-7:]
error_litera2 = (
    'Chcesz mnie oszukać spacją/tabulatorem?? \nNie ładnie kłamczuszku :P')
end_literal = ('Dziękuje za skorzystanie z programu')
fun_literal = ("Zabawa trwa dalej :) \n Wracamy do kroku 1")
step_1_literal = ('''
KROK 1:
Określ ilość elementów listy''')
step_2_literal = ('''
KROK 2:
Czy uzupełnić listę automatycznie?
    
        WPISZ: 
        1 - uzupełnij automatycznie
        2 - uzupełniam ręcznie
        BACK - cofnij do menu''')
step_3_literal = ('''
KROK 3: ''')
step_4_literal = ('''
KROK 4: ''')
sort_list_literal_1 = ('Sortowanie listy:')
sort_list_literal_2 = ('Lista posortowana')
manual_score = ('Określ {i} z {podana_dlugosc_listy} element listy')
new_list_literal = ("Podaj liczbę elementów nowej listy.")
null_literal = ("Nic nie wpisałeś.")
orginal_list_literal = ('Twoja lista w oryginale:')
ready_list_literal = ('Lista elementów jest gotowa')
refresh_literal = (
    'Podal liczbę elementów listy. Lub cofnij do menu wisując "BACK"')
reverse_list_literal_1 = ('Twoja lista po przyłożeniu lusterka:')
reverse_list_literal_2 = ('Lista odwrócona')
validation_input_1 = ('Nie rozpoznano dyspozycji.')
validation_input_corect_2 = (
    'Podaj swoją decyzję (1/2) lub cofnij do menu wisując "BACK"')
validation_input_corect_3 = ("Jak mam z tego określić liczbę elementów??")
welcome_literal = ('To jest program do tworzenia listy elementów')
zero_validation = ('Lista ma nie mieć elementów? To bez sensu.')


def item_list_input_data_version_1():
    print(welcome_literal, '(WERSJA 1)')
    print(step_1_literal, back_literal)
    length_declared_list = input('')
    validation_first_imput(length_declared_list)


def validation_first_imput(length_declared_list):
    while True:
        try:
            if length_declared_list == (""):
                print(null_literal, '\n', refresh_literal)

            elif length_declared_list.isspace():
                print(error_litera2, '\n', refresh_literal)

            elif length_declared_list.upper() == ('BACK'):
                print(end_literal, '\n')
                menu_module.menu_download_decision()
            elif int(length_declared_list) < 0:
                print(below_zero_validation, '\n', refresh_literal)

            elif int(length_declared_list) == 0:
                print(zero_validation, '\n', refresh_literal)

            elif int(length_declared_list) > 0:
                lista = []
                i = 0
                print(step_2_literal)
                decyzja = input('')
                validation_second_imput(
                    decyzja, lista, length_declared_list, i)
        except ValueError:
            print(validation_input_corect_3)
            print(new_list_literal, back_literal)
        length_declared_list = input('')
        print()


def validation_second_imput(decyzja, lista, length_declared_list, i):
    while decyzja.upper() == ("BACK"):
        print(end_literal)
        menu_module.menu_download_decision()
    if decyzja == ("1"):
        print(step_3_literal)
        while (int(length_declared_list) > int(i)):
            print(auto_score[:7], (i+1), auto_score[12],
                  length_declared_list, auto_score[-7:])
            element = (i+1)
            lista.insert(i, str(element))
            i = i + 1
            print(element)
            print()
            #print (lista)
            # print(i)
            printme_result(element, i, length_declared_list, lista)
    elif decyzja == ("2"):
        print(step_3_literal)
        while (int(length_declared_list) > int(i)):
            print(manual_score[:6], (i+1), manual_score[11],
                  length_declared_list, manual_score[-13:],)
            element = input("")
            print()
            lista.insert(i, str(element))
            i = i + 1
            #print (lista)
            # print(i)
            printme_result(element, i, length_declared_list, lista)
    else:
        print(validation_input_1)
        print(validation_input_corect_2)
        decyzja = input()
        validation_second_imput(decyzja, lista, length_declared_list, i)


def printme_result(element, i, length_declared_list, lista):
    if (int(length_declared_list) == int(i)):
        print(step_4_literal)
        print("    ", ready_list_literal, '\n')
        print("    ", orginal_list_literal,)
        print("        ", lista, '\n')

        print("    ", reverse_list_literal_1, '\n')

        print("        ", reverse_list_literal_2,
              'za pomocą [::-1]')
        print("        ", lista[::-1], '\n')

        lista_r = (lista)
        lista_r.reverse()
        print("        ", reverse_list_literal_2,
              'funkcją ".reverse"')
        print("        ", lista_r, '\n')

        print("    ", sort_list_literal_1, '\n')

        lista.sort()
        print("        ", sort_list_literal_2, 'funkcją ".sort"')
        print("        ", lista, '\n')

        print(fun_literal)
        print(step_1_literal, back_literal)
