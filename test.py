from hardware import *

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

