from my_library.pet import pet
from my_library.human import Human

class HumanWithPet():
    Human = None
    PetList = list()

    def __init__(self, human):
        self._set_human(human)

    def __str__(self):
        if len(self.PetList) == 0:
            return f"{self.Human} with no pets"
        elif len(self.PetList) == 1:
            return f"{self.Human} with a pet:{','.join(str(e) for e in self.PetList)}"
        else:
            return f"{self.Human} with {len(self.PetList)} pets:{','.join(str(e) for e in self.PetList)}"

    def _set_human(self, human):
        self.Human = str(human)
        return self.Human

    def _set_pet(self, pet):
        self.adopt_new_pet(pet)
        return self.PetList

    def adopt_new_pet(self, newpet):
        return self.PetList.append(newpet)

    def give_away_pet(self, losepet):
        return self.PetList.remove(losepet)

