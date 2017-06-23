# from kombu.mixins import ConsumerMixin
# from config import settings

# # basic conumer - consume to queue 1

# # consumer mixin class more detail here 
# # http://docs.celeryproject.org/projects/kombu/en/latest/userguide/consumers.html?highlight=consumer
# class C(ConsumerMixin):

#     def __init__(self, connection,queue,exchange):
#     	self.task_queue = queue
#     	self.test_exchange = exchange
#     	self.connection = connection

#     def get_consumers(self, Consumer, channel):
#         return [Consumer(queues=[self.task_queue],callbacks=[self.on_task])]

#     def on_task(self, body, message):
#     	# when ever messgae received
#     	print("Data is")
#     	print(body)
#     	message.ack()
#     def on_consumer_end(self, connection, default_channel):
#         connection.close()
#         print("dsd")
# data = settings()
# connection,exchange,task_queue1,task_queue2 = data.get_settings()
# C(connection,task_queue1,exchange).run()