"""
Base classes and classes for hardware
"""

class Device:
    def __init__(self):
        self.firmware = ""
        self.serial = ""
        self.make = ""
        self.model = ""

    def setSerial(self, serial):
        self.serial = serial

    def setFirmware(self, fw):
        self.firmware = fw

    def setMake(self, mk):
        self.make = mk

    def setModel(self, md):
        self.model = md

    def infoStr(self):
        return (self.firmware, self.serial, self.make, self.model)
    
    def info(self):
        return "Make : %s Model : %s Serial : %s  Firmware : %s" % (self.make,self.model, self.serial, self.firmware)
    
class Transciever(Device):
    def __init__(self):
        Device.__init__(self)        
        self.trType = "-"
        self.portSpeed = 0

    def info(self):
        return self.trType

class SwitchPort():
    def __init__(self):
        self.portNo = 0
        self.portType = ""
        self.portSpeed = 0
        self.vlanTag = ""
        self.destination = ""
        self.hasTransciever = False
        self.transciever = 0
        self.svg = '<symbol id="rj45">  <rect x=0  y=0 widht=12mm height= 9mm> </symbol>'
        
    def svgSymbol(self):
        return svg
    
    def addTransciever(self, tcv):
        self.transciever = tcv
    
    def setPortNo(self, no):
        self.portNo = no

    def setSpeed(self, spd):
        self.portSpeed = spd
    
    def setType(self, typ):
        self.portType = typ
            
    def info(self):
        t = "port no: %s port speed : %d  port type : %s" % (self.portNo, self.portSpeed, self.portType)
        return t

class SwitchPortFiber(SwitchPort):
    def __init__(self):
        SwitchPort.__init__(self)
        self.placeHolder = 0
        
class SwitchPortLC(SwitchPortFiber):
    def __init__(self):
        SwitchPortFiber.__init__(self)
        self.svg = '<symbol id=fbLC> <rect x=0  y=0 widht=12mm height=9mm> <rect x=3  y=3 widht=6mm height= 3mm> </symbol>'

class SwitchPortCX4(SwitchPort):
    def __init__(self):
        SwitchPort.__init__(self)
        self.svg = '<symbol id=cx4> <rect x=0  y=0 widht=12mm height=9mm> <rect x=3  y=3 widht=6mm height= 3mm> </symbol>'

class SwitchModule(Device):
    def __init__(self):
        Device.__init__(self)
        self.numPorts = 0
        self.slot = 0
        self.ports = []

    def setPortCount(self, numPorts):
        self.numPorts = numPorts
        for i in range(numPorts):
            xx = SwitchPort()
            xx.portNo = i
            self.ports.append(xx)

    def setAllPortSpeed(self, speed):
        for i in range(len(self.ports)):
            self.ports[i].setSpeed(speed)

    def setPortSpeed(self, portNo, speed):
        self.ports[portNo].setSpeed(speed)
            
    def info(self):
        if self.numPorts > 0:
            t = []
            print self.make
            t.append("%s %s" % (self.make, self.model))
            for i in self.ports:
                t.append(i.info())
            return t
        else:
            return None

class Switch(Device):
    def __init__(self):
        Device.__init__(self)
        self.numPorts = 0
        self.numSlots = 0
        self.slots = []
        self.ports = []
        self.location = ""
        self.rackUnitLocation = 0

    def setSlotCount(self, num):
        self.slots = []
        for i in range(num):
            self.slots.append(None)

    def setSlotModule(self, slotNo, module):
        self.slots[slotNo] = module

    def setPortCount(self, num):
        for i in range(num):
            xx = SwitchPort()
            xx.portNo = i
            self.ports.append(xx)
            xx = 0

    def info(self):
        temp = "Make : %s   Model : %s Serial : %s  Firmware : %s" % (self.make,self.model, self.serial, self.firmware)
        t = []
        t.append(temp)
        for i in self.ports:
            xx = i.info()
            t.append(xx)
        x = 0
        for i in self.slots:
            
            if i != None:
                for port in i.info():
                    t.append(port)
            else:
                t.append("Empty Slot %d " % x)
            x += 1
        return t



class Server(Device):
    def __init__(self):
        Device.__init__(self)
        
        
class Disk(Device):
    def __init__(self):
        Device.__init__(self)
        self.interface = ""
        self.capacity  = 0
        self.enclosure = 0
        self.slot = 0
        self.devName = ""
        self.uuid = ""
        self.diskType = ""

    def setInterface(self, ifc):
        self.interface = ifc

    def setCapacity(self, cap):
        self.capacity = cap
    
    def setLocation(self, enc, slt):
        self.enclosure = enc
        self.slot = slt

    def setDeviceName(self, devname):
        self.devName = devname

    def setType(self, typ):
        self.diskType = typ

class DiskEnclosure(Device):
    def __init__(self):
        Device.__init__(self)

class IPV4():
    def __init__(self):
        self.ip = ""
        self.netmask = ""
        self.gateway = ""
        self.speed = 0

    def __init__(self):
        self.ip = ""

    def setIp(self, ipaddr):
        self.ip = ipaddr

    def setMask(self,mask):
        self.netmask = mask
        
    def setGateway(self, gw):
        self.gateway = gw

    def setSpeed(self, sp):
        self.speed = sp

class Interface(Device):
    def __init__(self, MAC, ipv4, devName):
        Device.__init__(self)        
        self.MAC = MAC
        self.devName = devName
        self.IpV4 = IPV4()
        self.IpV6 = IPV4()
        self.bonded = False
        self.slave = False
        self.slaves = []
        self.type = ""
        self.IpV4.setIp(ipv4)
        
    def setType(self, typ):
        self.type = typ

    def setDevice(self, fw, serial, mk, md):
        self.setFirmware(fw)
        self.setSerial(serial)
        self.setMake(mk)
        self.setModel(md)

    def printInterface(self):
        print self.MAC, self.IpV4.ip, self.IpV6.ip , self.devName
        for ss in self.slaves:
            fw,sr,mk, md = ss.infoStr()
            print " -> ", ss.MAC, ss.devName, fw, sr,mk, md, ss.type

    def addSlave(self, MAC, devName):
        self.slaves.append(Interface(MAC,"", devName))
