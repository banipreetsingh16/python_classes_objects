#first Example
class motorcycle():
    wheels = 2
    engine = "small"
    def speed(self):
        print("Motorcycles these days are really fast")
bullet = motorcycle()
bullet.speed()
print(motorcycle.wheels)
print(motorcycle.engine)
motorcycle.speed(bullet)
print("------------------------------------------------------")


#second example
class states():
    Num_of_States=28
    Area_covered=3,287,263
    def diversity(self):
        print("India is a very diverse country!")
Punjab = states()
Punjab.diversity()
print(states.Num_of_States)
print(states.Area_covered)
states.diversity(Punjab)
print("------------------------------------------------------")


# Third Example
class dogs():
    legs = 4
    tail = "yes"
    def bark(self):
        print("Dog barks loudly")
Saint_Brenard = dogs()
print(dogs.legs)
Saint_Brenard.bark()
dogs.bark(Saint_Brenard)
print(dogs.tail)
print("------------------------------------------------------")


# Fourth Example
class hotel():
    floors=5
    rooms=30
    def size(self):
        print("This hotel is really big!!!")
TheTaj = hotel()
TheTaj.size()
print(hotel.floors)
print(hotel.rooms)
hotel.size(TheTaj)
print("------------------------------------------------------")


# Fifth Example'
class laptops():
    handy = "yes"
    size = "small"
    def use(self):
        print("Laptops are handy and we can use them anywhere")
macbook= laptops()
print(laptops.handy)
print(laptops.size)
laptops.use(macbook)
macbook.use()
print("------------------------------------------------------")










    