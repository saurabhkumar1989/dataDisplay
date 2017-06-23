# only reason to create this is to integrate everthing with django command , even this can be done without this, directly run below 
# program
from channels import Group
from django.core.management import BaseCommand
import time
from json import dumps as jsondumps


# for consumer
from kombu.mixins import ConsumerMixin
from sensorWorker.celery_prj.config import settings

# basic conumer - consume to queue 1

# consumer mixin class more detail here 
# http://docs.celeryproject.org/projects/kombu/en/latest/userguide/consumers.html?highlight=consumer
class dataConsume(ConsumerMixin):
    def __init__(self, connection,queue,exchange):
        self.task_queue = queue
        self.test_exchange = exchange
        self.connection = connection

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=[self.task_queue],callbacks=[self.on_task])]

    # Function call when message arrived
    def on_task(self, body, message):
        # when ever messgae received
        Group("sensor").send({'text': jsondumps({"data": body})
            })
        print(body)
        message.ack()


# print("at latest")
        
#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand,dataConsume):
    # Show this when the user types help
    help = "Simulates reading sensor and sending over Channel."

    # A command must define handle()
    def handle(self, *args, **options):
        data = settings()
        connection,exchange,task_queue1,task_queue2 = data.get_settings()
        # call consumer
        dataConsume(connection,task_queue1,exchange).run()