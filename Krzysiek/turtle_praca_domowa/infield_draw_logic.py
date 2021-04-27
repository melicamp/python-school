def draw_infield(zolw_liniowy, c):

    for _ in range(2):
        zolw_liniowy.pendown()
        zolw_liniowy.forward(c/7)
        zolw_liniowy.left(90)
        zolw_liniowy.forward(c/2.5)
        zolw_liniowy.left(90)
