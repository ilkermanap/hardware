

class Address:
    def __init__(self, adr, postcode, city, country):
        self.address = adr
        self.postcode = postcode
        self.city = city
        self.country = country

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def getCoords(self):
        return(self.x,self.y)

class Rect:
    def __init__(self,x,y,width, height):
        self.coordinate = Point(x,y)
        self.size = Point(width, height)
        self.svg = '<rect x = "%smm" y = "%smm"  width = "%smm" height = "%smm"   style="fill: none; stroke: black;"/>" ' % (x, y, width, height)
        
    def updateCoordinate(self, newCoord):
        self.coordinate = newCoord
        self.updateSvg()
        
    def updateSize(self, newSize):
        self.size = newSize
        self.updateSvg()
        
    def updateSvg(self):
        self.svg = '<rect x = "%smm" y = "%smm"  width = "%smm" height = "%smm"   style="fill: none; stroke: black;"/>" ' % (self.coordinate.x, self.coordinate.y, self.size.x, self.size.y)

class Location:
    def __init__(self):
        self.gps = "" 
        self.desc = ""
        self.shape = Rect(0,0,0,0)
        
    def setRect(self,x,y,width, height):
        self.shape=Rect(x,y,width,height)

    def setCoordinate(self, coords):
        self.shape.updateCoordinate(coords)
        
    def setSize(self, size):
        self.shape.updateSize(size)
        
    def updateSVG(self):
        self.shape.updateSvg()
    
class Rack:
    def __init__(self, height):
        self.height = height
        self.devices = []
        for i in range(self.height):
            self.devices.append("")
            
        
        
class Room:
    def __init__(self, desc, coords, size):
        self.racks = []
        self.location = Location()
        self.location.desc = desc
        self.location.setCoordinate(coords)
        self.location.setSize(size)
    
    def addRack(self, rack):
        self.racks.append(rack)
        
    def info(self):
        return self.location.desc
    
class Floor:
    
    def __init__(self, desc):
        self.location = Location()
        self.rooms = []

        self.location.desc = desc
        
    def addRoom(self, newRoom):
        self.rooms.append(newRoom)
        
        
    def graph(self):
        temp = []
        temp.append(self.location.shape.svg)
        for room in self.rooms:
            temp.append(room.location.shape.svg)
        return temp
            
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
f1.location.setRect(0,0,300,300)
f2 = Floor("f2")
r1 = Room("r1", Point(10,10), Point(20,20))

f1.addRoom(r1)
r2 = Room("r2", Point(10,40), Point(20,20))
f1.addRoom(r2)

s.addFloor(f1)
s.addFloor(f2)
print '<svg xmlns="http://www.w3.org/2000/svg" version="1.1">'
for lines in f1.graph():
    print lines
print '</svg>'