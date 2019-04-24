# Класс счетчика баллов
class GreatScorer:
    def __init__(self):
        self.vars = {}  # Просто кучка переменных внутри словаря будет
        # ТАм будут храниться оценки, полученные от пользователя
        self.marks_1 = []
        self.marks_2 = []
        # Читаем настройки расчетов. Если они повреждены, сбрасываем их
        # и снова читаем
        if not self.read_file():
            self.reset_file()
            self.read_file()

    # Просто метод чтения настроек в словарь из файла, скучно комментировать
    def read_file(self):
        try:
            with open('res/settings.txt', 'r') as f:
                spisok = f.read().split('\n')
            self.vars['marks_sp'] = []
            self.vars['marks_sl'] = {}
            for i in spisok[1:11]:
                perem = i.split()
                ocenka = perem[0].split('"')[1]
                self.vars['marks_sp'].append(ocenka)
                self.vars['marks_sl'][ocenka] = int(perem[1])
            self.vars['max'] = int(spisok[13].split()[1])
            self.vars['min'] = int(spisok[14].split()[1])
            if self.vars['max'] < 0:
                return False
            if self.vars['min'] < 0:
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

    # Метод сброса настроек - создает файл по текстовому шаблону
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

    # Метод расчета баллов за доклад - передаем 2 группы оценок
    def docladchik(self, line1, line2):
        # По правилам количество оценок в группах равно, если нет,
        # пользователь накосячил, кидаем ошибку
        if len(line1) != len(line2):
            return 'Error'
        # Преобразуем группы оценок в тб
        marks1 = self.translate(line1)[
                 self.vars['min']: len(line1) - self.vars['max']]
        marks2 = self.translate(line2)[
                 self.vars['min']: len(line1) - self.vars['max']]
        # Находим средний тб, умножаем на коэффициент, округляем,
        # возвращаем - вот весь расчет тб за одну роль
        oc1 = sum(marks1) / len(marks1) * self.vars['k_doc_1']
        oc2 = sum(marks1) / len(marks1) * self.vars['k_doc_1']
        return str(self.round(oc1 + oc2))

    # Аналогичный метод роли оппонента, но ряд оценок один
    def oppoent(self, line1):
        marks1 = self.translate(line1)[
                 self.vars['min']: len(line1) - self.vars['max']]
        oc1 = sum(marks1) / len(marks1) * self.vars['k_opp']
        return str(self.round(oc1))

    # Аналогично рецензирование. Сделал 2 метода из-за разных коэффициентов
    def recenzent(self, line1):
        marks1 = self.translate(line1)[
                 self.vars['min']: len(line1) - self.vars['max']]
        oc1 = sum(marks1) / len(marks1) * self.vars['k_rec']
        return str(self.round(oc1))

    # Метод перевода оценок в тб, принимает список оценок, находит словарь для
    # перевода каждой оценки в соответствующий ей тб, подставляет
    def translate(self, spisok):
        spisok2 = []
        for i in spisok:
            spisok2.append(self.vars['marks_sl'][i])
        return spisok2

    # Собственный метод округления, чтобы было красиво. Встроенный
    # раунд всегда лагает
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

    # Метод ввода оценки в первое поле из переменной text
    # (Или удаления последней оценки, если переменная пустая)
    def input_k1(self, text):
        if text in self.vars['marks_sp']:
            self.marks_1.append(text)
        else:
            if len(self.marks_1) == 0:
                return
            del self.marks_1[-1]

    # Аналогично для второго поля
    def input_k2(self, text):
        if text in self.vars['marks_sp']:
            self.marks_2.append(text)
        else:
            if len(self.marks_2) == 0:
                return
            del self.marks_2[-1]

    # Метод нажатия на кнопку расчета. По её номеру понимаем,
    # какую роль нам надо считать. Отсылаем к конкретному методу расчета.
    # Если он выдает ошибку, кидаем её пользователю
    def keydown(self, key):
        try:
            if key == 1:
                res2 = self.docladchik(self.marks_1, self.marks_2)
                return 'Результат: ' + res2
            if key == 2:
                return 'Результат: ' + self.oppoent(self.marks_1)
            if key == 3:
                return 'Результат: ' + self.recenzent(self.marks_1)
        except Exception:
            return 'Результат: Error'

    # Метод, который следит за тем, чтобы в окне программы оценки не вылезли
    # за прямоугольник. Не показывает больше 10 с конца. Это для первого поля
    def get_text1(self):
        x = 10
        if len(self.marks_1) <= x:
            return ' '.join(self.marks_1)
        else:
            return ' '.join(self.marks_1[len(self.marks_1) - x:])

    # Аналогично для второго
    def get_text2(self):
        x = 10
        if len(self.marks_2) <= x:
            return ' '.join(self.marks_2)
        else:
            return ' '.join(self.marks_2[len(self.marks_2) - x:])

    # Просто сброс оценок в списках
    def reset_marks(self):
        self.marks_1 = []
        self.marks_2 = []
