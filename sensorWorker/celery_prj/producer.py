# Producer - take data from the sensor , data_sensor folder
from kombu.connection import Connection
from kombu import Producer
from time import sleep
from config import settings
import sys,os
# from sensorWorker.data_sensor import sensorReading
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data_sensor.sensorReading import SensorData

# Sensor data object
tmp = SensorData(None)


data = settings()
connection,exchange,task_queue1,task_queue2 = data.get_settings()

publisher = Producer(connection,exchange=exchange)

publisher.publish("dta22")
for i in range(1000):
	# routing key is not required in case of fanout method
	publisher.publish(tmp.getData())
	print(i)
	sleep(.9)
publisher.close()
connection.close()