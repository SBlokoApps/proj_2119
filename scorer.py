class GreatScorer:
    def __init__(self):
        self.vars = {}
        if not self.read_file():
            self.reset_file()
            self.read_file()

    def read_file(self):
        try:
            with open('res/settings.txt', 'r') as f:
                spisok = f.read().split('\n')
                for i in spisok:
                    print(spisok.index(i), i)
            self.vars['marks_sp'] = []
            self.vars['marks_sl'] = {}
            for i in spisok[1:11]:
                perem = i.split()
                ocenka = perem[0].split('"')[1]
                self.vars['marks_sp'].append(ocenka)
                self.vars['marks_sl'][ocenka] = perem[1]
            self.vars['max'] = int(spisok[13].split()[1])
            self.vars['min'] = int(spisok[14].split()[1])
            if self.vars['max'] < 0:
                return False
            if self.vars['in'] < 0:
                return False
            self.vars['k_doc_1'] = float(spisok[17].split()[3])
            self.vars['k_doc_2'] = float(spisok[18].split()[3])
            self.vars['k_opp'] = float(spisok[19].split()[1])
            self.vars['k_rec'] = float(spisok[20].split()[1])
            self.vars['rb'] = []
            for i in spisok[27:32]:
                sp2 = i.split('|')
                stroka = [int(ii) for ii in sp2[2:-1]]
                str2 = sp2[1].split() + stroka
                self.vars['rb'].append(stroka)
            return True
        except Exception:
            return False

    def reset_file(self):
        sogerjimoe = '''*Стоимость оценок (ТБ)*
"2":\t2
"3-":\t5
"3":\t9
"3+":\t14
"4-":\t20
"4":\t27
"4+":\t34
"5-":\t42
"5":\t51
"5+":\t60

*Максимальных и минимальных оценок не учитывается*
"Max":\t0
"Min":\t0

*Коэффициенты при переводе ТБ*
"Доклад за научность":\t2
"Доклад за культуру":\t2
"Оппонирование":\t2
"Рецензирование":\t1

*Перевод ТБ в РБ*
+---------+-----------+-----------+----------+-----------+----------+
|    -    |     №1    |   №2,3,4  |    №2    |    №3,4   |  №3, 4   |
+---------+-----------+-----------+----------+-----------+----------+
|    -    | просто №1 | ТБ>=№1-10 | ТБ<№1-10 | ТБ>=№2-10 | ТБ<№2-10 |
|  >=300  |     6     |     6     |    5     |     5     |    4     |
| 230-299 |     5     |     5     |    4     |     4     |    3     |
| 130-229 |     4     |     4     |    3     |     3     |    2     |
|  60-129 |     3     |     3     |    2     |     2     |    1     |
|   <60   |     2     |     2     |    1     |     1     |    0     |
+---------+-----------+-----------+----------+-----------+----------+'''
        with open('res/settings.txt', 'w') as f:
            print(sogerjimoe, file=f)

    def docladchik(self, line1, line2):
        if len(line1) != len(line2):
            return 'Error'
        marks1 = self.translate(line1)[self.vars['min']:len(line1)-self.vars['max']]
        marks2 = self.translate(line2)[self.vars['min']:len(line1)-self.vars['max']]
        oc1 = sum(marks1) / len(marks1) * self.vars['k_doc_1']
        oc2 = sum(marks1) / len(marks1) * self.vars['k_doc_1']
        return self.round(oc1 + oc2)

    def oppoent(self, line1):
        marks1 = self.translate(line1)[self.vars['min']:len(line1)-self.vars['max']]
        oc1 = sum(marks1) / len(marks1) * self.vars['k_opp']
        return self.round(oc1)

    def recenzent(self, line1):
        marks1 = self.translate(line1)[self.vars['min']:len(line1)-self.vars['max']]
        oc1 = sum(marks1) / len(marks1) * self.vars['k_rec']
        return self.round(oc1)

    def translate(self, spisok):
        spisok2 = []
        for i in spisok:
            spisok2.append(self.vars['marks_sl'][i])
        return spisok2

    def round(self, num):
        prib = False
        num *= 1000
        num2 = str(num).split('.')[0]
        if int(num2[-1]) >= 5:
            prib = True
        num = int(num2[:-1])
        if prib:
            num += 1
        return num / 100
