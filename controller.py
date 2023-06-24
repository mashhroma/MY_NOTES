from time import sleep
import model
import view
import commands

notebook = model.Notebook()
path_exist = False

view.show_greeding()

if input('Введите 1 или 2: ') == '2':
    path = input(
        'Загрузите файл с заметками в директорию и напишите его название: ')
    notebook.load_notebook(path)
    path_exist = True
    print('>>> Заметки загружены в программу.\n')

sleep(1)

view.show_menu(commands.text_menu)

while True:
    choice = input('ВВЕДИТЕ КОМАНДУ (подсказка - help): ')
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
            index = int(input('Введите номер заметки: '))
            if notebook.check_index(index):
                edit_info = view.get_new_info()
                notebook.edit_note(index, edit_info)
                print('>>> Заметка изменена.')
            else:
                print('Заметки с таким номером нет.')

        case '4' | 'del':
            index = int(input('Введите номер заметки: '))
            if notebook.check_index(index):
                notebook.del_note(index)
                print('>>> Заметка удалена.')
            else:
                print('Заметки с таким номером нет.')

        case '5' | 'show by data':
            date = notebook.find_note(input('Введите дату: '))
            print(f'>>> Заметки на дату: {date}:')
            print(search)

        case '6' | 'show':
            print(notebook)

        case '7' | 'save':
            if path_exist == False:
                file_name = input('Укажите наименование файла заметок: ')
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
