#ADXL_LCD
# smbus library
import smbus
import I2C_driver as LCD
# time library
import time

mylcd=LCD.lcd()

bus = smbus.SMBus(1)

# IC address
address = 0x1D

# x-axis, y-axis, z-axis adress
x_adr = 0x32
y_adr = 0x34
z_adr = 0x36

# ADXL345 init
def init_ADXL345():    
    bus.write_byte_data(address, 0x2D, 0x08)

# data measure
def measure_acc(adr):    
    acc0 = bus.read_byte_data(address, adr)

    acc1 = bus.read_byte_data(address, adr + 1)

    acc = (acc1 << 8) + acc0

    if acc > 0x1FF:
        acc = (65536 - acc) * -1

    acc = acc * 3.9 / 1000

    return acc


def main():
    init_ADXL345()

    while 1:
        choice=input('')
        if choice=='1': #if user choice number 1
            mylcd.lcd_display_string("your choice",1)
            mylcd.lcd_display_string("1",2)
        elif choice=='2': #if user choice number 2
            x_acc = measure_acc(x_adr)
            y_acc = measure_acc(y_adr)
            z_acc = measure_acc(z_adr)
            print ('X = %2.2f' % x_acc, '[g], Y = %2.2f' % y_acc, '[g], Z = %2.2f' % z_acc, '[g]')
            time.sleep(1)
        elif choice=='g': #if user choice number g
            break
    mylcd.lcd_clear()
if __name__ == '__main__':
    main()




