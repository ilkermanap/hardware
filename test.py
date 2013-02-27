from hardware import *

#x = Interface("EE:FF:AA:BB:CC:DD", "192.168.1.1", "/dev/bond0")
#x.bonded = True
#x.addSlave("00:11:22:33:44:55", "/dev/eth0")
#x.addSlave("00:11:22:33:44:56", "/dev/eth1")
#x.addSlave("00:11:22:33:44:57", "/dev/eth2")
#x.slaves[0].setDevice("JJE4","A123QWE45","Intel","e1000 server adapter")
#x.slaves[0].setType("Ethernet")
#x.slaves[1].setDevice("JJE4","A123QWE46","IBM", "e2000 server adapter")
#x.slaves[1].setType("Infiniband")
#x.slaves[2].setDevice("12.3.3","23213123","HP", "HP FDR Infiniband adapter")
#x.slaves[2].setType("MyreNet")
#x.printInterface()



tt = DiskEnclosure()
tt.setMake("Hp")
print tt.info()
print "---------------"

z = Switch()
z.setMake("HP")
z.setModel("Procurve 5412")
z.setSerial("XXYP23ABC")
z.setFirmware("1.02.33")
z.setSlotCount(12)
m1 = SwitchModule()
m2 = SwitchModule()
m3 = SwitchModule()
m1.setPortCount(2)
m2.setPortCount(4)
m3.setPortCount(16)

m3.setAllPortSpeed(100)


yy = SwitchPortLC()
xx = SwitchPortCX4()
xx.portNo = 15
m3.ports[15] = xx
print xx.svg

m1.setMake("HP")
m1.setModel("CX4 10GB Module")


m1.setAllPortSpeed(10000)
z.setSlotModule(4,m1)
z.setSlotModule(6,m2)
z.setSlotModule(1,m3)

print '-----------'
print
for i in z.info():
    print i
