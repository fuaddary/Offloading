from bluepy import btle
import struct

class MyDelegate(btle.DefaultDelegate):
    def __init__(self,params):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self,cHandle,data):
        print("handling notification...")
##        print(self)
##        print(cHandle)
        print(data)

p = btle.Peripheral('00:15:85:14:9c:09')
p.setDelegate(MyDelegate(0))

while True:
    if p.waitForNotifications(1.0):
        continue
    print("waiting...")
