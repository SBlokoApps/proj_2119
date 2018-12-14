# -*- coding: utf-8 -*-
def be_a_part(posit1, posit2, deltax, deltay):
    x1, y1 = posit1
    x2, y2 = posit2
    if x2<=x1<x2+deltax and y2<=y1<y2+deltay:
        return True
    else:
        return False
def be_a_part_menu(pos1, pos2):
    return be_a_part(pos1, pos2, 300, 80)
def be_a_part_keyboard(pos1, pos2):
    return be_a_part(pos1, pos2, 550, 50)
def be_a_part_buttons(pos1, pos2):
    return be_a_part(pos1, pos2, 200, 50)
def be_a_part_buttons_reset(pos1, pos2):
    return be_a_part(pos1, pos2, 150, 50)
def be_a_part_buttons_reseted(pos1, pos2):
    return be_a_part(pos1, pos2, 400, 100)
def be_a_part_buttons_new(pos1, pos2):
    return be_a_part(pos1, pos2, 300, 100)
def be_a_part_tb_keys(pos1, poses):
    for pos2 in poses:
        if be_a_part(pos1, pos2, 200, 50):
            return [True, poses.index(pos2)]
    return [False, 0]
def be_a_part_tb_keys_mm(pos1, poses):
    for pos2 in poses:
        if be_a_part(pos1, pos2, 450, 50):
            return [True, poses.index(pos2)]
    return [False, 0]
def be_a_part_buttons_tb_on(pos1, pos2):
    return be_a_part(pos1, pos2, 150, 50)
def be_a_part_rb_34(pos1, pos2):
    return be_a_part(pos1, pos2, 250, 250)
def be_a_part_rb_three_nazv(pos1, pos2):
    return be_a_part(pos1, pos2, 681, 75)
def be_a_part_okpad(pos1, pos2):
    return be_a_part(pos1, pos2, 100, 50)
def be_a_part_rb_4_nazv(pos1, pos2):
    return be_a_part(pos1, pos2, 681, 56)