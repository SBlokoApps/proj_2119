# -*- coding: utf-8 -*-

def nround(ch):
    ch *= 100
    a = int(ch)
    b = ch - a
    if b >= 0.5:
        a += 1
    return a/100

def koeff_otkaz(kolvo):
    slovar = {'4': 0.8, '5': 0.7, '6': 0.6, '7': 0.5, '8': 0.4}
    if 4 <= kolvo <= 7:
        return slovar[str(kolvo)]
    elif kolvo > 7:
        return slovar['8']
    else:
        return 1


def docladchic(oc1, oc2, k, values, max_ocen, min_ocen):
    global k_doc2
    score = 0
    score2 = 0
    if len(oc1) != len(oc2):
        raise Exception
    new_oc1 = obrabotka(oc1, values, max_ocen, min_ocen)
    new_oc2 = obrabotka(oc2, values, max_ocen, min_ocen)
    for i in new_oc1:
        score += i
    for i in new_oc2:
        score2 += i
    score /= len(new_oc1)
    score2 /= len(new_oc1)
    score2 *= k_doc2
    score *= k
    return nround(score + score2)


def opponent_recenzent(oc1, k, values, max_ocen, min_ocen):
    score = 0
    new_oc = obrabotka(oc1, values, max_ocen, min_ocen)
    for i in new_oc:
        score += i
    score /= len(new_oc)
    score *= k
    return nround(score)


def obrabotka(sp, slovarik, ma, mi):
    sp2 = [slovarik[i] for i in sp]
    for i in range(ma):
        del sp2[sp2.index(max(sp2))]
    for i in range(mi):
        del sp2[sp2.index(min(sp2))]
    return sp2


def reiting(slovarik, rb1, rb2, rb3, rb4, rb5):
    global granits
    a = int(granits[0])
    b = int(granits[1][0])
    c = int(granits[2][0])
    d = int(granits[3][0])
    pusto_slovarik = False
    slovarik2 = {}
    if not('1' in slovarik):
        slovarik['1'] = 0
        pusto_slovarik = True
    if not('2' in slovarik):
        slovarik['2'] = 0
        pusto_slovarik = True
    for i in slovarik.keys():
        if i == '1':
            if slovarik[i] >= a:
                slovarik2[i] = rb1[0]
            elif slovarik[i] >= b:
                slovarik2[i] = rb2[0]
            elif slovarik[i] >= c:
                slovarik2[i] = rb3[0]
            elif slovarik[i] >= d:
                slovarik2[i] = rb4[0]
            else:
                slovarik2[i] = rb5[0]
        elif (i == '2' or i == '3' or i == '4') and slovarik[i] >= slovarik['1']-10:
            if slovarik[i] >= a:
                slovarik2[i] = rb1[1]
            elif slovarik[i] >= b:
                slovarik2[i] = rb2[1]
            elif slovarik[i] >= c:
                slovarik2[i] = rb3[1]
            elif slovarik[i] >= d:
                slovarik2[i] = rb4[1]
            else:
                slovarik2[i] = rb5[1]
        elif i == '2' and slovarik[i] < slovarik['1']:
            if slovarik[i] >= a:
                slovarik2[i] = rb1[2]
            elif slovarik[i] >= b:
                slovarik2[i] = rb2[2]
            elif slovarik[i] >= c:
                slovarik2[i] = rb3[2]
            elif slovarik[i] >= d:
                slovarik2[i] = rb4[2]
            else:
                slovarik2[i] = rb5[2]
        elif (i == '3' or i == '4') and slovarik[i] >= slovarik['2']-10:
            if slovarik[i] >= a:
                slovarik2[i] = rb1[3]
            elif slovarik[i] >= b:
                slovarik2[i] = rb2[3]
            elif slovarik[i] >= c:
                slovarik2[i] = rb3[3]
            elif slovarik[i] >= d:
                slovarik2[i] = rb4[3]
            else:
                slovarik2[i] = rb5[3]
        elif (i == '3' or i == '4') and slovarik[i] < slovarik['2']:
            if slovarik[i] >= a:
                slovarik2[i] = rb1[4]
            elif slovarik[i] >= b:
                slovarik2[i] = rb2[4]
            elif slovarik[i] >= c:
                slovarik2[i] = rb3[4]
            elif slovarik[i] >= d:
                slovarik2[i] = rb4[4]
            else:
                slovarik2[i] = rb5[4]
        else:
            slovarik2[i] = 0
    return [pusto_slovarik, slovarik2]


def soedslovar(sl1, sl2):  # sl2 k название, v тб, sl1 k место, v тб
    sl3 = {}
    for k, v in sl2.items():
        if str(v) in sl3.keys():
            sl3[str(v)].append(k)
        else:
            sl3[str(v)] = [k]
    sl4 = {}
    for k in sorted(sl1.keys(), key=lambda x:int(x)):
        if len(sl3[str(sl1[k])]) == 1:
            sl4[k] = sl3[str(sl1[k])][0]
        else:
            sl4[k] = sl3[str(sl1[k])][0]
            del sl3[str(sl1[k])][0]
    return sl4


def threeteams(res1, res2, res3, nazv, k_d, k_o, k_r, ma_oc, mi_oc,
               perevod, rbs1, rbs2, rbs3, rbs4, rbs5, otkaz):  # в рес1 4 списка оценок 0д. 1д. 2о. 3р
    tb_1 = opponent_recenzent(res1[2], k_o, perevod, ma_oc, mi_oc)+opponent_recenzent(res2[3], k_r, perevod, ma_oc, mi_oc)+nround(docladchic(res3[0], res3[1], k_d, perevod, ma_oc, mi_oc)*koeff_otkaz(otkaz[0]))
    tb_2 = opponent_recenzent(res1[3], k_r, perevod, ma_oc, mi_oc)+nround(docladchic(res2[0], res2[1], k_d, perevod, ma_oc, mi_oc)*koeff_otkaz(otkaz[0]))+opponent_recenzent(res3[2], k_o, perevod, ma_oc, mi_oc)
    tb_3 = nround(docladchic(res1[0], res1[1], k_d, perevod, ma_oc, mi_oc)*koeff_otkaz(otkaz[2]))+opponent_recenzent(res2[2], k_o, perevod, ma_oc, mi_oc)+opponent_recenzent(res3[3], k_r, perevod, ma_oc, mi_oc)
    nazvania = {nazv[0][0]:tb_1, nazv[1][0]:tb_2, nazv[2][0]:tb_3}
    q = sorted([tb_1, tb_2, tb_3])
    mesta = {'1':q[2], '2':q[1], '3':q[0]}
    mesta_nazv = soedslovar(mesta, nazvania)
    otvet = reiting(mesta, rbs1, rbs2, rbs3, rbs4, rbs5)
    if otvet[0]:
        return [False, False, False]
    else:
        return [mesta, mesta_nazv, otvet[1]]


def fourteams(res1, res2, res3, res4, nazv, k_d, k_o, k_r, ma_oc, mi_oc, perevod, rbs1, rbs2, rbs3, rbs4, rbs5, otkaz):
    tb_1 = opponent_recenzent(res1[2], k_o, perevod, ma_oc, mi_oc)+opponent_recenzent(res3[3], k_r, perevod, ma_oc, mi_oc)+nround(docladchic(res4[0], res4[1], k_d, perevod, ma_oc, mi_oc)*koeff_otkaz(otkaz[0]))
    tb_2 = opponent_recenzent(res2[3], k_r, perevod, ma_oc, mi_oc)+nround(docladchic(res3[0], res3[1], k_d, perevod, ma_oc, mi_oc)*koeff_otkaz(otkaz[0]))+opponent_recenzent(res4[2], k_o, perevod, ma_oc, mi_oc)
    tb_3 = opponent_recenzent(res1[3], k_r, perevod, ma_oc, mi_oc) + nround(docladchic(res2[0], res2[1], k_d, perevod, ma_oc, mi_oc) * koeff_otkaz(otkaz[0])) + opponent_recenzent(res3[2], k_o, perevod, ma_oc, mi_oc)
    tb_4 = nround(docladchic(res1[0], res1[1], k_d, perevod, ma_oc, mi_oc)*koeff_otkaz(otkaz[2]))+opponent_recenzent(res2[2], k_o, perevod, ma_oc, mi_oc)+opponent_recenzent(res4[3], k_r, perevod, ma_oc, mi_oc)
    nazvania = {nazv[0][0]:tb_1, nazv[1][0]:tb_2, nazv[2][0]:tb_3, nazv[3][0]:tb_4}
    q = sorted([tb_1, tb_2, tb_3, tb_4])
    mesta = {'1':q[3], '2':q[2], '3':q[1], '4':q[0]}
    mesta_nazv = soedslovar(mesta, nazvania)
    otvet = reiting(mesta, rbs1, rbs2, rbs3, rbs4, rbs5)
    if otvet[0]:
        return [False, False, False]
    else:
        return [mesta, mesta_nazv, otvet[1]]


def otherteams(kolvo, nazv, tbs, otkaz, k_d, k_o, k_r, ma_oc, mi_oc, perevod, rbs1, rbs2, rbs3, rbs4, rbs5):
    tbs_ok = [round(docladchic(tbs[i][0], tbs[i][1], k_d, perevod, ma_oc, mi_oc)*koeff_otkaz(otkaz[i]), 2) +
              opponent_recenzent(tbs[i][2], k_o, perevod, ma_oc, mi_oc) +
              opponent_recenzent(tbs[i][3], k_r, perevod, ma_oc, mi_oc) for i in range(kolvo)]
    nazvania = {}
    for i in range(kolvo):
        nazvania[nazv[i]] = tbs_ok[i]
    tbs_ok2 = sorted(tbs_ok, reverse=True)
    mesta = {}
    for i in range(kolvo):
        mesta[str(i+1)] = tbs_ok2[i]
    mesta_nazv = soedslovar(mesta, nazvania)
    otvet = reiting(mesta, rbs1, rbs2, rbs3, rbs4, rbs5)
    if otvet[0]:
        return [False, False, False]
    else:
        return [mesta, mesta_nazv, otvet]