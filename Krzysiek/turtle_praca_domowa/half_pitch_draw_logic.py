def draw_half_pitch(zolw_liniowy, c):
    for _ in range(4):
        zolw_liniowy.pendown()
        zolw_liniowy.forward(c)
        zolw_liniowy.right(90)
