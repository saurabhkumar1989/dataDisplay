from kombu.connection import Connection
from kombu import Queue,Exchange

# Basic settings for queue, routing key and connection
class settings():
	def __init__(self):
		self.connection = Connection('amqp://kgmcrbkn:JEWBpwC2KUnSahYN680d9lkpqr8eh62o@fish.rmq.cloudamqp.com/kgmcrbkn')
		# exchange queue - Fanout connection - data transfer to every queue
		self.direct_exchange = Exchange(name='test1',type='fanout')
		# first queue, routing key is not needed in fanout method
		self.task_queue1 = Queue(name ='queue1',exchange=self.direct_exchange)
		# second queue, routing key is not needed in fanout method
		self.task_queue2 = Queue(name ='queue2',exchange=self.direct_exchange)
		
	def get_settings(self):
		return[self.connection,self.direct_exchange,self.task_queue1,self.task_queue2]


if __name__ == "__main__":
	data = settings()
	print(data.get_settings())