import os, sys
"""
server 
storage 
switch
"""


import os, sys



class Device:
    firmware = ""
    serial = ""
    manufacturer = ""


    def setSerial(self, serial):
        self.serial = serial

    def setFirmware(self, fw):
        self.firmware = fw

    def setManufacturer(self, mf):
        self.manufacturer = mf

    def infoStr(self):
        return (self.firmware, self.serial, self.manufacturer)

class Disk(Device):
    interface = ""
    capacity  = 0
    enclosure = 0
    slot = 0
    devName = ""
    uuid = ""
    type = ""

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
        self.type = typ

class IPV4():
    ip = ""
    netmask = ""
    gateway = ""
    speed = 0

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
    MAC = ""
    IpV4 = IPV4()
    IpV6 = IPV4()
    bonded = False
    slave = False
    slaves = []
    type = ""
    devName = ""

    def __init__(self, MAC, ipv4, devName):
        self.MAC = MAC
        self.IpV4.setIp(ipv4)
        self.devName = devName
        
    def setType(self, type):
        self.type = type

    def setDevice(self, fw, serial, mf):
        rr = 1
        self.setFirmware(fw)
        self.setSerial(serial)
        self.setManufacturer(mf)
        
    def printInterface(self):
        print self.MAC, self.IpV4.ip, self.IpV6.ip , self.devName
        for ss in self.slaves:
            fw,sr,mf = ss.infoStr()
            print " -> ", ss.MAC, ss.devName, fw, sr,mf, ss.type

    def addSlave(self, MAC, devName):
        self.slaves.append(Interface(MAC,"", devName))



x = Interface("EE:FF:AA:BB:CC:DD", "192.168.1.1", "/dev/bond0")
x.bonded = True
x.addSlave("00:11:22:33:44:55", "/dev/eth0")
x.addSlave("00:11:22:33:44:56", "/dev/eth1")
x.addSlave("00:11:22:33:44:57", "/dev/eth2")
x.slaves[0].setDevice("JJE4","A123QWE45","Dell")
x.slaves[0].setType("Ethernet")
x.slaves[1].setDevice("JJE4","A123QWE46","Dell")
x.slaves[1].setType("Infiniband")
x.slaves[2].setDevice("12.3.3","23213123","HP")
x.slaves[2].setType("MyreNet")
x.printInterface()
