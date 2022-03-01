class pet():
    Name = None
    Type = None
    FavoriteFood = None

    def __init__(self, name, type, favoritefood):
        self._set_name(self._check_name(name))
        self._set_type(self._check_type(type))
        self._set_favoritefood(self._check_favoritefood(favoritefood))

    def _check_name(self, name):
        if type(name) is not str:
            raise Exception("Name need to be a String")
        return name

    def _check_type(self, fel):
        if type(fel) is not str:
            raise Exception("Type need to be a String")
        return fel

    def _check_favoritefood(self, favoritefood):
        if type(favoritefood) is not str:
            raise Exception("Favorite Food need to be a String")
        return favoritefood

    def _set_name(self, name):
        self.Name = name
        return self.Name

    def _set_type(self, type):
        self.Type = type
        return self.Type

    def _set_favoritefood(self, favoritefood):
        self.FavoriteFood = favoritefood
        return self.FavoriteFood