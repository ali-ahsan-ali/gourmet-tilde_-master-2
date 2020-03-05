class Customer:
    def __init__(self, name, licence):
        self._name = name
        self._licence = licence

    # TODO make getters and setters

    # name getters and setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def licence(self):
        return self._licence

    @licence.setter
    def licence(self, new_licence):
        self._name = new_licence
    # licence - getters and setters

    def __str__(self):
        return "Made by Customer < name: {}, licence: {} >" .format(self._name, self._licence)
