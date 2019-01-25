from project_R import *


class GUI:
    def __init__(self, window, size_master):
        prefix = size_master.get_prefix()
        self.win = window
        self.fld = size_master.transform(pygame.image.load(prefix + 'field.png'), (1920, 1080))
        self.menu_objs = {}
        self.settings_objs = {}
        self.set_scors_objs = {}
        self.about_pr_objs = {}
        self.graph_objs = {}
        self.vers_menu_objs = {}
        self.scors_menu_objs = {}
        self.games_objs = {}
        self.simple_objs = {}
        self.master_init_ui_objs = {}
        self.size_master = size_master
        self.inited_names = []
        self.master_init_ui_init(size_master)

    def master_init(self, *names):
        self.master_init_ui()
        master_slovar = {'menu': self.menu_init, 'sets': self.settings_init, 'set_scors': self.set_scors_init,
                         'about_pr': self.about_pr_init, 'graph': self.graph_init, 'vers_menu': self.vers_menu_init,
                         'scors_menu': self.scors_menu_init, 'games': self.games_init, 'simple': self.simple_init}
        for i in names:
            if i in self.inited_names:
                continue
            pygame.display.update()
            master_slovar[i](self.size_master)
            self.inited_names.append(i)

    def menu_init(self, size_master):
        factor = size_master.get_factor()
        prefix = size_master.get_prefix()
        colors = size_master.get_colors()
        a0 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_off.png'), (800, 150))
        a1 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_on.png'), (800, 150))
        a2 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_on2.png'), (800, 150))
        text_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf'),
                       'color': colors[0], 'text': 'ВЫХОД'}
        title_slovar = {'positions': size_master.repos_and_resize((0, 20)), 'win': self.win,
                        'font': 'res/fonts/Staatliches-Regular.ttf',
                        'text_size': size_master.resize_text('res/fonts/Staatliches-Regular.ttf'),
                        'color': colors[2], 'color2': colors[1], 'text': 'The United Scorer',
                        'indent': size_master.resize_one(3)}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((800, 150)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        base_slovar = {'positions': size_master.repos_and_resize((860, 230)),
                       'picture': size_master.transform(pygame.image.load(prefix + 'us-f-ct_image.png'), (1000, 812)),
                       'win': self.win}
        self.menu_objs['picture'] = RBase(base_slovar.copy())
        self.menu_objs['title1'] = RTitle(title_slovar.copy())
        self.menu_objs['title1'].move_center(size_master.resize_one(1920))
        self.menu_objs['title1'].move_center_y(size_master.resize_one(250))
        self.menu_objs['exit'] = RButton(rbut_slovar.copy())
        self.menu_objs['exit'].set_text(text_slovar)
        self.menu_objs['exit'].move_center_text()
        rbut_slovar['animations'] = [[a0], [a1]]
        rbut_slovar['positions'] = size_master.repos_and_resize((0, 650))
        text_slovar['text'] = 'НАСТРОЙКИ'
        text_slovar['positions'] = size_master.repos_and_resize((0, 650))
        self.menu_objs['sets'] = RButton(rbut_slovar.copy())
        self.menu_objs['sets'].set_text(text_slovar)
        self.menu_objs['sets'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((0, 450))
        text_slovar['text'] = 'ИГРЫ'
        text_slovar['positions'] = size_master.repos_and_resize((0, 450))
        self.menu_objs['games'] = RButton(rbut_slovar.copy())
        self.menu_objs['games'].set_text(text_slovar)
        self.menu_objs['games'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((0, 250))
        text_slovar['text'] = 'СЧЕТЧИКИ'
        text_slovar['positions'] = size_master.repos_and_resize((0, 250))
        self.menu_objs['itogi'] = RButton(rbut_slovar.copy())
        self.menu_objs['itogi'].set_text(text_slovar)
        self.menu_objs['itogi'].move_center_text()

    def scors_menu_init(self, size_master):
        factor = size_master.get_factor()
        prefix = size_master.get_prefix()
        colors = size_master.get_colors()
        a0 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_off.png'), (800, 150))
        a1 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_on.png'), (800, 150))
        a2 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_on2.png'), (800, 150))
        a10 = size_master.transform(
            pygame.image.load(prefix + 'b_1500_150_off.png'), (1500, 150))
        a11 = size_master.transform(
            pygame.image.load(prefix + 'b_1500_150_on.png'), (1500, 150))
        a12 = size_master.transform(
            pygame.image.load(prefix + 'b_1500_150_on2.png'), (1500, 150))
        text_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf'),
                       'color': colors[0], 'text': 'НАЗАД'}
        title_slovar = {'positions': size_master.repos_and_resize((0, 0)), 'win': self.win,
                        'font': 'res/fonts/labor-union-regular.otf',
                        'text_size': size_master.resize_text('res/fonts/labor-union-regular.otf'),
                        'color': colors[2], 'color2': colors[1], 'text': 'СЧЕТЧИКИ',
                        'indent': size_master.resize_one(3)}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((800, 150)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        self.scors_menu_objs['title1'] = RTitle(title_slovar.copy())
        self.scors_menu_objs['title1'].move_center(size_master.resize_one(1920))
        self.scors_menu_objs['title1'].move_center_y(size_master.resize_one(250))
        self.scors_menu_objs['exit'] = RButton(rbut_slovar.copy())
        self.scors_menu_objs['exit'].set_text(text_slovar)
        self.scors_menu_objs['exit'].move_center_text()
        rbut_slovar['size'] = size_master.repos_and_resize((1500, 150))
        rbut_slovar['animations'] = [[a10], [a11]]
        rbut_slovar['positions'] = size_master.repos_and_resize((210, 650))
        text_slovar['text'] = 'КАЛЬКУЛЯТОР'
        text_slovar['positions'] = size_master.repos_and_resize((210, 650))
        self.scors_menu_objs['calc'] = RButton(rbut_slovar.copy())
        self.scors_menu_objs['calc'].set_text(text_slovar)
        self.scors_menu_objs['calc'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((210, 450))
        text_slovar['text'] = 'БАЛЛЫ ЗА БОЙ'
        text_slovar['positions'] = size_master.repos_and_resize((210, 450))
        self.scors_menu_objs['battle'] = RButton(rbut_slovar.copy())
        self.scors_menu_objs['battle'].set_text(text_slovar)
        self.scors_menu_objs['battle'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((210, 250))
        text_slovar['text'] = 'БАЛЛЫ ЗА ДЕЙСТВИЕ'
        text_slovar['positions'] = size_master.repos_and_resize((210, 250))
        self.scors_menu_objs['simple'] = RButton(rbut_slovar.copy())
        self.scors_menu_objs['simple'].set_text(text_slovar)
        self.scors_menu_objs['simple'].move_center_text()

    def games_init(self, size_master):
        factor = size_master.get_factor()
        prefix = size_master.get_prefix()
        colors = size_master.get_colors()
        a0 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_off.png'), (800, 150))
        a1 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_on.png'), (800, 150))
        a2 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_on2.png'), (800, 150))
        a10 = size_master.transform(
            pygame.image.load(prefix + 'b_1500_150_off.png'), (1500, 150))
        a11 = size_master.transform(
            pygame.image.load(prefix + 'b_1500_150_on.png'), (1500, 150))
        a12 = size_master.transform(
            pygame.image.load(prefix + 'b_1500_150_on2.png'), (1500, 150))
        text_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf'),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((800, 150)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        title_slovar = {'positions': size_master.repos_and_resize((0, 0)), 'win': self.win,
                        'font': 'res/fonts/labor-union-regular.otf',
                        'text_size': size_master.resize_text('res/fonts/labor-union-regular.otf'),
                        'color': colors[2], 'color2': colors[1], 'text': 'ИГРЫ',
                        'indent': size_master.resize_one(3)}
        self.games_objs['title1'] = RTitle(title_slovar.copy())
        self.games_objs['title1'].move_center(size_master.resize_one(1920))
        self.games_objs['title1'].move_center_y(size_master.resize_one(250))
        self.games_objs['exit'] = RButton(rbut_slovar.copy())
        self.games_objs['exit'].set_text(text_slovar)
        self.games_objs['exit'].move_center_text()
        rbut_slovar['size'] = size_master.repos_and_resize((1500, 150))
        rbut_slovar['animations'] = [[a10], [a11]]
        rbut_slovar['positions'] = size_master.repos_and_resize((210, 650))
        text_slovar['text'] = '3'
        text_slovar['positions'] = size_master.repos_and_resize((210, 650))
        self.games_objs['3'] = RButton(rbut_slovar.copy())
        self.games_objs['3'].set_text(text_slovar)
        self.games_objs['3'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((210, 450))
        text_slovar['text'] = '2'
        text_slovar['positions'] = size_master.repos_and_resize((210, 450))
        self.games_objs['2'] = RButton(rbut_slovar.copy())
        self.games_objs['2'].set_text(text_slovar)
        self.games_objs['2'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((210, 250))
        text_slovar['text'] = '1'
        text_slovar['positions'] = size_master.repos_and_resize((210, 250))
        self.games_objs['1'] = RButton(rbut_slovar.copy())
        self.games_objs['1'].set_text(text_slovar)
        self.games_objs['1'].move_center_text()

    def settings_init(self, size_master):
        factor = size_master.get_factor()
        prefix = size_master.get_prefix()
        colors = size_master.get_colors()
        a0 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_off.png'), (800, 150))
        a1 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_on.png'), (800, 150))
        a2 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_on2.png'), (800, 150))
        text_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf'),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((800, 150)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        title_slovar = {'positions': size_master.repos_and_resize((0, 0)), 'win': self.win,
                        'font': 'res/fonts/labor-union-regular.otf',
                        'text_size': size_master.resize_text('res/fonts/labor-union-regular.otf'),
                        'color': colors[2], 'color2': colors[1], 'text': 'НАСТРОЙКИ',
                        'indent': size_master.resize_one(3)}
        self.settings_objs['title1'] = RTitle(title_slovar.copy())
        self.settings_objs['title1'].move_center(size_master.resize_one(1920))
        self.settings_objs['title1'].move_center_y(size_master.resize_one(250))
        self.settings_objs['exit'] = RButton(rbut_slovar.copy())
        self.settings_objs['exit'].set_text(text_slovar)
        self.settings_objs['exit'].move_center_text()
        rbut_slovar['animations'] = [[a0], [a1]]
        rbut_slovar['positions'] = size_master.repos_and_resize((0, 650))
        text_slovar['text'] = 'О ПРОГРАММЕ'
        text_slovar['positions'] = size_master.repos_and_resize((0, 650))
        self.settings_objs['vers'] = RButton(rbut_slovar.copy())
        self.settings_objs['vers'].set_text(text_slovar)
        self.settings_objs['vers'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((0, 450))
        text_slovar['text'] = 'ГРАФИЧЕСКИЕ'
        text_slovar['positions'] = size_master.repos_and_resize((0, 450))
        self.settings_objs['graphs'] = RButton(rbut_slovar.copy())
        self.settings_objs['graphs'].set_text(text_slovar)
        self.settings_objs['graphs'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((0, 250))
        text_slovar['text'] = 'СЧЕТЧИКИ'
        text_slovar['positions'] = size_master.repos_and_resize((0, 250))
        self.settings_objs['scors'] = RButton(rbut_slovar.copy())
        self.settings_objs['scors'].set_text(text_slovar)
        self.settings_objs['scors'].move_center_text()

    def graph_init(self, size_master):
        factor = size_master.get_factor()
        prefix = size_master.get_prefix()
        colors = size_master.get_colors()
        a0 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_off.png'), (800, 150))
        a1 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_on.png'), (800, 150))
        a2 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_on2.png'), (800, 150))
        a3 = size_master.transform(
            pygame.image.load(prefix + 'b_600_115_off.png'), (600, 115))
        a4 = size_master.transform(
            pygame.image.load(prefix + 'b_600_115_on.png'), (600, 115))
        text_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf'),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((800, 150)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        title_slovar = {'positions': size_master.repos_and_resize((0, 0)), 'win': self.win,
                        'font': 'res/fonts/labor-union-regular.otf',
                        'text_size': size_master.resize_text('res/fonts/labor-union-regular.otf', 0.7),
                        'color': colors[2], 'color2': colors[1], 'text': 'ГРАФИЧЕСКИЕ НАСТРОЙКИ',
                        'indent': size_master.resize_one(3)}
        text_box_slovar = {'positions': size_master.repos_and_resize((0, 220)), 'win': self.win,
                           'font': 'res/fonts/RobotoSlab-Regular.ttf',
                           'text_size': size_master.resize_text('res/fonts/RobotoSlab-Regular.ttf', 0.66),
                           'color': colors[0],
                           'text': '''Для изменения размера окна и выбора темы оформления нажмите кнопку "Открыть WSM".
                           При нажатии программа закроется, и откроется утилита WindowSizeMaster, которую вы
                           видели при первом запуске данной программы''', 'auto': 0,
                           'window_width': size_master.resize_one(1700), 'indent': size_master.resize_one(80)}
        self.graph_objs['text_box'] = RTextBox(text_box_slovar.copy())
        self.graph_objs['text_box'].move_center(size_master.resize_one(1920))
        self.graph_objs['title1'] = RTitle(title_slovar.copy())
        self.graph_objs['title1'].move_center(size_master.resize_one(1920))
        self.graph_objs['title1'].move_center_y(size_master.resize_one(220))
        self.graph_objs['exit'] = RButton(rbut_slovar.copy())
        self.graph_objs['exit'].set_text(text_slovar)
        self.graph_objs['exit'].move_center_text()
        rbut_slovar['animations'] = [[a0], [a1]]
        rbut_slovar['positions'] = size_master.repos_and_resize((1120, 850))
        text_slovar['text'] = 'Открыть WSM'
        text_slovar['positions'] = size_master.repos_and_resize((1120, 850))
        self.graph_objs['save'] = RButton(rbut_slovar.copy())
        self.graph_objs['save'].set_text(text_slovar)
        self.graph_objs['save'].move_center_text()

    def about_pr_init(self, size_master):
        factor = size_master.get_factor()
        prefix = size_master.get_prefix()
        colors = size_master.get_colors()
        a0 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_off.png'), (800, 150))
        a1 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_on.png'), (800, 150))
        a2 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_on2.png'), (800, 150))
        text_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf'),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((800, 150)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        title_slovar = {'positions': size_master.repos_and_resize((0, 0)), 'win': self.win,
                        'font': 'res/fonts/labor-union-regular.otf',
                        'text_size': size_master.resize_text('res/fonts/labor-union-regular.otf', 0.8),
                        'color': colors[2], 'color2': colors[1], 'text': 'О ПРОГРАММЕ',
                        'indent': size_master.resize_one(3)}
        text_box_slovar = {'positions': size_master.repos_and_resize((20, 200)), 'win': self.win,
                           'font': 'res/fonts/RobotoSlab-Regular.ttf',
                           'text_size': size_master.resize_text('res/fonts/RobotoSlab-Regular.ttf', 0.44),
                           'color': colors[0],
                           'text': '''The United Scorer for Chemistry Tournament предназначен для подсчета баллов на Межрегиональном Химическом Турнире
                           и других мероприятиях с подобной сложной системой расчета. Средства разработки: python 3 &
                           pygame & project_R, *#enter#* Версия: 4.0.0, *#enter#* Разработчик:
                           SBlokoApps *#enter#* github.com/SBlokoApps
                           *#enter#* mailbloko@gmail.com''', 'auto': 0,
                           'window_width': size_master.resize_one(1700), 'indent': size_master.resize_one(80)}
        base_slovar = {'positions': size_master.repos_and_resize((660, 480)),
                       'picture': size_master.transform(pygame.image.load(prefix + 'SBApps.png'), (650, 306)),
                       'win': self.win}
        base2_slovar = {'positions': size_master.repos_and_resize((1360, 428)),
                       'picture': size_master.transform(pygame.image.load(prefix + 'project_r_image.png'), (410, 410)),
                       'win': self.win}
        self.about_pr_objs['proj_r'] = RBase(base2_slovar.copy())
        self.about_pr_objs['sbapps'] = RBase(base_slovar.copy())
        self.about_pr_objs['text_box'] = RTextBox(text_box_slovar.copy())
        self.about_pr_objs['title1'] = RTitle(title_slovar.copy())
        self.about_pr_objs['title1'].move_center(size_master.resize_one(1920))
        self.about_pr_objs['title1'].move_center_y(size_master.resize_one(220))
        self.about_pr_objs['exit'] = RButton(rbut_slovar.copy())
        self.about_pr_objs['exit'].set_text(text_slovar)
        self.about_pr_objs['exit'].move_center_text()
        rbut_slovar['animations'] = [[a0], [a1]]
        rbut_slovar['positions'] = size_master.repos_and_resize((1120, 850))
        text_slovar['text'] = 'МЕНЮ ВЕРСИЙ'
        text_slovar['positions'] = size_master.repos_and_resize((1120, 850))
        self.about_pr_objs['version'] = RButton(rbut_slovar.copy())
        self.about_pr_objs['version'].set_text(text_slovar)
        self.about_pr_objs['version'].move_center_text()

    def vers_menu_init(self, size_master):
        factor = size_master.get_factor()
        prefix = size_master.get_prefix()
        colors = size_master.get_colors()
        a0 = size_master.transform(
            pygame.image.load(prefix + 'b_600_115_off.png'), (600, 115))
        a1 = size_master.transform(
            pygame.image.load(prefix + 'b_600_115_on.png'), (600, 115))
        a2 = size_master.transform(
            pygame.image.load(prefix + 'b_600_115_on2.png'), (600, 115))
        text_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf', 0.8),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((600, 115)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        base_slovar = {'positions': size_master.repos_and_resize((0, 0)),
                       'picture': size_master.transform(pygame.image.load(prefix + 'versions_pic.png'), (1920, 850)),
                       'win': self.win}
        self.vers_menu_objs['picture'] = RBase(base_slovar.copy())
        self.vers_menu_objs['exit'] = RButton(rbut_slovar.copy())
        self.vers_menu_objs['exit'].set_text(text_slovar)
        self.vers_menu_objs['exit'].move_center_text()
        rbut_slovar['animations'] = [[a0], [a1]]
        rbut_slovar['positions'] = size_master.repos_and_resize((660, 850))
        text_slovar['text'] = 'ПОЛУЧИТЬ'
        text_slovar['positions'] = size_master.repos_and_resize((660, 850))
        self.vers_menu_objs['roman'] = RButton(rbut_slovar.copy())
        self.vers_menu_objs['roman'].set_text(text_slovar)
        self.vers_menu_objs['roman'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((1320, 850))
        text_slovar['text'] = 'ПОЛУЧИТЬ'
        text_slovar['positions'] = size_master.repos_and_resize((1320, 850))
        self.vers_menu_objs['pavel'] = RButton(rbut_slovar.copy())
        self.vers_menu_objs['pavel'].set_text(text_slovar)
        self.vers_menu_objs['pavel'].move_center_text()

    def set_scors_init(self, size_master):
        factor = size_master.get_factor()
        prefix = size_master.get_prefix()
        colors = size_master.get_colors()
        a0 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_off.png'), (800, 150))
        a1 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_on.png'), (800, 150))
        a2 = size_master.transform(
            pygame.image.load(prefix + 'b_800_150_on2.png'), (800, 150))
        text_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf'),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((800, 150)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        title_slovar = {'positions': size_master.repos_and_resize((0, 0)), 'win': self.win,
                        'font': 'res/fonts/labor-union-regular.otf',
                        'text_size': size_master.resize_text('res/fonts/labor-union-regular.otf', 0.64),
                        'color': colors[2], 'color2': colors[1], 'text': 'НАСТРОЙКИ РАСЧЕТА БАЛЛОВ',
                        'indent': size_master.resize_one(3)}
        text_box_slovar = {'positions': size_master.repos_and_resize((0, 220)), 'win': self.win, 'font': 'res/fonts/RobotoSlab-Regular.ttf',
                           'text_size': size_master.resize_text('res/fonts/RobotoSlab-Regular.ttf', 0.66),
                           'color': colors[0],
                           'text': '''Для настройки счетчиков нажмите на кнопку "Открыть файл" или
                           откройте файл settings.txt в директории res папки с
                           данной программой. Все числа, коэффициенты и названия
                           оценок редактируются именно там. После нажатия на кнопку "Открыть файл" программа
                           закроется. Не забудьте сохранить файл после редактирования.''', 'auto': 0,
                           'window_width': size_master.resize_one(1700), 'indent': size_master.resize_one(80)}
        self.set_scors_objs['text_box'] = RTextBox(text_box_slovar.copy())
        self.set_scors_objs['text_box'].move_center(size_master.resize_one(1920))
        self.set_scors_objs['title1'] = RTitle(title_slovar.copy())
        self.set_scors_objs['title1'].move_center(size_master.resize_one(1920))
        self.set_scors_objs['title1'].move_center_y(size_master.resize_one(220))
        self.set_scors_objs['exit'] = RButton(rbut_slovar.copy())
        self.set_scors_objs['exit'].set_text(text_slovar)
        self.set_scors_objs['exit'].move_center_text()
        rbut_slovar['animations'] = [[a0], [a1]]
        rbut_slovar['positions'] = size_master.repos_and_resize((1120, 850))
        text_slovar['text'] = 'ОТКРЫТЬ ФАЙЛ'
        text_slovar['positions'] = size_master.repos_and_resize((1120, 850))
        self.set_scors_objs['open'] = RButton(rbut_slovar.copy())
        self.set_scors_objs['open'].set_text(text_slovar)
        self.set_scors_objs['open'].move_center_text()

    def simple_init(self, size_master):
        factor = size_master.get_factor()
        prefix = size_master.get_prefix()
        colors = size_master.get_colors()
        a0 = size_master.transform(
            pygame.image.load(prefix + 'b_600_115_off.png'), (600, 115))
        a1 = size_master.transform(
            pygame.image.load(prefix + 'b_600_115_on.png'), (600, 115))
        a2 = size_master.transform(
            pygame.image.load(prefix + 'b_600_115_on2.png'), (600, 115))
        a3 = size_master.transform(
            pygame.image.load(prefix + 'b_100_100_off.png'), (100, 100))
        a4 = size_master.transform(
            pygame.image.load(prefix + 'b_100_100_on.png'), (100, 100))
        a5 = size_master.transform(
            pygame.image.load(prefix + 'b_100_100_on2.png'), (100, 100))
        pic1 = size_master.transform(
            pygame.image.load(prefix + 'pic_1100_100.png'), (1100, 100))
        pic2 = size_master.transform(
            pygame.image.load(prefix + 'pic_1820_150.png'), (1820, 150))
        text_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf', 0.8),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((600, 115)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        rkeyb_slovar = {'positions': size_master.repos_and_resize((110, 485)), 'tap_buts': (1, 3),
                        'size': size_master.repos_and_resize((100, 100)), 'win': self.win,
                        'horizontal': True, 'indent': 0, 'kolvo': 11, 'texts': ['2', '3-',
                                                                                '3', '3+','4-', '4', '4+', '5-',
                                                                                '5', '5+', 'del']}
        rkeyb2_slovar = {'positions': size_master.repos_and_resize((110, 485)), 'win': self.win,
                         'font': 'res/fonts/RobotoSlab-Regular.ttf',
                         'text_size': size_master.resize_text('res/fonts/RobotoSlab-Regular.ttf', 0.7),
                         'color': colors[0], 'indent': size_master.resize_one(100)}
        frame_text_sl = {'positions': size_master.repos_and_resize((120, 385)), 'win': self.win, 'font': 'res/fonts/RobotoSlab-Regular.ttf',
                         'text_size': size_master.resize_text('res/fonts/RobotoSlab-Regular.ttf', 0.7),
                         'color': colors[0], 'text': '5+ 5- 4'}
        title_slovar = {'positions': size_master.repos_and_resize((0, 0)), 'win': self.win,
                        'font': 'res/fonts/labor-union-regular.otf',
                        'text_size': size_master.resize_text('res/fonts/labor-union-regular.otf', 0.7),
                        'color': colors[2], 'color2': colors[1], 'text': 'БАЛЛЫ ЗА ДЕЙСТВИЕ',
                        'indent': size_master.resize_one(3)}
        self.simple_objs['title1'] = RTitle(title_slovar.copy())
        self.simple_objs['title1'].move_center(size_master.resize_one(1920))
        self.simple_objs['title1'].move_center_y(size_master.resize_one(220))
        frame_slovar = {'picture': pic1, 'positions': size_master.repos_and_resize([110, 385]), 'win': self.win}
        anims_spisok = [[[a3], [a4], [a5]] for i in range(10)]
        anims_spisok.append([[a3], [a5]])
        self.simple_objs['exit'] = RButton(rbut_slovar.copy())
        self.simple_objs['exit'].set_text(text_slovar)
        self.simple_objs['exit'].move_center_text()
        self.simple_objs['keyboard1'] = RKeyboard(rkeyb_slovar.copy(), rkeyb2_slovar.copy(), anims_spisok.copy())
        self.simple_objs['keyboard1'].move_center_text()
        rkeyb_slovar['positions'] = size_master.repos_and_resize((110, 718))
        rkeyb2_slovar['positions'] = size_master.repos_and_resize((110, 718))
        self.simple_objs['keyboard2'] = RKeyboard(rkeyb_slovar.copy(), rkeyb2_slovar.copy(), anims_spisok.copy())
        self.simple_objs['keyboard2'].move_center_text()
        rbut_slovar['animations'] = [[a0], [a1]]
        rbut_slovar['positions'] = size_master.repos_and_resize((1320, 850))
        text_slovar['text'] = 'РЕЦЕНЗЕНТ'
        text_slovar['positions'] = size_master.repos_and_resize((1320, 850))
        self.simple_objs['recenz'] = RButton(rbut_slovar.copy())
        self.simple_objs['recenz'].set_text(text_slovar)
        self.simple_objs['recenz'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((1320, 660))
        text_slovar['text'] = 'ОППОНЕНТ'
        text_slovar['positions'] = size_master.repos_and_resize((1320, 660))
        self.simple_objs['oppon'] = RButton(rbut_slovar.copy())
        self.simple_objs['oppon'].set_text(text_slovar)
        self.simple_objs['oppon'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((1320, 470))
        text_slovar['text'] = 'ДОКЛАДЧИК'
        text_slovar['positions'] = size_master.repos_and_resize((1320, 470))
        self.simple_objs['doclad'] = RButton(rbut_slovar.copy())
        self.simple_objs['doclad'].set_text(text_slovar)
        self.simple_objs['doclad'].move_center_text()
        self.simple_objs['keyb1_text'] = RTextFrame(frame_text_sl.copy(), frame_slovar.copy())
        frame_text_sl['positions'] = size_master.repos_and_resize((120, 618))
        frame_text_sl['text'] = '3 2 2'
        frame_slovar['positions'] = size_master.repos_and_resize((110, 618))
        self.simple_objs['keyb2_text'] = RTextFrame(frame_text_sl.copy(), frame_slovar.copy())
        frame_text_sl['positions'] = size_master.repos_and_resize((80, 200))
        frame_text_sl['text'] = 'Результат:'
        frame_slovar['positions'] = size_master.repos_and_resize((50, 200))
        frame_text_sl['text_size'] = size_master.resize_text('res/fonts/RobotoSlab-Regular.ttf', 1.1)
        frame_slovar['picture'] = pic2
        self.simple_objs['result_text'] = RTextFrame(frame_text_sl.copy(), frame_slovar.copy())
        self.simple_objs['result_text'].move_center_y()
        self.simple_objs['keyb2_text'].move_center_y()
        self.simple_objs['keyb1_text'].move_center_y()

    def master_init_ui_init(self, size_master):
        factor = size_master.get_factor()
        prefix = size_master.get_prefix()
        colors = size_master.get_colors()
        text_slovar = {'positions': size_master.repos_and_resize((0, 300)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf'),
                       'color': colors[0], 'text': 'НИКУДА НЕ НАЖИМАЙТЕ!!!'}
        title_slovar = {'positions': size_master.repos_and_resize((0, 0)), 'win': self.win,
                        'font': 'res/fonts/labor-union-regular.otf',
                        'text_size': size_master.resize_text('res/fonts/labor-union-regular.otf'),
                        'color': colors[2], 'color2': colors[1], 'text': 'ИДЕТ ЗaГРУЗКА',
                        'indent': size_master.resize_one(3)}
        self.master_init_ui_objs['title1'] = RTitle(title_slovar.copy())
        self.master_init_ui_objs['title1'].move_center(size_master.resize_one(1920))
        self.master_init_ui_objs['title1'].move_center_y(size_master.resize_one(1080))
        self.master_init_ui_objs['text'] = RText(text_slovar.copy())
        self.master_init_ui_objs['text'].move_center(size_master.resize_one(1920))
        self.master_init_ui_objs['text'].move_center_y(size_master.resize_one(1080))
        text_slovar['positions'] = size_master.repos_and_resize((0, 400))
        text_slovar['text'] = '(если не хотите проблем)'
        self.master_init_ui_objs['text2'] = RText(text_slovar.copy())
        self.master_init_ui_objs['text2'].move_center(
            size_master.resize_one(1920))
        self.master_init_ui_objs['text2'].move_center_y(
            size_master.resize_one(1080))

    def print_field(self):
        self.win.blit(self.fld, (0, 0))

    def menu(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in self.menu_objs:
            try:
                self.menu_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.menu_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.menu_objs['itogi'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 1
            if self.menu_objs['games'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 2
            if self.menu_objs['sets'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 3
            if self.menu_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4

    def scors_menu(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in self.scors_menu_objs:
            try:
                self.scors_menu_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.scors_menu_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.scors_menu_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4
            if self.scors_menu_objs['simple'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 1

    def games(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in self.games_objs:
            try:
                self.games_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.games_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.games_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4

    def settings(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in self.settings_objs:
            try:
                self.settings_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.settings_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.settings_objs['scors'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 1
            if self.settings_objs['graphs'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 2
            if self.settings_objs['vers'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 3
            if self.settings_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4

    def set_scors(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in self.set_scors_objs:
            try:
                self.set_scors_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.set_scors_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.set_scors_objs['open'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 1
            if self.set_scors_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4

    def about_pr(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in self.about_pr_objs:
            try:
                self.about_pr_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.about_pr_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.about_pr_objs['version'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 1
            if self.about_pr_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4

    def graph(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in self.graph_objs:
            try:
                self.graph_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.graph_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.graph_objs['save'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 1
            if self.graph_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4

    def vers_menu(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in self.vers_menu_objs:
            try:
                self.vers_menu_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.vers_menu_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.vers_menu_objs['roman'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 1
            if self.vers_menu_objs['pavel'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 2
            if self.vers_menu_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4

    def simple(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in self.simple_objs:
            try:
                self.simple_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.simple_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.simple_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4
            self.simple_objs['keyboard1'].taps(event, pygame.mouse.get_pos(), delay=30, animation=2)


    def master_init_ui(self):
        for i in self.master_init_ui_objs:
            self.master_init_ui_objs[i].draw()