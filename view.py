def show_greeding():
    print('''Добрый день!
Данная программа поможет Вам создавать заметки и управлять ими.
Выберите действие:
1. Создать новую записную книжку
2. Загрузить записную книжку из файла (json)''')


def show_menu(text_menu: str):
    menu = text_menu.split('\n')
    for i, item in enumerate(menu):
        if i == 0:
            print(item)
        else:
            print(i, item)


def get_new_info():
    date = input('Укажите дату в формате: ').split('.')
    if len(date) == 2:
        date.append('2023')
    else:
        if len(date[2]) < 4:
            date[2] = '20' + date[2]
    date = '.'.join(date)
    title = input('Название заметки: ')
    comment = input('Комментарии к заметке: ')
    return {'date': date, 'title': title, 'comment': comment}
