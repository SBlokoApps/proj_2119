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
        self.menu_init(size_master)
        self.settings_init(size_master)
        self.set_scors_init(size_master)
        self.about_pr_init(size_master)
        self.graph_init(size_master)
        self.vers_menu_init(size_master)
        self.scors_menu_init(size_master)
        self.games_init(size_master)


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
        text_slovar = {'positions': size_master.repos_and_resize((0, 860)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf'),
                       'color': colors[0], 'text': 'ВЫХОД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((800, 150)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        self.menu_objs['exit'] = RButton(rbut_slovar.copy())
        self.menu_objs['exit'].set_text(text_slovar)
        self.menu_objs['exit'].move_center_text()
        rbut_slovar['animations'] = [[a0], [a1]]
        rbut_slovar['positions'] = size_master.repos_and_resize((0, 650))
        text_slovar['text'] = 'НАСТРОЙКИ'
        text_slovar['positions'] = size_master.repos_and_resize((0, 660))
        self.menu_objs['sets'] = RButton(rbut_slovar.copy())
        self.menu_objs['sets'].set_text(text_slovar)
        self.menu_objs['sets'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((0, 450))
        text_slovar['text'] = 'ИГРЫ'
        text_slovar['positions'] = size_master.repos_and_resize((0, 460))
        self.menu_objs['games'] = RButton(rbut_slovar.copy())
        self.menu_objs['games'].set_text(text_slovar)
        self.menu_objs['games'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((0, 250))
        text_slovar['text'] = 'СЧЕТЧИКИ'
        text_slovar['positions'] = size_master.repos_and_resize((0, 260))
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
        text_slovar = {'positions': size_master.repos_and_resize((0, 860)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf'),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((800, 150)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        self.scors_menu_objs['exit'] = RButton(rbut_slovar.copy())
        self.scors_menu_objs['exit'].set_text(text_slovar)
        self.scors_menu_objs['exit'].move_center_text()
        rbut_slovar['size'] = size_master.repos_and_resize((1500, 150))
        rbut_slovar['animations'] = [[a10], [a11]]
        rbut_slovar['positions'] = size_master.repos_and_resize((210, 650))
        text_slovar['text'] = 'КАЛЬКУЛЯТОР'
        text_slovar['positions'] = size_master.repos_and_resize((210, 660))
        self.scors_menu_objs['calc'] = RButton(rbut_slovar.copy())
        self.scors_menu_objs['calc'].set_text(text_slovar)
        self.scors_menu_objs['calc'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((210, 450))
        text_slovar['text'] = 'БАЛЛЫ ЗА БОЙ'
        text_slovar['positions'] = size_master.repos_and_resize((210, 460))
        self.scors_menu_objs['battle'] = RButton(rbut_slovar.copy())
        self.scors_menu_objs['battle'].set_text(text_slovar)
        self.scors_menu_objs['battle'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((210, 250))
        text_slovar['text'] = 'БАЛЛЫ ЗА ДЕЙСТВИЕ'
        text_slovar['positions'] = size_master.repos_and_resize((210, 260))
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
        text_slovar = {'positions': size_master.repos_and_resize((0, 860)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf'),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((800, 150)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        self.games_objs['exit'] = RButton(rbut_slovar.copy())
        self.games_objs['exit'].set_text(text_slovar)
        self.games_objs['exit'].move_center_text()
        rbut_slovar['size'] = size_master.repos_and_resize((1500, 150))
        rbut_slovar['animations'] = [[a10], [a11]]
        rbut_slovar['positions'] = size_master.repos_and_resize((210, 650))
        text_slovar['text'] = '3'
        text_slovar['positions'] = size_master.repos_and_resize((210, 660))
        self.games_objs['3'] = RButton(rbut_slovar.copy())
        self.games_objs['3'].set_text(text_slovar)
        self.games_objs['3'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((210, 450))
        text_slovar['text'] = '2'
        text_slovar['positions'] = size_master.repos_and_resize((210, 460))
        self.games_objs['2'] = RButton(rbut_slovar.copy())
        self.games_objs['2'].set_text(text_slovar)
        self.games_objs['2'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((210, 250))
        text_slovar['text'] = '1'
        text_slovar['positions'] = size_master.repos_and_resize((210, 260))
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
        text_slovar = {'positions': size_master.repos_and_resize((0, 860)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf'),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((800, 150)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        self.settings_objs['exit'] = RButton(rbut_slovar.copy())
        self.settings_objs['exit'].set_text(text_slovar)
        self.settings_objs['exit'].move_center_text()
        rbut_slovar['animations'] = [[a0], [a1]]
        rbut_slovar['positions'] = size_master.repos_and_resize((0, 650))
        text_slovar['text'] = 'О ПРОГРАММЕ'
        text_slovar['positions'] = size_master.repos_and_resize((0, 660))
        self.settings_objs['vers'] = RButton(rbut_slovar.copy())
        self.settings_objs['vers'].set_text(text_slovar)
        self.settings_objs['vers'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((0, 450))
        text_slovar['text'] = 'ГРАФИЧЕСКИЕ'
        text_slovar['positions'] = size_master.repos_and_resize((0, 460))
        self.settings_objs['graphs'] = RButton(rbut_slovar.copy())
        self.settings_objs['graphs'].set_text(text_slovar)
        self.settings_objs['graphs'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((0, 250))
        text_slovar['text'] = 'СЧЕТЧИКИ'
        text_slovar['positions'] = size_master.repos_and_resize((0, 260))
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
        text_slovar = {'positions': size_master.repos_and_resize((0, 860)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf'),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((800, 150)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        self.graph_objs['exit'] = RButton(rbut_slovar.copy())
        self.graph_objs['exit'].set_text(text_slovar)
        self.graph_objs['exit'].move_center_text()
        rbut_slovar['animations'] = [[a0], [a1]]
        rbut_slovar['positions'] = size_master.repos_and_resize((1120, 850))
        text_slovar['text'] = 'СОХРАНИТЬ'
        text_slovar['positions'] = size_master.repos_and_resize((1120, 860))
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
        text_slovar = {'positions': size_master.repos_and_resize((0, 860)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf'),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((800, 150)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        self.about_pr_objs['exit'] = RButton(rbut_slovar.copy())
        self.about_pr_objs['exit'].set_text(text_slovar)
        self.about_pr_objs['exit'].move_center_text()
        rbut_slovar['animations'] = [[a0], [a1]]
        rbut_slovar['positions'] = size_master.repos_and_resize((1120, 850))
        text_slovar['text'] = 'МЕНЮ ВЕРСИЙ'
        text_slovar['positions'] = size_master.repos_and_resize((1120, 860))
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
        text_slovar = {'positions': size_master.repos_and_resize((0, 860)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf', 0.8),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((600, 115)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        self.vers_menu_objs['exit'] = RButton(rbut_slovar.copy())
        self.vers_menu_objs['exit'].set_text(text_slovar)
        self.vers_menu_objs['exit'].move_center_text()
        rbut_slovar['animations'] = [[a0], [a1]]
        rbut_slovar['positions'] = size_master.repos_and_resize((660, 850))
        text_slovar['text'] = 'ПОЛУЧИТЬ'
        text_slovar['positions'] = size_master.repos_and_resize((660, 860))
        self.vers_menu_objs['roman'] = RButton(rbut_slovar.copy())
        self.vers_menu_objs['roman'].set_text(text_slovar)
        self.vers_menu_objs['roman'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((1320, 850))
        text_slovar['text'] = 'ПОЛУЧИТЬ'
        text_slovar['positions'] = size_master.repos_and_resize((1320, 860))
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
        text_slovar = {'positions': size_master.repos_and_resize((0, 860)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf'),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 850)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((800, 150)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a2]]}
        self.set_scors_objs['exit'] = RButton(rbut_slovar.copy())
        self.set_scors_objs['exit'].set_text(text_slovar)
        self.set_scors_objs['exit'].move_center_text()
        rbut_slovar['animations'] = [[a0], [a1]]
        rbut_slovar['positions'] = size_master.repos_and_resize((1120, 850))
        text_slovar['text'] = 'ОТКРЫТЬ ФАЙЛ'
        text_slovar['positions'] = size_master.repos_and_resize((1120, 860))
        self.set_scors_objs['open'] = RButton(rbut_slovar.copy())
        self.set_scors_objs['open'].set_text(text_slovar)
        self.set_scors_objs['open'].move_center_text()

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
