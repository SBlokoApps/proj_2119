import pygame
from pygame.locals import *
from win32api import GetKeyboardLayout, GetKeyState


def default(*buts):
    for i in buts:
        i.set_Animation(0)


# Для упрощения создания подобных элементов интерфейса (кнопок, которые отличаются только текстом и расположением)
# аргументы передаются в словаре. Описание ключей словаря ниже
# positions координаты левого верхнего угла объекта - список
# size размеры объекта - список
# animations картинки для анимации кнопок - список
# win окно, которое объявил pygame
# picture просто картинка для RBase/фон диалогового окна
# tap_buts - список номеров кнопок мыши, которыми можно нажать
# text строка текста, которая будет выводиться в кнопке/текстовом поле
# font название шрифта для текста
# text_size размер шрифта у текста
# color кортеж из трех чисел для цвета текста
# color2 аналогично для тени заголовка
# indent расстояние между текстом и тенью в заголовке
# speed скорость моргания курсора в текстовом поле
# max_len
# active
# kolvo
# horizontal
# texts
#
# Базовый класс - картинка, которая по команде рисуется в заранее заданных координатах
class RBase:
    def __init__(self, slovar):  # Получает минимум аргументов
        self.pos = slovar['positions']
        self.pic = slovar['picture']
        self.win = slovar['win']

    def draw(self):  # Согласитесь, прописать метод быстрее, чем команду blit
        self.win.blit(self.pic, self.pos)


# Класс кнопки, просто кнопка с текстом, которая может менять анимацию
class RButton:
    def __init__(self, slovar):  # Принимаем словарь, но в нём уже нужны анимация, номера кнопок мыши
        self.pos = slovar['positions']
        self.win = slovar['win']
        self.size = slovar['size']
        self.animations = slovar['animations']
        self.tap_buttons = slovar['tap_buts']
        self.is_text = False  # оказывает, есть ли текст в кнопке, очень важно
        self.pic = self.animations[0]  # В этой переменной хранится анимация, которую надо показать сейчас
        self.text = ''  # На будущее

    def new_animation(self, name):  # Если вдруг надо добавить новую анимацию, она добавится в конец, угадайте её номер
        self.animations.append(name)

    def del_animation(self, num):  # далит картинку анимации по её номеру
        del self.animations[num]

    def set_text(self, slovar):  # Добавит текст в кнопку, в словаре настройки текста
        self.is_text = True
        self.text = RText(slovar)  # Создаём текст, с этим классом познакомитесь позже

    def new_text(self, text1):  # Установит новый текст для кнопки
        self.text.new_text(text1)

    def set_animation(self, nom):  # Элементарный метод, ставит нужную анимацию
        self.pic = self.animations[nom]

    def check(self, m_pos, num_animation=0, old_animation=0):  # Проверяет, наведен ли курсор мыши на кнопку, ставит нужную анимацию,
        # передаём положение курсора и номер нужной картинки
        if (self.pos[0] <= m_pos[0] <= self.pos[0] + self.size[0])\
                and (self.pos[1] <= m_pos[1] <= self.pos[1] + self.size[1]):
            self.set_animation(num_animation)
            return True
        # Если курсор не наведён, ставит нулевую анимацию
        self.set_animation(0)
        return False

    def is_tap(self, ev, m_pos, num_animation=0):  # Проверяет, нажали ли на кнопку нужной клавишей мыши, ставит
        # анимацию, которая нужна при нажатии, принимает событие, положение курсора и номер нужной картинки
        if ev.type == pygame.MOUSEBUTTONUP and ev.button in self.tap_buttons and self.check(m_pos, num_animation):
            return True
        return False

    def draw(self):  # Рисует кнопку в окне в нужных координатах, которые заданы при объявлении, рисует текст кнопки,
        # если такой есть
        self.win.blit(self.pic, self.pos)  # Сама картинка
        if self.is_text:  # Именно для этого нам нужен был флажок текста
            self.text.draw()  # Текст может рисоваться своим методом


# Класс строки текста, наследует от базового его минимум методов, чтобы не писать их снова
class RText(RBase):
    def __init__(self, slovar):  # Снова словарь, но с настройками текста
        self.font = pygame.font.Font(slovar['font'], slovar['text_size'])
        self.color = slovar['color']
        self.text = slovar['text']
        slovar['picture'] = self.font.render(self.text, True, self.color)  # Немного поправим словарь, загрузим в него
        # зарендеренный текст как картинку для базового класса
        super().__init__(slovar)  # Не забываем, кого мы наследуем

    def new_text(self, text):  # Если вдруг надо сменить текст, мы снова его рендерим, кидаем сразу в pic
        self.text = text  # Если захотим получить текст кнопки, он должен быть актуален, поэтому обновим его
        self.pic = self.font.render(text, True, self.color)
    # Напоминаю, что метод прорисовки есть в базовом классе


# Класс заголовка, просто двойной текст, которым легче управлять, чем просто двумя текстами
class RTitle:
    def __init__(self, slovar):  # В словаре еще нужны второй текст и отступ
        self.text1 = RText(slovar)  # Создаём текст, который будет сверху
        # Немного меняем словарь для заднего текста, нам надо сменить цвет и сделать отступ
        posits = slovar['pos']
        slovar['color'] = slovar['color2']
        slovar['pos'] = [posits[0] + slovar['indent'], posits[1] + slovar['indent']]
        self.text2 = RText(slovar)

    def new_text(self, text):  # Если вдруг надо заменить текст
        self.text1.new_text(text)
        self.text2.new_text(text)

    def draw(self):  # Прорисовка текста, сначала задний, потом передний
        self.text2.draw()
        self.text1.draw()


# Класс элемента ввода текста, принимает 2 языка, снован на обычной кнопке
class RInput(RButton):
    def __init__(self, slovar, slovar2):  # Первый словарь содержит настройки кнопки, второй содержит настройки текста
        # Во втором словаре надо передать текст, который будет написан до ввода
        # Добавляем несколько переменных на будущее и словари с сигналами клавиатуры pygame, которым соответствуют
        # символы 2 языков с шифтом и без
        self.speed = slovar['speed']
        self.shift = False
        self.timer = slovar['speed']
        self.max_len = slovar['max_len']  # Максимальная длина показываемого текста, остальную часть он просто скроет
        self.active = slovar['active']  # Активно сразу или нет наше поле ввода
        self.slovar_en = {K_a: 'a', K_b: 'b', K_c: 'c', K_d: 'd', K_e: 'e', K_f: 'f', K_g: 'g', K_h: 'h', K_i: 'i',
                          K_j: 'j', K_k: 'k', K_l: 'l', K_m: 'm', K_n: 'n', K_o: 'o', K_p: 'p', K_q: 'q', K_r: 'r',
                          K_s: 's', K_t: 't', K_u: 'u', K_v: 'v', K_w: 'w', K_x: 'x', K_y: 'y', K_z: 'z', K_0: '0',
                          K_1: '1', K_2: '2', K_3: '3', K_4: '4', K_5: '5', K_6: '6', K_7: '7', K_8: '8', K_9: '9',
                          K_BACKQUOTE: '`', K_MINUS: '-', K_EQUALS: '=', K_LEFTBRACKET: '[', K_RIGHTBRACKET: ']',
                          K_SEMICOLON: ';', K_QUOTE: "'", K_COMMA: ',', K_PERIOD: '.', K_SLASH: '/', K_BACKSLASH: '\\',
                          K_SPACE: '  '}
        self.slovar_en_up = {K_a: 'A', K_b: 'B', K_c: 'C', K_d: 'D', K_e: 'E', K_f: 'F', K_g: 'G', K_h: 'H', K_i: 'I',
                             K_j: 'J', K_k: 'K', K_l: 'L', K_m: 'M', K_n: 'N', K_o: 'O', K_p: 'P', K_q: 'Q', K_r: 'R',
                             K_s: 'S', K_t: 'T', K_u: 'U', K_v: 'V', K_w: 'W', K_x: 'X', K_y: 'Y', K_z: 'Z', K_0: ')',
                             K_1: '!', K_2: '@', K_3: '#', K_4: '$', K_5: '%', K_6: '^', K_7: '&', K_8: '*', K_9: '(',
                             K_BACKQUOTE: '~', K_MINUS: '_', K_EQUALS: '+', K_LEFTBRACKET: '{', K_RIGHTBRACKET: '}',
                             K_SEMICOLON: ':', K_QUOTE: '"', K_COMMA: '<', K_PERIOD: '>', K_SLASH: '?',
                             K_BACKSLASH: '|', K_SPACE: '  '}
        self.slovar_ru = {K_a: 'ф', K_b: 'и', K_c: 'с', K_d: 'в', K_e: 'у', K_f: 'а', K_g: 'п', K_h: 'р', K_i: 'ш',
                          K_j: 'о', K_k: 'л', K_l: 'д', K_m: 'ь', K_n: 'т', K_o: 'щ', K_p: 'з', K_q: 'й', K_r: 'к',
                          K_s: 'ы', K_t: 'е', K_u: 'г', K_v: 'м', K_w: 'ц', K_x: 'ч', K_y: 'н', K_z: 'я', K_0: '0',
                          K_1: '1', K_2: '2', K_3: '3', K_4: '4', K_5: '5', K_6: '6', K_7: '7', K_8: '8', K_9: '9',
                          K_BACKQUOTE: 'ё', K_MINUS: '-', K_EQUALS: '=', K_LEFTBRACKET: 'х', K_RIGHTBRACKET: 'ъ',
                          K_SEMICOLON: 'ж', K_QUOTE: 'э', K_COMMA: 'б', K_PERIOD: 'ю', K_SLASH: '.', K_BACKSLASH: '\\',
                          K_SPACE: '  '}
        self.slovar_ru_up = {K_a: 'Ф', K_b: 'И', K_c: 'С', K_d: 'В', K_e: 'У', K_f: 'А', K_g: 'П', K_h: 'Р', K_i: 'Ш',
                             K_j: 'О', K_k: 'Л', K_l: 'Д', K_m: 'Ь', K_n: 'Т', K_o: 'Щ', K_p: 'З', K_q: 'Й', K_r: 'К',
                             K_s: 'Ы', K_t: 'Е', K_u: 'Г', K_v: 'М', K_w: 'Ц', K_x: 'Ч', K_y: 'Н', K_z: 'Я', K_0: ')',
                             K_1: '!', K_2: '"', K_3: '№', K_4: ';', K_5: '%', K_6: ':', K_7: '?', K_8: '*', K_9: '(',
                             K_BACKQUOTE: 'Ё', K_MINUS: '_', K_EQUALS: '+', K_LEFTBRACKET: 'Х', K_RIGHTBRACKET: 'Ъ',
                             K_SEMICOLON: 'Ж', K_QUOTE: 'Э', K_COMMA: 'Б', K_PERIOD: 'Ю', K_SLASH: ',',
                             K_BACKSLASH: '/', K_SPACE: '  '}
        if not(self.active):
            self.first = True  # Флажок для базового текста, чтобы его убрать при первой активации
        else:
            self.first = False
        # Вспоминаем. кого мы наследуем, сразу поставим текст
        super().__init__(slovar)
        self.set_text(slovar2)

    def actived(self, ev, mouse_pos):  # Метод активирует поле ввода и ставит нужную анимацию по нажатию мыши
        if not(self.active):
            if self.is_tap(ev, mouse_pos, 2):
                if self.first:
                    self.first = False
                    self.new_text('')
                self.set_animation(2)
                self.active = True
            else:
                self.set_animation(0)
        else:
            if self.is_tap(ev, mouse_pos, 0):
                self.set_animation(0)
                self.active = False
            else:
                self.set_animation(2)

    def draw(self):  # Рисуем нашу почти кнопку с текстом, который уезжает влево, если больше максимальной длины
        if self.active:
            txt = self.text.text[-1*self.max_len:]
            txt2 = self.text.text
            # Добавляем курсор, если пришло его время
            if self.time():
                txt += '|'
            self.new_text(txt)
            super().draw()
            self.new_text(txt2)  # После прорисовки возвращаем текст без курсора
        else:
            super().draw()

    def time(self):  # Таймер для постановки курсора в конце текста, чтобы не забыть, что мы еще пишем, работает
        # элементарно, просто считает количество вызовов, до половины максимума вызовов рисует, потом не рисует (иначе
        # сделать нельзя, тк он будет очень быстро моргать, а так есть задержка)
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
                if event.type == KEYUP and (event.key == K_LSHIFT or event.key == K_RSHIFT):
                    self.shift = False  # Если отпустили шифт, программа поймёт
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:  # удаляем последний символ
                        self.text.text = self.text.text[:-1]
                    elif event.key == K_LSHIFT or event.key == K_RSHIFT:
                        self.shift = True  # Если нажали шифт, программа поймёт
                    if GetKeyState(0x14):  # Caps и shift различаются, поэтомы мы отслеживаем нажатие капса, добавляем
                        # его эффект к подходящему алфавиту(если также нажат шифт, мы берём большой и делаем буквы
                        # маленькими, а не маленький, тк тогда не совпадут небуквенные символы)
                        if str(GetKeyboardLayout()) == '68748313':  # Это русский
                            if not self.shift:
                                self.text.text += self.slovar_ru[event.key].upper()
                            else:
                                self.text.text += self.slovar_ru_up[event.key].lower()
                        else:
                            if not self.shift:
                                self.text.text += self.slovar_en[event.key].upper()
                            else:
                                self.text.text += self.slovar_en_up[event.key].lower()
                    else:
                        if str(GetKeyboardLayout()) == '68748313':  # Это русский
                            if not self.shift:
                                self.text.text += self.slovar_ru[event.key]
                            else:
                                self.text.text += self.slovar_ru_up[event.key]
                        else:
                            if not self.shift:
                                self.text.text += self.slovar_en[event.key]
                            else:
                                self.text.text += self.slovar_en_up[event.key]
        except Exception:  # Исключение вылезет, когда нажмете клавишу, не прописанную в словаре букв
            pass


# Класс клавиатуры - несколько кнопок в ряд горизонтально или вертикально
class RKeyboard:
    def __init__(self, slovar, slovar2):  # Первый словарь содержит настройки кнопки, второй содержит настройки текста
        pos0 = slovar['positions']
        kolvo = slovar['kolvo']
        size = slovar['size']
        ots = slovar['indent']
        text_ots = slovar2['indent']
        texts = slovar['texts']
        self.buts = []
        if slovar['horizontal']:
            poses = [[pos0[0] + (ots + size[0]) * i, pos0[1]] for i in range(kolvo)]
            indents = [text_ots, 0]
        else:
            poses = [[pos0[0], pos0[1] + (ots + size[1]) * i] for i in range(kolvo)]
            indents = [0, text_ots]
        for i in range(kolvo):
            try:
                slovar['positions'] = poses[i]
                self.buts.append(RButton(slovar))
                slovar2['positions'] = [poses[i][0] + indents[0], poses[i][1] + indents[1]]
                slovar2['text'] = texts[i]
                self.buts[i].set_text(slovar2)
            except Exception:
                pass

    def set_animation(self, noms, animation=0):
        for i in noms:
            self.buts[i].set_animation(animation)

    def new_animation(self, noms, animation=''):
        for i in noms:
            self.buts[i].new_animation(animation)

    def check(self, m_pos):
        for i in self.buts:
            if i.check(m_pos, 1):
                i.set_animation(1)
            else:
                i.set_animation(0)

    def taps(self, ev, m_pos):
        for i in self.buts:
            if i.is_tap(ev, m_pos, 1):
                return [True, self.buts.index(i), i.text.text]
        return [False]

    def draw(self):
        print(0)
        print(self.buts)
        for i in self.buts:
            i.draw()
