import print_setting


def start_screen():

    print('Program rysowania żółwiami')
    print('Podaj wielkość boiska (w pixelach)')
    pitch_size = input('')

    print_setting.draw_setting(pitch_size)


start_screen()