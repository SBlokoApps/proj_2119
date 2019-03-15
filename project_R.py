import pygame
from pygame.locals import *
from win32api import GetKeyboardLayout, GetKeyState


# Для упрощения создания подобных элементов интерфейса (кнопок, которые
# отличаются только текстом и расположением) аргументы передаются в словаре.
# Описание ключей словаря есть перед каждым классом
#
# Базовый класс - картинка, которая по команде рисуется в заранее заданных
# координатах - почти спрайт, но без лишнего, нужен для других классов
# В словарь нужны positions - координаты левого верхнего угла объекта -
# список или кортеж, picture - отображаемая картинка,
# win - окно, которое объявил pygame
class RBase:
    def __init__(self, slovar):  # Получает минимум аргументов
        self.pos = list(slovar['positions'])  # В один момент в
        # проекте я стал писать координаты в кортеже, а это плохо для
        # выравнивания текста, поэтому мы конвертируем в словарь
        self.pic = slovar['picture']
        self.win = slovar['win']

    def draw(self):  # Согласитесь, прописать метод быстрее, чем команду blit
        self.win.blit(self.pic, self.pos)

    def get_width(self):  # Вернет ширину, прописать метод быстрее на 3 буквы
        return self.pic.get_width()

    def get_height(self):  # Вернет высоту, прописать метод быстрее на 3 буквы
        return self.pic.get_height()


# Класс кнопки, просто кнопка с текстом, которая может менять анимацию
# В словарь нужны positions, win, size - размер кнопки,
# animations список, в нём передаются списки из картинки и
# кортежа нового положения картинки, если оно другое нужно. Для нулевой
# анимации положение не указывается. Например, [[anim0], [anim1, (120, 230)]],
# tap_buts - кортеж из кнопок мыши, на которые реагирует кнопка
# invisible - показывать/не показывать кнопку
class RButton:
    def __init__(self, slovar):
        self.closed = False  # флажок: кнопка включена или нет
        # Запоминаем данные из словаря
        self.pos = slovar['positions']
        self.win = slovar['win']
        self.size = slovar['size']
        self.animations = slovar['animations']
        self.tap_buttons = slovar['tap_buts']
        if 'invisible' in slovar:
            self.inv = True
        else:
            self.inv = False
        self.default = 0  # Анимация по-умолчанию
        self.is_text = False  # показывает, есть ли текст в кнопке, важно
        self.pic = self.animations[0][0]  # В этой переменной хранится
        # анимация, которую надо показать сейчас
        self.text = ''  # На будущее
        # Переменные для задержки показа анимации
        self.already_iters = 0
        self.need_iters = 0

    def new_animation(self, name):  # Если вдруг надо добавить новую анимацию,
        # она добавится в конец, угадайте её номер
        self.animations.append(name)

    def set_inv(self, bool):
        self.inv = bool

    def del_animation(self, num):  # yдалит картинку анимации по её номеру
        del self.animations[num]

    def set_text(self, slovar):  # Добавит текст в кнопку, В словарь нужны
        # positions, win, font - название шрифта, text_size - размер шрифта,
        # color - цвет текста, text - текст текста
        self.is_text = True
        self.text = RText(slovar)  # Создаём текст, с этим классом
        # познакомитесь позже

    def get_text_size(self):  # Вернет размер текста
        return self.text.get_width()

    def move_center_text(self):  # Выравнивает текст по центру кнопки
        self.text.move_center(self.size[0])  # Использует методы, которые
        # есть в классе текста
        self.text.move_center_y(self.size[1])

    def new_text(self, text1):  # Установит новый текст для кнопки
        self.text.new_text(text1)

    def set_animation(self, nom):  # Элементарный метод ставит нужную анимацию
        # Проверка на задержку, при 0 задержка не работает, иначе просто не
        # пускает метод сменить анимацию и прибавляет 1 итерацию
        if 0 < self.already_iters <= self.need_iters:
            self.already_iters += 1
            return
        if len(self.animations[nom]) != 1:
            self.pos = self.animations[nom][1]
        self.pic = self.animations[nom][0]

    def check(self, m_pos, num_animation=0):  # Проверяет,
        # наведен ли курсор мыши на кнопку, ставит нужную анимацию,
        # передаём положение курсора и номер нужной картинки
        if self.closed:
            return False
        # Проверяет, находится ли курсор в кнопке
        if (self.pos[0] <= m_pos[0] <= self.pos[0] + self.size[0])\
                and (self.pos[1] <= m_pos[1] <= self.pos[1] + self.size[1]):
            self.set_animation(num_animation)
            return True
        # Если курсор не наведён, ставит нулевую анимацию
        self.set_animation(self.default)
        return False

    def set_closed_animation(self, anim):  # Ставит анимацию для
        # выключенной кнопки
        self.closed_animat = len(self.animations)
        self.animations.append(anim)

    def is_tap(self, ev, m_pos, num_animation=0):  # Проверяет, нажали ли на
        # кнопку нужной клавишей мыши, ставит анимацию, которая нужна при
        # нажатии принимает событие, положение курсора и номер нужной картинки
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button in self.tap_buttons and self.check(
                    m_pos, num_animation):
                return True
        return False

    def is_enter(self, ev):  # Проверяет нажатие на клавишу enter,
        # можно включать, когда на экране одна кнопка, сам код прост и логичен
        if ev.type == KEYDOWN:
            if ev.key == K_RETURN:
                return True
        return False

    def set_closed(self, flag=True):  # Вкл или выкл кнопки
        self.closed = flag

    def get_closed(self):  # Возвращает статус включенности кнопки
        return self.closed

    # Метод создания задержки в отображении анимации, полезен, когда после
    # нажатия на кнопку надо еще подержать анимацию нажатой кнопки, в метод
    # отправляем количество итераций главного цикла, в течение которых надо
    # сохранять старую картинку
    def delay(self, need):
        # Активируем счетчик итераций
        self.already_iters = 1
        self.need_iters = need

    def draw(self):  # Рисует кнопку в окне в нужных координатах, которые
        # заданы при объявлении, рисует текст кнопки, если такой есть
        if self.inv:
            return
        self.win.blit(self.pic, self.pos)  # Сама картинка
        if self.is_text:  # Именно для этого нам нужен был флажок текста
            self.text.draw()  # Текст может рисоваться своим методом
        if self.closed:  # Если кнопка выключена, рисуется её особая
            # анимация
            try:
                self.win.blit(self.animations[self.closed_animat], self.pos)
            except Exception:
                pass


# Класс строки текста, наследует от базового его минимум методов, чтобы не
# писать их снова
# В словарь нужны positions, win, font - название шрифта, text_size - размер
# шрифта, color - цвет текста, text - текст текста
class RText(RBase):
    def __init__(self, slovar):
        self.font = pygame.font.Font(slovar['font'], slovar['text_size'])
        self.color = slovar['color']
        self.text = slovar['text']
        slovar['picture'] = self.font.render(self.text, True, self.color)
        # Немного поправим словарь, загрузим в него
        # зарендеренный текст как картинку для базового класса
        super().__init__(slovar)  # Не забываем, кого мы наследуем

    def new_text(self, text):  # Если вдруг надо сменить текст, мы снова его
        # рендерим, кидаем сразу в pic
        self.text = text  # Если захотим получить текст кнопки,
        # он должен быть актуален, поэтому обновим его
        self.pic = self.font.render(text, True, self.color)
    # Напоминаю, что метод прорисовки есть в базовом классе

    def move_text_x(self, indent):  # Смещение текста по оси х на indent
        self.pos[0] += indent

    def move_text_y(self, indent):  # Смещение текста по оси у на indent
        self.pos[1] += indent

    def move_center(self, needed_size):  # Ставит текст по центру в ширине,
        # которая передана. При использовании, не забудьте, что у текста уже
        # было свое положение по оси х, оно просто сместится. Если надо
        # поставить текст в центре экрана, начальный х ставьте 0
        # Считает, на сколько надо сместить и смещает
        popravka = (needed_size - self.get_width()) // 2
        self.move_text_x(popravka)

    def move_center_y(self, needed_size):  # Аналогично центрированию по х,
        # но на другой оси
        popravka = (needed_size - self.get_height()) // 2
        self.move_text_y(popravka)

    def move_right(self, needed_size):  # Выравнивание текста по правому краю
        # Надо передать. Чтобы понять, как она работает, проверьте на практике
        # Считает, на сколько надо сместить и смещает
        popravka = (needed_size - self.get_width())
        self.move_text_x(popravka)


# Текст с картинкой на фоне. Нужны словарь1 - полностью как у RText,
# словарь2 полностью как у RBase
class RTextFrame:
    def __init__(self, slovar, slovar2):
        self.base = RBase(slovar2)  # Создаем картинку и текст
        # как отдельные классы
        self.text = RText(slovar)

    def draw(self):  # Прорисовка: сначала картинка, потом текст
        self.base.draw()
        self.text.draw()

    def new_text(self, text):  # Если вдруг надо сменить текст, мы снова его
        # рендерим, кидаем сразу в pic
        self.text.text = text  # Если захотим получить текст кнопки,
        # он должен быть актуален, поэтому обновим его
        self.text.pic = self.text.font.render(text, True, self.text.color)

    def move_center(self):  # Центрирование текста в своей рамке по оси х,
        # метод текста, а размер рамки
        self.text.move_center(self.base.get_width())

    def move_center_y(self):  # Аналогично для оси у
        self.text.move_center_y(self.base.get_height())
# Класс заголовка, просто двойной текст, которым легче управлять,
# чем просто двумя текстами
# В словарь нужны positions, win, font, text_size, color, text,
# color2 - цвет заднего текста, indent - отступ между текстами


class RTitle:
    def __init__(self, slovar):  # В словаре еще нужны второй текст и отступ
        self.text1 = RText(slovar)  # Создаём текст, который будет сверху
        # Немного меняем словарь для заднего текста, нам надо сменить цвет и
        # сделать отступ от координат
        posits = slovar['positions']
        slovar['color'] = slovar['color2']
        slovar['positions'] = [posits[0] + slovar['indent'], posits[1] +
                               slovar['indent']]
        # Создаем второй текст
        self.text2 = RText(slovar)
        self.ind = slovar['indent']

    def new_text(self, text):  # Если вдруг надо заменить текст, вызываем
        # метод замены у каждого текста
        self.text1.new_text(text)
        self.text2.new_text(text)

    def draw(self):  # Прорисовка текста, сначала задний, потом передний
        self.text2.draw()
        self.text1.draw()

    def move_center(self, needed_size):  # Выравнивание заголовка по центру
        # оси х, просто вызываем метод у каждого текста, отступ сохраняется
        # из-за особенностей работы метода
        self.text1.move_center(needed_size)
        self.text2.move_center(needed_size)

    def move_center_y(self, needed_size):  # Аналогично для оси у
        self.text1.move_center_y(needed_size)
        self.text2.move_center_y(needed_size)

    def move_right(self, needed_size):  # Аналогично для для правого края
        self.text1.move_right(needed_size)
        self.text2.move_right(needed_size)


# Класс элемента ввода текста, работает на 2 языка, снован на обычной кнопке
# В словарь нужны positions, size, win,
# animations, active - флаг - включен ввод сразу или нет, tap_buts,
# speed - скорость моргания курсора, max_len - максимальная длина
# отображаемого текста, остальное просто уезжает влево
# В словарь2 нужны positions, win, font, text_size, color,
# text - изначальный текст, который показывается до первого ввода
class RInput(RButton):
    def __init__(self, slovar, slovar2):
        # Добавляем несколько переменных на будущее и словари с сигналами
        # клавиатуры pygame, которым соответствуют символы 2 языков с
        # шифтом и без
        self.slovar1 = slovar.copy()
        self.slovar2 = slovar2.copy()
        self.speed = slovar['speed']
        self.shift = False
        self.timer = slovar['speed']
        self.max_len = slovar['max_len']  # Максимальная длина показываемого
        # текста
        self.active = slovar['active']  # Активно сразу или нет наше поле
        # Словари с соответствием кнопок клавиатуры и символов для 2 языков
        # с шифтом и без
        self.slovar_en = {K_a: 'a', K_b: 'b', K_c: 'c', K_d: 'd', K_e: 'e',
                          K_f: 'f', K_g: 'g', K_h: 'h', K_i: 'i', K_j: 'j',
                          K_k: 'k', K_l: 'l', K_m: 'm', K_n: 'n', K_o: 'o',
                          K_p: 'p', K_q: 'q', K_r: 'r', K_s: 's', K_t: 't',
                          K_u: 'u', K_v: 'v', K_w: 'w', K_x: 'x', K_y: 'y',
                          K_z: 'z', K_0: '0', K_1: '1', K_2: '2', K_3: '3',
                          K_4: '4', K_5: '5', K_6: '6', K_7: '7', K_8: '8',
                          K_9: '9', K_BACKQUOTE: '`', K_MINUS: '-',
                          K_EQUALS: '=', K_LEFTBRACKET: '[',
                          K_RIGHTBRACKET: ']', K_SEMICOLON: ';', K_QUOTE: "'",
                          K_COMMA: ',', K_PERIOD: '.', K_SLASH: '/',
                          K_BACKSLASH: '\\', K_SPACE: '  '}
        self.slovar_en_up = {K_a: 'A', K_b: 'B', K_c: 'C', K_d: 'D', K_e: 'E',
                             K_f: 'F', K_g: 'G', K_h: 'H', K_i: 'I', K_j: 'J',
                             K_k: 'K', K_l: 'L', K_m: 'M', K_n: 'N', K_o: 'O',
                             K_p: 'P', K_q: 'Q', K_r: 'R', K_s: 'S', K_t: 'T',
                             K_u: 'U', K_v: 'V', K_w: 'W', K_x: 'X', K_y: 'Y',
                             K_z: 'Z', K_0: ')', K_1: '!', K_2: '@', K_3: '#',
                             K_4: '$', K_5: '%', K_6: '^', K_7: '&', K_8: '*',
                             K_9: '(', K_BACKQUOTE: '~', K_MINUS: '_',
                             K_EQUALS: '+', K_LEFTBRACKET: '{',
                             K_RIGHTBRACKET: '}', K_SEMICOLON: ':',
                             K_QUOTE: '"', K_COMMA: '<', K_PERIOD: '>',
                             K_SLASH: '?', K_BACKSLASH: '|', K_SPACE: '  '}
        self.slovar_ru = {K_a: 'ф', K_b: 'и', K_c: 'с', K_d: 'в', K_e: 'у',
                          K_f: 'а', K_g: 'п', K_h: 'р', K_i: 'ш', K_j: 'о',
                          K_k: 'л', K_l: 'д', K_m: 'ь', K_n: 'т', K_o: 'щ',
                          K_p: 'з', K_q: 'й', K_r: 'к', K_s: 'ы', K_t: 'е',
                          K_u: 'г', K_v: 'м', K_w: 'ц', K_x: 'ч', K_y: 'н',
                          K_z: 'я', K_0: '0', K_1: '1', K_2: '2', K_3: '3',
                          K_4: '4', K_5: '5', K_6: '6', K_7: '7', K_8: '8',
                          K_9: '9', K_BACKQUOTE: 'ё', K_MINUS: '-',
                          K_EQUALS: '=', K_LEFTBRACKET: 'х',
                          K_RIGHTBRACKET: 'ъ', K_SEMICOLON: 'ж', K_QUOTE: 'э',
                          K_COMMA: 'б', K_PERIOD: 'ю', K_SLASH: '.',
                          K_BACKSLASH: '\\', K_SPACE: '  '}
        self.slovar_ru_up = {K_a: 'Ф', K_b: 'И', K_c: 'С', K_d: 'В', K_e: 'У',
                             K_f: 'А', K_g: 'П', K_h: 'Р', K_i: 'Ш', K_j: 'О',
                             K_k: 'Л', K_l: 'Д', K_m: 'Ь', K_n: 'Т', K_o: 'Щ',
                             K_p: 'З', K_q: 'Й', K_r: 'К', K_s: 'Ы', K_t: 'Е',
                             K_u: 'Г', K_v: 'М', K_w: 'Ц', K_x: 'Ч', K_y: 'Н',
                             K_z: 'Я', K_0: ')', K_1: '!', K_2: '"',
                             K_3: '№', K_4: ';', K_5: '%', K_6: ':',
                             K_7: '?', K_8: '*', K_9: '(', K_BACKQUOTE: 'Ё',
                             K_MINUS: '_', K_EQUALS: '+', K_LEFTBRACKET: 'Х',
                             K_RIGHTBRACKET: 'Ъ', K_SEMICOLON: 'Ж',
                             K_QUOTE: 'Э', K_COMMA: 'Б', K_PERIOD: 'Ю',
                             K_SLASH: ',', K_BACKSLASH: '/', K_SPACE: '  '}
        if not(self.active):
            self.first = True  # Флажок для базового текста, чтобы его убрать
            # при первой активации и текст начинается с пустой строки
        else:
            self.first = False
        # Вспоминаем. кого мы наследуем, сразу поставим текст
        super().__init__(slovar)
        self.set_text(slovar2)

    def check2(self, mouse_pos, new_animat=2):  # Новая проверка
        # на наведение мыши, тк унаследованную портить нельзя
        if not(self.active):
            self.check(mouse_pos, new_animat)

    def is_active(self, ev, mouse_pos):  # Метод активирует поле ввода, ставит
        # нужную анимацию по нажатию мыши, всё очень логично
        if not(self.active):
            if self.is_tap(ev, mouse_pos, 1):
                if self.first:  # Убирает изначальный текст при первой
                    # активации
                    self.first = False
                    self.new_text('')
                self.set_animation(1)
                self.active = True
                return True
            else:
                self.set_animation(0)
                return False
        else:
            if self.is_tap(ev, mouse_pos, 0) or self.is_enter(ev):
                self.set_animation(0)
                self.active = False
                return False
            else:
                self.set_animation(1)
                return True

    def reset(self):  # Просто возврат поля ввода в исходное состояние
        self.__init__(self.slovar1, self.slovar2)

    def draw(self):  # Рисуем нашу почти кнопку с текстом, который уезжает
        # влево, если больше максимальной длины
        if self.active:
            txt = self.text.text[-1*self.max_len:]
            txt2 = self.text.text
            # Добавляем курсор, если пришло его время
            if self.time():
                txt += '|'
            self.new_text(txt)
            super().draw()
            self.new_text(txt2)  # После прорисовки возвращаем текст без
            # курсора
        else:
            super().draw()

    def get_text(self):  # Просто возвращает текст, который сейчас введен
        return self.text.text

    def time(self):  # Таймер для постановки курсора в конце текста, чтобы не
        # забыть, что мы еще пишем, работает элементарно, просто считает
        # количество вызовов, до половины максимума вызовов рисует, потом не
        # рисует (иначе сделать нельзя, тк он будет очень быстро моргать,
        # а так есть задержка)
        if self.timer == self.speed:
            self.timer = 0
        elif 0 < self.timer < self.speed // 2:
            self.timer += 1
            return True
        else:
            self.timer += 1
            return False

    def input(self, event):  # Самая главная часть класса - пишет нужные буквы
        try:
            if self.active:  # Только когда активны
                if event.type == KEYUP:
                    if event.key == K_LSHIFT or event.key == K_RSHIFT:
                        self.shift = False
                    # Если отпустили шифт, программа поймёт
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:  # удаляем последний символ
                        self.text.text = self.text.text[:-1]
                    elif event.key == K_LSHIFT or event.key == K_RSHIFT:
                        self.shift = True
                        # Если нажали шифт, программа поймёт
                    if GetKeyState(0x14):  # Это состояние caps
                        # Caps и shift различаются, поэтомы мы отслеживаем
                        # нажатие капса, добавляем его эффект к подходящему
                        # алфавиту(если также нажат шифт, мы берём большой и
                        # делаем буквы маленькими, а не маленький,
                        # тк тогда не совпадут небуквенные символы)
                        if str(GetKeyboardLayout()) == '68748313':
                            # Это русская раскладка клавиатуры
                            if not self.shift:
                                self.text.text +=\
                                    self.slovar_ru[event.key].upper()
                            else:
                                self.text.text +=\
                                    self.slovar_ru_up[event.key].lower()
                        else:
                            if not self.shift:
                                self.text.text +=\
                                    self.slovar_en[event.key].upper()
                            else:
                                self.text.text +=\
                                    self.slovar_en_up[event.key].lower()
                    else:
                        if str(GetKeyboardLayout()) == '68748313':
                            # Это русская раскладка
                            if not self.shift:
                                self.text.text += self.slovar_ru[event.key]
                            else:
                                self.text.text += self.slovar_ru_up[event.key]
                        else:
                            if not self.shift:
                                self.text.text += self.slovar_en[event.key]
                            else:
                                self.text.text += self.slovar_en_up[event.key]
        except Exception:  # Исключение вылезет, когда нажмете клавишу,
            # не прописанную в словаре букв
            pass
        self.new_text(self.text.text)


# Класс клавиатуры - несколько кнопок в ряд горизонтально или вертикально
# В словарь нужны tap_buts, positions, size, win, animations,
# horizontal - флаг, в какую сторону направлена клавиатура,
# indent - расстояние между кнопками, kolvo - количество кнопок,
# texts - список текстов для кнопок
# В словарь2 нужны positions, win, font, text_size, color, indent -
# расстояние между текстами
class RKeyboard:
    def __init__(self, slovar, slovar2, animations=''):
        # Пропишем переменные, чтобы не писать длинное
        # название словаря с ключем
        pos0 = slovar['positions']
        kolvo = slovar['kolvo']
        size = slovar['size']
        ots = slovar['indent']
        text_pos0 = slovar2['positions']
        text_ots = slovar2['indent']
        texts = slovar['texts']
        self.buts = []  # Здесь будут храниться кнопки
        # Генерируем положения кнопок по горизонтали или вертикали
        if 'animations' not in slovar:
            new_animation = True
        else:
            new_animation = False
        if slovar['horizontal']:
            poses = [[pos0[0] + (ots + size[0]) * i,
                      pos0[1]] for i in range(kolvo)]
            text_poses = [[text_pos0[0] + text_ots * i,
                           text_pos0[1]] for i in range(kolvo)]
        else:
            poses = [[pos0[0],
                      pos0[1] + (ots + size[1]) * i] for i in range(kolvo)]
            text_poses = [[text_pos0[0],
                           text_pos0[1] + text_ots * i] for i in range(kolvo)]
        # Создаём кнопки с текстом в нужных местах с нужным текстом
        for i in range(kolvo):
            try:
                if new_animation:
                    slovar['animations'] = animations[i]
                slovar['positions'] = poses[i]
                self.buts.append(RButton(slovar.copy()))
                slovar2['positions'] = text_poses[i]
                slovar2['text'] = texts[i]
                self.buts[i].set_text(slovar2.copy())
            except Exception:
                pass

    def set_animation(self, nums, animation=0):  # Ставим нужную анимацию на
        # определенные кнопки (передаём список номеров)
        for i in nums:
            self.buts[i].set_animation(animation)

    def set_default_animation(self, nums, anim):
        for i in nums:
            self.buts[i].default = anim

    def check(self, m_pos, animation=1):  # Проверка на наведение курсора всех
        # кнопок одновременно, чтобы было проще
        for i in self.buts:
            i.check(m_pos, animation)

    def taps(self, ev, m_pos, animation=1, delay=1):  # Проверка на нажатие
        # всех кнопок одновременно, вернет текст и номер нажатой кнопки
        # Можно поставить задержку анимации у кнопки
        for i in self.buts:
            if i.is_tap(ev, m_pos, animation):
                if delay > 1:
                    i.delay(delay)
                return [True, self.buts.index(i), i.text.text]
        return [False]

    def draw(self):  # Прорисовка всех кнопок одновременно
        for i in self.buts:
            i.draw()

    def move_center_text(self):  # Центрирование текста в кнопках, проще,
        # чем писать метод для каждой
        for i in self.buts:
            i.move_center_text()


# Особое поле текста, которое равномерно распределяет переданный текст на
# строки равной длины
# В словарь нужны positions, win, font, text_size, color, text,
# indent - расстояние между строками
# max_len - длина строки. Если надо автоматически подогнать текст под
# ширину экрана, в словарь нужны auto - с любым значением, важен сам ключ,
# window_width - нужная ширина текста в пикселях
class RTextBox:
    def __init__(self, slovar):
        slovar['text'] = ' '.join(slovar['text'].split())  # Убираем лишние
        # табы, пробелы и тд, потому что я понимаю, что записать длинный текст
        # и войти в пеп-8 можно только с '''abc''', а это лишние табы перед
        # строкой
        if 'auto' in slovar:  # Если авто, вызываем метод подгона
            slovar['max_len'] = self.auto_detect(slovar.copy())
        # Вызываем особый метод для разбивки текста на строки
        new_text = self.my_split(slovar['text'], slovar['max_len'])
        self.r_texts = []  # Здесь будут строки
        for i in range(len(new_text)):
            # Немного меняем словарь при создании строк
            slovar['text'] = new_text[i]
            if i != 0:
                slovar['positions'] = [slovar['positions'][0],
                                       slovar['positions'][1] +
                                       slovar['indent']]
            # Создаем строки как отдельные тексты
            self.r_texts.append(RText(slovar.copy()))

    # Тот самый метод определения ширины строки
    def auto_detect(self, new_slovar):
        my_len = 1  # Начиная с длины 1
        while True:
            # Мы создаем текст разной длины в символах с данным шрифтом
            new_slovar['text'] = 'a' * my_len
            text = RText(new_slovar.copy())
            # И проверяем его длину, если она меньше, увеличиваем длину
            # строки, иначе возвращаем длину на 1 меньше
            if text.get_width() >= new_slovar['window_width']:
                return my_len - 1
            my_len += 1

    # Делит текст на строки
    def my_split(self, txt, max_len):
        many_txts = []
        stroka = ''
        # Нам надо переносить слова нацело, поэтому делим текст на слова
        txts = txt.split()
        # Сейчас будем добавлять слова в строки и смотреть на их длину
        for i in range(len(txts)):
            # Есть кодовое слово на перенос строки, оно сразу добавляет
            # сформированную строку и делает пустую
            if txts[i] == '*#enter#*':
                many_txts.append(stroka)
                stroka = ''
            # Если при добавлении слова к строке, длина будет нормальной, мы
            # просто добавляем в строку слово
            # Но если строка была не пустая, нам надо добавить пробел
            elif len(stroka + txts[i]) + 1 <= max_len and stroka == '':
                stroka += txts[i]
            elif len(stroka + txts[i]) + 1 <= max_len:
                stroka += ' '
                stroka += txts[i]
            # Иначе выкидываем строку в список и создаем пустую
            else:
                many_txts.append(stroka)
                stroka = txts[i]
        # Добавляем последнюю строку и отправляем результат
        many_txts.append(stroka)
        return many_txts

    # Прорисовка текста - прорисовка каждой строки
    def draw(self):
        for i in self.r_texts:
            i.draw()

    # Выравнивание по правому краю - выравнивание каждой строки
    def move_right(self, needed_size):
        for i in self.r_texts:
            i.move_right(needed_size)

    # Выравнивание по центру - выравнивание каждой строки
    def move_center(self, needed_size):
        for i in self.r_texts:
            i.move_center(needed_size)


# Поле заголовка, аналогичное RTextBox, но строки созданы классом RTitle, а
# не RText
# В словарь нужны positions, win, font, text_size, color, text,
# color2 - цвет заднего текста, indent - отступ между текстом и фоном
# indent2 - расстояние между строками
# max_len - длина строки. Если надо автоматически подогнать текст под
# ширину экрана, в словарь нужны auto - с любым значением, важен сам ключ,
# window_width - нужная ширина текста в пикселях
class RTitleBox:
    def __init__(self, slovar):
        slovar['text'] = ' '.join(slovar['text'].split())  # Убираем лишние
        # табы, пробелы и тд, потому что я понимаю, что записать длинный текст
        # и войти в пеп-8 можно только с '''abc''', а это лишние табы перед
        # строкой
        if 'auto' in slovar:  # Если авто, вызываем метод подгона
            slovar['max_len'] = self.auto_detect(slovar.copy())
        # Вызываем особый метод для разбивки текста на строки
        new_text = self.my_split(slovar['text'], slovar['max_len'])
        self.r_texts = []  # Здесь будут строки
        for i in range(len(new_text)):
            # Немного меняем словарь при создании строк
            if i != 0:
                slovar['positions'] = [slovar['positions'][0],
                                       slovar['positions'][1] +
                                       slovar['indent2']]
            self.r_texts.append(RTitle(slovar.copy()))

    # Тот самый метод определения ширины строки
    def auto_detect(self, new_slovar):
        my_len = 1  # Начиная с длины 1
        while True:
            # Мы создаем текст разной длины в символах с данным шрифтом
            new_slovar['text'] = 'a' * my_len
            text = RText(new_slovar.copy())
            # И проверяем его длину, если она меньше, увеличиваем длину
            # строки, иначе возвращаем длину на 1 меньше
            if text.get_width() >= new_slovar['window_width']:
                return my_len - 1
            my_len += 1

    # Делит текст на строки
    def my_split(self, txt, max_len):
        many_txts = []
        stroka = ''
        # Нам надо переносить слова нацело, поэтому делим текст на слова
        txts = txt.split()
        # Сейчас будем добавлять слова в строки и смотреть на их длину
        for i in range(len(txts)):
            # Есть кодовое слово на перенос строки, оно сразу добавляет
            # сформированную строку и делает пустую
            if txts[i] == '*#enter#*':
                many_txts.append(stroka)
                stroka = ''
            # Если при добавлении слова к строке, длина будет нормальной, мы
            # просто добавляем в строку слово
            # Но если строка была не пустая, нам надо добавить пробел
            elif len(stroka + txts[i]) + 1 <= max_len and stroka == '':
                stroka += txts[i]
            elif len(stroka + txts[i]) + 1 <= max_len:
                stroka += ' '
                stroka += txts[i]
            # Иначе выкидываем строку в список и создаем пустую
            else:
                many_txts.append(stroka)
                stroka = txts[i]
        # Добавляем последнюю строку и отправляем результат
        many_txts.append(stroka)
        return many_txts

    # Прорисовка текста - прорисовка каждой строки
    def draw(self):
        for i in self.r_texts:
            i.draw()

    # Выравнивание по правому краю - выравнивание каждой строки
    def move_right(self, needed_size):
        for i in self.r_texts:
            i.move_right(needed_size)

    # Выравнивание по центру - выравнивание каждой строки
    def move_center(self, needed_size):
        for i in self.r_texts:
            i.move_center(needed_size)


class RItemList:
    def __init__(self):
        self.list = []

    def append(self, item):
        self.list.append(item)

    def draw(self):
        for i in self.list:
            i.draw()
