#first Example
class Motorcycle:
    wheels = 2
    engine = "small"
    def speed(self):
        print("Motorcycles these days are really fast")
bullet = Motorcycle()
bullet.speed()
print(Motorcycle.wheels)
print(Motorcycle.engine)
Motorcycle.speed(bullet)
print("------------------------------------------------------")


#second example
class States:
    Num_of_States=28
    Area_covered=3,287,263
    def diversity(self):
        print("India is a very diverse country!")
Punjab = States()
Punjab.diversity()
print(States.Num_of_States)
print(States.Area_covered)
States.diversity(Punjab)
print("------------------------------------------------------")


# Third Example
class Dogs:
    legs = 4
    tail = "yes"
    def bark(self):
        print("Dog barks loudly")
Saint_Brenard = Dogs()
print(Dogs.legs)
Saint_Brenard.bark()
Dogs.bark(Saint_Brenard)
print(Dogs.tail)
print("------------------------------------------------------")


# Fourth Example
class Hotel:
    floors=5
    rooms=30
    def size(self):
        print("This hotel is really big!!!")
TheTaj = Hotel()
TheTaj.size()
print(Hotel.floors)
print(Hotel.rooms)
Hotel.size(TheTaj)
print("------------------------------------------------------")


# Fifth Example'
class Laptops:
    handy = "yes"
    size = "small"
    def use(self):
        print("Laptops are handy and we can use them anywhere")
macbook= Laptops()
print(Laptops.handy)
print(Laptops.size)
Laptops.use(macbook)
macbook.use()
print("------------------------------------------------------")










    
