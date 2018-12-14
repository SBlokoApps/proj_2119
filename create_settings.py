# -*- coding: utf-8 -*-
def reset_set():
    lines2 = ['*Стоимость оценок (ТБ)*', '"2":\t2', '"3-":\t5', '"3":\t9', '"3+":\t14', '"4-":\t20', '"4":\t27',
              '"4+":\t34', '"5-":\t42', '"5":\t51', '"5+":\t60', '',
              '*Максимальных и минимальных оценок не учитывается*', '"Max":\t0', '"Min":\t0', '',
              '*Программа была запущена ранее*', 'NO', '', '*Коэффициенты при переводе ТБ*',
              '"Доклад за научность":\t2', '"Доклад за культуру":\t2', '"Оппонирование":\t2', '"Рецензирование":\t1',
              '', '*Название команды*', 'Teamname', '', '*Перевод ТБ в РБ*',
              '+---------+-----------+-----------+----------+-----------+----------+',
              '|    -    |     №1    |   №2,3,4  |    №2    |    №3,4   |  №3, 4   |',
              '+---------+-----------+-----------+----------+-----------+----------+',
              '|    -    | просто №1 | ТБ>=№1-10 | ТБ<№1-10 | ТБ>=№2-10 | ТБ<№2-10 |',
              '|  >=300  |     6     |     6     |    5     |     5     |    4     |',
              '| 230-299 |     5     |     5     |    4     |     4     |    3     |',
              '| 130-229 |     4     |     4     |    3     |     3     |    2     |',
              '|  60-129 |     3     |     3     |    2     |     2     |    1     |',
              '|   <60   |     2     |     2     |    1     |     1     |    0     |',
              '+---------+-----------+-----------+----------+-----------+----------+']
    file_set = open('res/settings.txt', 'w')
    for index in lines2:
        file_set.write(index+'\n')
    file_set.close()
def save_set():
    global username, lines2
    lines2[26] = username
    with open('res/settings.txt', 'w') as file:
        for index in lines2:
            file.write(index + '\n')
try:
    spisok = ['2', '3-', '3', '3+', '4-', '4', '4+', '5-', '5', '5+']
    slovar = {}
    lines2 = []
    lines = []
    with open('res/settings.txt', 'r') as file:
        for line in file:
            lines2.append(line[:-1])
            lines.append(line[:-1].split('|'))
    for i in range(1, 11):
        slovar[spisok[i - 1]] = int(lines[i][0].split('\t')[1])
    max_oc = int(lines[13][0].split('\t')[1])
    min_oc = int(lines[14][0].split('\t')[1])
    new_open = lines[17][0]
    k_doc = int(lines[20][0].split('\t')[1])
    k_doc2 = int(lines[21][0].split('\t')[1])
    k_opp = int(lines[22][0].split('\t')[1])
    k_rec = int(lines[23][0].split('\t')[1])
    username = lines[26][0]
    rbs1 = lines[33][1:-1]
    rbs2 = lines[34][1:-1]
    rbs3 = lines[35][1:-1]
    rbs4 = lines[36][1:-1]
    rbs5 = lines[37][1:-1]
    granits = [rbs1[0].split('>=')[1], rbs2[0].split('-'),
               rbs3[0].split('-'), rbs4[0].split('-'), rbs5[0].split('<')[1]]
    rb300 = [int(i) for i in rbs1[1:]]
    rb230 = [int(i) for i in rbs2[1:]]
    rb130 = [int(i) for i in rbs3[1:]]
    rb60 = [int(i) for i in rbs4[1:]]
    rb0 = [int(i) for i in rbs5[1:]]
    if new_open == 'NO':
        lines2[17] = 'YES'
        with open('res/settings.txt', 'w') as file:
            for index in lines2:
                file.write(index + '\n')
except:
    reset_set()
    spisok = ['2', '3-', '3', '3+', '4-', '4', '4+', '5-', '5', '5+']
    slovar = {}
    lines2 = []
    lines = []
    with open('res/settings.txt', 'r') as file:
        for line in file:
            lines2.append(line[:-1])
            lines.append(line[:-1].split('|'))
    for i in range(1, 11):
        slovar[spisok[i - 1]] = int(lines[i][0].split('\t')[1])
    max_oc = int(lines[13][0].split('\t')[1])
    min_oc = int(lines[14][0].split('\t')[1])
    new_open = lines[17][0]
    k_doc = float(lines[20][0].split('\t')[1])
    k_doc2 = float(lines[21][0].split('\t')[1])
    k_opp = float(lines[22][0].split('\t')[1])
    k_rec = float(lines[23][0].split('\t')[1])
    username = lines[26][0]
    rbs1 = lines[33][1:-1]
    rbs2 = lines[34][1:-1]
    rbs3 = lines[35][1:-1]
    rbs4 = lines[36][1:-1]
    rbs5 = lines[37][1:-1]
    granits = [rbs1[0].split('>=')[1], rbs2[0].split('-'),
               rbs3[0].split('-'), rbs4[0].split('-'), rbs5[0].split('<')[1]]
    rb300 = [int(i) for i in rbs1[1:]]
    rb230 = [int(i) for i in rbs2[1:]]
    rb130 = [int(i) for i in rbs3[1:]]
    rb60 = [int(i) for i in rbs4[1:]]
    rb0 = [int(i) for i in rbs5[1:]]
    if new_open == 'NO':
        lines2[17] = 'YES'
        with open('res/settings.txt', 'w') as file:
            for index in lines2:
                file.write(index + '\n')
