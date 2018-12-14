import pygame
from pygame.locals import *
from win32api import GetKeyboardLayout



def default(*buts):
    for i in buts:
        i.set_Animation(0)


class RBase:
    def __init__(self, picture, positions, win):
        self.pos = positions
        self.pic = picture
        self.win = win

    def draw(self):
        self.win.blit(self.pic, self.pos)


class RButton(RBase):
    def __init__(self, size, pos, an0, an1, win, tap_button=1):
        self.size = size
        self.animations = []
        self.tap_button = tap_button
        self.is_text = False
        super().__init__('', pos, win)
        self.new_Animation(an0)
        self.new_Animation(an1)
        self.pic = an0

    def new_Animation(self, name):
        self.animations.append(name)

    def set_text(self, text, pos, font='freesansbold.ttf', size=30, color=(0, 0, 0)):
        self.is_text = True
        self.text = RText(text, pos, self.win, font, size, color)

    def set_Animation(self, nom):
        self.pic = self.animations[nom]

    def check(self, pos1, a1):
        if (self.pos[0] <= pos1[0] <= self.pos[0] + self.size[0])\
                and (self.pos[1] <= pos1[1] <= self.pos[1] + self.size[1]):
            self.set_Animation(a1)
            return True
        self.set_Animation(0)
        return False

    def is_tap(self, ev, pos1, a1):
        if ev.type == pygame.MOUSEBUTTONUP and ev.button == self.tap_button and self.check(pos1, a1):
            return True
        return False

    def draw(self):
        if self.is_text:
            self.win.blit(self.pic, self.pos)
            self.text.draw()
        else:
            super().draw()


class RText(RBase):
    def __init__(self, text, pos, win, font='freesansbold.ttf', size=30, color=(0, 0, 0)):
        self.font = pygame.font.Font(font, size)
        self.color = color
        self.text = text
        render_text = self.font.render(text, True, self.color)
        super().__init__(render_text, pos, win)

    def new_text(self, text):
        self.text = text
        self.pic = self.font.render(text, True, self.color)


class RTitle:
    def __init__(self, text, pos, win, font='freesansbold.ttf', size=80, color1=(50, 0, 200), color2=(0, 0, 0), ind=1):
        self.t1 = RText(text, [pos[0]-ind, pos[1]-ind], win, font, size, color1)
        self.t2 = RText(text, [pos[0]+ind, pos[1]+ind], win, font, size, color2)

    def new_text(self, text):
        self.t1.new_text(text)
        self.t2.new_text(text)

    def draw(self):
        self.t2.draw()
        self.t1.draw()


class RInput(RBase):
    def __init__(self, pos, win, font='freesansbold.ttf', size=30, color=(0, 0, 0), speed=20, base='>', max=32):
        self.base = base
        self.text = ''
        self.speed = speed
        self.max = max
        self.window = win
        self.font = pygame.font.Font(font, size)
        self.color = color
        self.sh = False
        self.timer = speed
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
        super().__init__('', pos, win)

    def print(self):
        txt = self.base + self.text
        if self.time():
            txt += '|'
        self.pic = self.font.render(txt, True, self.color)
        super().draw()

    def time(self):
        if self.timer == self.speed:
            self.timer = 0
        elif 0 < self.timer < self.speed // 2:
            self.timer += 1
            return True
        else:
            self.timer += 1
            return False

    def input(self, event):
        try:
            if event.type == KEYUP and (event.key == K_LSHIFT or event.key == K_RSHIFT):
                self.sh = False
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == K_LSHIFT or event.key == K_RSHIFT:
                    self.sh = True
                elif str(GetKeyboardLayout()) == '68748313':
                    if not self.sh:
                        self.text += self.slovar_ru[event.key]
                    else:
                        self.text += self.slovar_ru_up[event.key]
                else:
                    if not self.sh:
                        self.text += self.slovar_en[event.key]
                    else:
                        self.text += self.slovar_en_up[event.key]

        except Exception:
            pass


class RDialogSimple:
    pass


class RDialogInput:
    pass


class Keyboard:
    def __init__(self, pos, kolvo, win, texts, ind_size, hor=True, text_ots=(3, 3), font='freesansbold.ttf', size=30,
                 color=(0, 0, 0), ots=0):
        self.window = win
        self.font = pygame.font.Font(font, size)
        self.color = color
        self.pos = pos
        self.kolvo = kolvo
        self.size = ind_size
        self.ots = ots
        self.buts = []
        if hor:
            poses = [[pos[0] + (ots+ind_size[0]) * i, pos[1]] for i in range(kolvo)]
        for i in range(kolvo):
            try:
                self.buts.append(RButton(ind_size, poses[i], win))
                self.buts[i].set_text(texts[i], [poses[i][0] + text_ots[0], poses[i][1] + text_ots[1]])
            except Exception:
                pass

    def set_Animation(self, noms, animation=0):
        for i in noms:
            self.buts[i].set_Animation(animation)

    def new_Animation(self, noms, animation=''):
        for i in noms:
            self.buts[i].new_Animation(animation)

    def proverka(self, m_pos):
        for i in self.buts:
            if i.check(m_pos):
                i.set_Animation(1)
            else:
                i.set_Animation(0)

    def taps(self, ev, m_pos):
        for i in self.buts:
            if i.is_tap(ev, m_pos):
                return [True, i.text.text]
        return [False]

    def draw(self):
        for i in self.buts:
            i.draw()
