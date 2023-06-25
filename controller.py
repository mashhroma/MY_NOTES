from time import sleep
import model
import view
import commands

notebook = model.Notebook()
path_exist = False

view.show_greeding()

if input('Введите 1 или 2: ') == '2':
    try_flag = True
    while try_flag:
        path = input(
            'Загрузите файл с заметками в директорию и напишите его название с расширением: ')
        try:
            notebook.load_notebook(path)
            print('>>> Заметки загружены в программу.\n')
            path_exist = True
            try_flag = False
        except FileNotFoundError:
            print(f'Файл "{path}" не найден.')
            do_next = input('(Создать новый файл? Y/N): ').lower()
            if do_next == 'y':
                try_flag = False

sleep(0.5)

view.show_menu(commands.text_menu)

while True:
    choice = input('\nВВЕДИТЕ КОМАНДУ (подсказка - help): ')
    match choice:
        case '1' | 'add':
            add = view.get_new_info()
            notebook.add_note(add)
            print('>>> Заметка добавлена.')

        case '2' | 'find':
            search = notebook.find_note(
                input('Введите данные для поиска: ')).lower()
            print('>>> Результаты поиска:')
            print(search)

        case '3' | 'edit':
            index = input('Введите номер заметки: ')
            if notebook.check_index(index):
                edit_info = view.get_new_info()
                notebook.edit_note(index, edit_info)
                print('>>> Заметка изменена.')
            else:
                print('Заметки с таким номером нет.')

        case '4' | 'del':
            index = input('Введите номер заметки: ')
            if notebook.check_index(index):
                notebook.del_note(index)
                print('>>> Заметка удалена.')
            else:
                print('Заметки с таким номером нет.')

        case '5' | 'show':
            print(notebook)

        case '6' | 'show by term':
            term = input('Введите дату срока: ')
            search = notebook.find_by_date(term)
            print(f'Заметки с данным сроком:')
            print(search)

        case '7' | 'show by data':
            date = input('Введите дату создания или изменения: ')
            search = notebook.find_by_create_date(date)
            print(f'Заметки, созданные в эту дату:')
            print(search)

        case '8' | 'show':
            print(notebook)

        case '9' | 'save':
            if path_exist == False:
                file_name = input(
                    'Укажите наименование файла заметок без расширения: ')
                path = f'{file_name}.json'
                path_exist = True
            notebook.save_notebook(path)
            print(f'>>> Заметки сохранены в файл {path}.')

        case '8' | 'help':
            view.show_menu(commands.text_menu)

        case '9' | 'exit':
            print('До встречи!')
            exit()

        case _:
            print('ЭТО НЕ КОМАНДА!')
