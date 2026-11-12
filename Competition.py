class Competition:
    __raise_amount=1.10

    def __init__(self,name,prize):
        self.name=name
        self.prize=prize

    def get_name(self):
        return self.name

    def get_prize(self):
        return ("Prize : " + str(self.prize))

    def raise_prize(self):
        self.prize=int(self.prize*self.__raise_amount)


race=Competition('Race', 1000)
race.raise_prize()
print(race.get_name())
print(race.get_prize())

class Sprint(Competition):
    def __init__(self,name,prize):
        super().__init__(name,prize)

sprint=Competition('100m',1000)
sprint.raise_prize()
print(sprint.get_name())
print(sprint.get_prize())
print(sprint.__dict__)

help(Sprint)
print(Sprint.__dict__)


class Cycling(Competition):
    def __init__(self,name,prize, country):
        super().__init__(name,prize)
        self.__country=country

    def get_country(self):
        return self.__country


tourdefrance=Cycling('Tour de France', 10000, 'France')
tourdefrance.raise_prize()
print(tourdefrance.get_name())
print(tourdefrance.get_prize())

cycling1000=Cycling('Cycling 1000km', 5000, 'USA')
cycling1000.raise_prize()
print(cycling1000.get_name())
print(cycling1000.get_prize())
print(cycling1000.get_country())

