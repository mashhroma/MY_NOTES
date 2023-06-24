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

def get_date():
    date = input('Укажите дату в формате: ')
    if date != '':
        while '.' not in date:
            date = input('Неверный формат даты, укажите дату, разделяя точкой: ')
        split_date = date.split('.')
        if len(split_date) == 2:
            split_date.append('2023')
        else:
            if len(split_date[2]) < 4:
                split_date[2] = '20' + split_date[2]
        date = '.'.join(split_date)
    return date

def get_new_info():
    date = get_date()
    title = input('Название заметки: ')
    comment = input('Комментарии к заметке: ')
    return {'date': date, 'title': title, 'comment': comment}
