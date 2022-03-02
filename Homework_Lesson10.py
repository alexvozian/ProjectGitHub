#Ex1:
class Human():
    FirstName = None
    LastName = None
    DateOfBirth = None

    def __init__(self, firstname, lastname, dateofbirth):
        self._set_firstname(self._check_firstname(firstname))
        self._set_lastname(self._check_lasttname(lastname))
        self._set_dateofbirth(self._check_dateofbirth(dateofbirth))

    def __str__(self):
        from datetime import datetime
        return f"{self.FirstName} {self.LastName}, age {datetime.now().date().year - self.DateOfBirth.year}"

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

Marius = Human("Marius", "Tricolici", "03/01/1998")
print(Marius)

#or

from my_library.human import Human

Marius = Human("Marius", "Tricolici", "03/01/1998")
print(f"{Marius.FirstName} {Marius.LastName}, age {Marius.human_age()}")


#Ex2:
class pet():
    Name = None
    Type = None
    FavoriteFood = None

    def __init__(self, name, type, favoritefood):
        self._set_name(self._check_name(name))
        self._set_type(self._check_type(type))
        self._set_favoritefood(self._check_favoritefood(favoritefood))


    def __str__(self):
        return f"{self.Type} called {self.Name} that loves {self.FavoriteFood}"

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



class Human():
    FirstName = None
    LastName = None
    DateOfBirth = None

    def __init__(self, firstname, lastname, dateofbirth):
        self._set_firstname(self._check_firstname(firstname))
        self._set_lastname(self._check_lasttname(lastname))
        self._set_dateofbirth(self._check_dateofbirth(dateofbirth))

    def __str__(self):
        from datetime import datetime
        return f"{self.FirstName} {self.LastName}, age {datetime.now().date().year - self.DateOfBirth.year}"

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




class HumanWithPet():
    FirstName = None
    LastName = None
    DateOfBirth = None
    PetList = list()

    def __init__(self, firstname, lastname, dateofbirth, petlist):
        self._set_firstname(self._check_firstname(firstname))
        self._set_lastname(self._check_lasttname(lastname))
        self._set_dateofbirth(self._check_dateofbirth(dateofbirth))
        self._set_petlist(self._check_petlist(petlist))

    def __str__(self):
        from datetime import datetime
        if len(self.PetList) == 0:
            return f"{self.FirstName} {self.LastName}, age {datetime.now().date().year - self.DateOfBirth.year} with no pets"
        elif len(self.PetList) == 1:
            return f"{self.FirstName} {self.LastName}, age {datetime.now().date().year - self.DateOfBirth.year} with a pet: {self.PetList}"
        else:
            return f"{self.FirstName} {self.LastName}, age {datetime.now().date().year - self.DateOfBirth.year} with pets: {self.PetList}"

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

    def _check_petlist(self, petlist):
        if type(petlist) is not list:
            raise Exception("Pet List need to be a List")
        return petlist

    def _set_firstname(self, firstname):
        self.FirstName = firstname
        return self.FirstName

    def _set_lastname(self, lastname):
        self.LastName = lastname
        return self.LastName

    def _set_dateofbirth(self, dateofbirth):
        self.DateOfBirth = dateofbirth
        return self.DateOfBirth

    def _set_petlist(self, petlist):
        for el in petlist:
            self.adopt_new_pet(el)
        return self.PetList
    def adopt_new_pet(self, newpet):
        return self.PetList.append(newpet)

    def give_away_pet(self, losepet):
        return self.PetList.remove(losepet)





Bobic = pet("Bobic", "dog", "bone")
Miron = pet("Miron", "cat", "fish")
Chesha = pet("Chesha", "bird", "seeds")
print(Bobic)
print(Miron)
print(Chesha)
Marius = Human("Marius", "Tricolici", "03/01/1998")
print(Marius)
MariusWithPets = HumanWithPet("Marius", "Tricolici", "03/01/1998", [Bobic, Miron, Chesha])
print(MariusWithPets)

#or

from my_library.pet import pet
from my_library.human import Human
from my_library.humanwithpet import HumanWithPet

Bobic = pet("Bobic", "dog", "bone")
Miron = pet("Miron", "cat", "fish")
Chesha = pet("Chesha", "bird", "seeds")
Marius = Human("Marius", "Tricolici", "03/01/1998")
MariusWithPets = HumanWithPet(Marius)
print(MariusWithPets)

MariusWithPets.adopt_new_pet(Bobic)
print(MariusWithPets)
MariusWithPets.adopt_new_pet(Miron)
print(MariusWithPets)
MariusWithPets.adopt_new_pet(Chesha)
print(MariusWithPets)

MariusWithPets.give_away_pet(Bobic)
print(MariusWithPets)
MariusWithPets.give_away_pet(Miron)
print(MariusWithPets)
MariusWithPets.give_away_pet(Chesha)
print(MariusWithPets)