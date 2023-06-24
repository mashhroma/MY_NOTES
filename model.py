class Note:
    def __init__(self, date: str, title: str, comment: str):
        self.date = date
        self.title = title
        self.comment = comment

    def __init__(self, note_info: dict):
        self.date = note_info.get('date')
        self.title = note_info.get('title')
        self.comment = note_info.get('comment')

    def __str__(self) -> str:
        return f'{self.date: <12} | {self.title: <20} | {self.comment: <35}'

    def to_str(self) -> str:
        return f'{self.date: <12} | {self.title: <20} | {self.comment: <35}'

    def to_json(self):
        return f'{{\n   "date": "{self.date}",\n   "title": "{self.title}",\n   "comment": "{self.comment}"\n}}'


class Notebook:
    def __init__(self):
        self.note_list = []

    def load_notebook(self, path: str):
        with open(path, 'r', encoding='UTF-8') as file:
            data = file.read().strip('[]').split('},')
            for line in data:
                new_line = line.replace('\n', '').replace(
                    '{', '').replace('}', '').replace('"', '').split(',')
                dict = {}
                for item in new_line:
                    for_dict = item.strip().split(':')
                    dict[for_dict[0].strip()] = for_dict[1].strip()
                note = Note(dict)
                self.note_list.append(note)

    def save_notebook(self, path: str):
        data = []
        for note in self.note_list:
            data.append(note.to_json())
        data = '[\n'+',\n'.join(data)+'\n]'

        with open(path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def add_note(self, note_info: dict):
        self.note_list.append(Note(note_info))

    def find_note(self, find: str):
        search_result = []
        for i, note in enumerate(self.note_list):
            if find in note.to_str().lower():
                search_result.append(f'{i+1} {note}')
        if len(search_result) < 1:
            search_result.append('Данные не обнаружены.')
        return '\n'.join(search_result)

    def check_index(self, note_id: int):
        if note_id <= len(self.note_list):
            return True
        else:
            return False

    def edit_note(self, note_id: int, note_info: dict):
        if note_info.get('date') == '':
            note_info['date'] = self.note_list[note_id-1].date
        if note_info.get('title') == '':
            note_info['title'] = self.note_list[note_id-1].title
        if note_info.get('comment') == '':
            note_info['comment'] = self.note_list[note_id-1].comment
        self.note_list[note_id-1] = Note(note_info)

    def del_note(self, note_id: int):
        self.note_list.pop(note_id-1)

    def __str__(self) -> str:
        head = ['N', 'Дата', 'Название', 'Комментарии']
        result = f'{head[0]: <4} | {head[1]: <12} | {head[2]: <20} | {head[3]: <35}\n'
        for i, note in enumerate(self.note_list):
            result += f'{i+1: <4} | {note}\n'
        return result[:-2]
