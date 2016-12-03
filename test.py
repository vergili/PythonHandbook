class Pet:
    def __init__(self):
        self.__species = None  # private variable

    def fill(self, species):
        self.__species = species

    def empty(self):
        self.__species = None

    def show(self):
        print self.__species


pet = Pet()
pet.fill('van')
pet.show()

