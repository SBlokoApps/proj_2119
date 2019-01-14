from project_R import *
from win32api import GetSystemMetrics, SetFileAttributes


class WSM:
    def __init__(self):
        with open('res/screen_sets.txt', 'r') as f:
            vse = f.read().split()
        self.size = [int(vse[0]), int(vse[1])]
        self.factor = self.size[0] / 1920
        self.theme = vse[2]

    def get_size(self):
        return self.size

    def get_fullscreen(self):
        if self.size[0] == GetSystemMetrics(0) and self.size[1] == GetSystemMetrics(1):
            return True
        return False

    def get_factor(self):
        return self.factor

    def get_prefix(self):
        if self.theme == '0':
            return 'res/dark/'
        return 'res/light/'

    def transform(self, image, size):
        return pygame.transform.scale(image, [int(self.factor * i) for i in size])

    def repos_and_resize(self, old):
        return [int(self.factor * i) for i in old]

    def resize_one(self, old):
        return int(self.factor * old)

    def resize_text(self, font, factor=1):
        if font == 'res/fonts/RobotoSlab-Regular.ttf':
            return int((0.045 * self.size[0] + 4.286) * factor)
        elif font == 'res/fonts/labor-union-regular.otf':
            return int((0.0893 * self.size[0] + 8/571) * factor)
        elif font == 'res/fonts/Staatliches-Regular.ttf':
            return int((0.125 * self.size[0] - 10) * factor)

    def get_colors(self):
        if self.theme == '1':
            return [(255, 0, 0), (150, 150, 150), (200, 50, 50)]
        return [(255, 255, 255), (200, 10, 10), (255, 255, 255)]


class WSMGUI:
    def __init__(self, window):
        self.theme = -1
        self.screen_size = []
        self.win = window
        self.fld = pygame.image.load('res/wsm/field.png')
        self.zero_objs = {}
        self.first_objs = {}
        self.sec_objs = {}
        self.third_objs = {}
        a0 = pygame.image.load('res/wsm/button_off.png')
        a1 = pygame.image.load('res/wsm/button_on.png')
        a2 = pygame.image.load('res/wsm/button_on2.png')
        a3 = pygame.image.load('res/wsm/input_off.png')
        a4 = pygame.image.load('res/wsm/input_on.png')
        t_slovar = {'positions': (15, 3), 'win': self.win, 'font': 'res/fonts/Staatliches-Regular.ttf', 'text_size': 55,
                    'color': (255, 0, 0), 'text': 'The United Scorer', 'color2': (0, 255, 255), 'indent': 1}
        text_slovar = {'positions': (15, 65), 'win': self.win, 'font': 'res/fonts/RobotoSlab-Regular.ttf', 'text_size': 30,
                       'color': (255, 255, 255),
                       'text': 'Перед первым запуском US-f-CT необходимо настроить размер окна программы',
                       'indent': 28, 'max_len': 22}
        rbut_slovar = {'positions': (0, 240), 'win': self.win, 'size': (150, 50), 'tap_buts': (1, 3),
                       'animations': [[a0], [a1]]}
        key_slovar = {'positions': (50, 160), 'win': self.win, 'size': (150, 50), 'tap_buts': (1, 3),
                      'animations': [[a0], [a2]], 'horizontal': True, 'kolvo': 2, 'texts': ['ТЁМНАЯ', 'СВЕТЛАЯ'],
                      'indent': 0}
        inp_slovar = {'positions': (20, 160), 'win': self.win, 'size': (150, 50), 'tap_buts': (1, 3),
                      'animations': [[a3], [a4]], 'active': False, 'speed': 25, 'max_len': 5}
        self.zero_objs['title'] = RTitle(t_slovar.copy())
        self.first_objs['title'] = self.zero_objs['title']
        self.sec_objs['title'] = self.zero_objs['title']
        self.third_objs['title'] = self.zero_objs['title']
        self.zero_objs['text'] = RTextBox(text_slovar.copy())
        text_slovar['text'] = 'Не закрывайте это окно, иначе программа не запустится. Соотношение сторон 16:9 ставится автоматически'
        self.first_objs['text'] = RTextBox(text_slovar.copy())
        text_slovar['text'] = 'Введите размер экрана в пикселях (не ниже 800х450)'
        self.sec_objs['text'] = RTextBox(text_slovar.copy())
        text_slovar['text'] = 'Выберите тему оформления программы'
        self.third_objs['text'] = RTextBox(text_slovar.copy())
        text_slovar['text'] = 'х'
        text_slovar['positions'] = [192, 162]
        self.sec_objs['text2'] = RText(text_slovar.copy())
        self.zero_objs['exit'] = RButton(rbut_slovar.copy())
        self.first_objs['exit'] = RButton(rbut_slovar.copy())
        self.sec_objs['exit'] = RButton(rbut_slovar.copy())
        self.third_objs['exit'] = RButton(rbut_slovar.copy())
        text_slovar['text'] = 'ВЫХОД'
        text_slovar['positions'] = (19, 244)
        self.zero_objs['exit'].set_text(text_slovar.copy())
        text_slovar['text'] = 'НАЗАД'
        text_slovar['positions'] = (22, 244)
        self.first_objs['exit'].set_text(text_slovar.copy())
        self.sec_objs['exit'].set_text(text_slovar.copy())
        self.third_objs['exit'].set_text(text_slovar.copy())
        rbut_slovar['positions'] = [250, 240]
        self.zero_objs['ok'] = RButton(rbut_slovar.copy())
        self.first_objs['ok'] = RButton(rbut_slovar.copy())
        self.sec_objs['ok'] = RButton(rbut_slovar.copy())
        self.third_objs['ok'] = RButton(rbut_slovar.copy())
        self.sec_objs['ok'].actived = False
        self.third_objs['ok'].actived = False
        text_slovar['text'] = 'ДАЛЕЕ'
        text_slovar['positions'] = (273, 244)
        self.zero_objs['ok'].set_text(text_slovar.copy())
        self.sec_objs['ok'].set_text(text_slovar.copy())
        self.first_objs['ok'].set_text(text_slovar.copy())
        text_slovar['text'] = 'ГОТОВО'
        text_slovar['positions'] = (266, 244)
        self.third_objs['ok'].set_text(text_slovar.copy())
        text_slovar['text_size'] = 25
        text_slovar['positions'] = (71, 168)
        text_slovar['indent'] = 146
        self.third_objs['keyboard'] = RKeyboard(key_slovar.copy(), text_slovar.copy())
        text_slovar['text_size'] = 35
        text_slovar['positions'] = (31, 158)
        text_slovar['text'] = 'нажми'
        self.sec_objs['input1'] = RInput(inp_slovar, text_slovar)
        text_slovar['positions'] = (241, 158)
        inp_slovar['positions'] = (230, 160)
        self.sec_objs['input2'] = RInput(inp_slovar, text_slovar)

    def print_field(self):
        self.win.blit(self.fld, (0, 0))

    def zero_screen(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in self.zero_objs:
            try:
                self.zero_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.zero_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.zero_objs['ok'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 1
            if self.zero_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4

    def first_screen(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in self.first_objs:
            try:
                self.first_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.first_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.first_objs['ok'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 1
            if self.first_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4

    def second_screen(self):
        self.equal()
        mouse_pos = pygame.mouse.get_pos()
        try:
            prosto_name = int(self.sec_objs['input1'].get_text())
            prosto_name2 = int(self.sec_objs['input2'].get_text())
            self.sec_objs['ok'].actived = True
            if prosto_name < 800 or prosto_name2 < 450:
                self.sec_objs['ok'].actived = False
        except Exception:
            self.sec_objs['ok'].actived = False
        for i in self.sec_objs:
            try:
                self.sec_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.sec_objs[i].draw()
        for event in pygame.event.get():
            if not(self.sec_objs['input2'].active):
                self.sec_objs['input1'].is_active(event, pygame.mouse.get_pos())
            if not(self.sec_objs['input1'].active):
                self.sec_objs['input2'].is_active(event, pygame.mouse.get_pos())
            self.sec_objs['input1'].input(event)
            self.sec_objs['input2'].input(event)
            if event.type == pygame.QUIT:
                return -1
            if self.sec_objs['ok'].is_tap(event, pygame.mouse.get_pos(), 1):
                self.screen_size = [int(self.sec_objs['input1'].get_text()), int(self.sec_objs['input2'].get_text())]
                return 1
            if self.sec_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4

    def third_screen(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in self.third_objs:
            try:
                self.third_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.third_objs[i].draw()
        if self.theme == -1:
            self.third_objs['keyboard'].set_default_animation([0, 1], 0)
            self.third_objs['ok'].actived = False
        else:
            self.third_objs['ok'].actived = True
            self.third_objs['keyboard'].set_default_animation([self.theme], 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.third_objs['ok'].is_tap(event, pygame.mouse.get_pos(), 1):
                SetFileAttributes('res/screen_sets.txt', 128)
                with open('res/screen_sets.txt', 'w') as f:
                    print(self.screen_size[0], file=f)
                    print(self.screen_size[1], file=f)
                    print(self.theme, file=f)
                SetFileAttributes('res/screen_sets.txt', 2)
                return 1
            if self.third_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4
            result = self.third_objs['keyboard'].taps(event, pygame.mouse.get_pos())
            if result[0]:
                if self.theme == result[1]:
                    self.theme = -1
                else:
                    self.theme = result[1]
                    if self.theme != -1:
                        self.third_objs['keyboard'].set_default_animation([0, 1], 0)
                        self.third_objs['keyboard'].set_default_animation([self.theme], 1)

    def equal(self):
        lmbd1 = lambda x: int(int(x) * 9 / 16)
        lmbd2 = lambda x: int(int(x) * 16 / 9)
        if self.sec_objs['input1'].active:
            try:
                length = lmbd1(self.sec_objs['input1'].get_text())
                self.sec_objs['input2'].new_text(str(length))
            except Exception:
                self.sec_objs['input2'].new_text('')
        if self.sec_objs['input2'].active:
            try:
                length = lmbd2(self.sec_objs['input2'].get_text())
                if lmbd1(length) == self.sec_objs['input2'].get_text():
                    self.sec_objs['input1'].new_text(str(length))
                else:
                    self.sec_objs['input1'].new_text(str(length + 1))
            except Exception:
                self.sec_objs['input1'].new_text('')
