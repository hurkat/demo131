class Car:
    def engine_on(self):
        print("engine is on and car has been started")
        return self
    def drive(self):
        print("you are driving the car.")
        return self
    def brake(self):
        print("you have stopped your car")
        return self
    def engine_off(self):
        print("engine is off now")
        return self
car=Car()
car.engine_on()\
    .drive()\
    .brake()\
    .engine_off()
