# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.

import os
import pathlib
from pathlib import Path, PureWindowsPath
from PIL import Image, ImageDraw, ImageFont, ImageColor


class TicketFiller:

    def __init__(self, fio, from_, to, date, template=None, font_path=None):
        self.fio = fio
        self.from_ = from_
        self.to = to
        self.date = date
        # self.template = PureWindowsPath("images", "ticket.template.jpg") if template is None else template
        self.template = pathlib.Path(
            "C:\\Users\\Home\\PycharmProjects\\AirLineTicketFiller\\images\\ticket_template.png") if template is None else template        # if font_path is None:
        #     self.font_path = os.path.join("fonts", "ofont_ru_DS Eraser2.ttf")
        # else:
        #     self.font_path = font_path

    def make_ticket(self):
        ticket = Image.open(self.template)
        ticket.show()


if __name__ == '__main__':
    ticket_filler = TicketFiller(fio='Boev R.S', from_='Moscow', to='New York', date='12.09.2022')
    ticket_filler.make_ticket()