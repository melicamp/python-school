def draw_penatly_box(zolw_liniowy, c):
    for _ in range(2):
        zolw_liniowy.pendown()
        zolw_liniowy.forward(c/3)
        zolw_liniowy.left(90)
        zolw_liniowy.forward(c/1.5)
        zolw_liniowy.left(90)
