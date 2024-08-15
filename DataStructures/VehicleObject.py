from datetime import datetime

class Vehicle:
    def __init__(self, vehicleYear=None, vehicleMake=None, vehicleModel=None, vehicleModification=None,vehicleDistance=None, vehicleClass=None,
                 vehicleEngine=None, vehicleTransmission=None, vehicleBatteryPower=None, vehicleSteering=None,
                 vehicleOuterColor=None, vehicleInnerColor=None, vehicleHorsepower=None, engineVolume=None,
                 cylinderNumber=None,qarshakType=None,vehicleCondition=None,tireSize=None,vehicleVin=None,
                 vehicleDescription=None, vehiclePrice=None,phoneNumber=None):
        self.year = vehicleYear
        self.make = vehicleMake
        self.model = vehicleModel
        self.modification = vehicleModification
        self.distance = vehicleDistance
        self.bodyClass = vehicleClass
        self.engineType = vehicleEngine
        self.transmission = vehicleTransmission
        self.batteryPower = vehicleBatteryPower
        self.steering = vehicleSteering
        self.outerColor = vehicleOuterColor
        self.innerColor = vehicleInnerColor
        self.horsepower = vehicleHorsepower
        self.engineVolume = engineVolume
        self.cylinderNumber = cylinderNumber
        self.qarshak = qarshakType
        self.tire = tireSize
        self.vin = vehicleVin
        self.condition = vehicleCondition
        self.description = vehicleDescription
        self.price = vehiclePrice
        self.phone = phoneNumber
        self.parsedTime = datetime.now()


if __name__ == '__main__':
    car = Vehicle()
    print(car.parsedTime)
