import machine
import time 
i2c=machine.I2C(machine.Pin(sda=1),machine.Pin(scl=2),freq=400000)
#SD0 MPU-6000
#buffer=[]
print(i2c.scan())
#while True:
  # time.sleep(5)
  # numt.append(i2c.readfrom_mem(111011101,2,2))
    #time.sleep(5)
   #numa.append(i2c.readfrom_mem(1101000,2,2))
   
    