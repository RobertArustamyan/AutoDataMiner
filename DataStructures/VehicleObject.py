from datetime import datetime
from bs4 import BeautifulSoup

class Vehicle:
    def __init__(self, vehicleYear=None, vehicleMake=None, vehicleModel=None, vehicleModification=None, vehicleDistance=None, vehicleClass=None,
                 vehicleEngine=None, vehicleTransmission=None, vehicleBatteryPower=None, vehicleSteering=None,
                 vehicleOuterColor=None, vehicleInnerColor=None, vehicleHorsepower=None, engineVolume=None,
                 cylinderNumber=None, vehicleDriveType=None, vehicleCondition=None, tireSize=None, vehicleVin=None,
                 vehicleDescription=None, vehiclePrice=None, phoneNumber=None):
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
        self.driveType = vehicleDriveType
        self.tire = tireSize
        self.vin = vehicleVin
        self.condition = vehicleCondition
        self.description = vehicleDescription
        self.price = vehiclePrice
        self.phone = phoneNumber
        self.parsedTime = datetime.now()

    @classmethod
    def createObject(cls, cardHtml):
        soup = BeautifulSoup(cardHtml, 'lxml')

        yearTag = soup.find('a', class_='grey-text')
        carYear = yearTag.text if yearTag else None

        makeTag = yearTag.find_next_sibling('a')
        carMake = makeTag.text if makeTag else None

        modelTag = makeTag.find_next_sibling('a')
        carModel = modelTag.text if modelTag else None

        try:
            price_dropdown = soup.find('ul', class_='price-dropdown')

            if price_dropdown:
                price = price_dropdown.find('span', text=lambda t: '$' in t)
                usdPrice = price.text.strip() if price else None
            else:
                usdPrice = None

        except AttributeError as e:
            usdPrice = None

        try:
            descriptionDiv = soup.find('div', class_='ad-options', itemprop='description')
            carDescription = descriptionDiv.text.strip() if descriptionDiv else None
        except AttributeError as e:
            carDescription = None
        try:
            vinDiv = soup.find('div',class_='pad-left-6')
            carVin = vinDiv.text.strip() if vinDiv else None
        except AttributeError as e:
            carVin = None

        try:
            contactDiv = soup.find('div',class_='contact-start')
            phoneNumber = '\n'.join([link['href'].replace('tel:', '') for link in contactDiv.find_all('a', href=True) if link['href'].startswith('tel:')])
        except AttributeError as e:
            phoneNumber = None

        label_map = {
            'Վազքը': 'vehicleDistance',
            'Թափքը': 'vehicleClass',
            'Մոդիֆիկացիան':'vehicleModification',
            'Շարժիչը': 'vehicleEngine',
            'Փոխանցման տուփը': 'vehicleTransmission',
            'Ղեկը': 'vehicleSteering',
            'Գույնը': 'vehicleOuterColor',
            'Սրահի գույնը': 'vehicleInnerColor',
            'Ձիաուժը': 'vehicleHorsepower',
            'Վիճակը': 'vehicleCondition',
            'Շարժիչի ծավալը': 'engineVolume',
            'Մարտկոցի տարողունակույունը կվտ': 'vehicleBatteryPower',
            'Մխոցների քանակը': 'cylinderNumber',
            'Քարշակը': 'vehicleDriveType',
            'Անվահեծերը': 'tireSize'
        }
        vehicle_data = {
            'vehicleYear': carYear,
            'vehicleMake': carMake,
            'vehicleModel': carModel,
            'vehiclePrice': usdPrice,
            'vehicleDescription': carDescription,
            'vehicleVin': carVin,
            'phoneNumber': phoneNumber
        }
        table = soup.find('table', class_='pad-top-6 ad-det')
        if table:
            for row in table.find_all('tr'):
                label = row.find('td', class_='bold').text.strip()
                value_td = row.find('td', class_='bold').find_next_sibling('td')
                value = ''.join([str(content).strip() for content in value_td.contents if isinstance(content, str)])

                if label in label_map:
                    vehicle_data[label_map[label]] = value
        return cls(**vehicle_data)

    def showObject(self):
        attributes = vars(self)
        for key, value in attributes.items():
            print(f"{key}: {value}")

if __name__ == '__main__':
    car = Vehicle()
    print(car.parsedTime)
