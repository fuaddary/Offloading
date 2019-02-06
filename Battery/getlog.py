# Example of Raspi UPS Hat
#
# You should install wiringPi first.
# sudo apt-get update
# sudo apt-get upgrade
# git clone git://git.drogon.net/wiringPi
# cd wiringPi
# git pull origin
# cd wiringPi
# ./build

import sys
import time
# import Raspi UPS Hat library
import raspiupshat

# init Raspi UPS Hat
raspiupshat.init();

time.localtime(time.time())

f = open('logcharge.txt','a')
f.write('---------------------------------------------------\n')
f.write(time.strftime("[%Y-%m-%d %H:%M:%S] Start logging...\n", time.localtime()))
f.close()

while True:
	f = open('log.txt','a')
	f.write(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime()))
	f.write("Voltage:%5.2fV," % raspiupshat.getv())
	f.write("Battery:%5i%%\n" % raspiupshat.getsoc())
	f.close()
	print "Battery:%5i%%\n" % raspiupshat.getsoc()
	time.sleep(60)

