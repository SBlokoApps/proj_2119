# Берем всё из наших файлов + библиотеку ос, она нужна для игры
from window_size_master import *
from user_interface import *
from colber import Colber
import os


# Загоним всё в функцию, чтобы хоть чуть-чуть быстрее работало
def main():
    pygame.init()
    pygame.event.set_allowed([QUIT, MOUSEBUTTONDOWN, KEYDOWN, KEYUP])
    clock = pygame.time.Clock()
    # Читаем файлик с настройками экрана, если в нём написано, что программа
    # была запущена хоть раз, мы не запустим ВСМ(это несколько ниже).
    # Если там написано другое, или файлика просто нет, мы запустим ВСМ
    try:
        with open('res/screen_sets.txt', 'r') as f:
            vse = f.read().split()
        if vse[3] == '1':
            new_open = False
        else:
            new_open = True
    except Exception:
        new_open = True
    # Маленькая переменная, которая не позволит запустить основную программу
    # при выходе из ВСМ раньше времени
    breaked = False
    if new_open:
        # Мы запускаем ВСМ
        wsm_screen = pygame.display.set_mode((400, 300), pygame.DOUBLEBUF)
        pygame.display.set_caption('WindowSizeMaster')
        pygame.display.set_icon(pygame.image.load('res/wsm/icon.png'))
        # Логические переменные для разных окон
        wsm0 = True
        wsm1 = False
        wsm3 = False
        wsm2 = False
        # Класс интерфейса для ВСМ
        user_wsm = WSMGUI(wsm_screen)
        # Главный цикл. В нем разные экраны программы (между которыми мы
        # переходим кнопками дальше и назад) разделены логическими переменными
        # Принцип работы всех экранов одинаковый. Рисуем интерфейс через
        # метод класса ВСМГУИ, принимаем нажатия, получаем ответ -
        # какую кнопку нажали. Либо переходим назад, либо выходим из
        # программы, либо переходим на следующий экран
        # Комментировать только нулевой экран буду,
        # остальные в исключительных случаях
        while True:
            # Прорисуем фон
            user_wsm.print_field()
            if wsm0:
                # Прорисуем нулевой экран, получим от него результат нажатия
                # кнопки, если оно было
                res = user_wsm.zero_screen()
                if res == -1 or res == 4:  # Выход или крестик - прерываем
                    # работу всей программы
                    breaked = True
                    break
                if res == 1:  # Кнопка дальше - переходим на новый экран
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
            # Запускаем часы, чтобы они подождали, обновляем дисплей
            clock.tick(60)
            pygame.display.update()
        # Если мы вышли из ВСМ, надо удалить весь его интерфейс,
        # который ест много памяти
        del user_wsm
    # Запустим класс ВСМ (Уже не гуи)
    my_wsm = WSM()
    # Если программа не была прервана ранее, запускаем основное окно
    if not(breaked):
        pd = pygame.display
        if my_wsm.get_fullscreen():  # В всм смотрим,
            # полноэкранный режим у нас, или нет
            window = pd.set_mode(my_wsm.get_size(),
                                 pygame.FULLSCREEN | pygame.DOUBLEBUF)
        else:
            window = pd.set_mode(my_wsm.get_size(), pygame.DOUBLEBUF)
        # Настроим иконку и название
        pd.set_caption('US-f-CT')
        pd.set_icon(pygame.image.load('res/icon.png'))
        my_gui = GUI(window, my_wsm)  # Создаем класс интерфейса
        # основной программы, инициализируем окна программы
        my_gui.master_init('menu', 'sets', 'games', 'scors_menu',
                           'simple', 'vers_menu', 'set_scors',
                           'about_pr', 'graph')
        # Логика для главного цикла
        menu = True
        settings = False
        set_scors = False
        about_pr = False
        graph = False
        vers_menu = False
        scors_menu = False
        games = False
        simple = False
        # Переменная запуска игры колба головного мозга
        game_colber = False
        # Принцип работы главного цикла абсолютно аналогичен циклу из всм,
        # посмотрите комментарий перед ним
        while True:
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
                if res == 1:  # Если запустили игру, даем переменной тру,
                    # закрываем главный цикл программы
                    game_colber = True
                    break
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
                if res == 5:
                    break
            if set_scors:
                res = my_gui.set_scors()
                if res == -1:
                    break
                if res == 4:
                    settings = True
                    set_scors = False
                    continue
                if res == 1:  # Кнопка открытия файла настроек. Открываем его
                    # через ос. А потом закрываем программу, тк настройки
                    # надо будет обновить
                    os.startfile(os.getcwd() + '/res/settings.txt')
                    break
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
                    continue
            if graph:
                res = my_gui.graph()
                if res == -1:
                    break
                if res == 4:
                    graph = False
                    settings = True
                    continue
                if res == 1:  # Открываем всм. Для этого надо сбросить
                    # настройки всм и перезапустить программу, тогда всм
                    # откроется сам при запуске
                    my_wsm.reset_sets()
                    os.startfile(os.getcwd() + '/main.py')
                    break
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
            clock.tick(60)
            pygame.display.update()
        # Если мы запускаем игру Колба головного мозга
        if game_colber:
            # Сначала удаляем интерфейс основной программы, он ест память
            del my_gui
            menu = True
            progr = False
            play = False
            shop_c = False
            shop_t = False
            half = False
            half_prew = False
            # Класс игры. Там интерфейс и куча всего
            game = Colber(my_wsm, window)
            # Очередной главный цикл, принцип работы которого за 2 раза
            # вы могли запомнить, повторять его описание не буду
            while True:
                if menu:
                    res = game.menu()
                    if res == -1:
                        break
                    if res == 4:  # Если мы выходим из игры: мы уже выкинули
                        # всё об основной пограмме из памяти, поэтому
                        # придется перезапустить программу через ос
                        os.startfile(os.getcwd() + '/main.py')
                        break
                    if res == 2:
                        progr = True
                        menu = False
                        continue
                    if res == 1:
                        play = True
                        menu = False
                        continue
                if progr:
                    res = game.progress()
                    if res == 44:  # Если совершены обновления настроек,
                        # перезапускаем программу
                        os.startfile(os.getcwd() + '/main.py')
                        break
                    if res == -1:
                        break
                    if res == 4:
                        progr = False
                        menu = True
                        continue
                if play:
                    res = game.choose_lvl()
                    if res == -1:
                        break
                    if res == 4:
                        play = False
                        menu = True
                        continue
                    if res == 1001:
                        shop_c = True
                        play = False
                        continue
                    if res == 1002:
                        shop_t = True
                        play = False
                        continue
                    if res == 1003:
                        half = True
                        play = False
                        continue
                if shop_c:
                    res = game.shop_c()
                    if res == -1:
                        break
                    if res == 4:
                        shop_c = False
                        play = True
                        continue
                if shop_t:
                    res = game.shop_t()
                    if res == -1:
                        break
                    if res == 4:
                        shop_t = False
                        play = True
                        continue
                if half:
                    res = game.half()
                    if res == -1:
                        break
                    if res == 4:
                        half = False
                        menu = True
                        continue
                    if res == 1:
                        half = False
                        play = True
                        continue
                    if res == 1234:
                        half = False
                        half_prew = True
                if half_prew:
                    res = game.hf_prew()
                    if res == -1:
                        break
                    if res == 4:
                        half_prew = False
                        half = True
                        continue
                clock.tick(60)
                pygame.display.update()
    pygame.quit()


# Не забудем запустить эту функцию
main()
