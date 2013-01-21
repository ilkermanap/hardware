

class Address:
    address =""
    postcode = ""
    city = ""
    country = ""
    def __init__(self, adr, postcode, city, country):
        self.address = adr
        self.postcode = postcode
        self.city = city
        self.country = country

class Location:
    def __init__(self):
        self.gps = ""
        self.desc = ""
    

class Rack:
    def __init__(self, height):
        self.height = height
        
class Room:
    
    def __init__(self, desc):
        self.location = Location()
        self.location.desc = desc
        
    def info(self):
        return self.location.desc
    
class Floor:
    
    def __init__(self, desc):
        self.location = Location()
        self.rooms = []

        self.location.desc = desc
        
    def addRoom(self, newRoom):
        self.rooms.append(newRoom)
        
    def info(self):
        temp = []
        temp.append(self.location.desc)
        for room in self.rooms:
            temp.append(room.info())
        return temp
    
    def printFloor(self):
        for line in self.info():
            print line
            

class Site:
    def __init__(self, desc):
        self.location = Location()
        self.floors = []

        self.location.desc = desc
    
    def addFloor(self, newFloor):
        self.floors.append(newFloor)
    
    def printSite(self):
        print self.location.desc
        for floor in self.floors:
            print floor.info()
            
s = Site("Test Site")
f1 = Floor("f1")
print f1.info()
f2 = Floor("f2")
print f1.info()
print f2.info()
r1 = Room("r1")
f1.addRoom(r1)
f2.addRoom(r1)
s.addFloor(f1)
s.addFloor(f2)

s.printSite()