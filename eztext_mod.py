# -*- coding: utf-8 -*-
# input lib
#http://www.pygame.org/project-EzText-920-.html
#mod by mailbloko@gmail.com
from pygame.locals import *
import pygame, string
from win32api import GetKeyboardLayout

class ConfigError(KeyError): pass

class Config:
    """ A utility for configuration """
    def __init__(self, options, *look_for):
        assertions = []
        for key in look_for:
            if key[0] in options.keys(): exec('self.'+key[0]+' = options[\''+key[0]+'\']')
            else: exec('self.'+key[0]+' = '+key[1])
            assertions.append(key[0])
        for key in options.keys():
            if key not in assertions: raise ConfigError(key+' not expected as option')

class Input:
    """ A text input for pygame apps """
    def __init__(self, **options):
        """ Options: x, y, font, color, restricted, maxlength, prompt """
        self.options = Config(options, ['x', '0'], ['y', '0'], ['font', 'pygame.font.Font(None, 32)'],
                              ['color', '(0,0,0)'],
                              ['maxlength', '-1'], ['prompt', '\'\''])
        self.x = self.options.x; self.y = self.options.y
        self.font = self.options.font
        self.color = self.options.color
        self.maxlength = self.options.maxlength
        self.prompt = self.options.prompt; self.value = ''
        self.shifted = False

    def set_pos(self, x, y):
        """ Set the position to x, y """
        self.x = x
        self.y = y

    def set_font(self, font):
        """ Set the font for the input """
        self.font = font

    def draw(self, surface):
        """ Draw the text input to a surface """
        text = self.font.render(self.prompt+self.value, 1, self.color)
        surface.blit(text, (self.x, self.y))

    def update(self, events):
        """ Update the input based on passed events """
        for event in events:
            if event.type == KEYUP:
                if event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = False
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE: self.value = self.value[:-1]
                elif event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = True
                elif event.key == K_SPACE: self.value += ' '
                if str(GetKeyboardLayout()) =='68748313':
                    if not self.shifted:
                        if event.key == K_a: self.value += 'ф'
                        elif event.key == K_b: self.value += 'и'
                        elif event.key == K_c: self.value += 'с'
                        elif event.key == K_d: self.value += 'в'
                        elif event.key == K_e: self.value += 'у'
                        elif event.key == K_f: self.value += 'а'
                        elif event.key == K_g: self.value += 'п'
                        elif event.key == K_h: self.value += 'р'
                        elif event.key == K_i: self.value += 'ш'
                        elif event.key == K_j: self.value += 'о'
                        elif event.key == K_k: self.value += 'л'
                        elif event.key == K_l: self.value += 'д'
                        elif event.key == K_m: self.value += 'ь'
                        elif event.key == K_n: self.value += 'т'
                        elif event.key == K_o: self.value += 'щ'
                        elif event.key == K_p: self.value += 'з'
                        elif event.key == K_q: self.value += 'й'
                        elif event.key == K_r: self.value += 'к'
                        elif event.key == K_s: self.value += 'ы'
                        elif event.key == K_t: self.value += 'е'
                        elif event.key == K_u: self.value += 'г'
                        elif event.key == K_v: self.value += 'м'
                        elif event.key == K_w: self.value += 'ц'
                        elif event.key == K_x: self.value += 'ч'
                        elif event.key == K_y: self.value += 'н'
                        elif event.key == K_z: self.value += 'я'
                        elif event.key == K_0: self.value += '0'
                        elif event.key == K_1: self.value += '1'
                        elif event.key == K_2: self.value += '2'
                        elif event.key == K_3: self.value += '3'
                        elif event.key == K_4: self.value += '4'
                        elif event.key == K_5: self.value += '5'
                        elif event.key == K_6: self.value += '6'
                        elif event.key == K_7: self.value += '7'
                        elif event.key == K_8: self.value += '8'
                        elif event.key == K_9: self.value += '9'
                        elif event.key == K_BACKQUOTE: self.value += 'ё'
                        elif event.key == K_MINUS: self.value += '-'
                        elif event.key == K_EQUALS: self.value += '='
                        elif event.key == K_LEFTBRACKET: self.value += 'х'
                        elif event.key == K_RIGHTBRACKET: self.value += 'ъ'
                        elif event.key == K_BACKSLASH: self.value += '\\'
                        elif event.key == K_SEMICOLON: self.value += 'ж'
                        elif event.key == K_QUOTE: self.value += 'э'
                        elif event.key == K_COMMA: self.value += 'б'
                        elif event.key == K_PERIOD: self.value += 'ю'
                        elif event.key == K_SLASH: self.value += '.'
                    elif self.shifted:
                        if event.key == K_a: self.value += 'Ф'
                        elif event.key == K_b: self.value += 'И'
                        elif event.key == K_c: self.value += 'С'
                        elif event.key == K_d: self.value += 'В'
                        elif event.key == K_e: self.value += 'У'
                        elif event.key == K_f: self.value += 'А'
                        elif event.key == K_g: self.value += 'П'
                        elif event.key == K_h: self.value += 'Р'
                        elif event.key == K_i: self.value += 'Ш'
                        elif event.key == K_j: self.value += 'О'
                        elif event.key == K_k: self.value += 'Л'
                        elif event.key == K_l: self.value += 'Д'
                        elif event.key == K_m: self.value += 'Ь'
                        elif event.key == K_n: self.value += 'Т'
                        elif event.key == K_o: self.value += 'Щ'
                        elif event.key == K_p: self.value += 'З'
                        elif event.key == K_q: self.value += 'Й'
                        elif event.key == K_r: self.value += 'К'
                        elif event.key == K_s: self.value += 'Ы'
                        elif event.key == K_t: self.value += 'Е'
                        elif event.key == K_u: self.value += 'Г'
                        elif event.key == K_v: self.value += 'М'
                        elif event.key == K_w: self.value += 'Ц'
                        elif event.key == K_x: self.value += 'Ч'
                        elif event.key == K_y: self.value += 'Н'
                        elif event.key == K_z: self.value += 'Я'
                        elif event.key == K_0: self.value += ')'
                        elif event.key == K_1: self.value += '!'
                        elif event.key == K_2: self.value += '"'
                        elif event.key == K_3: self.value += '№'
                        elif event.key == K_4: self.value += ';'
                        elif event.key == K_5: self.value += '%'
                        elif event.key == K_6: self.value += ':'
                        elif event.key == K_7: self.value += '?'
                        elif event.key == K_8: self.value += '*'
                        elif event.key == K_9: self.value += '('
                        elif event.key == K_BACKQUOTE: self.value += 'Ё'
                        elif event.key == K_MINUS: self.value += '_'
                        elif event.key == K_EQUALS: self.value += '+'
                        elif event.key == K_LEFTBRACKET: self.value += 'Х'
                        elif event.key == K_RIGHTBRACKET: self.value += 'Ъ'
                        elif event.key == K_BACKSLASH: self.value += '/'
                        elif event.key == K_SEMICOLON: self.value += 'Ж'
                        elif event.key == K_QUOTE: self.value += 'Э'
                        elif event.key == K_COMMA: self.value += 'Б'
                        elif event.key == K_PERIOD: self.value += 'Ю'
                        elif event.key == K_SLASH: self.value += ','
                else:
                    if not self.shifted:
                        if event.key == K_a: self.value += 'a'
                        elif event.key == K_b: self.value += 'b'
                        elif event.key == K_c: self.value += 'c'
                        elif event.key == K_d: self.value += 'd'
                        elif event.key == K_e: self.value += 'e'
                        elif event.key == K_f: self.value += 'f'
                        elif event.key == K_g: self.value += 'g'
                        elif event.key == K_h: self.value += 'h'
                        elif event.key == K_i: self.value += 'i'
                        elif event.key == K_j: self.value += 'j'
                        elif event.key == K_k: self.value += 'k'
                        elif event.key == K_l: self.value += 'l'
                        elif event.key == K_m: self.value += 'm'
                        elif event.key == K_n: self.value += 'n'
                        elif event.key == K_o: self.value += 'o'
                        elif event.key == K_p: self.value += 'p'
                        elif event.key == K_q: self.value += 'q'
                        elif event.key == K_r: self.value += 'r'
                        elif event.key == K_s: self.value += 's'
                        elif event.key == K_t: self.value += 't'
                        elif event.key == K_u: self.value += 'u'
                        elif event.key == K_v: self.value += 'v'
                        elif event.key == K_w: self.value += 'w'
                        elif event.key == K_x: self.value += 'x'
                        elif event.key == K_y: self.value += 'y'
                        elif event.key == K_z: self.value += 'z'
                        elif event.key == K_0: self.value += '0'
                        elif event.key == K_1: self.value += '1'
                        elif event.key == K_2: self.value += '2'
                        elif event.key == K_3: self.value += '3'
                        elif event.key == K_4: self.value += '4'
                        elif event.key == K_5: self.value += '5'
                        elif event.key == K_6: self.value += '6'
                        elif event.key == K_7: self.value += '7'
                        elif event.key == K_8: self.value += '8'
                        elif event.key == K_9: self.value += '9'
                        elif event.key == K_BACKQUOTE: self.value += '`'
                        elif event.key == K_MINUS: self.value += '-'
                        elif event.key == K_EQUALS: self.value += '='
                        elif event.key == K_LEFTBRACKET: self.value += '['
                        elif event.key == K_RIGHTBRACKET: self.value += ']'
                        elif event.key == K_BACKSLASH: self.value += '\\'
                        elif event.key == K_SEMICOLON: self.value += ';'
                        elif event.key == K_QUOTE: self.value += '\''
                        elif event.key == K_COMMA: self.value += ','
                        elif event.key == K_PERIOD: self.value += '.'
                        elif event.key == K_SLASH: self.value += '/'
                    elif self.shifted:
                        if event.key == K_a: self.value += 'A'
                        elif event.key == K_b: self.value += 'B'
                        elif event.key == K_c: self.value += 'C'
                        elif event.key == K_d: self.value += 'D'
                        elif event.key == K_e: self.value += 'E'
                        elif event.key == K_f: self.value += 'F'
                        elif event.key == K_g: self.value += 'G'
                        elif event.key == K_h: self.value += 'H'
                        elif event.key == K_i: self.value += 'I'
                        elif event.key == K_j: self.value += 'J'
                        elif event.key == K_k: self.value += 'K'
                        elif event.key == K_l: self.value += 'L'
                        elif event.key == K_m: self.value += 'M'
                        elif event.key == K_n: self.value += 'N'
                        elif event.key == K_o: self.value += 'O'
                        elif event.key == K_p: self.value += 'P'
                        elif event.key == K_q: self.value += 'Q'
                        elif event.key == K_r: self.value += 'R'
                        elif event.key == K_s: self.value += 'S'
                        elif event.key == K_t: self.value += 'T'
                        elif event.key == K_u: self.value += 'U'
                        elif event.key == K_v: self.value += 'V'
                        elif event.key == K_w: self.value += 'W'
                        elif event.key == K_x: self.value += 'X'
                        elif event.key == K_y: self.value += 'Y'
                        elif event.key == K_z: self.value += 'Z'
                        elif event.key == K_0: self.value += ')'
                        elif event.key == K_1: self.value += '!'
                        elif event.key == K_2: self.value += '@'
                        elif event.key == K_3: self.value += '#'
                        elif event.key == K_4: self.value += '$'
                        elif event.key == K_5: self.value += '%'
                        elif event.key == K_6: self.value += '^'
                        elif event.key == K_7: self.value += '&'
                        elif event.key == K_8: self.value += '*'
                        elif event.key == K_9: self.value += '('
                        elif event.key == K_BACKQUOTE: self.value += '~'
                        elif event.key == K_MINUS: self.value += '_'
                        elif event.key == K_EQUALS: self.value += '+'
                        elif event.key == K_LEFTBRACKET: self.value += '{'
                        elif event.key == K_RIGHTBRACKET: self.value += '}'
                        elif event.key == K_BACKSLASH: self.value += '|'
                        elif event.key == K_SEMICOLON: self.value += ':'
                        elif event.key == K_QUOTE: self.value += '"'
                        elif event.key == K_COMMA: self.value += '<'
                        elif event.key == K_PERIOD: self.value += '>'
                        elif event.key == K_SLASH: self.value += '?'

        if len(self.value) > self.maxlength and self.maxlength >= 0: self.value = self.value[:-1]
