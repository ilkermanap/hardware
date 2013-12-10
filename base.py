import math


units = {
  'm->dm':10,'m->cm':100, 'm->mm':1000,'m->km':0.001,
  'm2->dm2':100,'m2->cm2':10000, 'm2->mm2':1000000,'m2->km2':0.000001,
  'm3->dm3':1000,'m3->cm3':1000000, 'm3->mm3':1000000000,'m3->km3':0.000000001
  }

def unitConvert(inVal, inUnit, outUnit):
  
  return 0
  

class Point:
  def __init__(self, x = 0, y = 0, color="black"):
    self.x = x
    self.y = y
    self.color = color
    self.zoomLevel = 1
    self.area = 0

  def setColor(self, _color):
    self.color = _color

  def getPolyPoint(self, zoomLevel = 1):
    return "%.3f,%.3f " % (self.x * zoomLevel, self.y * zoomLevel)

  def svgText(self, zoomLevel = 1):
    if zoomLevel >= 1:
      r = zoomLevel 
      x1 = (self.x * 1.0) * zoomLevel
      y1 = (self.y * 1.0) * zoomLevel
      text = '<circle cx="%d" cy="%d" r="%d" stroke="%s" stroke-width="1" fill="%s"/>' \
          % (x1,y1, r,  self.color, self.color)
      return text
    else:
      return ""

class  Line:
  def __init__(self, x1=0, y1=0, x2=0, y2=0, color = "black", unit="cm"):
    self.start = Point(x1, y1)
    self.finish = Point(x2, y2)
    self.color = color
    self.area = 0
    self.unit = unit

  def lineLength(self):
    _x = self.finish.x - self.start.x
    _xx = _x ** 2
    _y = self.finish.y - self.start.y
    _yy = _y ** 2
    return math.sqrt(_xx + _yy)

  def svgText(self, zoomLevel=1):
    l = self.lineLength() * zoomLevel
    x1 = (self.start.x * 1.0) * zoomLevel
    y1 = (self.start.y * 1.0) * zoomLevel
    x2 = (self.finish.x * 1.0) * zoomLevel
    y2 = (self.finish.y * 1.0) * zoomLevel
    
    
    if (l >= 1):
      text ='<line x1="%.3f" y1="%.3f" x2="%.3f" y2="%.3f" stroke="%s">'\
          % (x1, y1, x2, y2, self.color)
    else:
      text = ""

    return text

class Rect:
  def __init__(self, color = "black", x=0, y=0, width=0, height=0 , zoomLevel=1, fill = "none"):
    self.color = color
    self.zoomLevel = zoomLevel
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.fill = fill


  def svgText(self, zoomLevel = 1):
    x = self.x * zoomLevel
    y = self.y * zoomLevel
    w = self.width * zoomLevel
    h = self.height * zoomLevel
    
    text = '<rect x="%.3f" y="%.3f" width="%.3f" height="%.3f" ' \
        % (x, y, w, h)
    text += ' fill="%s" stroke="%s" stroke-width="1" />' \
        % (self.fill, self.color)
    return text
  
  def area(self):
    return (self.width * self.height * (self.zoomLevel ** 2))
        

class Polygon:
  def __init__(self, color = "black", points="", zoomLevel=1):
    self.points = []
    self.color = color
    self.zoomLevel = zoomLevel
    self.addPoints(points)
    
  def addPoints(self, points):
    s = points.split(",")
    for i in range(0, len(s) / 2):
      self.addPoint(Point( x= int(s[i * 2]), y=int(s[( i * 2) + 1])))


  def addPoint(self, point):
    self.points.append(point)

  def svgText(self, zoomLevel = 1):
    text = "<polygon points=\""
    for p in self.points:
      text += p.getPolyPoint(zoomLevel= zoomLevel)
    text += "\" style=\"stroke:%s;stroke-width:1\" />" % (self.color)
    return text


class Polyline(Polygon):
  def drawSVG(self, zoomLevel = 1):
    text = Polygon.drawSVG(self,zoomLevel=zoomLevel)
    x = text.replace("polygon", "polyline")
    return x


class Base:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.z = 0
    
    
# def __init__(self, color = "black", x=0, y=0, width=0, height=0 , zoomLevel=1, fill = "none"):    

r = Rect(x=100, y=100, width=150,height=200)
print r.svgText(zoomLevel=0.5)

y = Polyline(points="0,0,10,0,10,10,0,10")
print y.svgText(zoomLevel=0.87)
