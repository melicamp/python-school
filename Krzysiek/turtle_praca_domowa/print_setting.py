import print_pitch_module
import turtle


def draw_setting(pitch_size):
    c = int(pitch_size)
    a = 0
    b = c/2

    backgroud = turtle.Screen()
    backgroud.bgcolor('green')
    zolw_liniowy = turtle.Turtle()
    zolw_liniowy.color('white')
    zolw_liniowy.speed(50)

    print_pitch_module.pitch_print(c, a, b, backgroud, zolw_liniowy)
