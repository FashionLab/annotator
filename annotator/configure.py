class AppConfigure(object):
    def __init__(self):
        self._classes = None
        self._data_folder = None
        self._go_button = 0

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
