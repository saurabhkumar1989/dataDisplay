from kombu.mixins import ConsumerMixin
from config import settings

# basic conumer - consume to queue 2


data = settings()
connection,exchange,task_queue1,task_queue2 = data.get_settings()
class C(ConsumerMixin):

    def __init__(self, connection,queue,exchange):
    	self.task_queue = queue
    	self.test_exchange = exchange
    	self.connection = connection

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=[self.task_queue],callbacks=[self.on_task])]

    def on_task(self, body, message):
    	# when ever messgae received,this function calls
    	print("Data is ")
    	print(body)
    	message.ack()

# consumer mixin class more detail here 
# http://docs.celeryproject.org/projects/kombu/en/latest/userguide/consumers.html?highlight=consumer
C(connection,task_queue2,exchange).run()
consumer.close()
connection.close()