class Human():
    FirstName = None
    LastName = None
    DateOfBirth = None

    def __init__(self, firstname, lastname, dateofbirth):
        self._set_firstname(self._check_firstname(firstname))
        self._set_lastname(self._check_lasttname(lastname))
        self._set_dateofbirth(self._check_dateofbirth(dateofbirth))

    def _check_firstname(self, firstname):
        if type(firstname) is not str:
            raise Exception("First Name need to be a String")
        return firstname

    def _check_lasttname(self, lastname):
        if type(lastname) is not str:
            raise Exception("Last Name need to be a String")
        return lastname

    def _check_dateofbirth(self, dateofbirth):
        from datetime import datetime
        date = datetime.strptime(dateofbirth, "%m/%d/%Y").date()
        if type(date) is datetime.date:
            raise Exception("Date of birth need to be a Date")
        return date

    def _set_firstname(self, firstname):
        self.FirstName = firstname
        return self.FirstName

    def _set_lastname(self, lastname):
        self.LastName = lastname
        return self.LastName

    def _set_dateofbirth(self, dateofbirth):
        self.DateOfBirth = dateofbirth
        return self.DateOfBirth

    def human_age(self):
        from datetime import datetime
        return datetime.now().date().year - self.DateOfBirth.year
