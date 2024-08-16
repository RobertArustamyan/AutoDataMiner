from datetime import datetime
from bs4 import BeautifulSoup

class Vehicle:
    """
    Represents a vehicle with various attributes and details extracted from an HTML card page.

    Represents a vehicle with various attributes and details extracted from an HTML card page.

    Attributes:
    vehicleUrl (str): The URL of the vehicle listing.
    year (str): The year the vehicle was manufactured.
    make (str): The manufacturer or brand of the vehicle.
    model (str): The model name or number of the vehicle.
    modification (str): The modification or trim level of the vehicle.
    distance (str): The distance the vehicle has traveled.
    bodyClass (str): The body class of the vehicle (e.g., sedan, SUV).
    engineType (str): The type of engine in the vehicle.
    transmission (str): The type of transmission (e.g., automatic, manual).
    batteryPower (str): The battery power of the vehicle (for electric vehicles).
    steering (str): The type of steering (e.g., power, manual).
    outerColor (str): The color of the vehicle's exterior.
    innerColor (str): The color of the vehicle's interior.
    horsepower (str): The horsepower of the vehicle's engine.
    engineVolume (str): The engine volume or displacement.
    cylinderNumber (str): The number of cylinders in the engine.
    driveType (str): The type of drive (e.g., front-wheel drive, all-wheel drive).
    tire (str): The size of the tires.
    vin (str): The Vehicle Identification Number (VIN).
    condition (str): The condition of the vehicle.
    description (str): A textual description of the vehicle.
    options (str): Additional options or features of the vehicle.
    customsClear (bool): Whether the vehicle is customs cleared or not.
    price (str): The price of the vehicle in USD.
    phone (str): Contact phone number for the vehicle.
    parsedTime (datetime): The time when the information was parsed.

    Methods:
    createObject(cardHtml: str, cardUrl: str) -> 'Vehicle':
    Creates an instance of Vehicle from the provided HTML code and URL of the card page.

    Usage:
    vehicle_instance = Vehicle.createObject(cardHtml, cardUrl)
    print(vehicle_instance.make)
    """

    def __init__(self,vehicleUrl=None, vehicleYear=None, vehicleMake=None, vehicleModel=None, vehicleModification=None, vehicleDistance=None, vehicleClass=None,
                 vehicleEngine=None, vehicleTransmission=None, vehicleBatteryPower=None, vehicleSteering=None,
                 vehicleOuterColor=None, vehicleInnerColor=None, vehicleHorsepower=None, engineVolume=None,
                 cylinderNumber=None, vehicleDriveType=None, vehicleCondition=None, tireSize=None, vehicleVin=None,
                 vehicleDescription=None,vehicleOptions=None, customsClear=None, vehiclePrice=None, phoneNumber=None):
        self.vehicleUrl = vehicleUrl
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
        self.options = vehicleOptions
        self.customsClear = customsClear
        self.price = vehiclePrice
        self.phone = phoneNumber
        self.parsedTime = datetime.now()

    @classmethod
    def createObject(cls, cardHtml: str, cardUrl: str)-> 'Vehicle':
        """
        Creates an instance of Vehicle and fills it with information from cardHtml.
        :param cardHtml: Html code of Card page.
        :param cardUrl: Offer link of current Card.
        :return: returns an instance of Vehicle.
        """
        soup = BeautifulSoup(cardHtml, 'lxml')

        # Year of car
        yearTag = soup.find('a', class_='grey-text')
        carYear = yearTag.text if yearTag else None
        # Make of car
        makeTag = yearTag.find_next_sibling('a')
        carMake = makeTag.text if makeTag else None
        # Model of car
        modelTag = makeTag.find_next_sibling('a')
        carModel = modelTag.text if modelTag else None

        # Price of car in Usd
        try:
            price_dropdown = soup.find('ul', class_='price-dropdown')

            if price_dropdown:
                price = price_dropdown.find('span', text=lambda t: '$' in t)
                usdPrice = price.text.strip() if price else None
            else:
                usdPrice = None

        except AttributeError as e:
            usdPrice = None

        # Description of car
        try:
            descriptionReference = soup.find('div',class_='nottii bltitle medium', text='Լրացուցիչ')
            descriptionDiv = descriptionReference.find_next('div', class_='ad-options', itemprop='description')
            carDescription = descriptionDiv.text.strip() if descriptionDiv else None
        except AttributeError as e:
            carDescription = None
        try:
            vinDiv = soup.find('div',class_='pad-left-6')
            carVin = vinDiv.text.strip() if vinDiv else None
        except AttributeError as e:
            carVin = None

        # Contacts of person selling car
        try:
            contactDiv = soup.find('div',class_='contact-start')
            phoneNumber = '\n'.join([link['href'].replace('tel:', '') for link in contactDiv.find_all('a', href=True) if link['href'].startswith('tel:')])
        except AttributeError as e:
            phoneNumber = None
        # Options of car
        try:
            referenceDiv = soup.find('div', class_='nottii bltitle medium', text='Օպցիաներ')
            optionsDiv = referenceDiv.find_next('div', class_='ad-options', itemprop='description')
            options = optionsDiv.text.strip() if optionsDiv else None
        except AttributeError as e:
            options = None
        # True if car is customs clear
        try:
            customsSpan = soup.find('span', class_='green-text', text='Մաքսազերծված է')
            customInfo = True if customsSpan else False
        except AttributeError as e:
            customInfo = False

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
            'vehicleOptions': options,
            'vehicleVin': carVin,
            'phoneNumber': phoneNumber,
            'customsClear': customInfo,
            'vehicleUrl': 'https://auto.am' + cardUrl
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

    def showObject(self) -> None:
        """
        Prints all parameters of object.
        """
        attributes = vars(self)
        for key, value in attributes.items():
            print(f"{key}: {value}")

if __name__ == '__main__':
    car = Vehicle()
    print(car.parsedTime)
