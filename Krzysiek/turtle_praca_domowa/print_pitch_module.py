import half_pitch_draw_logic
import penatly_box_draw_logic
import infield_draw_logic
import circle_arc_draw_logic


def pitch_print(c, a, b, backgroud, zolw_liniowy):
    zolw_liniowy.penup()

    zolw_liniowy.goto(a, b)
    print_element(zolw_liniowy, c, a, b, backgroud)

    c = c * (-1)
    b = b * - 1

    zolw_liniowy.goto(a, b)
    print_element(zolw_liniowy, c, a, b, backgroud)

    zolw_liniowy.goto(a, 1.05*c)

    backgroud.exitonclick()


def print_element(zolw_liniowy, c, a, b, wn):
    # opuszczenie pędzla
    zolw_liniowy.pendown()

    # tworzenie jednej z połów
    half_pitch_draw_logic.draw_half_pitch(zolw_liniowy, c)

    # podniesienie pędzla, i przejście w nowe miejsce (do jedenego z narożników pola karnego)
    zolw_liniowy.penup()
    zolw_liniowy.goto(c, c/3)
    zolw_liniowy.right(180)

    # tworzenie pola karnego
    penatly_box_draw_logic.draw_penatly_box(zolw_liniowy, c)

    # podniesienie pędzla, i przejście w nowe miejsce (jeden z narożników pola bramkowego)
    zolw_liniowy.penup()
    zolw_liniowy.goto(c, c/5)
    zolw_liniowy.pendown()

    # tworzenie pola bramkowego
    infield_draw_logic.draw_infield(zolw_liniowy, c)

    # podniesienie pędzla, i przejście w nowe miejsce (na wysokość przecięcia się przedłużenia lini pola bramkowego z granicą pola karnego)
    zolw_liniowy.penup()
    zolw_liniowy.goto(c-c/3.75, c/5)
    zolw_liniowy.pendown()

    # tworzenie łuku pola karnego
    p = 2.5
    zolw_liniowy.penup()
    kroki_petla = 20
    circle_arc_draw_logic.draw_circle_arc_universal(
        zolw_liniowy, c, kroki_petla, p)
    zolw_liniowy.down()
    kroki_petla = 141
    circle_arc_draw_logic.draw_circle_arc_universal(
        zolw_liniowy, c, kroki_petla, p)
    zolw_liniowy.penup()
    kroki_petla = 19
    circle_arc_draw_logic.draw_circle_arc_universal(
        zolw_liniowy, c, kroki_petla, p)

    # podniesienie pędzla, i przejście w nowe miejsce (na wysokość przecięcia przedłużenia lini pola bramkowego na linią środkową boiska)
    zolw_liniowy.penup()
    zolw_liniowy.goto(0, -c/5)
    zolw_liniowy.pendown()

    # tworzenie części koła na środdku boiska
    p = 2.5
    kroki_petla = 180
    circle_arc_draw_logic.draw_circle_arc_universal(
        zolw_liniowy, c, kroki_petla, p)
    zolw_liniowy.penup()
    zolw_liniowy.right(180)

    # podniesienie pędzla, i przejście w nowe miejsce (w okolice pierwszego z narożników)
    zolw_liniowy.penup()
    zolw_liniowy.goto(c-c/20, b)
    zolw_liniowy.right(90)
    zolw_liniowy.pendown()

    # tworzenie pierwszego z łuków przy narożniku
    p = 10
    kroki_petla = 90
    circle_arc_draw_logic.draw_circle_arc_universal(
        zolw_liniowy, c, kroki_petla, p)
    zolw_liniowy.penup()

    # podniesienie pędzla, i przejście w nowe miejsce (w okolice drugiego z narożników)
    zolw_liniowy.penup()
    zolw_liniowy.goto(c, (b-c/20) * -1)
    zolw_liniowy.left(180)
    zolw_liniowy.pendown()

    # tworzenie drugiego z łuków przy narożniku
    p = 10
    kroki_petla = 90
    circle_arc_draw_logic.draw_circle_arc_universal(
        zolw_liniowy, c, kroki_petla, p)
    zolw_liniowy.penup()
    zolw_liniowy.left(90)

    # podniesienie pędzla, i przejście w nowe miejsce (w miejsce rzutu karnego)
    zolw_liniowy.penup()
    zolw_liniowy.goto(c-c/4.5, 0)

    # tworzenie kropki dla rzutu karnego
    zolw_liniowy.down()
    zolw_liniowy.forward(1)
    zolw_liniowy.penup()
