from window_size_master import *
from user_interface import *


pygame.init()
new_open = True
breaked = False
if new_open:
    wsm_screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('WindowSizeMaster')
    pygame.display.set_icon(pygame.image.load('res/wsm/icon.png'))
    wsm0 = True
    wsm1 = False
    wsm3 = False
    wsm2 = False
    user_wsm = WSMGUI(wsm_screen)
    while True:
        pygame.time.delay(10)
        user_wsm.print_field()
        if wsm0:
            res = user_wsm.zero_screen()
            if res == -1 or res == 4:
                breaked = True
                break
            if res == 1:
                wsm0 = False
                wsm1 = True
                continue
        if wsm1:
            res = user_wsm.first_screen()
            if res == -1:
                breaked = True
                break
            if res == 4:
                wsm1 = False
                wsm0 = True
                continue
            if res == 1:
                wsm1 = False
                wsm2 = True
                continue
        if wsm2:
            res = user_wsm.second_screen()
            if res == -1:
                breaked = True
                break
            if res == 4:
                wsm1 = True
                wsm2 = False
                continue
            if res == 1:
                wsm3 = True
                wsm2 = False
                continue
        if wsm3:
            res = user_wsm.third_screen()
            if res == -1:
                breaked = True
                break
            if res == 4:
                wsm3 = False
                wsm2 = True
                continue
            if res == 1:
                break
        pygame.display.update()
my_wsm = WSM()
if not(breaked):
    if my_wsm.get_fullscreen():
        window = pygame.display.set_mode(my_wsm.get_size(), pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode(my_wsm.get_size())
    pygame.display.set_caption('US-f-CT')
    pygame.display.set_icon(pygame.image.load('res/icon.png'))
    my_gui = GUI(window, my_wsm)
    menu = True
    settings = False
    set_scors = False
    about_pr = False
    graph = False
    vers_menu = False
    scors_menu = False
    games = False
    simple = False
    while True:
        pygame.time.delay(10)
        my_gui.print_field()
        if menu:
            res = my_gui.menu()
            if res == -1 or res == 4:
                break
            if res == 1:
                scors_menu = True
                menu = False
                continue
            if res == 2:
                games = True
                menu = False
                continue
            if res == 3:
                settings = True
                menu = False
                continue
        if scors_menu:
            res = my_gui.scors_menu()
            if res == -1:
                break
            if res == 4:
                scors_menu = False
                menu = True
                continue
            if res == 1:
                scors_menu = False
                simple = True
                continue
        if games:
            res = my_gui.games()
            if res == -1:
                break
            if res == 4:
                games = False
                menu = True
                continue
        if settings:
            res = my_gui.settings()
            if res == -1:
                break
            if res == 4:
                settings = False
                menu = True
                continue
            if res == 1:
                set_scors = True
                settings = False
                continue
            if res == 2:
                graph = True
                settings = False
                continue
            if res == 3:
                about_pr = True
                settings = False
                continue
        if set_scors:
            res = my_gui.set_scors()
            if res == -1:
                break
            if res == 4:
                settings = True
                set_scors = False
                continue
            if res == 1:
                pass
        if about_pr:
            res = my_gui.about_pr()
            if res == -1:
                break
            if res == 4:
                about_pr = False
                settings = True
                continue
            if res == 1:
                about_pr = False
                vers_menu = True
        if graph:
            res = my_gui.graph()
            if res == -1:
                break
            if res == 4:
                graph = False
                settings = True
                continue
            if res == 1:
                pass
        if vers_menu:
            res = my_gui.vers_menu()
            if res == -1:
                break
            if res == 4:
                about_pr = True
                vers_menu = False
                continue
            if res == 1:
                pass
            if res == 2:
                pass
        if simple:
            res = my_gui.simple()
            if res == -1:
                break
            if res == 4:
                simple = False
                scors_menu = True
                continue
        pygame.display.update()
pygame.quit()
