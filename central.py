# ble_scan_connect.py:
from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate

class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        # print(cHandle, data)
        if cHandle == 13: # heartrate
            print("Heartrate:", data[1])
        if cHandle == 19: # magnet
            list_data = list(data)
            x_value = list_data[1]*256 + list_data[2] - 1024
            y_value = list_data[3]*256 + list_data[4] - 1024
            z_value = list_data[5]*256 + list_data[6] - 1024
            print("Magneto: x = ", x_value, ", y = ", y_value, ", z = ", z_value, sep = "")

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev , isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)
scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
n=0
addr=[]
found_success = False
for dev in devices:
    print ("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr , dev.addrType , dev.rssi))
    addr.append(dev.addr)
    n += 1
    for (adtype , desc , value) in dev.getScanData():
        print (" %s = %s" % (desc,value))
        if value == "Group9": 
            found_success = True
            number = n - 1

if not found_success: 
    number = input('Enter your device number: ')
print ('Device', number)
num = int (number)
print (addr[num])
#
print ("Connecting...")
dev = Peripheral(addr[num], 'random')
dev.setDelegate(MyDelegate())
#
# print ("Services...")
# for svc in dev.services:
#     print (str(svc))
#
try:
    # service = dev.getServiceByUUID(UUID(0x180D))
    # for ch in service.getCharacteristics():
    #     print(str(ch))
#
    
    ch = dev.getCharacteristics(uuid=UUID(0x2A37))[0]
    ch2 = dev.getCharacteristics(uuid=UUID(0x2A15))[0]
    print("Handle of heartrate:", ch.getHandle())
    print("Handle of magnetometer:", ch2.getHandle())
    # if ch.supportsRead() and ch2.supportsRead():
    #     print("readable before editing CCCD: ", ch.read(), "and", ch2.read())
    # else:
    #     print("Do not support read() before editing CCCD. ")

    desc  = ch.getDescriptors(forUUID=0x2902)[0]
    desc2 = ch2.getDescriptors(forUUID=0x2902)[0]
    # print("Original CCCD:", desc.read(), "and", desc2.read())
    desc.write(b"\x01\x00")
    desc2.write(b"\x01\x00")
    # print("Modified CCCD:", desc.read(), "and", desc2.read())

    # if ch.supportsRead() and ch2.supportsRead():
    #     print("readable after editing CCCD: ", ch.read(), "and", ch2.read())
    # else:
    #     print("Do not support read() after editing CCCD. ")


    while True:
        dev.waitForNotifications(1.0)

    #if (ch.supportsRead()):
        #print(ch.read())
#
finally:
    dev.disconnect()
