from random import uniform,random

class SensorData():
    """docstring for SensorData"""
    def __init__(self, arg):
        self.connect = arg
        self.temperature = None
        self.humidity = None
    def getData(self):
        self.humidity = random()
        self.temperature = random()
        return self.temperature,self.humidity
        
if __name__ == "__main__":
    data = SensorData(None)
    print(data.getData())