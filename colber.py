from project_R import *
import time
import random


# Класс спрайта-частицы
class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    def __init__(self, pos, dx, dy, group, sm, a, b, c, d, e, img):
        super().__init__(group)
        sizes = [(scale, scale) for scale in (c, d, e)]
        self.image = pygame.transform.scale(img, random.choice(sizes))
        self.rect = self.image.get_rect()
        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos
        # гравитация будет одинаковой (значение константы)
        self.gravity = 3
        self.size_master = sm
        self.a = a
        self.b = b

    def update(self, noname):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect((0, 0, self.a, self.b)):
            self.kill()


# Класс спрайта-колбы
class MySprite(pygame.sprite.Sprite):
    def __init__(self, group, pos, image, image2, click_image, click_image2,
                 size_mas):  # На входе разные картинки анимации, группа
        super().__init__(group)
        # Загружаем нужную анимацию
        self.img = [click_image, click_image2]
        self.no_img = [image, image2]
        # Важные переменные для спрайта
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        # Таймер анимации нажатия - некоторое время после нажатия должна
        # отображаться именно анимация нажатия
        self.timer = 0
        # Таймер и флаг-номер чередования анимаций
        self.flag = 0
        self.anim_time = 0
        # Запомним в памяти несколько переменных для создания частиц
        self.size_master = size_mas
        self.group = group
        self.part_img = pygame.image.load("res/colber/part.png")
        self.part_vars = [self.size_master.resize_one(1920),
                          self.size_master.resize_one(1080),
                          self.size_master.resize_one(20),
                          self.size_master.resize_one(30),
                          self.size_master.resize_one(15)]

    # Метод чередования анимации: колба не просто стоит на месте,
    # а меняется со временем
    def anim_update(self):
        # Первые 5 кадров - картинка 0
        if self.anim_time in range(8):
            self.flag = 0
            self.anim_time += 1
        # Вторые 5 кадров картинка 1
        elif self.anim_time in range(8, 16):
            self.flag = 1
            self.anim_time += 1
        # Потом сброс и заново
        else:
            self.flag = 0
            self.anim_time = 0

    # Метод обновления спрайта, в словаре можно подать ключ события
    def update(self, slovar):
        # Сначала обновим анимацию
        self.anim_update()
        # Если в словаре ключ события, проверяем его на клик по колбе
        if 'event' in slovar:
            if self.rect.collidepoint(slovar['pos']):
                # Надо записать в особый файл, что произошел клик
                with open('res/colber/noname', 'w') as f:
                    f.write('1')
                # Меняем анимацию, запускаем таймер, создаем частицы
                self.timer = 1
                self.image = self.img[self.flag]
                self.create_particles(slovar['pos'])
                # Вернем функцию, чтобы не выполнить остальное
                return
        # Иначе - просто обновление анимации с проверкой по таймеру.
        # Таймер 0 означает, что он закончился - надо сменить картинку
        # на некликнутую. Иначе - обновим таймер по остатку деления на 5 -
        # так легче следить за его отключением
        if self.timer == 0:
            self.image = self.no_img[self.flag]
        else:
            self.timer += 1
            self.timer = self.timer % 5
            self.image = self.img[self.flag]
        # Запишем в файлик, что не было нажатия
        with open('res/colber/noname', 'w') as f:
            f.write('0')

    # Метод создания частиц
    def create_particles(self, pos):
        # количество создаваемых частиц
        particle_count = 6
        # возможные скорости
        numbers = range(-5, 6)
        for i in range(particle_count):
            Particle(pos, random.choice(numbers), random.choice(numbers),
                     self.group, self.size_master,
                     *self.part_vars, self.part_img)


# Класс полоски жизней
class HP(pygame.sprite.Sprite):
    # На входе разные картинки анимации, группа
    def __init__(self, group, pos, image1, image2, image3, maxhp):
        super().__init__(group)
        # Загружаем нужную анимацию
        self.img = [image1, image2, image3]
        self.image = image1
        # Текущее количество жизней
        self.hp = maxhp
        # Важные для спрайтов переменные
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.x = self.image.get_width()
        self.y = self.image.get_height()

    # Метод сужения картинки при изменении жизней
    def resize(self, new_hp):
        # Ширина по процентному изменению жизней, высота обычная
        x = int(self.x * (new_hp / self.hp))
        self.image = pygame.transform.scale(self.image, [x, self.y])

    # Метод изменения картинки в зависимости от количества жизней
    def reimage(self, new_hp):
        # Процент от изначального количества
        x = new_hp / self.hp
        # Ставим нужную картинку
        if x <= 0.25:
            self.image = self.img[2]
        elif x <= 0.5:
            self.image = self.img[1]
        else:
            self.image = self.img[0]

    # Обновление - меняем картинку и размер
    def update(self, slovar):
        if 'new_hp' in slovar:
            self.reimage(slovar['new_hp'])
            self.resize(slovar['new_hp'])
        return


# Класс самой игры
class Colber:
    # Просто инициализация
    def __init__(self, size_master, win):
        self.win = win
        # Переменные для игры
        self.score = 0
        self.sc_click = 1
        self.sc_time = 0
        self.level = 1
        # Параметры магазинов
        self.c_bought = [[0, 10], [0, 400], [0, 5000], [0, 12000], [0, 100000]]
        self.c_effect = [2, 40, 100, 200, 400]
        self.t_bought = [[0, 50], [0, 500], [0, 10000], [0, 90000], [0, 150000]]
        self.t_effect = [2, 12, 36, 120, 300]
        self.all_score = 0
        self.half_first = '0'
        # Пытаемся прочитать сохранения, если не получится, позже сохранятся
        # настройки в переменных выше
        try:
            self.read_file()
        except Exception:
            pass
        # 2 переменные для урона в секунду
        self.time_flag = True
        self.time_check = 0
        # Всякие словари для инициализации
        self.menu_objs = {}
        self.progress_objs = {}
        self.first_objs = {}
        self.fs_click_objs = {}
        self.fs_time_objs = {}
        self.sec_objs = {}
        self.ss_click_objs = {}
        self.ss_time_objs = {}
        self.fs_half_objs = {}
        self.hf_prew_objs = {}
        # Инициализируем меню и настройки. Да, они в коде называются
        # прогрессом, но это пережитки прошлого, которые мне лень править
        self.menu_init(size_master)
        self.progress_init()
        self.size_master = size_master
        self.pervii_raz = True  # Во избежание повторной инициализации
        # Фон загрузки
        self.loading = size_master.transform(
            pygame.image.load('res/loading.png').convert(), (1920, 1080))
        self.half_time = 0
        self.half_flag = 0
        self.half_start = 0

    # Метод чтения настроек и прогресса из файла
    def read_file(self):
        with open('res/colber_sets.txt', 'r') as f:
            vse = f.read().split('\n')
        # Просто читаем и записываем в переменные
        self.level = int(vse[0])
        self.score = int(vse[1])
        self.sc_click = int(vse[2])
        self.sc_time = int(vse[3])
        for i in range(5):
            self.c_bought[i] = [int(aa) for aa in vse[4 + i].split()]
        for i in range(5):
            self.t_bought[i] = [int(aa) for aa in vse[9 + i].split()]
        self.all_score = int(vse[14])
        self.half_first = vse[15]

    # Метод записи настроек и прогресса в файл
    def write_file(self):
        # Просто записываем в файл
        with open('res/colber_sets.txt', 'w') as f:
            bought = [str(i[0]) + ' ' + str(i[1]) for i in self.c_bought]
            bought2 = [str(i[0]) + ' ' + str(i[1]) for i in self.t_bought]
            f.write(str(self.level) + '\n')
            f.write(str(self.score) + '\n')
            f.write(str(self.sc_click) + '\n')
            f.write(str(self.sc_time) + '\n')
            for i in range(5):
                f.write(str(bought[i]) + '\n')
            for i in range(5):
                f.write(str(bought2[i]) + '\n')
            f.write(str(self.all_score) + '\n')
            f.write(str(self.half_first) + '\n')

    # Метод перехода на новый уровень menu - флаг перехода из меню/с другого
    # уровня показывает - надо ли сбрасывать переменные, или они
    # правильные при переходе из меню
    def new_level(self, num, menu=False):
        # Экран загрузки, тк инициализация длится долго
        self.draw_field(self.loading)
        pygame.display.update()
        if num == 1 and self.pervii_raz:
            self.pervii_raz = False
            # Инициализация первого уровня, если он не был инициализирован
            self.first_init(self.size_master)
            self.fs_click_init(self.size_master)
            self.fs_time_init(self.size_master)
            self.fs_half_init(self.size_master)
        if num == 2 and self.pervii_raz:  # Второй уровень
            # Если перешло не из меню, значит прошел переход уровня -
            # надо сбросить значения главных переменных
            self.pervii_raz = False
            if not(menu):
                self.level = 2
                self.score = 0
                self.all_score = 0
                self.sc_click = 1
                self.sc_time = 0
                self.c_bought = [[0, 10], [0, 400], [0, 5000], [0, 12000],
                                 [0, 100000]]
                self.c_effect = [2, 40, 100, 200, 400]
                self.t_bought = [[0, 50], [0, 500], [0, 10000], [0, 90000],
                                 [0, 150000]]
                self.t_effect = [2, 12, 36, 120, 300]
                self.write_file()
                # Удалим ресурсы первого уровня
                try:
                    del self.first_objs
                    del self.fs_time_objs
                    del self.fs_click_objs
                    del self.fsc_pics
                    del self.fst_pics
                    del self.first_sprites
                except Exception:
                    pass
            # Инициализация второго уровня
            self.sec_init(self.size_master)
            self.ss_click_init(self.size_master)
            self.ss_time_init(self.size_master)

    # Метод, который посылает на нужный уровень, так проще писать,
    # чем посылать из главного цикла прямо
    def choose_lvl(self):
        if self.level == 1:
            return self.first()
        if self.level == 2:
            return self.sec()

    # Аналогично для магазина урон
    def shop_c(self):
        if self.level == 1:
            return self.fs_click()
        if self.level == 2:
            return self.ss_click()

    # Аналогично для магазина у/сек
    def shop_t(self):
        if self.level == 1:
            return self.fs_time()
        if self.level == 2:
            return self.ss_time()

    # Аналогично для полминуток безумия
    def half(self):
        if self.level == 1:
            return self.fs_half()
        if self.level == 2:
            return self.ss_half()

    # Прорисовываем фон
    def draw_field(self, field):
        self.win.blit(field, (0, 0))

    # Инициализация меню
    def menu_init(self, size_master):
        # Фон
        self.menu_field = size_master.transform(
            pygame.image.load('res/colber/field.png').convert(), (1920, 1080))
        # Картинки кнопки
        a0 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_off.png'), (600, 115))
        a1 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_on.png'), (600, 115))
        a2 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_on2.png'), (600, 115))
        # Словари для проджект р
        text_slovar = {'positions': size_master.repos_and_resize((1320, 313)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf', 0.7),
                       'color': (255, 216, 0), 'text': 'ИГРАТЬ'}
        rbut_slovar = {'positions': size_master.repos_and_resize((1320, 313)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((600, 115)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a1]]}
        # Кнопка играть
        self.menu_objs['play'] = RButton(rbut_slovar.copy())
        self.menu_objs['play'].set_text(text_slovar)
        self.menu_objs['play'].move_center_text()
        # Меняем словарь, кнопка настроек
        rbut_slovar['positions'] = size_master.repos_and_resize((1320, 483))
        text_slovar['text'] = 'НАСТРОЙКИ'
        text_slovar['positions'] = size_master.repos_and_resize((1320, 483))
        self.menu_objs['progress'] = RButton(rbut_slovar.copy())
        self.menu_objs['progress'].set_text(text_slovar)
        self.menu_objs['progress'].move_center_text()
        # Меняем словарь, кнопка выхода
        rbut_slovar['animations'] = [[a0], [a2]]
        rbut_slovar['positions'] = size_master.repos_and_resize((1320, 653))
        text_slovar['text'] = 'ВЫХОД'
        text_slovar['positions'] = size_master.repos_and_resize((1320, 653))
        self.menu_objs['exit'] = RButton(rbut_slovar.copy())
        self.menu_objs['exit'].set_text(text_slovar)
        self.menu_objs['exit'].move_center_text()

    # Инициализируем настройки
    def progress_init(self):
        pass

    # Инициализируем первый уровень
    def first_init(self, size_master):
        # Фон и фон после победы
        self.first_field2 = size_master.transform(
            pygame.image.load('res/colber/first/last_field.png').convert(), (1920, 1080))
        self.first_field = size_master.transform(
            pygame.image.load('res/colber/first/field.png').convert(), (1920, 1080))
        # Картинки колбы
        pic0 = size_master.transform(
            pygame.image.load('res/colber/first/colb_noclick.png'),
            (720, 720))
        pic00 = size_master.transform(
            pygame.image.load('res/colber/first/colb_noclick2.png'),
            (720, 720))
        pic1 = size_master.transform(
            pygame.image.load('res/colber/first/colb_click.png'), (720, 720))
        pic11 = size_master.transform(
            pygame.image.load('res/colber/first/colb_click2.png'), (720, 720))
        # Картинки кнопки
        a0 = size_master.transform(
            pygame.image.load('res/colber/first/b_600_115_off.png'),
            (600, 115))
        a1 = size_master.transform(
            pygame.image.load('res/colber/first/b_600_115_on.png'),
            (600, 115))
        # Картинки кнопок магазинов
        a3 = size_master.transform(
            pygame.image.load('res/colber/first/cs_off.png'), (500, 500))
        a4 = size_master.transform(
            pygame.image.load('res/colber/first/cs_on.png'), (500, 500))
        a5 = size_master.transform(
            pygame.image.load('res/colber/first/ts_off.png'), (500, 500))
        a6 = size_master.transform(
            pygame.image.load('res/colber/first/ts_on.png'), (500, 500))
        # Картинки полоски здоровья
        h1 = size_master.transform(
            pygame.image.load('res/colber/first/hp1.png').convert(), (500, 40))
        h2 = size_master.transform(
            pygame.image.load('res/colber/first/hp2.png').convert(), (500, 40))
        h3 = size_master.transform(
            pygame.image.load('res/colber/first/hp3.png').convert(), (500, 40))
        # Координаты спрайтов - колбы и здоровья
        pos = size_master.repos_and_resize((600, 130))
        pos2 = size_master.repos_and_resize((710, 50))
        # Создаем группу спрайтов и сами спрайты
        self.first_sprites = pygame.sprite.Group()
        MySprite(self.first_sprites, pos, pic0, pic00, pic1,
                 pic11, size_master)
        HP(self.first_sprites, pos2, h1, h2, h3, 10000000)
        # Словари для интерфейса
        text_slovar = {'positions': size_master.repos_and_resize((0, 920)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf', 0.7),
                       'color': (255, 255, 255), 'text': 'НАЗАД'}
        text2_slovar = {'positions': size_master.repos_and_resize((10, 10)),
                        'win': self.win,
                        'font': 'res/fonts/RobotoSlab-Regular.ttf',
                        'text_size': size_master.resize_text(
                            'res/fonts/RobotoSlab-Regular.ttf', 0.7),
                        'color': (255, 255, 255), 'text': 'СЧЕТ:'}
        text3_slovar = {'positions': size_master.repos_and_resize((120, 550)),
                        'win': self.win,
                        'font': 'res/fonts/RobotoSlab-Regular.ttf',
                        'text_size': size_master.resize_text(
                            'res/fonts/RobotoSlab-Regular.ttf', 1),
                        'color': (200, 10, 10), 'text': '0'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 920)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((600, 115)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a1]]}
        rbut2_slovar = {'positions': size_master.repos_and_resize((10, 350)),
                        'win': self.win,
                        'size': size_master.repos_and_resize((500, 500)),
                        'tap_buts': (1, 3), 'animations': [[a3], [a4]]}
        # Кнопка назад
        self.first_objs['exit'] = RButton(rbut_slovar.copy())
        self.first_objs['exit'].set_text(text_slovar)
        self.first_objs['exit'].move_center_text()
        # Меняем словарь, кнопка дальше, выключим её
        rbut_slovar['invisible'] = 0
        rbut_slovar['positions'] = size_master.repos_and_resize((1320, 920))
        text_slovar['text'] = 'ИДТИ ДАЛЬШЕ'
        text_slovar['positions'] = size_master.repos_and_resize((1320, 920))
        self.first_objs['cont'] = RButton(rbut_slovar.copy())
        self.first_objs['cont'].set_text(text_slovar)
        self.first_objs['cont'].move_center_text()
        self.first_objs['cont'].closed = True
        # Кнопки магазинов
        self.first_objs['click'] = RButton(rbut2_slovar.copy())
        rbut2_slovar['positions'] = size_master.repos_and_resize((1410, 350))
        rbut2_slovar['animations'] = [[a5], [a6]]
        self.first_objs['time'] = RButton(rbut2_slovar.copy())
        # Текст с счетом
        self.first_objs['t1'] = RText(text2_slovar.copy())
        text2_slovar['positions'] = size_master.repos_and_resize((10, 80))
        text2_slovar['text'] = str(self.score)
        self.first_objs['score'] = RText(text2_slovar.copy())
        text2_slovar['positions'] = size_master.repos_and_resize((1000, 10))
        # Текст с урон и у/сек
        self.first_objs['uron'] = RText(text3_slovar.copy())
        text3_slovar['positions'] = size_master.repos_and_resize((1600, 550))
        self.first_objs['usec'] = RText(text3_slovar.copy())
        # Текст с осталось, выравниваем по правому краю
        text2_slovar['text'] = 'ОСТАЛОСЬ:'
        self.first_objs['t2'] = RText(text2_slovar.copy())
        self.first_objs['t2'].move_right(size_master.resize_one(910))
        text2_slovar['positions'] = size_master.repos_and_resize((1000, 80))
        text2_slovar['text'] = '10000000'
        self.first_objs['t3'] = RText(text2_slovar.copy())
        self.first_objs['t3'].move_right(size_master.resize_one(910))

    # Инициализируем магазин урон первого уровня
    def fs_click_init(self, size_master):
        # Картинки кнопки
        a0 = size_master.transform(
            pygame.image.load('res/colber/first/b_600_115_off.png'),
            (600, 115))
        a1 = size_master.transform(
            pygame.image.load('res/colber/first/b_600_115_on.png'),
            (600, 115))
        # Картинки кнопок-панелей покупки
        a2 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_off.png'),
            (300, 600))
        a3 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_on.png'),
            (300, 600))
        a4 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_on2.png'),
            (300, 600))
        # Словари для интерфейса
        text_slovar = {'positions': size_master.repos_and_resize((0, 920)),
                       'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': size_master.resize_text(
                           'res/fonts/RobotoSlab-Regular.ttf', 0.7),
                       'color': (255, 255, 255), 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 920)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((600, 115)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a1]]}
        rkeyb_slovar = {'positions': size_master.repos_and_resize((70, 250)),
                        'tap_buts': (1, 3),
                        'size': size_master.repos_and_resize((300, 600)),
                        'win': self.win,
                        'horizontal': True,
                        'indent': size_master.resize_one(70), 'kolvo': 5,
                        'texts': ['+' + str(i) for i in self.c_effect],
                        'animations': [[a2], [a3], [a4]]}
        rkeyb2_slovar = {'positions': size_master.repos_and_resize((70, 270)),
                         'win': self.win,
                         'font': 'res/fonts/RobotoSlab-Regular.ttf',
                         'text_size': size_master.resize_text(
                             'res/fonts/RobotoSlab-Regular.ttf', 0.7),
                         'color': (255, 0, 0),
                         'indent': size_master.resize_one(370)}
        text2_slovar = {'positions': size_master.repos_and_resize((10, 10)),
                        'win': self.win,
                        'font': 'res/fonts/RobotoSlab-Regular.ttf',
                        'text_size': size_master.resize_text(
                            'res/fonts/RobotoSlab-Regular.ttf', 0.7),
                        'color': (255, 255, 255), 'text': 'СЧЕТ:'}
        base_slovar = {'positions': 0, 'picture': 0, 'win': self.win}
        # Панели покупки - клавиатура
        self.fs_click_objs['keyb'] = RKeyboard(rkeyb_slovar.copy(),
                                               rkeyb2_slovar.copy())
        self.fs_click_objs['keyb'].move_center_text()
        # Выход
        self.fs_click_objs['exit'] = RButton(rbut_slovar.copy())
        self.fs_click_objs['exit'].set_text(text_slovar)
        self.fs_click_objs['exit'].move_center_text()
        # Аналог группы спрайтов - чтобы прорисовать в нужном порядке
        self.fs_click_objs['c_items'] = RItemList()
        self.fs_click_objs['c_items2'] = RItemList()
        # Тексты какие-то
        self.fs_click_objs['t1'] = RText(text2_slovar.copy())
        text2_slovar['positions'] = size_master.repos_and_resize((10, 80))
        text2_slovar['text'] = str(self.score)
        self.fs_click_objs['score'] = RText(text2_slovar.copy())
        text2_slovar['positions'] = size_master.repos_and_resize((1000, 10))
        text2_slovar['text'] = 'УРОН:'
        self.fs_click_objs['t2'] = RText(text2_slovar.copy())
        self.fs_click_objs['t2'].move_right(size_master.resize_one(910))
        text2_slovar['positions'] = size_master.repos_and_resize((1000, 80))
        text2_slovar['text'] = '10000000'
        self.fs_click_objs['t3'] = RText(text2_slovar.copy())
        self.fs_click_objs['t3'].move_right(size_master.resize_one(910))
        # Дальше создание картинок и дополнительных текстов на
        # клавиатуре покупок
        poses1 = [70 + 370 * i for i in range(5)]
        text_slovar['color'] = (255, 0, 0)
        self.fsc_pics = []
        for i in range(5):
            text_slovar['positions'] = size_master.repos_and_resize(
                (poses1[i], 620))
            text_slovar['text'] = str(self.c_bought[i][1])
            self.fs_click_objs['c_items'].append(RText(text_slovar.copy()))
            self.fs_click_objs['c_items'].list[i].move_center(size_master.
                                                              resize_one(300))
            base_slovar['positions'] = size_master.repos_and_resize(
                (poses1[i], 250))
            base_slovar['picture'] = size_master.transform(pygame.image.load(
                'res/colber/first/c_' + str(i + 1) + '.png'), (300, 300))
            self.fsc_pics.append(RBase(base_slovar))
        for i in range(5):
            text_slovar['positions'] = size_master.repos_and_resize(
                (poses1[i], 720))
            text_slovar['text'] = str(self.c_bought[i][0])
            self.fs_click_objs['c_items2'].append(RText(text_slovar.copy()))
            self.fs_click_objs['c_items2'].list[i].move_center(
                size_master.resize_one(300))

    # Инициализация магазина у/сек первого уроня, код аналогичен коду
    # магазина выше, комментировать не буду
    def fs_time_init(self, size_master):
        a0 = size_master.transform(
            pygame.image.load('res/colber/first/b_600_115_off.png'),
            (600, 115))
        a1 = size_master.transform(
            pygame.image.load('res/colber/first/b_600_115_on.png'),
            (600, 115))
        a2 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_off.png'),
            (300, 600))
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
                       'color': (255, 255, 255), 'text': 'НАЗАД'}
        rbut_slovar = {'positions': size_master.repos_and_resize((0, 920)),
                       'win': self.win,
                       'size': size_master.repos_and_resize((600, 115)),
                       'tap_buts': (1, 3), 'animations': [[a0], [a1]]}
        rkeyb_slovar = {'positions': size_master.repos_and_resize((70, 250)),
                        'tap_buts': (1, 3),
                        'size': size_master.repos_and_resize((300, 600)),
                        'win': self.win,
                        'horizontal': True, 'indent': size_master.resize_one(70), 'kolvo': 5,
                        'texts': ['+' + str(i) for i in self.t_effect],
                        'animations': [[a2], [a3], [a4]]}
        rkeyb2_slovar = {'positions': size_master.repos_and_resize((70, 270)),
                         'win': self.win,
                         'font': 'res/fonts/RobotoSlab-Regular.ttf',
                         'text_size': size_master.resize_text(
                             'res/fonts/RobotoSlab-Regular.ttf', 0.7),
                         'color': (255, 0, 0),
                         'indent': size_master.resize_one(370)}
        text2_slovar = {'positions': size_master.repos_and_resize((10, 10)),
                        'win': self.win,
                        'font': 'res/fonts/RobotoSlab-Regular.ttf',
                        'text_size': size_master.resize_text(
                            'res/fonts/RobotoSlab-Regular.ttf', 0.7),
                        'color': (255, 255, 255), 'text': 'СЧЕТ:'}
        base_slovar = {'positions': 0, 'picture': 0, 'win': self.win}
        self.fs_time_objs['t1'] = RText(text2_slovar.copy())
        text2_slovar['positions'] = size_master.repos_and_resize((10, 80))
        text2_slovar['text'] = str(self.score)
        self.fs_time_objs['score'] = RText(text2_slovar.copy())
        text2_slovar['positions'] = size_master.repos_and_resize((1000, 10))
        text2_slovar['text'] = 'У/СЕК:'
        self.fs_time_objs['t2'] = RText(text2_slovar.copy())
        self.fs_time_objs['t2'].move_right(size_master.resize_one(910))
        text2_slovar['positions'] = size_master.repos_and_resize((1000, 80))
        text2_slovar['text'] = '10000000'
        self.fs_time_objs['t3'] = RText(text2_slovar.copy())
        self.fs_time_objs['t3'].move_right(size_master.resize_one(910))
        self.fs_time_objs['keyb'] = RKeyboard(rkeyb_slovar.copy(),
                                              rkeyb2_slovar.copy())
        self.fs_time_objs['keyb'].move_center_text()
        self.fs_time_objs['exit'] = RButton(rbut_slovar.copy())
        self.fs_time_objs['exit'].set_text(text_slovar)
        self.fs_time_objs['exit'].move_center_text()
        self.fs_time_objs['t_items'] = RItemList()
        self.fs_time_objs['t_items2'] = RItemList()
        self.fst_pics = []
        poses1 = [70 + 370*i for i in range(5)]
        text_slovar['color'] = (255, 0, 0)
        for i in range(5):
            text_slovar['positions'] = size_master.repos_and_resize(
                (poses1[i], 620))
            text_slovar['text'] = str(self.t_bought[i][1])
            self.fs_time_objs['t_items'].append(RText(text_slovar.copy()))
            self.fs_time_objs['t_items'].list[i].move_center(
                size_master.resize_one(300))
            base_slovar['positions'] = size_master.repos_and_resize((poses1[i], 250))
            base_slovar['picture'] = size_master.transform(
                pygame.image.load('res/colber/first/t_' + str(i + 1) +
                                  '.png'), (300, 300))
            self.fst_pics.append(RBase(base_slovar))
        for i in range(5):
            text_slovar['positions'] = size_master.repos_and_resize(
                (poses1[i], 720))
            text_slovar['text'] = str(self.t_bought[i][0])
            self.fs_time_objs['t_items2'].append(RText(text_slovar.copy()))
            self.fs_time_objs['t_items2'].list[i].move_center(
                size_master.resize_one(300))

    # Инициализируем магазин урон первого уровня
    def fs_half_init(self, size_master):
        f1 = size_master.transform(
            pygame.image.load(
                'res/colber/first/half/pic.png').convert(), (1920, 1080))
        f2 = size_master.transform(
            pygame.image.load(
                'res/colber/first/half/pic2.png').convert(), (1920, 1080))
        f3 = size_master.transform(
            pygame.image.load(
                'res/colber/first/half/pic3.png').convert(), (1920, 1080))
        self.fs_h_fields = [f1, f2, f3]
        # Картинки кнопки
        a0 = size_master.transform(
            pygame.image.load(
                'res/colber/first/b_600_115_off.png'), (600, 115))
        a1 = size_master.transform(
            pygame.image.load(
                'res/colber/first/b_600_115_on.png'), (600, 115))
        # Словари для интерфейса
        text_slovar = {
            'positions': size_master.repos_and_resize((0, 920)),
            'win': self.win,
            'font': 'res/fonts/RobotoSlab-Regular.ttf',
            'text_size': size_master.resize_text(
                'res/fonts/RobotoSlab-Regular.ttf', 0.7),
            'color': (255, 255, 255), 'text': 'НАЗАД'}
        rbut_slovar = {
            'positions': size_master.repos_and_resize((0, 920)),
            'win': self.win,
            'size': size_master.repos_and_resize((600, 115)),
            'tap_buts': (1, 3), 'animations': [[a0], [a1]]}
        # Выход
        self.fs_half_objs['exit'] = RButton(rbut_slovar.copy())
        self.fs_half_objs['exit'].set_text(text_slovar)
        self.fs_half_objs['exit'].move_center_text()

    def ss_click_init(self, size_master):
        colors = [(255, 255, 255), (200, 10, 10), (255, 255, 255)]
        factor = size_master.get_factor()
        a0 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_off.png').convert(), (600, 115))
        a1 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_on.png').convert(), (600, 115))
        a2 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_off.png').convert(), (300, 600))
        a3 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_on.png').convert(),
            (300, 600))
        a4 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_on2.png').convert(),
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
        self.sec_field = size_master.transform(
            pygame.image.load('res/colber/first/field.png').convert(), (1920, 1080))
        pic0 = size_master.transform(
            pygame.image.load('res/colber/first/colb_noclick.png').convert(), (720, 720))
        pic00 = size_master.transform(
            pygame.image.load('res/colber/first/colb_noclick.png').convert(),
            (720, 720))
        pic1 = size_master.transform(
            pygame.image.load('res/colber/first/colb_click.png').convert(), (720, 720))
        pic11 = size_master.transform(
            pygame.image.load('res/colber/first/colb_click2.png').convert(), (720, 720))
        pos = size_master.repos_and_resize((600, 130))
        self.sec_sprites = pygame.sprite.Group()
        MySprite(self.sec_sprites, pos, pic0, pic00, pic1, pic11, size_master)
        colors = [(255, 255, 255), (200, 10, 10), (255, 255, 255)]
        factor = size_master.get_factor()
        a0 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_off.png').convert(), (600, 115))
        a1 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_on.png').convert(), (600, 115))
        a3 = size_master.transform(
            pygame.image.load('res/colber/b_500_500_off.png').convert(), (500, 500))
        a4 = size_master.transform(
            pygame.image.load('res/colber/b_500_500_on.png').convert(), (500, 500))
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
        text2_slovar['text'] = '100000000'
        self.sec_objs['t3'] = RText(text2_slovar.copy())
        self.sec_objs['t3'].move_right(size_master.resize_one(910))

    def ss_time_init(self, size_master):
        colors = [(255, 255, 255), (200, 10, 10), (255, 255, 255)]
        factor = size_master.get_factor()
        a0 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_off.png').convert(), (600, 115))
        a1 = size_master.transform(
            pygame.image.load('res/colber/b_600_115_on.png').convert(), (600, 115))
        a2 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_off.png').convert(), (300, 600))
        a3 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_on.png').convert(),
            (300, 600))
        a4 = size_master.transform(
            pygame.image.load('res/colber/first/b_300_600_on2.png').convert(),
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

    def hf_prew_init(self, size_master):
        # Картинки кнопки
        a0 = size_master.transform(
            pygame.image.load(
                'res/colber/first/b_600_115_off.png'), (600, 115))
        a1 = size_master.transform(
            pygame.image.load(
                'res/colber/first/b_600_115_on.png'), (600, 115))
        # Словари для интерфейса
        text_box_slovar = {
            'positions': size_master.repos_and_resize((0, 220)),
            'win': self.win,
            'font': 'res/fonts/RobotoSlab-Regular.ttf',
            'text_size': size_master.resize_text(
                'res/fonts/RobotoSlab-Regular.ttf', 0.66),
            'color': (255, 255, 255),
            'text': '''Вам повезло, впервые включился режим "Полминутки безум
            ия". В течение следующих 30 секунд ваши УРОН и У/СЕК увеличены в 
            некоторое количество раз. Режим можно выключить в настройках. 
            Ренкомендуем сделать это людям, страдающим неврологическими 
            заболеваниями или головной болью''',
            'auto': 0,
            'window_width': size_master.resize_one(1700),
            'indent': size_master.resize_one(80)}
        text_slovar = {
            'positions': size_master.repos_and_resize((660, 920)),
            'win': self.win,
            'font': 'res/fonts/RobotoSlab-Regular.ttf',
            'text_size': size_master.resize_text(
                'res/fonts/RobotoSlab-Regular.ttf', 0.7),
            'color': (255, 255, 255), 'text': 'ОК'}
        rbut_slovar = {
            'positions': size_master.repos_and_resize((660, 920)),
            'win': self.win,
            'size': size_master.repos_and_resize((600, 115)),
            'tap_buts': (1, 3), 'animations': [[a0], [a1]]}
        # Выход
        self.hf_prew_objs['exit'] = RButton(rbut_slovar.copy())
        self.hf_prew_objs['exit'].set_text(text_slovar)
        self.hf_prew_objs['exit'].move_center_text()
        self.hf_prew_objs['tb'] = RTextBox(text_box_slovar.copy())
        self.hf_prew_objs['tb'].move_center(size_master.resize_one(1920))

    # Меню - действие
    def menu(self):
        self.draw_field(self.menu_field)
        # Проверка и прорисовка элементов
        mouse_pos = pygame.mouse.get_pos()
        for i in self.menu_objs:
            try:
                self.menu_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.menu_objs[i].draw()
        # События - выход, нажатие на кнопки
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.menu_objs['exit'].is_tap(event,
                                             pygame.mouse.get_pos(), 1):
                # Кнопка выход
                return 4
            if self.menu_objs['progress'].is_tap(event,
                                                 pygame.mouse.get_pos(), 1):
                # Кнопка настройки
                return 2
            if self.menu_objs['play'].is_tap(event,
                                             pygame.mouse.get_pos(), 1):
                # Кнопка играть
                # Инициализация (сама понимает, надо ли) уровня
                self.new_level(self.level, menu=True)
                self.half_start = time.time()
                return 1

    def progress(self):
        return

    # Первый уровень - действие
    def first(self):
        if time.time() - self.half_start >= 120:
            ran_res = random.choice([True, True, False, False, False])
            if ran_res:
                self.half_time = time.time()
                return 1003
            else:
                self.half_start = time.time()
        self.draw_field(self.first_field)
        # Проверка на большой набранный счет (Закончили или нет уровень)
        if self.all_score >= 10000000:
            self.draw_field(self.first_field2)
            self.first_objs['t3'].new_text('0')
            self.first_objs['t3'].pos[0] = self.size_master.resize_one(1000)
            self.first_objs['t3'].move_right(
                self.size_master.resize_one(910))
            self.first_objs['cont'].closed = False
            self.first_objs['cont'].inv = False
            self.start = False
        else:
            self.draw_field(self.first_field)
            self.start = True
            # Обновляем текст урон и у/сек
            self.first_objs['uron'].new_text(str(self.sc_click))
            self.first_objs['usec'].new_text(str(self.sc_time))
            # Если флаг времени - делаем первый замер
            if self.time_flag:
                self.time_flag = False
                self.time_check = time.time()
            time_now = time.time()
            # Если прошло полсекунды, добавляем к счету половину у/сек,
            # обновляем замер времени и файл сохранений
            if self.time_check <= time_now - 0.5:
                add = self.sc_time // 2
                self.score += add
                self.all_score += add
                self.time_check = time_now
                self.write_file()
            # Обновляем полоску жизней и надпись осталось
            per = 10000000 - self.all_score
            self.first_objs['t3'].new_text(str(per))
            self.first_objs['t3'].pos[0] = self.size_master.resize_one(1000)
            self.first_objs['t3'].move_right(
                self.size_master.resize_one(910))
            self.first_sprites.update({'new_hp': per})
            self.first_sprites.draw(self.win)
        # Обновляем надпись счета
        self.first_objs['score'].new_text(str(self.score))
        # Прорисуем инерфейс
        mouse_pos = pygame.mouse.get_pos()
        for i in self.first_objs:
            try:
                self.first_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.first_objs[i].draw()
        # События
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Если мы еще не закончили уровень, проверяем спрайт
                # на нажатие, для этого читаем один файлик
                if self.start:
                    self.first_sprites.update({'pos':mouse_pos, 'event':0})
                    with open('res/colber/noname', 'r') as f:
                        result = f.read()
                        if result == '1':
                            # Обновляем переменные
                            self.score += self.sc_click
                            self.all_score += self.sc_click
            if self.first_objs['exit'].is_tap(event,
                                              pygame.mouse.get_pos(), 1):
                self.time_flag = True  # Остановим время при выходе
                return 4
            if self.first_objs['click'].is_tap(event,
                                               pygame.mouse.get_pos(), 1):
                if self.start:
                    return 1001  # При переходе в магазины не останавливаем
            if self.first_objs['time'].is_tap(event,
                                              pygame.mouse.get_pos(), 1):
                if self.start:
                    return 1002
            if self.first_objs['cont'].is_tap(event,
                                              pygame.mouse.get_pos(), 1):
                self.pervii_raz = True
                self.new_level(2)
                return 1

    # Магазин урон - действие
    def fs_click(self):
        self.draw_field(self.first_field)
        mouse_pos = pygame.mouse.get_pos()
        # Обновляем надписи - счет и урон
        self.fs_click_objs['score'].new_text(str(self.score))
        self.fs_click_objs['t3'].new_text(str(self.sc_click))
        self.fs_click_objs['t3'].pos[0] = self.size_master.resize_one(1000)
        self.fs_click_objs['t3'].move_right(self.size_master.resize_one(910))
        # Проверка на время - добавление у/сек, мы ведь в игре еще
        time_now = time.time()
        if self.time_check <= time_now - 0.5:
            add = self.sc_time // 2
            self.score += add
            self.all_score += add
            self.time_check = time_now
            self.write_file()
        # Проверка товаров на возможность купить -
        # закрываем кнопки, если мало счета
        for i in range(5):
            if self.score < self.c_bought[i][1]:
                self.fs_click_objs['keyb'].buts[i].set_animation(0)
                self.fs_click_objs['keyb'].buts[i].closed = True
            else:
                self.fs_click_objs['keyb'].buts[i].closed = False
        # Проверка и отрисовка интерфейса
        for i in self.fs_click_objs:
            try:
                self.fs_click_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.fs_click_objs[i].draw()
        # Отрисовка картинок на товарах
        for i in self.fsc_pics:
            i.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.fs_click_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                self.half_start = time.time()
                return 4
            # Проверка покупки
            tap = self.fs_click_objs['keyb'].taps(event,
                                                     pygame.mouse.get_pos(),
                                                     animation=2, delay=3)
            if tap[0]:
                num = tap[1]
                # Меняем числа у товара - цену и количество
                poses1 = [70 + 370 * i for i in range(5)]
                sc = self.c_bought[num][1]
                self.score -= sc
                if sc * 0.05 >= 1:
                    # Добавим 5% или 1
                    self.c_bought[num][1] += sc * 0.05
                    self.c_bought[num][1] = int(self.c_bought[num][1])
                else:
                    self.c_bought[num][1] += 1
                self.c_bought[num][0] += 1
                self.sc_click += self.c_effect[num]
                # Меняем стоимость на картинках
                self.fs_click_objs['c_items'].list[num].new_text(str(
                    self.c_bought[num][1]))
                self.fs_click_objs['c_items'].list[num].pos = \
                    self.size_master.repos_and_resize([poses1[num], 620])
                self.fs_click_objs['c_items'].list[num].move_center(
                    self.size_master.resize_one(300))
                self.fs_click_objs['c_items2'].list[num].new_text(
                    str(self.c_bought[num][0]))
                self.fs_click_objs['c_items2'].list[num].pos = \
                    self.size_master.repos_and_resize([poses1[num], 720])
                self.fs_click_objs['c_items2'].list[num].move_center(
                    self.size_master.resize_one(300))

    # Магазин у/сек - действие, аналогичен магазину выше,
    # комментировать не буду
    def fs_time(self):
        self.draw_field(self.first_field)
        mouse_pos = pygame.mouse.get_pos()
        time_now = time.time()
        self.fs_time_objs['score'].new_text(str(self.score))
        self.fs_time_objs['t3'].new_text(str(self.sc_time))
        self.fs_time_objs['t3'].pos[0] = self.size_master.resize_one(1000)
        self.fs_time_objs['t3'].move_right(self.size_master.resize_one(910))
        if self.time_check <= time_now - 0.5:
            add = self.sc_time // 2
            self.score += add
            self.all_score += add
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
        for i in self.fst_pics:
            i.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.fs_time_objs['exit'].is_tap(event,
                                                pygame.mouse.get_pos(), 1):
                self.half_start = time.time()
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
                self.fs_time_objs['t_items'].list[num].new_text(
                    str(self.t_bought[num][1]))
                self.fs_time_objs['t_items'].list[num].pos = \
                    self.size_master.repos_and_resize([poses1[num], 620])
                self.fs_time_objs['t_items'].list[num].move_center(
                    self.size_master.resize_one(300))
                self.fs_time_objs['t_items2'].list[num].new_text(
                    str(self.t_bought[num][0]))
                self.fs_time_objs['t_items2'].list[num].pos = \
                    self.size_master.repos_and_resize([poses1[num], 720])
                self.fs_time_objs['t_items2'].list[num].move_center(
                    self.size_master.resize_one(300))

    def sec(self):
        self.draw_field(self.sec_field)
        mouse_pos = pygame.mouse.get_pos()
        if self.time_flag:
            self.time_flag = False
            self.time_check = time.time()
        time_now = time.time()
        if self.time_check <= time_now - 0.5:
            self.score += self.sc_time // 2
            self.time_check = time_now
            self.write_file()
        if self.score >= 10000000:
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
        self.draw_field(self.sec_field)
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
                self.ss_click_objs['c_items'].list[num].pos = self.size_master.repos_and_resize([poses1[num], 470])
                self.ss_click_objs['c_items'].list[num].move_center(self.size_master.resize_one(300))
                self.ss_click_objs['c_items2'].list[num].new_text(str(self.c_bought[num][0]))
                self.ss_click_objs['c_items2'].list[num].pos = self.size_master.repos_and_resize([poses1[num], 570])
                self.ss_click_objs['c_items2'].list[num].move_center(self.size_master.resize_one(300))

    def ss_time(self):
        self.draw_field(self.sec_field)
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
                self.ss_time_objs['t_items'].list[num].pos = self.size_master.repos_and_resize([poses1[num], 470])
                self.ss_time_objs['t_items'].list[num].move_center(self.size_master.resize_one(300))
                self.ss_time_objs['t_items2'].list[num].new_text(str(self.t_bought[num][0]))
                self.ss_time_objs['t_items2'].list[num].pos = self.size_master.repos_and_resize([poses1[num], 570])
                self.ss_time_objs['t_items2'].list[num].move_center(self.size_master.resize_one(300))

    def fs_half(self):
        if self.half_first == '0':
            self.hf_prew_init(self.size_master)
            self.half_first = '1'
            return 1234
        if self.half_flag > 11:
            self.half_flag = 0
        if self.half_flag < 3:
            self.draw_field(self.fs_h_fields[0])
            self.half_flag += 1
        elif self.half_flag < 6:
            self.draw_field(self.fs_h_fields[1])
            self.half_flag += 1
        elif self.half_flag < 9:
            self.draw_field(self.fs_h_fields[2])
            self.half_flag += 1
        elif self.half_flag < 12:
            self.draw_field(self.fs_h_fields[1])
            self.half_flag += 1
        mouse_pos = pygame.mouse.get_pos()
        # Проверка на время - добавление у/сек, мы ведь в игре еще
        time_now = time.time()
        if self.time_check <= time_now - 0.5:
            add = int(self.sc_time / 2 * 1.5)
            self.score += add
            self.all_score += add
            self.time_check = time_now
            self.write_file()
        if time_now >= self.half_time + 30:
            self.half_start = time_now
            return 1
        # Проверка и отрисовка интерфейса
        for i in self.fs_half_objs:
            try:
                self.fs_half_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.fs_half_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.fs_half_objs['exit'].is_tap(event,
                                                 pygame.mouse.get_pos(), 1):
                return 4
            if event.type == pygame.MOUSEBUTTONDOWN:
                ms = pygame.mouse.get_pos()
                y0 = self.size_master.resize_one(280)
                y1 = self.size_master.resize_one(820)
                x0 = self.size_master.resize_one(710)
                x1 = self.size_master.resize_one(1210)
                if x0 <= ms[0] <= x1 and y0 <= ms[1] <= y1:
                    add = int(self.sc_click * 1.5)
                    self.score += add
                    self.all_score += add

    def ss_half(self):
        pass

    def hf_prew(self):
        self.draw_field(self.first_field)
        mouse_pos = pygame.mouse.get_pos()
        # Проверка на время - добавление у/сек, мы ведь в игре еще
        time_now = time.time()
        if self.time_check <= time_now - 0.5:
            add = int(self.sc_time / 2 * 1.5)
            self.score += add
            self.all_score += add
            self.time_check = time_now
            self.write_file()
        if time_now >= self.half_time + 30:
            self.half_start = time_now
            return 1
        # Проверка и отрисовка интерфейса
        for i in self.hf_prew_objs:
            try:
                self.hf_prew_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.hf_prew_objs[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.hf_prew_objs['exit'].is_tap(event,
                                                 pygame.mouse.get_pos(), 1):
                self.half_time = time.time()
                return 4
