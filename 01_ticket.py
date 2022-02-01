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
import argparse
import pathlib
from pprint import pprint

from PIL import Image, ImageDraw, ImageFont, ImageColor


class TicketFiller:

    def __init__(self, fio, from_, to, date, save_path=None, template=None):
        self.fio = fio
        self.from_ = from_
        self.to = to
        self.date = date
        self.template = pathlib.Path(
            "C:\\Users\\Home\\PycharmProjects\\AirLineTicketFiller\\images\\ticket_template.png") \
            if template is None else template
        self.font_path = pathlib.Path((
            "C:\\Users\\Home\\PycharmProjects\\AirLineTicketFiller\\fonts\\Cyntho Next Slab.ttf"))
        self.save_path = save_path if save_path is None else save_path

    def make_ticket(self):
        ticket = Image.open(self.template)
        width, height = ticket.size
        x = 717 - width
        y_fio = ticket.size[1] - 280
        y_from = ticket.size[1] - 210
        y_to = ticket.size[1] - 144
        x_date = 957 - width
        # print(width, height)
        draw = ImageDraw.Draw(ticket)
        font = ImageFont.truetype(str(self.font_path), size=20)
        font_date = ImageFont.truetype(str(self.font_path), size=15)
        draw.text((x, y_fio), text=self.fio, font=font, fill=ImageColor.colormap['black'])
        draw.text((x, y_from), text=self.from_, font=font, fill=ImageColor.colormap['black'])
        draw.text((x, y_to), text=self.to, font=font, fill=ImageColor.colormap['black'])
        draw.text((x_date, y_to + 4), text=self.date, font=font_date, fill=ImageColor.colormap['black'])
        ticket.show()
        ticket.save(self.save_path, format='PNG')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа для заполнения билета')
    parser.add_argument('-fio', dest='fio', type=str, help='Введите ФИО?')
    parser.add_argument('-from', dest='from_', type=str, help='Откуда летите?')
    parser.add_argument('-to', dest='to', type=str, help='Откуда летите?')
    parser.add_argument('-date', dest='date', type=str, help='Когда?')
    parser.add_argument('--save_to', dest='save_path', type=str, help='путь для сохранения билета')
    args = parser.parse_args()
    pprint(args)

    ticket_filler = TicketFiller(fio=args.fio, from_=args.from_, to=args.to, date=args.date, save_path=args.save_path)
    ticket_filler.make_ticket()
