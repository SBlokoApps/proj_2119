from project_R import *
from win32api import GetSystemMetrics, SetFileAttributes


# Window-size-master - утилита изменения размера экрана, размера картинок и
# всех необходимых для корректной работы экрана с заданным размером
# частей программы
#
# Класс WSM занимается изменением размеров изображений и подгоном
# переменных-координат под нужный размер экрана, также помогает найти
# изображения в соответствии с выбранной темой
class WSM:
    def __init__(self):
        # Читаем файл, о котором позже
        with open('res/screen_sets.txt', 'r') as f:
            vse = f.read().split()
        # Там записаны размеры экрана и номер темы
        self.size = [int(vse[0]), int(vse[1])]
        self.theme = vse[2]
        # Изначально программа создается под 1920*1080, соотношение сторон
        # неизменно, но для работы нам нужно отношение нужного размера
        # к изначально задуманному
        self.factor = self.size[0] / 1920

    def get_size(self):  # Просто вернет размеры окна
        return self.size

    def get_fullscreen(self):  # Проверяет размеры окна на полноэкранность
        # Соответствуют ли оба значения размера окна системным
        if self.size[0] == GetSystemMetrics(0) and self.size[1] ==\
                GetSystemMetrics(1):
            return True
        return False

    def get_factor(self):  # Вернет отношение размера экрана к 1920*1080
        return self.factor

    def get_prefix(self):  # Помогает найти картинки для выбранной темы
        # Доюбавляет первую часть пути файла - папку с картинками темы,
        # внутри названия между темами совпадают
        if self.theme == '0':
            return 'res/dark/'
        return 'res/light/'

    # Изменяет размер картинки. Для ускорения работы, метод не сам определяет
    # изначальный размер, мы передаем его сами
    # Для определения нового размера используется self.factor
    def transform(self, image, size):
        return pygame.transform.scale(image,
                                      [int(self.factor * i) for i in size])

    # Изменяет список/кортеж с 2 числами - размером чего-либо или
    # его координатами, использует self.factor
    def repos_and_resize(self, old):
        return [int(self.factor * i) for i in old]

    # Аналогично для 1 числа
    def resize_one(self, old):
        return int(self.factor * old)

    # Определяет размер шрифта по названию и коэффициенту уменьшения -
    # изначально размер шрифта подогнан под часто используемый текст на
    # определенном размере экрана, но иногда он может не влезать, его надо
    # уменьшить с помощью коэффициента
    def resize_text(self, font, factor=1):
        # Для определения оптимального размера шрифта используются уравнения
        # прямой, а шрифты подобраны с примерно равномерным ростом
        # Уравнения определялись по 2м точкам - ширина окна 1920 и оптимальный
        # размер для неё и 800 с оптимальным размером для него
        # Для каждого шрифта оно своё
        if font == 'res/fonts/RobotoSlab-Regular.ttf':
            return int((0.045 * self.size[0] + 4.286) * factor)
        elif font == 'res/fonts/labor-union-regular.otf':
            return int((0.0893 * self.size[0] + 8/571) * factor)
        elif font == 'res/fonts/Staatliches-Regular.ttf':
            return int((0.125 * self.size[0] - 10) * factor)

    # Возвращает цвета текста, нужные для каждой темы в списке -
    # цвет текста, тени и заголовка
    def get_colors(self):
        if self.theme == '1':
            return [(255, 0, 0), (150, 150, 150), (200, 50, 50)]
        return [(255, 255, 255), (200, 10, 10), (255, 255, 255)]

    # Сбрасывает графические настройки в файле
    def reset_sets(self):
        # Файл был скрыт, возвращаем его
        SetFileAttributes('res/screen_sets.txt', 128)
        with open('res/screen_sets.txt', 'w') as f:
            # Записываем нули, чтобы не было ошибок
            for i in range(4):
                print(0, file=f)
        # Снова скрываем
        SetFileAttributes('res/screen_sets.txt', 2)


# Класс интерфейса для утилиты - маленькое окошко,
# которое открывается при первом запуске
class WSMGUI:
    def __init__(self, window):
        # Парочка нужных переменных - номер темы и размеры окна программы на
        # будущее, само окно программы и фон окна
        self.theme = -1
        self.screen_size = []
        self.win = window
        self.fld = pygame.image.load('res/wsm/field.png').convert()
        # В каждом из таких словарей при инициализации запишутся
        # объекты интерфойса
        self.zero_objs = {}
        self.first_objs = {}
        self.sec_objs = {}
        self.third_objs = {}
        # Анимации кнопок и полей ввода
        a0 = pygame.image.load('res/wsm/button_off.png').convert()
        a1 = pygame.image.load('res/wsm/button_on.png').convert()
        a2 = pygame.image.load('res/wsm/button_on2.png').convert()
        a3 = pygame.image.load('res/wsm/input_off.png').convert()
        a4 = pygame.image.load('res/wsm/input_on.png').convert()
        # Словари для создания объектов project_R
        t_slovar = {'positions': (15, 3), 'win': self.win,
                    'font': 'res/fonts/Staatliches-Regular.ttf',
                    'text_size': 55, 'color': (255, 0, 0),
                    'text': 'The United Scorer',
                    'color2': (0, 255, 255), 'indent': 1}
        text_slovar = {'positions': (15, 65), 'win': self.win,
                       'font': 'res/fonts/RobotoSlab-Regular.ttf',
                       'text_size': 30, 'color': (255, 255, 255),
                       'text': '''Перед первым запуском US-f-CT необходимо
                       настроить размер окна программы''',
                       'indent': 28, 'max_len': 22}
        rbut_slovar = {'positions': (0, 240), 'win': self.win,
                       'size': (150, 50), 'tap_buts': (1, 3),
                       'animations': [[a0], [a1]]}
        key_slovar = {'positions': (50, 160), 'win': self.win,
                      'size': (150, 50), 'tap_buts': (1, 3),
                      'animations': [[a0], [a2]], 'horizontal': True,
                      'kolvo': 2, 'texts': ['ТЁМНАЯ', 'СВЕТЛАЯ'], 'indent': 0}
        inp_slovar = {'positions': (20, 160), 'win': self.win,
                      'size': (150, 50), 'tap_buts': (1, 3),
                      'animations': [[a3], [a4]], 'active': False,
                      'speed': 25, 'max_len': 5}
        # Далее окнами будут называться элементы графической оболочки
        # программы, содержащие обычно разные элементы интерфейса,
        # между которыми осуществляется переход кнопками
        # На нулевом - текст - описание утилиты, на первом - еще текст,
        # на втором - ввод размера окна, на третьем - выбор темы
        # Создаем заголовок во все окна
        self.zero_objs['title'] = RTitle(t_slovar.copy())
        self.first_objs['title'] = self.zero_objs['title']
        self.sec_objs['title'] = self.zero_objs['title']
        self.third_objs['title'] = self.zero_objs['title']
        # Создаем нужный текст-бокс во все окна, меняя в словаре
        # значение текста
        self.zero_objs['text'] = RTextBox(text_slovar.copy())
        text_slovar['text'] = '''Не закрывайте это окно, иначе программа не
        запустится. Соотношение сторон 16:9 ставится автоматически'''
        self.first_objs['text'] = RTextBox(text_slovar.copy())
        text_slovar['text'] = '''Введите размер экрана в пикселях
        (не ниже 800х450)'''
        self.sec_objs['text'] = RTextBox(text_slovar.copy())
        text_slovar['text'] = 'Выберите тему оформления программы'
        self.third_objs['text'] = RTextBox(text_slovar.copy())
        # Здесь буква х между окнами ввода размера экрана
        text_slovar['text'] = 'х'
        text_slovar['positions'] = [192, 162]
        self.sec_objs['text2'] = RText(text_slovar.copy())
        # Кнопка выхода на все окна
        self.zero_objs['exit'] = RButton(rbut_slovar.copy())
        self.first_objs['exit'] = RButton(rbut_slovar.copy())
        self.sec_objs['exit'] = RButton(rbut_slovar.copy())
        self.third_objs['exit'] = RButton(rbut_slovar.copy())
        # Делаем текст на эти кнопки, на 0 - выход, на 1, 2, 3 - назад
        text_slovar['text'] = 'ВЫХОД'
        text_slovar['positions'] = (19, 244)
        self.zero_objs['exit'].set_text(text_slovar.copy())
        text_slovar['text'] = 'НАЗАД'
        text_slovar['positions'] = (22, 244)
        self.first_objs['exit'].set_text(text_slovar.copy())
        self.sec_objs['exit'].set_text(text_slovar.copy())
        self.third_objs['exit'].set_text(text_slovar.copy())
        rbut_slovar['positions'] = [250, 240]
        # Кнопка далее на все окна, на 2 и 3 она закрыта
        self.zero_objs['ok'] = RButton(rbut_slovar.copy())
        self.first_objs['ok'] = RButton(rbut_slovar.copy())
        self.sec_objs['ok'] = RButton(rbut_slovar.copy())
        self.third_objs['ok'] = RButton(rbut_slovar.copy())
        self.sec_objs['ok'].actived = False
        self.third_objs['ok'].actived = False
        # Делаем текст на эти кнопки, на 0, 1, 2 - далее, на 3 - готово
        text_slovar['text'] = 'ДАЛЕЕ'
        text_slovar['positions'] = (273, 244)
        self.zero_objs['ok'].set_text(text_slovar.copy())
        self.sec_objs['ok'].set_text(text_slovar.copy())
        self.first_objs['ok'].set_text(text_slovar.copy())
        text_slovar['text'] = 'ГОТОВО'
        text_slovar['positions'] = (266, 244)
        self.third_objs['ok'].set_text(text_slovar.copy())
        # Чтобы не создавать новый словарь - меняем в текстовом некоторые
        # значения и отправляем его на создание клавиатуры на
        # 3 окне - выбор темы
        text_slovar['text_size'] = 25
        text_slovar['positions'] = (71, 168)
        text_slovar['indent'] = 146
        self.third_objs['keyboard'] = RKeyboard(key_slovar.copy(),
                                                text_slovar.copy())
        # Чтобы не создавать новый словарь - меняем в текстовом некоторые
        # значения и отправляем его на создание 2 полей ввода на
        # 2 окне - ввод размеров
        text_slovar['text_size'] = 35
        text_slovar['positions'] = (31, 158)
        text_slovar['text'] = 'нажми'
        self.sec_objs['input1'] = RInput(inp_slovar, text_slovar)
        text_slovar['positions'] = (241, 158)
        inp_slovar['positions'] = (230, 160)
        self.sec_objs['input2'] = RInput(inp_slovar, text_slovar)

    # Метод рисует фон
    def print_field(self):
        self.win.blit(self.fld, (0, 0))

    # Метод действий во время работы 0 окна
    def zero_screen(self):
        mouse_pos = pygame.mouse.get_pos()
        # Прорисовываем все объекты, которые можно прорисовать,
        # при этом проверяем их на наведение мыши
        for i in self.zero_objs:
            try:
                self.zero_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.zero_objs[i].draw()
        # Проверка на события, возвращаем некоторые значения при нажатиях на
        # крестик и кнопки - по этим значениям главный цикл определит,
        # что делать дальше
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.zero_objs['ok'].is_tap(event, mouse_pos, 1):
                return 1
            if self.zero_objs['exit'].is_tap(event, mouse_pos, 1):
                return 4

    # Метод действий во время работы 1 окна
    def first_screen(self):
        mouse_pos = pygame.mouse.get_pos()
        # Прорисовываем все объекты, которые можно прорисовать,
        # при этом проверяем их на наведение мыши
        for i in self.first_objs:
            try:
                self.first_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.first_objs[i].draw()
        # Проверка на события, возвращаем некоторые значения при нажатиях на
        # крестик и кнопки - по этим значениям главный цикл определит,
        # что делать дальше
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.first_objs['ok'].is_tap(event, mouse_pos, 1):
                return 1
            if self.first_objs['exit'].is_tap(event, mouse_pos, 1):
                return 4

    # Метод действий во время работы 2 окна
    def second_screen(self):
        # Когда мы вводим размер окна, мы пишем в одно окно ввода, а их 2,
        # поэтому второе надо синхронизировать, для этого вызывается особый
        # метод, о котором позже
        self.equal()
        mouse_pos = pygame.mouse.get_pos()
        try:
            # Проверяем правильность ввода - введены числа, которые не меньше
            # 800 или 450 - ограничения на размер экрана программы, только
            # если все хорошо, кнопка далее включится, иначе она выключится
            prosto_name = int(self.sec_objs['input1'].get_text())
            prosto_name2 = int(self.sec_objs['input2'].get_text())
            self.sec_objs['ok'].actived = True
            if prosto_name < 800 or prosto_name2 < 450:
                self.sec_objs['ok'].actived = False
        except Exception:
            self.sec_objs['ok'].actived = False
        # Прорисовываем все объекты, которые можно прорисовать,
        # при этом проверяем их на наведение мыши
        for i in self.sec_objs:
            try:
                self.sec_objs[i].check(mouse_pos, 1)
            except Exception:
                pass
            self.sec_objs[i].draw()
        for event in pygame.event.get():
            # Активация полей ввода - одновременно может быть включено только
            # одно поле, активируется нажатием на него мышью
            if not(self.sec_objs['input2'].active):
                self.sec_objs['input1'].is_active(event, mouse_pos)
            if not(self.sec_objs['input1'].active):
                self.sec_objs['input2'].is_active(event, mouse_pos)
            # Вводим с клавиатуры в поля, за их активированность можно не
            # беспокоится, проверка есть внутри метода ввода
            self.sec_objs['input1'].input(event)
            self.sec_objs['input2'].input(event)
            # Проверка на события, возвращаем некоторые значения при нажатиях
            # на крестик и кнопки - по этим значениям главный цикл определит,
            # что делать дальше, кроме того, мы сохраняем результат ввода
            # размеров в отдельный список при переходе далее
            if event.type == pygame.QUIT:
                return -1
            if self.sec_objs['ok'].is_tap(event, pygame.mouse.get_pos(), 1):
                self.screen_size = [int(self.sec_objs['input1'].get_text()),
                                    int(self.sec_objs['input2'].get_text())]
                return 1
            if self.sec_objs['exit'].is_tap(event, pygame.mouse.get_pos(), 1):
                return 4

    # Метод действий во время работы 3 окна
    def third_screen(self):
        mouse_pos = pygame.mouse.get_pos()
        # Прорисовываем все объекты, которые можно прорисовать,
        # при этом проверяем их на наведение мыши
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
        # Проверка на события, возвращаем некоторые значения при нажатиях на
        # крестик и кнопки - по этим значениям главный цикл определит,
        # что делать дальше. Здесь немного сложнее, чем раньше - при нажатии
        # на готово - мы сохраняем файл с значениями размеров экрана и темы,
        # + строка 1 показывает, что в программу уже входили
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if self.third_objs['ok'].is_tap(event, mouse_pos, 1):
                try:
                    SetFileAttributes('res/screen_sets.txt', 128)
                except Exception:
                    pass
                with open('res/screen_sets.txt', 'w') as f:
                    print(self.screen_size[0], file=f)
                    print(self.screen_size[1], file=f)
                    print(self.theme, file=f)
                    print(1, file=f)
                # Опять скрываем файл
                SetFileAttributes('res/screen_sets.txt', 2)
                return 1
            if self.third_objs['exit'].is_tap(event, mouse_pos, 1):
                return 4
            # Реакция на нажатия клавиатуры - установка анимаций, запись
            # номера темы в переменную, отключение при повторном нажатии
            result = self.third_objs['keyboard'].taps(event, mouse_pos)
            if result[0]:
                if self.theme == result[1]:
                    self.theme = -1
                else:
                    self.theme = result[1]
                    if self.theme != -1:
                        self.third_objs['keyboard'].\
                            set_default_animation([0, 1], 0)
                        self.third_objs['keyboard'].\
                            set_default_animation([self.theme], 1)

    # Раньше здесь были лямбды для определения другого числа из введенного
    # внутри следующего метода, но пеп8 требует вместо них
    # функции или методы, но переименовывать их и изменять слово "Лямбда" в
    # комментариях мне лень, поэтому вместо лямбда читайте метод
    def lmbd1(self, x):
        return int(int(x) * 9 / 16)

    def lmbd2(self, x):
        return int(int(x) * 16 / 9)

    # Метод синхронизации полей ввода
    def equal(self):
        # Если активно окно ширины, просто вставляем текст сгенерированной
        # лямбдой высоты окна во второе поле
        if self.sec_objs['input1'].active:
            # Сразу покажем, что поля уже были активированы, чтобы при
            # их "первой" активации не сбросился текст
            self.sec_objs['input2'].first = False
            try:
                length = self.lmbd1(self.sec_objs['input1'].get_text())
                self.sec_objs['input2'].new_text(str(length))
            # Если вдруг введено не число, ставим пустой текст
            except Exception:
                self.sec_objs['input2'].new_text('')
        # Если активно поле высоты, аналогично за небольшим исключением - все
        # классические размеры окон считались по ширине,
        # а при расчете по высоте из-за кривого округления может
        # получиться разная ширина, например, ширина 805 -> высота 452,
        # но высота 452 -> ширина 803. Некритично, но некрасиво. Чтобы этого
        # избежать, полученную ширину прогоняем через лямбду1 и сравниваем с
        # высотой. Если надо, прибавляем некоторое количество пикселей
        if self.sec_objs['input2'].active:
            self.sec_objs['input1'].first = False
            height = int(self.sec_objs['input2'].get_text())
            try:
                length = self.lmbd2(self.sec_objs['input2'].get_text())
                if self.lmbd1(length) == height:
                    self.sec_objs['input1'].new_text(str(length))
                else:
                    while self.lmbd1(length) != height:
                        length += 1
                    self.sec_objs['input1'].new_text(str(length))
            except Exception:
                self.sec_objs['input1'].new_text('')
