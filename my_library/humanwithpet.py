class HumanWithPet():
    Human = None
    PetList = list()

    def __init__(self, human):
        self._set_human(human)

    def __str__(self):
        return f"{self.Human} with a pet: {self.PetList}"

    def _set_human(self, human):
        self.Human = human
        return self.Human

    def _set_pet(self, pet):
        self.adopt_new_pet(pet)
        return self.PetList

    def adopt_new_pet(self, newpet):
        return self.PetList.append(newpet)

    def give_away_pet(self, losepet):
        return self.PetList.remove(losepet)

