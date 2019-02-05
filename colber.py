from project_R import *
import time


class MySprite(pygame.sprite.Sprite):
    def __init__(self, group, pos, image, click_image):
        super().__init__(group)
        self.no_image = image
        self.image = image
        self.click_image = click_image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.timer = 0

    def update(self, slovar):
        if 'event' in slovar:
            if self.rect.collidepoint(slovar['pos']):
                self.image = self.click_image
                self.timer = 1
                with open('res/colber/noname', 'w') as f:
                    f.write('1')
                return
            else:
                self.image = self.no_image
        else:
            if self.timer == 0:
                self.image = self.no_image
                self.timer += 1
            else:
                self.timer += 1
                self.timer = self.timer % 5
        with open('res/colber/noname', 'w') as f:
            f.write('0')
        return


class Colber:
    def __init__(self, size_master, win):
        self.win = win
        self.noname = 'menu'
        self.score = 0
        self.sc_click = 1
        self.sc_time = 0
        self.level = 1
        try:
            self.read_file()
        except Exception:
            pass
        self.time_flag = True
        self.time_check = 0
        self.field = size_master.transform(
            pygame.image.load('res/colber/field.png'), (1920, 1080))
        self.menu_objs = {}
        self.progress_objs = {}
        self.first_objs = {}
        self.menu_init(size_master)
        self.progress_init()
        self.first_init(size_master)

    def read_file(self):
        with open('res/colber_sets.txt', 'r') as f:
            vse = f.read().split('\n')
        self.level = int(vse[0])
        self.score = int(vse[1])
        self.sc_click = int(vse[2])
        self.sc_time = int(vse[3])

    def write_file(self):
        with open('res/colber_sets.txt', 'w') as f:
            print(self.level, file=f)
            print(self.score, file=f)
            print(self.sc_click, file=f)
            print(self.sc_time, file=f)

    def menu_init(self, size_master):
        self.field = size_master.transform(pygame.image.load('res/colber/field.png'), (1920, 1080))
        colors = [(255, 255, 255), (200, 10, 10), (255, 255, 255)]
        factor = size_master.get_factor()
        a0 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_off.png'), (600, 115))
        a1 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_on.png'), (600, 115))
        a2 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_on2.png'), (600, 115))
        text_slovar = {'positions': size_master.repos_and_resize((1320, 313)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf', 0.7),
                       'color': colors[0], 'text': 'ИГРАТЬ'}
        title_slovar = {'positions': size_master.repos_and_resize((0, 00)),
                        'win': self.win,
                        'font': 'res/fonts/Staatliches-Regular.ttf',
                        'text_size': size_master.resize_text(
                            'res/fonts/Staatliches-Regular.ttf'),
                        'color': colors[2], 'color2': colors[1],
                        'text': '"Название"',
                        'indent': size_master.resize_one(3)}
        rbut_slovar = {'positions': size_master.repos_and_resize((1320, 313)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((600, 115)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a1]]}
        self.menu_objs['title1'] = RTitle(title_slovar.copy())
        self.menu_objs['title1'].move_center(size_master.resize_one(1920))
        self.menu_objs['title1'].move_center_y(size_master.resize_one(250))
        self.menu_objs['play'] = RButton(rbut_slovar.copy())
        self.menu_objs['play'].set_text(text_slovar)
        self.menu_objs['play'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((1320, 483))
        text_slovar['text'] = 'ДОСТИЖЕНИЯ'
        text_slovar['positions'] = size_master.repos_and_resize((1320, 483))
        self.menu_objs['progress'] = RButton(rbut_slovar.copy())
        self.menu_objs['progress'].set_text(text_slovar)
        self.menu_objs['progress'].move_center_text()
        rbut_slovar['animations'] = [[a0], [a2]]
        rbut_slovar['positions'] = size_master.repos_and_resize((1320, 653))
        text_slovar['text'] = 'ВЫХОД'
        text_slovar['positions'] = size_master.repos_and_resize((1320, 653))
        self.menu_objs['exit'] = RButton(rbut_slovar.copy())
        self.menu_objs['exit'].set_text(text_slovar)
        self.menu_objs['exit'].move_center_text()

    def progress_init(self):
        pass

    def first_init(self, size_master):
        self.field = size_master.transform(
            pygame.image.load('res/colber/first/field.png'), (1920, 1080))
        pic0 = size_master.transform(
            pygame.image.load('res/colber/first/colb_no_click.png'), (720, 720))
        pic1 = size_master.transform(
            pygame.image.load('res/colber/first/colb_click.png'), (720, 720))
        pos = size_master.repos_and_resize((600, 130))
        self.first_sprites = pygame.sprite.Group()
        MySprite(self.first_sprites, pos, pic0, pic1)
        colors = [(255, 255, 255), (200, 10, 10), (255, 255, 255)]
        factor = size_master.get_factor()
        a0 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_off.png'), (600, 115))
        a1 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_on.png'), (600, 115))
        a3 = size_master.transform(
            pygame.image.load('res/colber/b_500_500_off.png'), (500, 500))
        a4 = size_master.transform(
            pygame.image.load('res/colber/b_500_500_on.png'), (500, 500))
        text_slovar = {'positions': size_master.repos_and_resize((0, 920)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf', 0.7),
                       'color': colors[0], 'text': 'НАЗАД'}
        text2_slovar = {'positions': size_master.repos_and_resize((10, 10)),
                      'win': self.win,
                      'font': 'res/fonts/RobotoSlab-Regular.ttf',
                      'text_size': size_master.resize_text(
                          'res/fonts/RobotoSlab-Regular.ttf', 0.7),
                      'color': colors[0], 'text': 'СЧЕТ:'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 920)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((600, 115)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a1]]}
        rbut2_slovar = {'positions': size_master.repos_and_resize((10, 350)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((500, 500)),
                       'tap_buts': (1, 3), 'animations': [[a3], [a4]]}
        self.first_objs['exit'] = RButton(rbut_slovar.copy())
        self.first_objs['exit'].set_text(text_slovar)
        self.first_objs['exit'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((1320, 920))
        text_slovar['text'] = 'ИДТИ ДАЛЬШЕ'
        text_slovar['positions'] = size_master.repos_and_resize((1320, 920))
        self.first_objs['cont'] = RButton(rbut_slovar.copy())
        self.first_objs['cont'].set_text(text_slovar)
        self.first_objs['cont'].move_center_text()
        self.first_objs['cont'].closed = True
        self.first_objs['click'] = RButton(rbut2_slovar.copy())
        rbut2_slovar['positions'] = size_master.repos_and_resize((1410, 350))
        self.first_objs['time'] = RButton(rbut2_slovar.copy())
        self.first_objs['t1'] = RText(text2_slovar.copy())
        text2_slovar['positions'] = size_master.repos_and_resize((10, 80))
        text2_slovar['text'] = str(self.score)
        self.first_objs['score'] = RText(text2_slovar.copy())
        text2_slovar['positions'] = size_master.repos_and_resize((1000, 10))
        text2_slovar['text'] = 'ДЛЯ ПЕРЕХОДА:'
        self.first_objs['t2'] = RText(text2_slovar.copy())
        self.first_objs['t2'].move_right(size_master.resize_one(910))
        text2_slovar['positions'] = size_master.repos_and_resize((1000, 80))
        text2_slovar['text'] = '40000'
        self.first_objs['t3'] = RText(text2_slovar.copy())
        self.first_objs['t3'].move_right(size_master.resize_one(910))


    def choose_lvl(self):
        if self.level == 1:
            return self.first()

    def draw_field(self):
        self.win.blit(self.field, (0, 0))

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
            if self.menu_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4
            if self.menu_objs['progress'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 2
            if self.menu_objs['play'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 1

    def progress(self):
        return

    def first(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.time_flag:
            self.time_flag = False
            self.time_check = time.time()
        time_now = time.time()
        if self.time_check <= time_now - 0.5:
            self.score += self.sc_time // 2
            self.time_check = time_now
            self.write_file()
        self.first_objs['score'].new_text(str(self.score))
        self.first_sprites.update({})
        for i in self.first_objs:
            try:
                self.first_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.first_objs[i].draw()
        self.first_sprites.draw(self.win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.first_sprites.update({'pos':mouse_pos, 'event':0})
                with open('res/colber/noname', 'r') as f:
                    result = f.read()
                    if result == '1':
                        self.score += self.sc_click
            if self.first_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                self.time_flag = True
                return 4