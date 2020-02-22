import os
import os.path


class AppConfigure(object):
    def __init__(self):
        self._classes = None
        self._data_folder = None
        self._go_button = 0

        self._count = 0
        self._files_by_brand = {}
        self._files = []
        self._selected = 0

        self._selected = 0
        self._next_clicks = 0
        self._prev_clicks = 0
        self._current_page = 0

    #################
    # Configuration #
    #################
    def setClasses(self, classes):
        self._classes = classes

    def classes(self):
        return self._classes

    def setDataFolder(self, data_folder):
        self._data_folder = data_folder

    def dataFolder(self):
        return self._data_folder

    def incGoButton(self, num):
        if num is None:
            num = 0
        self._go_button = num

    def count(self):
        return self._go_button

    def load(self):
        brands = [_ for _ in os.listdir(self._data_folder) if not (_ in ('data.csv', 'classes.txt', '.DS_Store') or _.endswith('_img_cache'))]

        self._classes = [
            {'label': _.strip().title(), 'value': _.strip()} for _ in sorted(self._classes)
        ]

        files = []
        files_by_brand = {}

        for folder in brands:
            files_by_brand[folder] = []
            for file in sorted(os.listdir(os.path.join(self._data_folder, folder))):
                path = os.path.join(self._data_folder, folder, file)
                files.append({'id': self._count, 'path': path, 'name': file, 'folder': folder})
                files_by_brand[folder].append(files[-1])
                self._count += 1

        self._files = files
        self._files_by_brand = files_by_brand
    #################
    #################

    ########
    # Main #
    ########
    def files_by_brand(self):
        return [{'label': x, 'value': x} for x in self._files_by_brand.keys()]

    def files(self):
        return self._files

    def selected(self):
        return self._selected
