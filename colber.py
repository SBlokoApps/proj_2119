from project_R import *
import time


class MySprite(pygame.sprite.Sprite):
    def __init__(self, group, pos, image, image2, click_image, click_image2):
        super().__init__(group)
        self.img = [click_image, click_image2]
        self.no_img = [image, image2]
        self.flag = 0
        self.image = image
        self.click_image = click_image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.timer = 0
        self.anim_time = 0
        self.tap = False

    def anim_update(self):
        if self.anim_time in range(5):
            self.flag = 0
            self.anim_time += 1
        elif self.anim_time in range(5, 10):
            self.flag = 1
            self.anim_time += 1
        else:
            self.flag = 0
            self.anim_time = 0

    def update(self, slovar):
        self.anim_update()
        if 'event' in slovar:
            if self.rect.collidepoint(slovar['pos']):
                with open('res/colber/noname', 'w') as f:
                    f.write('1')
                self.timer = 1
                self.image = self.img[self.flag]
                return
            else:
                self.timer = 0
                self.image = self.no_img[self.flag]
        else:
            if self.timer == 0:
                self.image = self.no_img[self.flag]
            else:
                self.timer += 1
                self.timer = self.timer % 5
                self.image = self.img[self.flag]
        with open('res/colber/noname', 'w') as f:
            f.write('0')
        return


class HP(pygame.sprite.Sprite):
    def __init__(self, group, pos, image1, image2, image3, maxhp, noimg):
        super().__init__(group)
        self.img = [image1, image2, image3, noimg]
        self.image = image1
        self.hp = maxhp
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def resize(self, new_hp):
        x = int(self.image.get_width() * (new_hp / self.hp))
        y = self.image.get_height()
        self.image = pygame.transform.scale(self.image, [x, y])

    def reimage(self, new_hp):
        x = new_hp / self.hp
        if x <= 0:
            self.image = self.img[3]
        elif x <= 0.25:
            self.image = self.img[2]
        elif x <= 0.5:
            self.image = self.img[1]
        else:
            self.image = self.img[0]

    def update(self, slovar):
        if 'new_hp' in slovar:
            self.reimage(slovar['new_hp'])
            self.resize(slovar['new_hp'])
        return


class Colber:
    def __init__(self, size_master, win):
        self.win = win
        self.score = 0
        self.sc_click = 1
        self.sc_time = 0
        self.level = 1
        self.c_bought = [[0, 10], [0, 100], [0, 1000], [0, 5000], [0, 10000]]
        self.c_effect = [1, 10, 25, 50, 100]
        self.t_bought = [[0, 50], [0, 500], [0, 1000], [0, 10000], [0, 50000]]
        self.t_effect = [2, 10, 25, 100, 400]
        self.all_score = 0
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
        self.fs_click_objs = {}
        self.fs_time_objs = {}
        self.sec_objs = {}
        self.ss_click_objs = {}
        self.ss_time_objs = {}
        self.menu_init(size_master)
        self.progress_init()
        self.first_init(size_master)
        self.fs_click_init(size_master)
        self.fs_time_init(size_master)
        self.sec_init(size_master)
        self.ss_click_init(size_master)
        self.ss_time_init(size_master)
        self.sm = size_master

    def new_level(self, num):
        if num == 2:
            self.level = 2
            self.score = 0
            self.all_score = 0
            self.sc_click = 1
            self.sc_time = 0
            self.c_bought = [[0, 10], [0, 150], [0, 1500], [0, 10000],
                             [0, 10000]]
            self.c_effect = [2, 15, 50, 100, 1000]
            self.t_bought = [[0, 50], [0, 550], [0, 1500], [0, 15000],
                             [0, 55000]]
            self.t_effect = [2, 15, 50, 150, 2000]
            poses1 = [70 + 370 * i for i in range(5)]
            for ii in range(5):
                self.ss_click_objs['c_items'].list[ii].new_text(
                    str(self.c_bought[ii][1]))
                self.ss_click_objs['c_items'].list[
                    ii].pos = self.sm.repos_and_resize([poses1[ii], 470])
                self.ss_click_objs['c_items'].list[ii].move_center(
                    self.sm.resize_one(300))
                self.ss_click_objs['c_items2'].list[ii].new_text(
                    str(self.c_bought[ii][0]))
                self.ss_click_objs['c_items2'].list[
                    ii].pos = self.sm.repos_and_resize([poses1[ii], 570])
                self.ss_click_objs['c_items2'].list[ii].move_center(
                    self.sm.resize_one(300))
        self.write_file()

    def read_file(self):
        with open('res/colber_sets.txt', 'r') as f:
            vse = f.read().split('\n')
        self.level = int(vse[0])
        self.score = int(vse[1])
        self.sc_click = int(vse[2])
        self.sc_time = int(vse[3])
        for i in range(5):
            self.c_bought[i] = [int(aa) for aa in vse[4 + i].split()]
        for i in range(5):
            self.t_bought[i] = [int(aa) for aa in vse[9 + i].split()]
        self.all_score = int(vse[14])

    def write_file(self):
        with open('res/colber_sets.txt', 'w') as f:
            bought = [str(i[0]) + ' ' + str(i[1]) for i in self.c_bought]
            bought2 = [str(i[0]) + ' ' + str(i[1]) for i in self.t_bought]
            print(self.level, file=f)
            print(self.score, file=f)
            print(self.sc_click, file=f)
            print(self.sc_time, file=f)
            for i in range(5):
                print(bought[i], file=f)
            for i in range(5):
                print(bought2[i], file=f)
            print(self.all_score, file=f)

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

    def fs_click_init(self, size_master):
        self.field = size_master.transform(
            pygame.image.load('res/colber/first/field.png'), (1920, 1080))
        colors = [(255, 255, 255), (200, 10, 10), (255, 255, 255)]
        factor = size_master.get_factor()
        a0 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_off.png'), (600, 115))
        a1 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_on.png'), (600, 115))
        a2 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_off.png'), (300, 600))
        a3 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_on.png'),
            (300, 600))
        a4 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_on2.png'),
            (300, 600))
        text_slovar = {'positions': size_master.repos_and_resize((0, 920)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf', 0.7),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 920)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((600, 115)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a1]]}
        rkeyb_slovar = {'positions': size_master.repos_and_resize((70, 100)),
                        'tap_buts': (1, 3),
                        'size': size_master.repos_and_resize((300, 600)),
                        'win': self.win,
                        'horizontal': True, 'indent': size_master.resize_one(70), 'kolvo': 5,
                        'texts': ['+' + str(i) for i in self.c_effect],
                        'animations': [[a2], [a3], [a4]]}
        rkeyb2_slovar = {
            'positions': size_master.repos_and_resize((70, 120)),
            'win': self.win,
            'font': 'res/fonts/RobotoSlab-Regular.ttf',
            'text_size': size_master.resize_text(
                'res/fonts/RobotoSlab-Regular.ttf', 0.7),
            'color': colors[0], 'indent': size_master.resize_one(370)}
        self.fs_click_objs['keyb'] = RKeyboard(rkeyb_slovar.copy(), rkeyb2_slovar.copy())
        self.fs_click_objs['keyb'].move_center_text()
        self.fs_click_objs['exit'] = RButton(rbut_slovar.copy())
        self.fs_click_objs['exit'].set_text(text_slovar)
        self.fs_click_objs['exit'].move_center_text()
        self.fs_click_objs['c_items'] = RItemList()
        self.fs_click_objs['c_items2'] = RItemList()
        poses1 = [70 + 370*i for i in range(5)]
        for i in range(5):
            text_slovar['positions'] = size_master.repos_and_resize((poses1[i], 470))
            text_slovar['text'] = str(self.c_bought[i][1])
            self.fs_click_objs['c_items'].append(RText(text_slovar.copy()))
            self.fs_click_objs['c_items'].list[i].move_center(size_master.resize_one(300))
        for i in range(5):
            text_slovar['positions'] = size_master.repos_and_resize((poses1[i], 570))
            text_slovar['text'] = str(self.c_bought[i][0])
            self.fs_click_objs['c_items2'].append(RText(text_slovar.copy()))
            self.fs_click_objs['c_items2'].list[i].move_center(size_master.resize_one(300))

    def first_init(self, size_master):
        self.field = size_master.transform(
            pygame.image.load('res/colber/first/field.png'), (1920, 1080))
        pic0 = size_master.transform(
            pygame.image.load('res/colber/first/colb_noclick.png'), (720, 720))
        pic00 = size_master.transform(
            pygame.image.load('res/colber/first/colb_noclick2.png'),
            (720, 720))
        pic1 = size_master.transform(
            pygame.image.load('res/colber/first/colb_click.png'), (720, 720))
        pic11 = size_master.transform(
            pygame.image.load('res/colber/first/colb_click2.png'), (720, 720))
        a0 = size_master.transform(
            pygame.image.load('res/colber/first/b_600_115_off.png'), (600, 115))
        a1 = size_master.transform(
            pygame.image.load('res/colber/first/b_600_115_on.png'), (600, 115))
        a3 = size_master.transform(
            pygame.image.load('res/colber/first/cs_off.png'), (500, 500))
        a4 = size_master.transform(
            pygame.image.load('res/colber/first/сs_on.png'), (500, 500))
        a5 = size_master.transform(
            pygame.image.load('res/colber/first/ts_off.png'), (500, 500))
        a6 = size_master.transform(
            pygame.image.load('res/colber/first/ts_on.png'), (500, 500))
        h1 = size_master.transform(
            pygame.image.load('res/colber/first/hp1.png'), (500, 40))
        h2 = size_master.transform(
            pygame.image.load('res/colber/first/hp2.png'), (500, 40))
        h3 = size_master.transform(
            pygame.image.load('res/colber/first/hp3.png'), (500, 40))
        noh = size_master.transform(
            pygame.image.load('res/colber/first/nohp.png'), (500, 40))
        pos = size_master.repos_and_resize((600, 130))
        pos2 = size_master.repos_and_resize((710, 50))
        self.first_sprites = pygame.sprite.Group()
        MySprite(self.first_sprites, pos, pic0, pic00, pic1, pic11)
        HP(self.first_sprites, pos2, h1, h2, h3, 1000000, noh)
        colors = [(255, 255, 255), (200, 10, 10), (255, 255, 255)]
        factor = size_master.get_factor()
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
        rbut_slovar['invisible'] = 0
        rbut_slovar['positions'] = size_master.repos_and_resize((1320, 920))
        text_slovar['text'] = 'ИДТИ ДАЛЬШЕ'
        text_slovar['positions'] = size_master.repos_and_resize((1320, 920))
        self.first_objs['cont'] = RButton(rbut_slovar.copy())
        self.first_objs['cont'].set_text(text_slovar)
        self.first_objs['cont'].move_center_text()
        self.first_objs['cont'].closed = True
        self.first_objs['click'] = RButton(rbut2_slovar.copy())
        rbut2_slovar['positions'] = size_master.repos_and_resize((1410, 350))
        rbut2_slovar['animations'] = [[a5], [a6]]
        self.first_objs['time'] = RButton(rbut2_slovar.copy())
        self.first_objs['t1'] = RText(text2_slovar.copy())
        text2_slovar['positions'] = size_master.repos_and_resize((10, 80))
        text2_slovar['text'] = str(self.score)
        self.first_objs['score'] = RText(text2_slovar.copy())
        text2_slovar['positions'] = size_master.repos_and_resize((1000, 10))
        text3_slovar = {'positions': size_master.repos_and_resize((120, 550)),
                        'win': self.win,
                        'font': 'res/fonts/RobotoSlab-Regular.ttf',
                        'text_size': size_master.resize_text(
                            'res/fonts/RobotoSlab-Regular.ttf', 1),
                        'color': colors[1], 'text': '0'}
        self.first_objs['uron'] = RText(text3_slovar.copy())
        text3_slovar['positions'] = size_master.repos_and_resize((1600, 550))
        self.first_objs['usec'] = RText(text3_slovar.copy())
        text2_slovar['text'] = 'ОСТАЛОСЬ:'
        self.first_objs['t2'] = RText(text2_slovar.copy())
        self.first_objs['t2'].move_right(size_master.resize_one(910))
        text2_slovar['positions'] = size_master.repos_and_resize((1000, 80))
        text2_slovar['text'] = '1000000'
        self.first_objs['t3'] = RText(text2_slovar.copy())
        self.first_objs['t3'].move_right(size_master.resize_one(910))

    def fs_time_init(self, size_master):
        self.field = size_master.transform(
            pygame.image.load('res/colber/first/field.png'), (1920, 1080))
        colors = [(255, 255, 255), (200, 10, 10), (255, 255, 255)]
        factor = size_master.get_factor()
        a0 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_off.png'), (600, 115))
        a1 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_on.png'), (600, 115))
        a2 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_off.png'), (300, 600))
        a3 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_on.png'),
            (300, 600))
        a4 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_on2.png'),
            (300, 600))
        text_slovar = {'positions': size_master.repos_and_resize((0, 920)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf', 0.7),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 920)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((600, 115)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a1]]}
        rkeyb_slovar = {'positions': size_master.repos_and_resize((70, 100)),
                        'tap_buts': (1, 3),
                        'size': size_master.repos_and_resize((300, 600)),
                        'win': self.win,
                        'horizontal': True, 'indent': size_master.resize_one(70), 'kolvo': 5,
                        'texts': ['+' + str(i) for i in self.t_effect],
                        'animations': [[a2], [a3], [a4]]}
        rkeyb2_slovar = {
            'positions': size_master.repos_and_resize((70, 120)),
            'win': self.win,
            'font': 'res/fonts/RobotoSlab-Regular.ttf',
            'text_size': size_master.resize_text(
                'res/fonts/RobotoSlab-Regular.ttf', 0.7),
            'color': colors[0], 'indent': size_master.resize_one(370)}
        self.fs_time_objs['keyb'] = RKeyboard(rkeyb_slovar.copy(), rkeyb2_slovar.copy())
        self.fs_time_objs['keyb'].move_center_text()
        self.fs_time_objs['exit'] = RButton(rbut_slovar.copy())
        self.fs_time_objs['exit'].set_text(text_slovar)
        self.fs_time_objs['exit'].move_center_text()
        self.fs_time_objs['t_items'] = RItemList()
        self.fs_time_objs['t_items2'] = RItemList()
        poses1 = [70 + 370*i for i in range(5)]
        for i in range(5):
            text_slovar['positions'] = size_master.repos_and_resize((poses1[i], 470))
            text_slovar['text'] = str(self.t_bought[i][1])
            self.fs_time_objs['t_items'].append(RText(text_slovar.copy()))
            self.fs_time_objs['t_items'].list[i].move_center(size_master.resize_one(300))
        for i in range(5):
            text_slovar['positions'] = size_master.repos_and_resize((poses1[i], 570))
            text_slovar['text'] = str(self.t_bought[i][0])
            self.fs_time_objs['t_items2'].append(RText(text_slovar.copy()))
            self.fs_time_objs['t_items2'].list[i].move_center(size_master.resize_one(300))

    def ss_click_init(self, size_master):
        self.field = size_master.transform(
            pygame.image.load('res/colber/first/field.png'), (1920, 1080))
        colors = [(255, 255, 255), (200, 10, 10), (255, 255, 255)]
        factor = size_master.get_factor()
        a0 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_off.png'), (600, 115))
        a1 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_on.png'), (600, 115))
        a2 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_off.png'), (300, 600))
        a3 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_on.png'),
            (300, 600))
        a4 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_on2.png'),
            (300, 600))
        text_slovar = {'positions': size_master.repos_and_resize((0, 920)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf', 0.7),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 920)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((600, 115)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a1]]}
        rkeyb_slovar = {'positions': size_master.repos_and_resize((70, 100)),
                        'tap_buts': (1, 3),
                        'size': size_master.repos_and_resize((300, 600)),
                        'win': self.win,
                        'horizontal': True, 'indent': size_master.resize_one(70), 'kolvo': 5,
                        'texts': ['+' + str(i) for i in self.c_effect],
                        'animations': [[a2], [a3], [a4]]}
        rkeyb2_slovar = {
            'positions': size_master.repos_and_resize((70, 120)),
            'win': self.win,
            'font': 'res/fonts/RobotoSlab-Regular.ttf',
            'text_size': size_master.resize_text(
                'res/fonts/RobotoSlab-Regular.ttf', 0.7),
            'color': colors[0], 'indent': size_master.resize_one(370)}
        self.ss_click_objs['keyb'] = RKeyboard(rkeyb_slovar.copy(), rkeyb2_slovar.copy())
        self.ss_click_objs['keyb'].move_center_text()
        self.ss_click_objs['exit'] = RButton(rbut_slovar.copy())
        self.ss_click_objs['exit'].set_text(text_slovar)
        self.ss_click_objs['exit'].move_center_text()
        self.ss_click_objs['c_items'] = RItemList()
        self.ss_click_objs['c_items2'] = RItemList()
        poses1 = [70 + 370*i for i in range(5)]
        for i in range(5):
            text_slovar['positions'] = size_master.repos_and_resize((poses1[i], 470))
            text_slovar['text'] = str(self.c_bought[i][1])
            self.ss_click_objs['c_items'].append(RText(text_slovar.copy()))
            self.ss_click_objs['c_items'].list[i].move_center(size_master.resize_one(300))
        for i in range(5):
            text_slovar['positions'] = size_master.repos_and_resize((poses1[i], 570))
            text_slovar['text'] = str(self.c_bought[i][0])
            self.ss_click_objs['c_items2'].append(RText(text_slovar.copy()))
            self.ss_click_objs['c_items2'].list[i].move_center(size_master.resize_one(300))

    def sec_init(self, size_master):
        self.field = size_master.transform(
            pygame.image.load('res/colber/first/field.png'), (1920, 1080))
        pic0 = size_master.transform(
            pygame.image.load('res/colber/first/colb_noclick.png'), (720, 720))
        pic00 = size_master.transform(
            pygame.image.load('res/colber/first/colb_noclick.png'),
            (720, 720))
        pic1 = size_master.transform(
            pygame.image.load('res/colber/first/colb_click.png'), (720, 720))
        pic11 = size_master.transform(
            pygame.image.load('res/colber/first/colb_click2.png'), (720, 720))
        pos = size_master.repos_and_resize((600, 130))
        self.sec_sprites = pygame.sprite.Group()
        MySprite(self.sec_sprites, pos, pic0, pic00, pic1, pic11)
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
        self.sec_objs['exit'] = RButton(rbut_slovar.copy())
        self.sec_objs['exit'].set_text(text_slovar)
        self.sec_objs['exit'].move_center_text()
        rbut_slovar['positions'] = size_master.repos_and_resize((1320, 920))
        text_slovar['text'] = 'ИДТИ ДАЛЬШЕ'
        text_slovar['positions'] = size_master.repos_and_resize((1320, 920))
        self.sec_objs['cont'] = RButton(rbut_slovar.copy())
        self.sec_objs['cont'].set_text(text_slovar)
        self.sec_objs['cont'].move_center_text()
        self.sec_objs['cont'].closed = True
        self.sec_objs['click'] = RButton(rbut2_slovar.copy())
        rbut2_slovar['positions'] = size_master.repos_and_resize((1410, 350))
        self.sec_objs['time'] = RButton(rbut2_slovar.copy())
        self.sec_objs['t1'] = RText(text2_slovar.copy())
        text2_slovar['positions'] = size_master.repos_and_resize((10, 80))
        text2_slovar['text'] = str(self.score)
        self.sec_objs['score'] = RText(text2_slovar.copy())
        text2_slovar['positions'] = size_master.repos_and_resize((1000, 10))
        text2_slovar['text'] = 'ДЛЯ ПЕРЕХОДА:'
        self.sec_objs['t2'] = RText(text2_slovar.copy())
        self.sec_objs['t2'].move_right(size_master.resize_one(910))
        text2_slovar['positions'] = size_master.repos_and_resize((1000, 80))
        text2_slovar['text'] = '10000000'
        self.sec_objs['t3'] = RText(text2_slovar.copy())
        self.sec_objs['t3'].move_right(size_master.resize_one(910))

    def ss_time_init(self, size_master):
        self.field = size_master.transform(
            pygame.image.load('res/colber/first/field.png'), (1920, 1080))
        colors = [(255, 255, 255), (200, 10, 10), (255, 255, 255)]
        factor = size_master.get_factor()
        a0 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_off.png'), (600, 115))
        a1 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_on.png'), (600, 115))
        a2 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_off.png'), (300, 600))
        a3 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_on.png'),
            (300, 600))
        a4 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_on2.png'),
            (300, 600))
        text_slovar = {'positions': size_master.repos_and_resize((0, 920)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf', 0.7),
                       'color': colors[0], 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 920)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((600, 115)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a1]]}
        rkeyb_slovar = {'positions': size_master.repos_and_resize((70, 100)),
                        'tap_buts': (1, 3),
                        'size': size_master.repos_and_resize((300, 600)),
                        'win': self.win,
                        'horizontal': True, 'indent': size_master.resize_one(70), 'kolvo': 5,
                        'texts': ['+' + str(i) for i in self.c_effect],
                        'animations': [[a2], [a3], [a4]]}
        rkeyb2_slovar = {
            'positions': size_master.repos_and_resize((70, 120)),
            'win': self.win,
            'font': 'res/fonts/RobotoSlab-Regular.ttf',
            'text_size': size_master.resize_text(
                'res/fonts/RobotoSlab-Regular.ttf', 0.7),
            'color': colors[0], 'indent': size_master.resize_one(370)}
        self.ss_time_objs['keyb'] = RKeyboard(rkeyb_slovar.copy(), rkeyb2_slovar.copy())
        self.ss_time_objs['keyb'].move_center_text()
        self.ss_time_objs['exit'] = RButton(rbut_slovar.copy())
        self.ss_time_objs['exit'].set_text(text_slovar)
        self.ss_time_objs['exit'].move_center_text()
        self.ss_time_objs['t_items'] = RItemList()
        self.ss_time_objs['t_items2'] = RItemList()
        poses1 = [70 + 370*i for i in range(5)]
        for i in range(5):
            text_slovar['positions'] = size_master.repos_and_resize((poses1[i], 470))
            text_slovar['text'] = str(self.t_bought[i][1])
            self.ss_time_objs['t_items'].append(RText(text_slovar.copy()))
            self.ss_time_objs['t_items'].list[i].move_center(size_master.resize_one(300))
        for i in range(5):
            text_slovar['positions'] = size_master.repos_and_resize((poses1[i], 570))
            text_slovar['text'] = str(self.t_bought[i][0])
            self.ss_time_objs['t_items2'].append(RText(text_slovar.copy()))
            self.ss_time_objs['t_items2'].list[i].move_center(size_master.resize_one(300))

    def choose_lvl(self):
        if self.level == 1:
            return self.first()
        if self.level == 2:
            try:
                del self.first_objs
            except Exception:
                pass
            return self.sec()

    def shop_c(self):
        if self.level == 1:
            return self.fs_click()
        if self.level == 2:
            return self.ss_click()

    def shop_t(self):
        if self.level == 1:
            return self.fs_time()
        if self.level == 2:
            return self.ss_time()

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
        self.first_objs['uron'].new_text(str(self.sc_click))
        self.first_objs['usec'].new_text(str(self.sc_time))
        if self.time_flag:
            self.time_flag = False
            self.time_check = time.time()
        time_now = time.time()
        if self.time_check <= time_now - 0.5:
            self.score += self.sc_time // 2
            self.all_score += self.sc_time // 2
            self.time_check = time_now
            self.write_file()
        if self.all_score >= 1000000:
            self.first_objs['t3'].new_text('0')
            self.first_objs['cont'].closed = False
            self.first_objs['cont'].inv = False
        else:
            self.first_objs['t3'].new_text(str(1000000 - self.all_score))
        self.first_objs['score'].new_text(str(self.score))
        self.first_sprites.update({'new_hp': 1000000 - self.all_score})
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
                        self.all_score += self.sc_click
            if self.first_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                self.time_flag = True
                return 4
            if self.first_objs['click'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 1001
            if self.first_objs['time'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 1002
            if self.first_objs['cont'].is_tap(event, pygame.mouse.get_pos(), 1):
                self.new_level(2)
                return 1

    def fs_click(self):
        mouse_pos = pygame.mouse.get_pos()
        time_now = time.time()
        if self.time_check <= time_now - 0.5:
            self.score += self.sc_time // 2
            self.time_check = time_now
            self.write_file()
        for i in range(5):
            if self.score < self.c_bought[i][1]:
                self.fs_click_objs['keyb'].buts[i].set_animation(0)
                self.fs_click_objs['keyb'].buts[i].closed = True
            else:
                self.fs_click_objs['keyb'].buts[i].closed = False
        for i in self.fs_click_objs:
            try:
                self.fs_click_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.fs_click_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.fs_click_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4
            tap = self.fs_click_objs['keyb'].taps(event,
                                                     pygame.mouse.get_pos(),
                                                     animation=2, delay=3)
            if tap[0]:
                num = tap[1]
                poses1 = [70 + 370 * i for i in range(5)]
                sc = self.c_bought[num][1]
                self.score -= sc
                if sc * 0.05 >= 1:
                    self.c_bought[num][1] += sc * 0.05
                    self.c_bought[num][1] = int(self.c_bought[num][1])
                else:
                    self.c_bought[num][1] += 1
                self.c_bought[num][0] += 1
                self.sc_click += self.c_effect[num]
                self.fs_click_objs['c_items'].list[num].new_text(str(self.c_bought[num][1]))
                self.fs_click_objs['c_items'].list[num].pos = self.sm.repos_and_resize([poses1[num], 470])
                self.fs_click_objs['c_items'].list[num].move_center(self.sm.resize_one(300))
                self.fs_click_objs['c_items2'].list[num].new_text(str(self.c_bought[num][0]))
                self.fs_click_objs['c_items2'].list[num].pos = self.sm.repos_and_resize([poses1[num], 570])
                self.fs_click_objs['c_items2'].list[num].move_center(self.sm.resize_one(300))

    def fs_time(self):
        mouse_pos = pygame.mouse.get_pos()
        time_now = time.time()
        if self.time_check <= time_now - 0.5:
            self.score += self.sc_time // 2
            self.time_check = time_now
            self.write_file()
        for i in range(5):
            if self.score < self.t_bought[i][1]:
                self.fs_time_objs['keyb'].buts[i].set_animation(0)
                self.fs_time_objs['keyb'].buts[i].closed = True
            else:
                self.fs_time_objs['keyb'].buts[i].closed = False
        for i in self.fs_time_objs:
            try:
                self.fs_time_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.fs_time_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.fs_time_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4
            tap = self.fs_time_objs['keyb'].taps(event,
                                                     pygame.mouse.get_pos(),
                                                     animation=2, delay=3)
            if tap[0]:
                num = tap[1]
                poses1 = [70 + 370 * i for i in range(5)]
                sc = self.t_bought[num][1]
                self.score -= sc
                if sc * 0.05 >= 1:
                    self.t_bought[num][1] += sc * 0.05
                    self.t_bought[num][1] = int(self.t_bought[num][1])
                else:
                    self.t_bought[num][1] += 1
                self.t_bought[num][0] += 1
                self.sc_time += self.t_effect[num]
                self.fs_time_objs['t_items'].list[num].new_text(str(self.t_bought[num][1]))
                self.fs_time_objs['t_items'].list[num].pos = self.sm.repos_and_resize([poses1[num], 470])
                self.fs_time_objs['t_items'].list[num].move_center(self.sm.resize_one(300))
                self.fs_time_objs['t_items2'].list[num].new_text(str(self.t_bought[num][0]))
                self.fs_time_objs['t_items2'].list[num].pos = self.sm.repos_and_resize([poses1[num], 570])
                self.fs_time_objs['t_items2'].list[num].move_center(self.sm.resize_one(300))

    def sec(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.time_flag:
            self.time_flag = False
            self.time_check = time.time()
        time_now = time.time()
        if self.time_check <= time_now - 0.5:
            self.score += self.sc_time // 2
            self.time_check = time_now
            self.write_file()
        if self.score >= 1000000:
            self.sec_objs['cont'].closed = False
        else:
            self.sec_objs['cont'].closed = True
        self.sec_objs['score'].new_text(str(self.score))
        self.sec_sprites.update({})
        for i in self.sec_objs:
            try:
                self.sec_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.sec_objs[i].draw()
        self.sec_sprites.draw(self.win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sec_sprites.update({'pos':mouse_pos, 'event':0})
                with open('res/colber/noname', 'r') as f:
                    result = f.read()
                    if result == '1':
                        self.score += self.sc_click
            if self.sec_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                self.time_flag = True
                return 4
            if self.sec_objs['click'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 1001
            if self.sec_objs['time'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 1002

    def ss_click(self):
        mouse_pos = pygame.mouse.get_pos()
        time_now = time.time()
        if self.time_check <= time_now - 0.5:
            self.score += self.sc_time // 2
            self.time_check = time_now
            self.write_file()
        for i in range(5):
            if self.score < self.c_bought[i][1]:
                self.ss_click_objs['keyb'].buts[i].set_animation(0)
                self.ss_click_objs['keyb'].buts[i].closed = True
            else:
                self.ss_click_objs['keyb'].buts[i].closed = False
        for i in self.ss_click_objs:
            try:
                self.ss_click_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.ss_click_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.ss_click_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4
            tap = self.ss_click_objs['keyb'].taps(event,
                                                     pygame.mouse.get_pos(),
                                                     animation=2, delay=3)
            if tap[0]:
                num = tap[1]
                poses1 = [70 + 370 * i for i in range(5)]
                sc = self.c_bought[num][1]
                self.score -= sc
                if sc * 0.05 >= 1:
                    self.c_bought[num][1] += sc * 0.05
                    self.c_bought[num][1] = int(self.c_bought[num][1])
                else:
                    self.c_bought[num][1] += 1
                self.c_bought[num][0] += 1
                self.sc_click += self.c_effect[num]
                self.ss_click_objs['c_items'].list[num].new_text(str(self.c_bought[num][1]))
                self.ss_click_objs['c_items'].list[num].pos = self.sm.repos_and_resize([poses1[num], 470])
                self.ss_click_objs['c_items'].list[num].move_center(self.sm.resize_one(300))
                self.ss_click_objs['c_items2'].list[num].new_text(str(self.c_bought[num][0]))
                self.ss_click_objs['c_items2'].list[num].pos = self.sm.repos_and_resize([poses1[num], 570])
                self.ss_click_objs['c_items2'].list[num].move_center(self.sm.resize_one(300))

    def ss_time(self):
        mouse_pos = pygame.mouse.get_pos()
        time_now = time.time()
        if self.time_check <= time_now - 0.5:
            self.score += self.sc_time // 2
            self.time_check = time_now
            self.write_file()
        for i in range(5):
            if self.score < self.t_bought[i][1]:
                self.ss_time_objs['keyb'].buts[i].set_animation(0)
                self.ss_time_objs['keyb'].buts[i].closed = True
            else:
                self.ss_time_objs['keyb'].buts[i].closed = False
        for i in self.ss_time_objs:
            try:
                self.ss_time_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.ss_time_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.ss_time_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4
            tap = self.ss_time_objs['keyb'].taps(event,
                                                     pygame.mouse.get_pos(),
                                                     animation=2, delay=3)
            if tap[0]:
                num = tap[1]
                poses1 = [70 + 370 * i for i in range(5)]
                sc = self.t_bought[num][1]
                self.score -= sc
                if sc * 0.05 >= 1:
                    self.t_bought[num][1] += sc * 0.05
                    self.t_bought[num][1] = int(self.t_bought[num][1])
                else:
                    self.t_bought[num][1] += 1
                self.t_bought[num][0] += 1
                self.sc_time += self.t_effect[num]
                self.ss_time_objs['t_items'].list[num].new_text(str(self.t_bought[num][1]))
                self.ss_time_objs['t_items'].list[num].pos = self.sm.repos_and_resize([poses1[num], 470])
                self.ss_time_objs['t_items'].list[num].move_center(self.sm.resize_one(300))
                self.ss_time_objs['t_items2'].list[num].new_text(str(self.t_bought[num][0]))
                self.ss_time_objs['t_items2'].list[num].pos = self.sm.repos_and_resize([poses1[num], 570])
                self.ss_time_objs['t_items2'].list[num].move_center(self.sm.resize_one(300))