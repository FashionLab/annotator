import base64
import os
import os.path
import pandas as pd


class AppConfigure(object):
    def __init__(self):
        self._classes = None
        self._data_folder = None
        self._data_file = None
        self._go_button = 0

        self._brand_filter = "all"
        self._order = "unlabeled"

        self._loaded = False
        self._count = 0
        self._files_by_brand = {}
        self._files_by_id = {}
        self._files = []

        self._selected = 0
        self._next_clicks = 0
        self._prev_clicks = 0
        self._current_page = 0
        self._max_per_page = 18

        self._data = None
        self._active_id = 0

    #################
    # Configuration #
    #################
    def setClasses(self, classes):
        content_type, content_string = classes.split(',')
        decoded = base64.b64decode(content_string).decode('ascii')
        self._classes = decoded.split('\n')
        for i in range(len(self._classes)):
            self._classes[i] = self._classes[i].strip()
        self._classes = [
            {'label': _.strip().title(), 'value': _.strip()} for _ in sorted(self._classes)
        ]

    def classes(self):
        return self._classes

    def setDataFolder(self, data_folder):
        self._data_folder = data_folder

    def dataFolder(self):
        return self._data_folder

    def setDataFile(self, data_file):
        self._data_file = data_file

    def dataFile(self):
        return self._data_file

    def incGoButton(self, num):
        if num is None:
            num = 0
        self._go_button = num

    def count(self):
        return self._go_button

    def setBrandFilter(self, brand_filter):
        self._brand_filter = brand_filter

    def setOrder(self, order):
        self._order = order

    def loaded(self):
        return self._loaded

    def load(self):
        if self._loaded:
            return

        brands = [_.title() for _ in os.listdir(self._data_folder) if not (_ in ('data.csv', 'classes.txt', '.DS_Store') or _.endswith('_img_cache'))]
        brands.append("all")

        files = []
        files_by_brand = {"all": []}
        files_by_id = {"all": []}

        for folder in brands:
            if folder == "all":
                # not a real folder
                continue

            folder = folder.lower()
            files_by_brand[folder] = []

            for file in sorted(os.listdir(os.path.join(self._data_folder, folder))):
                path = os.path.join(self._data_folder, folder, file)
                files.append({'id': self._count, 'path': path, 'name': file, 'folder': folder})
                files_by_brand[folder].append(files[-1])
                files_by_brand["all"].append(files[-1])
                files_by_id[self._count] = files[-1]
                self._count += 1

        self._files = files
        self._files_by_brand = files_by_brand
        self._files_by_id = files_by_id

        # name,folder,path,valid,class,ad,view,sex,color,notes
        self._data = pd.read_csv(self._data_file, header=0).fillna("")
        for col in self._data:
            self._data[col] = self._data[col].astype(str)
        self._data.set_index(["name", "folder"], inplace=True)
        self._loaded = True

    #################
    #################

    ########
    # Main #
    ########
    def files_by_brand(self):
        return [{'label': x, 'value': x} for x in self._files_by_brand.keys()]

    def brand_filter(self):
        return self._brand_filter

    def order(self):
        return self._order

    def files(self, id=None):
        if id is not None:
            self._active_id = id
            return self._files_by_id[id]
        return self._files_by_brand[self._brand_filter]

    def selected(self):
        return self._selected

    def storeRecord(self, key, value):
        if not self._active_id:
            return
        file = self._files_by_id[self._active_id]
        name = file["name"]
        folder = file["folder"]

        if not any(self._data.index.isin([(name, folder)])):
            # does not exist
            self._data.loc[(name, folder), :] = ''

        self._data.loc[(name, folder), :][key] = value
        self._data.fillna("").to_csv(self._data_file, header=self._data.columns)

    def loadRecord(self, key):
        file = self._files_by_id[self._active_id]
        name = file["name"]
        folder = file["folder"]

        if not any(self._data.index.isin([(name, folder)])):
            # does not exist
            return ""
        return self._data.loc[(name, folder), :][key]
