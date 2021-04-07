#Zestaw stringów:

#GLOBAL

hello_literal = ('Cześć')
welcome_literal =('To jest program,')
menu_present1 = ("COMBO trzy w jednym")
menu_present2 = ('Umiem robić kilka rzeczy')
liczba_present1 = ('sprawdzający liczby')
list_present1 = ('do tworzenia listy elementów')
char_present1 = ('do zliczania znaków w stringu')
null_literal = ("Nic nie wpisałeś.")
validation_input_1 = ('Nie rozpoznano dyspozycji.')
end_literal = ('Dziękuje za skorzystanie z programu')
back_literal = ('lub cofnij do menu wisując "BACK"')
back_literal_2 = ("Podaj element lub wyświelt wynik (RESULT) lub cofnij do menu (BACK)")
back_literal_3 =("Podaj kolejny element lub wyświelt wynik (RESULT) lub cofnij do menu (BACK)")



#MENU:
first_decision_literal = ('''Co chcesz zrobić?:
        1 - Okreśłić czy liczba jest parzysta
        2 - Stworzyć liste elementów (wersja 1)
        3 - Stworzyć liste elementów (wersja 2)
        4 - Przeanalizować wpisany string pod kątem ilośći liter, znaków i cyfr

        5 - "PSEUDO TEST AUTOMATYCZNY" - określania parzystości liczby
        6 - "PSEUDO TEST AUTOMATYCZNY" - analiza string pod kątem ilośći liter, znaków i cyfr
        
        CLOSE - Zakończyć program''')

validation_input_1 = ('Nie rozpoznano dyspozycji.')

validation_input_corect_1 = ('Podaj swoją decyzję (1/2/3/4) lub zakończ program (CLOSE)')



#LICZBY:
nr_input = ("Podaj liczbę")
return_literal = ('Spróbuj jeszcze raz.')
next_number_error = ('Podaj tym razem liczbę.')
next_number = ("Podaj kolejną cyfrę.")
positive_literal = ('Liczba x jest parzysta') # [:6], [-13:]
negative_literal = ('Liczba X jest nieparzysta')# [:6], [-16:]
error_literal =("Coś ty wpisał? \nTo nie jest liczba, tylko coś ze znakami specjalnymi. \nHieroglifów Ci nie zweryfikuje.")
error_litera2 = ('Chcesz mnie oszukać spacją/tabulatorem?? \nNie ładnie kłamczuszku :P')
error_litera3 = ("Coś ty wpisał? \nTo nie jest liczba. \nOperujesz na systemie rzymskim wpisując litery??")
float_literal = ('WIem że liczba jest zmiennoprzecinkowa, ale nie umiem okreśłić czy jest parzysta')



#LISTY:
step_1_literal =('''
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
null_literal_liszt = ("Nic nie wpisałeś.")
refresh_literal = ('Podal liczbę elementów listy. Lub cofnij do menu wisując "BACK"')
zero_validation = ('Lista ma nie mieć elementów? To bez sensu.')
below_zero_validation = ("Jak mam zrobić ujemną ilość elementów??")
auto_score = ('Element {i} z {podana_dlugosc_listy} z listy') # [:7], [12] [-7:]
manual_score = ('Określ {i} z {podana_dlugosc_listy} element listy') #[:6] [11] [-13:]
ready_list_literal = ('Lista elementów jest gotowa')
orginal_list_literal = ('Twoja lista w oryginale:')
reverse_list_literal_1 = ('Twoja lista po przyłożeniu lusterka:')
reverse_list_literal_2 = ('Lista odwrócona')
sort_list_literal_1 = ('Sortowanie listy:')
sort_list_literal_2 = ('Lista posortowana')
new_list_literal = ("Podaj liczbę elementów nowej listy.")
validation_input_corect_2 = ('Podaj swoją decyzję (1/2) lub cofnij do menu wisując "BACK"')
validation_input_corect_3 =("Jak mam z tego określić liczbę elementów??")
fun_literal = ("Zabawa trwa dalej :) \n Wracamy do kroku 1")



#LICZENIE ZNAKÓW:
input_text = ('Podaj tekst')
verify_1 = ("    - Weryfikowany tekst to       :")
verify_2 = ("    - Długość tekstu              :")
verify_3 = ("    - male litery                 :")
verify_4 = ("    - DUŻE LITERY                 :")
verify_5 = ("    - cyfry                       :")
verify_6 = ("    - puste znaki (spacja/tab)    :")
verify_7 = ("    - inne znaki (np. @%&$^)      :")





def menu ():
    print (hello_literal, '\n')
    print (welcome_literal, menu_present1)
    print (menu_present2)
    print (first_decision_literal)

    wybor = input()
    print()

    while True:
        if wybor ==("CLOSE") or wybor == ('close'):
            print (end_literal)
            import sys
            sys.exit();
        if wybor == ("1"):        
            liczba()
        elif wybor == ("2"):
            lista_wersja_1()
        elif wybor == ("3"):
            lista_wersja_2_1()
        elif wybor == ("4"):
            liczenie_znaków()
        elif wybor == ("5"):
            test_1()
        elif wybor == ("6"):
            test_2()
        else:
            print (validation_input_1)
            print (validation_input_corect_1)
            wybor = input()               
            print()
    







def liczba():
    print (welcome_literal, liczba_present1)
    print (nr_input, back_literal)
    podana_liczba = input('')
    liczba_logika(podana_liczba)

def liczba_logika (podana_liczba):
    
    while True:
        try:
            if podana_liczba == (""):
                print (null_literal)
                print (return_literal, next_number_error, back_literal, '\n')           
            elif podana_liczba.isspace():
                print (error_litera2)
                print (return_literal, next_number_error, back_literal, '\n')
            elif podana_liczba ==("BACK") or podana_liczba ==("back"):
                print (end_literal, liczba_present1, '\n')
                menu()
            elif podana_liczba.isalpha():
                print (error_litera3, '\n')
                print (return_literal, next_number_error, back_literal, '\n')
            
            else:
                wynik1 = float(podana_liczba) % 2         
                if wynik1 == 0:
                    print (positive_literal[0:6], podana_liczba, positive_literal[-13:], '\n')
                    print (return_literal)
                    print (next_number, back_literal, '\n')
                elif wynik1 == 1:
                    print (negative_literal[:6], podana_liczba, negative_literal[-16:], '\n')
                    print (return_literal)
                    print (next_number, back_literal,'\n')
                else:
                    print (float_literal,'\n')
                    print (return_literal)
                    print (next_number, back_literal,'\n')
                
        except ValueError:
                print(error_literal, '\n')
                print (return_literal, next_number_error, back_literal,'\n')           

        return     
        







def lista_wersja_1 ():
    print (welcome_literal, list_present1, '(WERSJA 1)')
    print (step_1_literal, back_literal)
    podana_dlugosc_listy = input('')

    while True:
        try:
            if podana_dlugosc_listy == (""):
                print (null_literal, '\n', refresh_literal)
            
            elif podana_dlugosc_listy.isspace():
                print (error_litera2, '\n', refresh_literal)
                
            elif podana_dlugosc_listy == ('BACK') or podana_dlugosc_listy == ('back'):
                print (end_literal, list_present1, '\n')
                menu()                
            elif int(podana_dlugosc_listy) < 0:                                                                                  
                print (below_zero_validation, '\n', refresh_literal)
                
            elif int(podana_dlugosc_listy) == 0:                                                                                
                print (zero_validation, '\n', refresh_literal)
                                         
            elif int(podana_dlugosc_listy) > 0:                                                                                            
                lista = []            
                i = 0                                                                                          
                print (step_2_literal)
                decyzja = input('')
                
                while (decyzja != ('1') and decyzja != ('2') and decyzja != ('BACK') and decyzja != ('back')):
                    print (validation_input_1)
                    print (validation_input_corect_2)
                    decyzja = input()
                    print()
                                  
                if decyzja ==("BACK") or decyzja ==("back") :
                    print (end_literal, list_present1)
                    menu()
                elif decyzja == ("1"):
                    print (step_3_literal)
                    while (int(podana_dlugosc_listy) > int(i)):                        
                        print (auto_score[:7], (i+1), auto_score [12], podana_dlugosc_listy, auto_score[-7:])
                        element = (i+1)                                                                       
                        lista.insert(i, str(element))                                                              
                        i = i + 1
                        print (element)
                        print ()
                        #print (lista)                                                                              
                        #print(i)                                                                                    
        
                elif decyzja ==("2"):
                    print (step_3_literal)
                    while (int(podana_dlugosc_listy) > int(i)):
                        print (manual_score[:6], (i+1), manual_score [11], podana_dlugosc_listy, manual_score[-13:],)
                        element = input("")
                        print ()
                        lista.insert(i, str(element))                                                               
                        i = i + 1
                        #print (lista)                                                                               
                        #print(i)                                                                                    
                        
                        
                if (int(podana_dlugosc_listy) == int(i)):                                                   
                            print (step_4_literal)
                            print ("    ", ready_list_literal, '\n')                                                       
                            print ("    ", orginal_list_literal,)
                            print ("        ", lista, '\n')

                            print ("    ", reverse_list_literal_1, '\n')

                            print ("        ", reverse_list_literal_2, 'za pomocą [::-1]')
                            print ("        ", lista[::-1],'\n')
                            

                            lista_r = (lista)
                            lista_r.reverse()
                            print ("        ", reverse_list_literal_2, 'funkcją ".reverse"')
                            print ("        ", lista_r, '\n')



                            print ("    ", sort_list_literal_1, '\n')

                            lista.sort()
                            print ("        ", sort_list_literal_2, 'funkcją ".sort"')
                            print ("        ", lista, '\n')
                            

                            sortowanie_babelkowe_up(lista)
                            print ("        ", sort_list_literal_2, 'bombelkowo rosnąco')
                            print ("        ", lista, '\n')

                            sortowanie_babelkowe_down(lista)
                            print ("        ", sort_list_literal_2, 'bombelkowo malejąco')
                            print ("        ", lista, '\n')
                            
                                                    
                            
                print (fun_literal) 
                    
                print (step_1_literal, back_literal)    
                                                              

        except ValueError:                                                                                     
            print(validation_input_corect_3)
            print(new_list_literal, back_literal)    
        podana_dlugosc_listy = input('')
        print()


def sortowanie_babelkowe_up(lista):
    zamiana = True
    while zamiana:
        zamiana = False
        for i in range(0, len(lista)-1):
            if lista[i] > lista[i+1]:
                tymczasowa = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = tymczasowa
                zamiana = True


def sortowanie_babelkowe_down(lista):
    zamiana = True
    while zamiana:
        zamiana = False
        for i in range(0, len(lista)-1):
            if lista[i] < lista[i+1]:
                tymczasowa = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = tymczasowa
                zamiana = True           











def lista_wersja_2_1():
    print (welcome_literal, list_present1, '(WERSJA 2)')
    lista_2_2 ()


def lista_2_2 ():
    lista = []
    print (back_literal_2)
    element = input()


    while True:
        if element == ('RESULT') or element == ('result'):
            print ("\n", ready_list_literal, "\n")
            print ("    ", orginal_list_literal)
            print ("        ", lista, '\n')
            
            print ("    ", reverse_list_literal_1)
            lista.reverse()
            print ("        ", lista, '\n')
            
            print ("    ", sort_list_literal_2)
            lista.sort()
            print ("        ", lista, '\n')
            
            print ('NOWA LISTA')
            lista_2_2() 

        elif element == ('BACK') or element == ('back'):     
            menu () 

        else:
            lista.append(element)
            #print (lista, '\n')        #wyświetla listę elementów po każdym dodaniu nowego wpisu
            print (back_literal_3)
            element = input()  








def liczenie_znaków():
    print (welcome_literal, char_present1, '\n')
    print (input_text, back_literal)                             
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
        print (null_literal)
        
    elif text == ('BACK') or text == ('back'):
        print (end_literal, char_present1, "\n")
        menu()

    for i in range (0, len(text)):
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


    print (verify_1, text)
    print (verify_2, len(text))
    print (verify_3, male_litery)
    print (verify_4, duze_litery)
    print (verify_5, cyfry)
    print (verify_6, puste_znaki)
    print (verify_7, inne_znaki)
    print ('')

    return
        



def test_1():    
    print ("START AUTO TESTU")
    wartosci = ['', ' ', 'test', "$@#@", '10', '11', '3.21']

    
    for i in range (0, len(wartosci)):
        podana_liczba = wartosci[i]
        print (podana_liczba)    
        i = i + 1
        liczba_logika (podana_liczba)
        
    if  i == len(wartosci):
        print ("KONIEC AUTO TESTU \n")
        menu()


def test_2():    
    print ("START AUTO TESTU")
    wartosci = ['abcd', 'ABCD', '123', "$@#@", 'AB CD', 'ab     cd', 'ABCD_EFG_hijk 12345    789']

    
    for i in range (0, len(wartosci)):
        text = wartosci[i]
        #print (wartosci[i])    
        i = i + 1
        liczenie_znaków_logika(text)
        
    if  i == len(wartosci):
        print ("KONIEC AUTO TESTU \n")
        menu()


        


#ROZPOCZĘCIE PROGRAMU:
menu()  # wywołujemy funkcję menu()



  

            

