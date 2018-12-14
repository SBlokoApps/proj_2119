# -*- coding: utf-8 -*-
from create_variables import *
from define_be_a_part import *
from define_calculation import *


def itogi_nazv_buttons(x):
    pass


def text_dlina(stroka, dlina):
    if len(stroka) <= dlina:
        return stroka
    else:
        return stroka[:dlina - 3] + '...'


def reset_inputs():
    global txtbx_new, tb_text_input
    txtbx_new = eztext_mod.Input(x=100, y=300, font=pygame.font.Font('res/fonts/times-new-roman.ttf', 72),
                                 maxlength=45, color=(255, 0, 0), prompt='> ')
    tb_text_input = eztext_mod.Input(x=230, y=300, font=pygame.font.Font('res/fonts/a_LCDNovaObl.ttf', 36),
                                     maxlength=45, color=(0, 0, 0), prompt='> ')


def reset_inputs_itogi():
    global itogi_text_input_1, itogi_text_input_2, itogi_text_input_3
    itogi_text_input_1 = eztext_mod.Input(x=303, y=200, font=pygame.font.Font('res/fonts/freesansbold.ttf', 32),
                                          maxlength=55, color=(0, 0, 0), prompt='> ')
    itogi_text_input_2 = eztext_mod.Input(x=303, y=282, font=pygame.font.Font('res/fonts/freesansbold.ttf', 32),
                                          maxlength=55, color=(0, 0, 0), prompt='> ')
    itogi_text_input_3 = eztext_mod.Input(x=303, y=364, font=pygame.font.Font('res/fonts/freesansbold.ttf', 32),
                                          maxlength=55, color=(0, 0, 0), prompt='> ')


def reset_inputs_itogi4():
    global itogi_text_input_1, itogi_text_input_2, itogi_text_input_3, itogi_text_input_4
    itogi_text_input_1 = eztext_mod.Input(x=303, y=176+16, font=pygame.font.Font('res/fonts/freesansbold.ttf', 32),
                                          maxlength=55, color=(0, 0, 0), prompt='> ')
    itogi_text_input_2 = eztext_mod.Input(x=303, y=237+16, font=pygame.font.Font('res/fonts/freesansbold.ttf', 32),
                                          maxlength=55, color=(0, 0, 0), prompt='> ')
    itogi_text_input_3 = eztext_mod.Input(x=303, y=298+16, font=pygame.font.Font('res/fonts/freesansbold.ttf', 32),
                                          maxlength=55, color=(0, 0, 0), prompt='> ')
    itogi_text_input_4 = eztext_mod.Input(x=303, y=359+16, font=pygame.font.Font('res/fonts/freesansbold.ttf', 32),
                                          maxlength=55, color=(0, 0, 0), prompt='> ')


def print_score(score, coords):
    font = pygame.font.Font('res/fonts/freesansbold.ttf', 110)
    text = font.render(str(score), True, [0, 0, 0])
    window.blit(text, [coords[0], coords[1]-20])


def print_version(v, coords):
    font = pygame.font.Font('res/fonts/freesansbold.ttf', 25)
    text = font.render(v, True, [0, 0, 0])
    window.blit(text, [coords[0], coords[1]-8])


def reset_simple():
    global ocenki1, ocenki2
    ocenki1 = []
    ocenki2 = []


def but_reset():
    global but_deistv
    for i in range(3):
        if but_deistv[i] == 1:
            but_deistv[i] = 0
def press_keyboard(pos1, pos2):
    global ocenki1, ocenki2
    x = pos1[0]
    if pos2[1] == 305:
        sp_oc = ocenki1
    else:
        sp_oc = ocenki2
    key = '2'
    keys_sl = {'2': 25, '3-': 75, '3': 125, '3+': 175, '4-': 225, '4': 275, '4+': 325, '5-': 375, '5': 425,
               '5+': 475, 'del': 525}
    for i in keys_sl.keys():
        x2 = keys_sl[i]
        if x2 <= x < x2 + 50:
            key = i
    if key == 'del':
        try:
            del sp_oc[-1]
        except:
            sp_oc = []
    else:
        sp_oc.append(key)
    if pos2[1] == 305:
        ocenki1 = sp_oc[:]
    else:
        ocenki2 = sp_oc[:]
def print_vse3(results):
    font = pygame.font.Font('res/fonts/freesansbold.ttf', 35)
    text11 = font.render('1', True, [0, 0, 0])
    text12 = font.render(text_dlina(str(results[1]['1']), 13), True, [0, 0, 0])
    text13 = font.render(str(results[0]['1']), True, [0, 0, 0])
    text14 = font.render(str(results[2]['1']), True, [0, 0, 0])
    text21 = font.render('2', True, [0, 0, 0])
    text22 = font.render(text_dlina(str(results[1]['2']), 13), True, [0, 0, 0])
    text23 = font.render(str(results[0]['2']), True, [0, 0, 0])
    text24 = font.render(str(results[2]['2']), True, [0, 0, 0])
    text31 = font.render('3', True, [0, 0, 0])
    text32 = font.render(text_dlina(str(results[1]['3']), 13), True, [0, 0, 0])
    text33 = font.render(str(results[0]['3']), True, [0, 0, 0])
    text34 = font.render(str(results[2]['3']), True, [0, 0, 0])
    window.blit(text11, [125, 260-2])
    window.blit(text21, [125, 330-2])
    window.blit(text31, [125, 400])
    window.blit(text12, [180, 260-2])
    window.blit(text22, [180, 330-2])
    window.blit(text32, [180, 400])
    window.blit(text13, [535, 260-2])
    window.blit(text23, [535, 330-2])
    window.blit(text33, [535, 400])
    window.blit(text14, [655, 260-2])
    window.blit(text24, [655, 330-2])
    window.blit(text34, [655, 400])


def print_vse4(results):
    font = pygame.font.Font('res/fonts/freesansbold.ttf', 35)
    text11 = font.render('1', True, [0, 0, 0])
    text12 = font.render(text_dlina(str(results[1]['1']), 13), True, [0, 0, 0])
    text13 = font.render(str(results[0]['1']), True, [0, 0, 0])
    text14 = font.render(str(results[2]['1']), True, [0, 0, 0])
    text21 = font.render('2', True, [0, 0, 0])
    text22 = font.render(text_dlina(str(results[1]['2']), 13), True, [0, 0, 0])
    text23 = font.render(str(results[0]['2']), True, [0, 0, 0])
    text24 = font.render(str(results[2]['2']), True, [0, 0, 0])
    text31 = font.render('3', True, [0, 0, 0])
    text32 = font.render(text_dlina(str(results[1]['3']), 13), True, [0, 0, 0])
    text33 = font.render(str(results[0]['3']), True, [0, 0, 0])
    text34 = font.render(str(results[2]['3']), True, [0, 0, 0])
    text41 = font.render('4', True, [0, 0, 0])
    text42 = font.render(text_dlina(str(results[1]['4']), 13), True, [0, 0, 0])
    text43 = font.render(str(results[0]['4']), True, [0, 0, 0])
    text44 = font.render(str(results[2]['4']), True, [0, 0, 0])
    window.blit(text11, [125, 198])
    window.blit(text21, [125, 258])
    window.blit(text31, [125, 318])
    window.blit(text41, [125, 378])

    window.blit(text12, [180, 198])
    window.blit(text22, [180, 258])
    window.blit(text32, [180, 318])
    window.blit(text42, [180, 378])

    window.blit(text13, [535, 198])
    window.blit(text23, [535, 258])
    window.blit(text33, [535, 318])
    window.blit(text43, [535, 378])

    window.blit(text14, [655, 198])
    window.blit(text24, [655, 258])
    window.blit(text34, [655, 318])
    window.blit(text44, [655, 378])


def print_nom_dei(nom):
    font = pygame.font.Font('res/fonts/freesansbold.ttf', 95)
    text = font.render(str(nom)+' Действие', True, [0, 0, 100])
    window.blit(text, [110, 40])


def print_buttons(but):
    global redbut, yebut, keypad
    if but[0] == 1:
        window.blit(yebut, [600, 280])
    if but[1] == 1:
        window.blit(yebut, [600, 380])
    if but[2] == 1:
        window.blit(yebut, [600, 480])
    if but[0] == 2:
        window.blit(redbut, [600, 280])
    if but[1] == 2:
        window.blit(redbut, [600, 380])
    if but[2] == 2:
        window.blit(redbut, [600, 480])
    window.blit(keypad, [600, 280])


def print_keys(spis, y):
    font = pygame.font.Font('res/fonts/freesansbold.ttf', 25)
    text = font.render(' '.join(spis), True, [0, 0, 0])
    window.blit(text, [40, y-40])


def print_nazv3(spisok):
    font = pygame.font.Font('res/fonts/freesansbold.ttf', 35)
    n1, nn1 = spisok[0][0], not(spisok[0][1])
    n2, nn2 = spisok[1][0], not(spisok[1][1])
    n3, nn3 = spisok[2][0], not(spisok[2][1])
    if nn1:
        text1 = font.render(text_dlina(n1, 21), True, [0, 0, 0])
        window.blit(text1, [320, 191])
    if nn2:
        text2 = font.render(text_dlina(n2, 21), True, [0, 0, 0])
        window.blit(text2, [320, 273])
    if nn3:
        text3 = font.render(text_dlina(n3, 21), True, [0, 0, 0])
        window.blit(text3, [320, 355])


def print_nazv4(spisok):
    font = pygame.font.Font('res/fonts/freesansbold.ttf', 35)
    n1, nn1 = spisok[0][0], not(spisok[0][1])
    n2, nn2 = spisok[1][0], not(spisok[1][1])
    n3, nn3 = spisok[2][0], not(spisok[2][1])
    n4, nn4 = spisok[3][0], not (spisok[3][1])
    if nn1:
        text1 = font.render(text_dlina(n1, 21), True, [0, 0, 0])
        window.blit(text1, [320, 187])
    if nn2:
        text2 = font.render(text_dlina(n2, 21), True, [0, 0, 0])
        window.blit(text2, [320, 248])
    if nn3:
        text3 = font.render(text_dlina(n3, 21), True, [0, 0, 0])
        window.blit(text3, [320, 309])
    if nn4:
        text4 = font.render(text_dlina(n4, 21), True, [0, 0, 0])
        window.blit(text4, [320, 370])


def print_on_tb(sl, sp, poses):
    font = pygame.font.Font('res/fonts/freesansbold.ttf', 25)
    for i in range(len(sp)):
        text = font.render(str(sl[sp[i]]), True, [0, 0, 0])
        window.blit(text, [poses[i][0]+162, poses[i][1]+10])


def input_nazv3(spisok, ev):
    global itogi_text_input_1, itogi_text_input_2, itogi_text_input_3
    n1, nn1 = spisok[0][0], spisok[0][1]
    n2, nn2 = spisok[1][0], spisok[1][1]
    n3, nn3 = spisok[2][0], spisok[2][1]
    a, b, c = 0, 0, 0
    if nn1:
        itogi_text_input_1.update(events)
        itogi_text_input_1.draw(window)
        a = itogi_text_input_1.value
    if nn2:
        itogi_text_input_2.update(events)
        itogi_text_input_2.draw(window)
        b = itogi_text_input_2.value
    if nn3:
        itogi_text_input_3.update(events)
        itogi_text_input_3.draw(window)
        c = itogi_text_input_3.value
    return [a, b, c, 'Название Команды']


def input_nazv4(spisok, ev):
    global itogi_text_input_1, itogi_text_input_2, itogi_text_input_3, itogi_text_input_4
    n1, nn1 = spisok[0][0], spisok[0][1]
    n2, nn2 = spisok[1][0], spisok[1][1]
    n3, nn3 = spisok[2][0], spisok[2][1]
    n4, nn4 = spisok[3][0], spisok[3][1]
    a, b, c, d = 0, 0, 0, 0
    if nn1:
        itogi_text_input_1.update(events)
        itogi_text_input_1.draw(window)
        a = itogi_text_input_1.value
    if nn2:
        itogi_text_input_2.update(events)
        itogi_text_input_2.draw(window)
        b = itogi_text_input_2.value
    if nn3:
        itogi_text_input_3.update(events)
        itogi_text_input_3.draw(window)
        c = itogi_text_input_3.value
    if nn4:
        itogi_text_input_4.update(events)
        itogi_text_input_4.draw(window)
        d = itogi_text_input_4.value
    return [a, b, c, d]


def zamena_fona_keys2(pos1, pos2):
    global but_on, risovat_key, deistv_no_keys, simple_keys, ocenki1, ocenki2, score_simple, nomer_deistv
    risovat_key = True
    x = pos2[0]
    x1 = pos1[0]
    positions = []
    for i in range(11):
        positions.append(x)
        x += 50
    for i in positions:
        if i <= x1 < i + 50:
            window.blit(deistv_no_keys, (0, 0))
            window.blit(but_on, (i, pos2[1]))
            window.blit(simple_keys, (0, 255))
            print_keys(ocenki1, 305)
            print_keys(ocenki2, 405)
            print_nom_dei(nomer_deistv)

def zamena_fona_keys(pos1, pos2):
    global but_on, risovat_key, field_simple_no_keys, simple_keys, ocenki1, ocenki2, score_simple
    risovat_key = True
    x = pos2[0]
    x1 = pos1[0]
    positions = []
    for i in range(11):
        positions.append(x)
        x += 50
    for i in positions:
        if i <= x1 < i + 50:
            window.blit(field_simple_no_keys, (0, 0))
            window.blit(but_on, (i, pos2[1]))
            window.blit(simple_keys, (0, 255))
            print_keys(ocenki1, 305)
            print_keys(ocenki2, 405)
            print_score(score_simple, [460, 130])


def zamena_tb(text, tb_k):
    global slovar, spisok
    try:
        nado = int(text)
    except:
        nado = 0
    slovar[spisok[tb_k.index(True)]] = nado * 1


def zamena_tb_mm(text, tb_k):
    global max_oc, min_oc
    try:
        nado = int(text)
    except:
        nado = 0
    if tb_k[1]:
        min_oc = nado * 1
    elif tb_k[0]:
        max_oc = nado * 1


def update():
    pygame.display.update()


pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Химический Баллометр')
pygame.display.set_icon(pygame.image.load('res/images/icon.png'))
run = True
reset_inputs()
reset_inputs_itogi()
if new_open=='T':
    menu = False
    new_open = True
else:
    menu = True
    new_open = False
while run:
    pygame.time.delay(10)
    if menu:
        window.blit(field, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        if be_a_part_menu(mouse_pos, pos_simple):
            field = on_simple
        elif be_a_part_menu(mouse_pos, pos_itogi):
            field = on_itogi
        elif be_a_part_menu(mouse_pos, pos_about_program):
            field = on_about_program
        elif be_a_part_menu(mouse_pos, pos_settings):
            field = on_settings
        elif be_a_part_menu(mouse_pos, pos_exit):
            field = on_exit
        else:
            field = field_main_off
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    pos = pygame.mouse.get_pos()
                    if be_a_part_menu(pos, pos_simple):
                        menu = False
                        simple = True
                        field = field_simple_off
                    if be_a_part_menu(pos, pos_itogi):
                        menu = False
                        itogi = True
                        field = field_itogi_off
                    if be_a_part_menu(pos, pos_about_program):
                        menu = False
                        about_program = True
                        field = field_about_off
                    if be_a_part_menu(pos, pos_settings):
                        menu = False
                        settings = True
                        field = field_settings_off
                    if be_a_part_menu(pos, pos_exit):
                        run = False
    if simple:
        if not(risovat_key):
            window.blit(field, (0, 0))
            print_keys(ocenki1, 305)
            print_keys(ocenki2, 405)
            print_score(score_simple, [460, 130])
        mouse_pos = pygame.mouse.get_pos()
        if be_a_part_buttons(mouse_pos, pos_simple_exit):
            risovat_key = False
            field = simple_on_exit
        elif be_a_part_buttons(mouse_pos, pos_simple_doc):
            risovat_key = False
            field = simple_on_doc
        elif be_a_part_buttons(mouse_pos, pos_simple_opp):
            risovat_key = False
            field = simple_on_opp
        elif be_a_part_buttons(mouse_pos, pos_simple_rec):
            risovat_key = False
            field = simple_on_rec
        elif be_a_part_keyboard(mouse_pos, keys1_pos):
            zamena_fona_keys(mouse_pos, keys1_pos)
        elif be_a_part_keyboard(mouse_pos, keys2_pos):
            zamena_fona_keys(mouse_pos, keys2_pos)
        else:
            field = field_simple_off
            risovat_key = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    pos = pygame.mouse.get_pos()
                    if be_a_part_buttons(pos, pos_simple_exit):
                        menu = True
                        simple = False
                        score_simple = 0
                        reset_simple()
                        field = field_main_off
                    if be_a_part_buttons(pos, pos_simple_doc):
                        try:
                            score_simple = docladchic(ocenki1, ocenki2, k_doc, slovar, max_oc, min_oc)
                        except Exception:
                            score_simple = 'Error'
                        reset_simple()
                    if be_a_part_buttons(pos, pos_simple_opp):
                        try:
                            score_simple = opponent_recenzent(ocenki1, k_opp, slovar, max_oc, min_oc)
                        except Exception:
                            pass
                        reset_simple()
                    if be_a_part_buttons(pos, pos_simple_rec):
                        try:
                            score_simple = opponent_recenzent(ocenki1, k_rec, slovar, max_oc, min_oc)
                        except Exception:
                            pass
                        reset_simple()
                    if be_a_part_keyboard(pos, keys1_pos):
                        press_keyboard(mouse_pos, keys1_pos)
                    if be_a_part_keyboard(pos, keys2_pos):
                        press_keyboard(mouse_pos, keys2_pos)
    if itogi:
        window.blit(field, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        if be_a_part_rb_34(mouse_pos, pos_rb_three):
            field = itogi_on_three
        elif be_a_part_rb_34(mouse_pos, pos_rb_four):
            field = itogi_on_four
        # elif be_a_part_buttons(mouse_pos, pos_rb_other):
        #     field = itogi_on_other
        elif be_a_part_buttons(mouse_pos, pos_rb_exit):
            field = itogi_on_exit
        else:
            field = field_itogi_off
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    pos = pygame.mouse.get_pos()
                    if be_a_part_rb_34(pos, pos_rb_three):
                        itogi = False
                        itogi_three = True
                        itogi_nazvania = True
                        field = field_itogi_nazv_three_off
                        reset_inputs_itogi()
                    if be_a_part_rb_34(pos, pos_rb_four):
                        itogi = False
                        itogi_four = True
                        itogi_nazvania = True
                        field = itogi_nazv_4_off
                        reset_inputs_itogi4()
                    # if be_a_part_buttons(pos, pos_rb_other):
                    #     itogi = False
                    #     itogi_other = True
                    #     itogi_nazvania = True
                    if be_a_part_buttons(pos, pos_rb_exit):
                        itogi = False
                        menu = True
                        field = field_main_off
    if itogi_three:
        if itogi_nazvania:
            window.blit(field, (0, 0))
            if okpad:
                window.blit(okpad_print, (300, 450))
            mouse_pos = pygame.mouse.get_pos()
            if be_a_part_okpad(mouse_pos, pos_okpad_ok):
                okpad_print = itogi_nazv_okpad_ok
            elif be_a_part_okpad(mouse_pos, pos_okpad_no):
                okpad_print = itogi_nazv_okpad_no
            else:
                okpad_print = itogi_nazv_okpad_off
            if be_a_part_rb_three_nazv(mouse_pos, pos_rb_nazv_3_1):
                field = itogi_nazv_three_1
            elif be_a_part_rb_three_nazv(mouse_pos, pos_rb_nazv_3_2):
                field = itogi_nazv_three_2
            elif be_a_part_rb_three_nazv(mouse_pos, pos_rb_nazv_3_3):
                field = itogi_nazv_three_3
            elif be_a_part_buttons(mouse_pos, pos_rb_other):
                field = itogi_nazv_three_on_ok
            elif be_a_part_buttons(mouse_pos, pos_rb_exit):
                field = itogi_nazv_three_on_exit
            else:
                field = field_itogi_nazv_three_off
            events = pygame.event.get()
            print_nazv3(nazv_vse)
            nazv_sp = input_nazv3(nazv_vse, events)
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if nazv_vse[0][1]:
                            nazv_vse[0][1] = False
                            nazv_vse[0][0] = nazv_sp[0]
                        if nazv_vse[1][1]:
                            nazv_vse[1][1] = False
                            nazv_vse[1][0] = nazv_sp[1]
                        if nazv_vse[2][1]:
                            nazv_vse[2][1] = False
                            nazv_vse[2][0] = nazv_sp[2]
                        reset_inputs_itogi()
                        okpad = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 or event.button == 3:
                        pos = pygame.mouse.get_pos()
                        if okpad:
                            if be_a_part_okpad(pos, pos_okpad_ok):
                                if nazv_vse[0][1]:
                                    nazv_vse[0][1] = False
                                    nazv_vse[0][0] = nazv_sp[0]
                                if nazv_vse[1][1]:
                                    nazv_vse[1][1] = False
                                    nazv_vse[1][0] = nazv_sp[1]
                                if nazv_vse[2][1]:
                                    nazv_vse[2][1] = False
                                    nazv_vse[2][0] = nazv_sp[2]
                                reset_inputs_itogi()
                                okpad = False
                            if be_a_part_okpad(pos, pos_okpad_no):
                                if nazv_vse[0][1]:
                                    nazv_vse[0][1] = False
                                if nazv_vse[1][1]:
                                    nazv_vse[1][1] = False
                                if nazv_vse[2][1]:
                                    nazv_vse[2][1] = False
                                reset_inputs_itogi()
                                okpad = False
                        if be_a_part_buttons(pos, pos_rb_other):
                            itogi_nazvania = False
                            itogi_deistvia = True
                            reset_inputs_itogi()
                            okpad = False
                        if be_a_part_buttons(pos, pos_rb_exit):
                            itogi_nazvania = False
                            itogi_three = False
                            itogi = True
                            okpad = False
                            field = field_itogi_off
                            reset_inputs_itogi()
                            nazv_vse = [['Название Команды', False] for i in range(4)]
                        if be_a_part_rb_three_nazv(pos, pos_rb_nazv_3_1) and not(
                                nazv_vse[0][1]) and not(nazv_vse[1][1]) and not(nazv_vse[2][1]):
                            nazv_vse[0][1] = True
                            okpad = True
                        if be_a_part_rb_three_nazv(pos, pos_rb_nazv_3_2) and not(
                                nazv_vse[0][1]) and not(nazv_vse[1][1]) and not(nazv_vse[2][1]):
                            nazv_vse[1][1] = True
                            okpad = True
                        if be_a_part_rb_three_nazv(pos, pos_rb_nazv_3_3) and not(
                                nazv_vse[0][1]) and not(nazv_vse[1][1]) and not(nazv_vse[2][1]):
                            nazv_vse[2][1] = True
                            okpad = True
        if itogi_deistvia:
            field = deistv_off
            nomer_deistv += 1
            but_deistv = [0, 0, 0]
            if nomer_deistv == 4:
                itogi_deistvia = False
                itogi_pokazat = True
            else:
                itogi_deistvia = False
                deistv = True
        if itogi_pokazat:
            if not(pokaz):
                r1 = three_ocenki['1']
                r2 = three_ocenki['2']
                r3 = three_ocenki['3']
                otkaz = [0, 0, 0]
                ress = threeteams(r1, r2, r3, nazv_vse, k_doc, k_opp, k_rec, max_oc, min_oc, slovar, rb300, rb230, rb130, rb60,
                           rb0, otkaz)
                pokaz = True
            window.blit(field, (0, 0))
            print_vse3(ress)
            mouse_pos = pygame.mouse.get_pos()
            if be_a_part_buttons(mouse_pos, pos_rb_exit):
                field = pokaz3_on_exit
            else:
                field = pokaz3_off
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 or event.button == 3:
                        pos = pygame.mouse.get_pos()
                        if be_a_part_buttons(pos, pos_rb_exit):
                            itogi_pokazat = False
                            itogi_nazvania = True
                            field = field_itogi_nazv_three_off
    if deistv:
        if not(risovat_key):
            window.blit(field, (0, 0))
            print_keys(ocenki1, 305)
            print_keys(ocenki2, 405)
        mouse_pos = pygame.mouse.get_pos()
        print_nom_dei(nomer_deistv)
        if be_a_part_buttons(mouse_pos, pos_simple_exit):
            field = deistv_on_exit
            but_reset()
        elif be_a_part_buttons(mouse_pos, pos_simple_doc):
            if but_deistv[0] == 0:
                but_deistv[0] = 1
            risovat_key = False
        elif be_a_part_buttons(mouse_pos, pos_simple_opp):
            if but_deistv[1] == 0:
                but_deistv[1] = 1
            risovat_key = False
        elif be_a_part_buttons(mouse_pos, pos_simple_rec):
            if but_deistv[2] == 0:
                but_deistv[2] = 1
            risovat_key = False
        elif be_a_part_keyboard(mouse_pos, keys1_pos):
            zamena_fona_keys2(mouse_pos, keys1_pos)
            risovat_key = False
        elif be_a_part_keyboard(mouse_pos, keys2_pos):
            zamena_fona_keys2(mouse_pos, keys2_pos)
            risovat_key = False
        else:
            but_reset()
            field = deistv_off
            risovat_key = False
        print_buttons(but_deistv)
        if 0 not in three_ocenki[str(nomer_deistv)]:
            deistv = False
            itogi_deistvia = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    pos = pygame.mouse.get_pos()
                    if be_a_part_buttons(pos, pos_simple_exit):
                        itogi_nazvania = True
                        deistv = False
                        nomer_deistv -= 1
                        reset_simple()
                        field = field_itogi_nazv_three_off
                    if be_a_part_buttons(pos, pos_simple_doc):
                        try:
                            assert len(ocenki1) == len(ocenki2)
                            assert len(ocenki1) > 0
                            three_ocenki[str(nomer_deistv)][0] = ocenki1
                            three_ocenki[str(nomer_deistv)][1] = ocenki2
                            but_deistv[0] = 2
                        except Exception:
                            pass
                        reset_simple()
                    if be_a_part_buttons(pos, pos_simple_opp):
                        try:
                            assert len(ocenki1) > 0
                            three_ocenki[str(nomer_deistv)][2] = ocenki1
                            but_deistv[1] = 2
                        except Exception:
                            pass
                        reset_simple()
                    if be_a_part_buttons(pos, pos_simple_rec):
                        try:
                            assert len(ocenki1) > 0
                            three_ocenki[str(nomer_deistv)][3] = ocenki1
                            but_deistv[2] = 2
                        except Exception:
                            pass
                        reset_simple()
                    if be_a_part_keyboard(pos, keys1_pos):
                        press_keyboard(mouse_pos, keys1_pos)
                    if be_a_part_keyboard(pos, keys2_pos):
                        press_keyboard(mouse_pos, keys2_pos)
    if itogi_four:
        if itogi_nazvania:
            if itogi_nazvania:
                window.blit(field, (0, 0))
                if okpad:
                    window.blit(okpad_print, (300, 450))
                mouse_pos = pygame.mouse.get_pos()
                if be_a_part_okpad(mouse_pos, pos_okpad_ok):
                    okpad_print = itogi_nazv_okpad_ok
                elif be_a_part_okpad(mouse_pos, pos_okpad_no):
                    okpad_print = itogi_nazv_okpad_no
                else:
                    okpad_print = itogi_nazv_okpad_off
                if be_a_part_rb_4_nazv(mouse_pos, pos_rb_nazv_4_1):
                    field = itogi_nazv_4_1
                elif be_a_part_rb_4_nazv(mouse_pos, pos_rb_nazv_4_2):
                    field = itogi_nazv_4_2
                elif be_a_part_rb_4_nazv(mouse_pos, pos_rb_nazv_4_3):
                    field = itogi_nazv_4_3
                elif be_a_part_rb_4_nazv(mouse_pos, pos_rb_nazv_4_4):
                    field = itogi_nazv_4_4
                elif be_a_part_buttons(mouse_pos, pos_rb_other):
                    field = itogi_nazv_4_ok
                elif be_a_part_buttons(mouse_pos, pos_rb_exit):
                    field = itogi_nazv_4_exit
                else:
                    field = itogi_nazv_4_off
                events = pygame.event.get()
                print_nazv4(nazv_vse)
                nazv_sp = input_nazv4(nazv_vse, events)
                for event in events:
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if nazv_vse[0][1]:
                                nazv_vse[0][1] = False
                                nazv_vse[0][0] = nazv_sp[0]
                            if nazv_vse[1][1]:
                                nazv_vse[1][1] = False
                                nazv_vse[1][0] = nazv_sp[1]
                            if nazv_vse[2][1]:
                                nazv_vse[2][1] = False
                                nazv_vse[2][0] = nazv_sp[2]
                            if nazv_vse[3][1]:
                                nazv_vse[3][1] = False
                                nazv_vse[3][0] = nazv_sp[3]
                            reset_inputs_itogi4()
                            okpad = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1 or event.button == 3:
                            pos = pygame.mouse.get_pos()
                            if okpad:
                                if be_a_part_okpad(pos, pos_okpad_ok):
                                    if nazv_vse[0][1]:
                                        nazv_vse[0][1] = False
                                        nazv_vse[0][0] = nazv_sp[0]
                                    if nazv_vse[1][1]:
                                        nazv_vse[1][1] = False
                                        nazv_vse[1][0] = nazv_sp[1]
                                    if nazv_vse[2][1]:
                                        nazv_vse[2][1] = False
                                        nazv_vse[2][0] = nazv_sp[2]
                                    if nazv_vse[3][1]:
                                        nazv_vse[3][1] = False
                                        nazv_vse[3][0] = nazv_sp[3]
                                    reset_inputs_itogi4()
                                    okpad = False
                                if be_a_part_okpad(pos, pos_okpad_no):
                                    if nazv_vse[0][1]:
                                        nazv_vse[0][1] = False
                                    if nazv_vse[1][1]:
                                        nazv_vse[1][1] = False
                                    if nazv_vse[2][1]:
                                        nazv_vse[2][1] = False
                                    if nazv_vse[3][1]:
                                        nazv_vse[3][1] = False
                                    reset_inputs_itogi4()
                                    okpad = False
                            if be_a_part_buttons(pos, pos_rb_other):
                                itogi_nazvania = False
                                itogi_deistvia = True
                                reset_inputs_itogi4()
                                okpad = False
                            if be_a_part_buttons(pos, pos_rb_exit):
                                itogi_nazvania = False
                                itogi_four = False
                                itogi = True
                                okpad = False
                                field = field_itogi_off
                                reset_inputs_itogi4()
                                nazv_vse = [['Название Команды', False] for i in range(4)]
                            if be_a_part_rb_4_nazv(pos, pos_rb_nazv_4_1) and not (
                                    nazv_vse[0][1]) and not (nazv_vse[1][1]) and not (nazv_vse[2][1]):
                                nazv_vse[0][1] = True
                                okpad = True
                            if be_a_part_rb_4_nazv(pos, pos_rb_nazv_4_2) and not (
                                    nazv_vse[0][1]) and not (nazv_vse[1][1]) and not (nazv_vse[2][1]):
                                nazv_vse[1][1] = True
                                okpad = True
                            if be_a_part_rb_4_nazv(pos, pos_rb_nazv_4_3) and not (
                                    nazv_vse[0][1]) and not (nazv_vse[1][1]) and not (nazv_vse[2][1]):
                                nazv_vse[2][1] = True
                                okpad = True
                            if be_a_part_rb_4_nazv(pos, pos_rb_nazv_4_4) and not (
                                    nazv_vse[0][1]) and not (nazv_vse[1][1]) and not (nazv_vse[2][1]):
                                nazv_vse[3][1] = True
                                okpad = True
        if itogi_deistvia:
            field = deistv_off
            nomer_deistv += 1
            but_deistv = [0, 0, 0]
            if nomer_deistv == 5:
                itogi_deistvia = False
                itogi_pokazat = True
            else:
                itogi_deistvia = False
                deistv = True
        if itogi_pokazat:
            if not(pokaz):
                r1 = three_ocenki['1']
                r2 = three_ocenki['2']
                r3 = three_ocenki['3']
                r4 = three_ocenki['4']
                otkaz = [0, 0, 0, 0]
                ress = fourteams(r1, r2, r3, r4, nazv_vse, k_doc, k_opp, k_rec, max_oc, min_oc, slovar, rb300, rb230, rb130, rb60,
                           rb0, otkaz)
                pokaz = True
            window.blit(field, (0, 0))
            print_vse4(ress)
            mouse_pos = pygame.mouse.get_pos()
            if be_a_part_buttons(mouse_pos, pos_rb_exit):
                field = pokaz4_on_exit
            else:
                field = pokaz4_off
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 or event.button == 3:
                        pos = pygame.mouse.get_pos()
                        if be_a_part_buttons(pos, pos_rb_exit):
                            itogi_pokazat = False
                            itogi_nazvania = True
                            field = itogi_nazv_4_off
    if itogi_other:
        if itogi_nazvania:
            razrab = True
            itogi_nazvania = False
            itogi_other = False
        if itogi_deistvia:
            razrab = True
            itogi_deistvia = False
            itogi_other = False
        if itogi_pokazat:
            razrab = True
            itogi_pokazat = False
            itogi_other = False
    if settings:
        window.blit(field, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        if be_a_part_menu(mouse_pos, pos_settings_exit):
            field = settings_on_exit
        elif be_a_part_menu(mouse_pos, pos_settings_reset):
            field = settings_on_reset
        else:
            field = field_settings_off
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    pos = pygame.mouse.get_pos()
                    if be_a_part_menu(pos, pos_settings_exit):
                        menu = True
                        settings = False
                        field = field_main_off
                    if be_a_part_menu(pos, pos_settings_reset):
                        settings = False
                        settings_reset = True
                        field = reset_settings_off
    if settings_reset:
        window.blit(field, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        if be_a_part_buttons_reset(mouse_pos, pos_reset_no):
            field = reset_settings_on_no
        elif be_a_part_buttons_reset(mouse_pos, pos_reset_yes):
            field = reset_settings_on_yes
        else:
            field = reset_settings_off
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    settings_reseted = True
                    settings_reset = False
                    reset_set()
                    field = reseted_settings_off
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    pos = pygame.mouse.get_pos()
                    if be_a_part_buttons_reset(pos, pos_reset_no):
                        settings = True
                        settings_reset = False
                        field = field_settings_off
                    if be_a_part_buttons_reset(pos, pos_reset_yes):
                        settings_reseted = True
                        settings_reset = False
                        reset_set()
                        field = reseted_settings_off
    if settings_reseted:
        window.blit(field, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        if be_a_part_buttons_reseted(mouse_pos, pos_reseted_ok):
            field = reseted_settings_on
        else:
            field = reseted_settings_off
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    pos = pygame.mouse.get_pos()
                    if be_a_part_buttons_reseted(pos, pos_reseted_ok):
                        run = False
    if about_program:
        window.blit(field, (0, 0))
        print_version(version, pos_version)
        mouse_pos = pygame.mouse.get_pos()
        if be_a_part_buttons(mouse_pos, pos_about_exit):
            field = about_on_exit
        else:
            field = field_about_off
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    pos = pygame.mouse.get_pos()
                    if be_a_part_buttons(pos, pos_about_exit):
                        menu = True
                        about_program = False
                        field = field_main_off
    if new_open:
        window.blit(field, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        if be_a_part_buttons_new(mouse_pos, pos_new_yes):
            field = new_on_yes
        elif be_a_part_buttons_new(mouse_pos, pos_new_no):
            field = new_on_no
        else:
            field = field_new_off
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    pos = pygame.mouse.get_pos()
                    if be_a_part_buttons_reseted(pos, pos_new_no):
                        username = txtbx_new.value
                        save_set()
                        menu = True
                        new_open = False
                        field = field_main_off
                    if be_a_part_buttons_reseted(pos, pos_new_yes):
                        username = txtbx_new.value
                        save_set()
                        school = True
                        new_open = False
                        field = field_main_off
        txtbx_new.update(events)
        txtbx_new.draw(window)
    if razrab:
        window.blit(field, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        if be_a_part_buttons(mouse_pos, pos_razrab_exit):
            field = razrab_on_exit
        else:
            field = field_razrab_off
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    pos = pygame.mouse.get_pos()
                    if be_a_part_buttons(pos, pos_razrab_exit):
                        menu = True
                        razrab = False
                        field = field_main_off
    update()
pygame.quit()
