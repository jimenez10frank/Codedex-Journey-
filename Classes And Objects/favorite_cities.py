class City: 
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

Kreta = City('Kreta', "Greece", 4.0, True)
London = City('London', "United Kingdom", 3.4, True)

print(vars(Kreta))
print(vars(London))
