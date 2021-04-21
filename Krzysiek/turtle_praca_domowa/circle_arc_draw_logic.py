def draw_circle_arc_universal(zolw_liniowy, c, kroki_petla, p):
    # c - wielkoć połowy boiska podana przez usera
    # p - dzielnik przez który dzielimy "c" by uzyskać odpowiedni fragment z długości boiska
    # r - promień okręgu z którego będziemy robić łuk
    # kroki_petla - ilość kroków żułwia po łuku (360-okrąg, 180-półokrąg, 90-ćwiartka okręgu)

    r = (c/p)/2

    for _ in range(kroki_petla):
        zolw_liniowy.forward((2*3.14*r)/360)
        zolw_liniowy.left(1)
