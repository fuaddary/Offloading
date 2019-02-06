import struct
import smbus
import sys
import time

state_charge = (3.622, 3.832, 4.043, 4.182, 4.21)
#state_discharge = (4.15, 3.74751, 3.501, 3.35, 2.756)
state_discharge = (3.806, 3.50751, 3.371, 3.25, 3.13)
state_charging = False;
v_current = 0;
v_old = 0;
capacity = 0;

def readVoltage(bus):

	"This function returns as float the voltage from the Raspi UPS Hat via the provided SMBus object"
	address = 0x36
	read = bus.read_word_data(address, 2)
	swapped = struct.unpack("<H", struct.pack(">H", read))[0]
	voltage = swapped * 78.125 /1000000
	return voltage


def readCapacity(bus):
	"This function returns as a float the remaining capacity of the battery connected to the Raspi UPS Hat via the provided SMBus object"
	address = 0x36
	read = bus.read_word_data(address, 4)
	swapped = struct.unpack("<H", struct.pack(">H", read))[0]
	capacity = swapped/256
	return capacity

time.localtime(time.time())

while 1:
	bus = smbus.SMBus(1)  # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
	mean = 0
	for i in range(100):
		mean = mean + (readVoltage(bus))
		print readVoltage(bus)
		time.sleep (0.6)
	
	v_old = mean / 100
	v_current = v_old
	
	
	if (v_current > state_discharge[0]):
		capacity = 100
	elif ((v_current < state_discharge[0]) and (v_current >= state_discharge[1])):
		capacity = (v_current - state_discharge[1]) /(state_discharge[0] - state_discharge[1]) * 25 + 75
	elif ((v_current < state_discharge[1]) and (v_current >= state_discharge[2])):
		capacity = (v_current - state_discharge[2]) /(state_discharge[1] - state_discharge[2]) * 25 + 50
	elif ((v_current < state_discharge[2]) and (v_current >= state_discharge[3])):
		capacity = (v_current - state_discharge[3]) /(state_discharge[2] - state_discharge[3]) * 25 + 25
	elif ((v_current < state_discharge[3]) and (v_current >= state_discharge[4])):
		capacity = (v_current - state_discharge[4]) /(state_discharge[3] - state_discharge[4]) * 25
	else:
		capacity = 0
	
	print "Voltage:%5.3fV" % v_current
	print "Battery:%5i%%" % capacity


        f = open('log.txt','a')
        f.write(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime()))
        f.write("Voltage:%5.3fV," % v_current)
        f.write("Battery:%5i%%\n" % capacity)
        f.close()

