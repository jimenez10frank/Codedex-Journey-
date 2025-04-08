class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught= is_caught
    def speak(self):
        print(self.name)
        print(self.name)
    def display_details(self):
        print("Entry Number:", self.entry)
        print("Name:", self.name)
        print("Type:", self.types)
        print("Description", self.description)
        if self.is_caught == True:
            print(self.name, "has already been caught")
        else:
            print(self.name, "Has not been caught yet")
pokemon1 = Pokemon(24, "Pikachu", "Electric", "Small Yellow pokemon but really strong", False)
pokemon2 = Pokemon(61, "Bulbasur", "Grass", "Small Green pokemon but really strong", True)

pokemon1.speak()
pokemon1.display_details()
pokemon2.speak()
pokemon2.display_details()