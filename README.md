# Auto Data Scraper

This project is a Python-based web scraper designed to extract detailed information about vehicles from various websites. The data is stored in a structured format using a custom `Vehicle` class.

## Example Data
| vehicleUrl            | year | make  | model | modification | distance | bodyClass | engineType | transmission | batteryPower | steering | outerColor | innerColor | horsepower | engineVolume | cylinderNumber | driveType | tire  | vin   | condition | description | options | customsClear | price  | phone       | parsedTime        |
|-----------------------|------|-------|-------|--------------|----------|-----------|------------|--------------|--------------|----------|------------|------------|------------|--------------|----------------|-----------|-------|-------|-----------|-------------|---------|--------------|--------|-------------|-------------------|
| https://example.com/1  | 2020 | Toyota| Camry | SE           | 30,000 km| Sedan     | Hybrid     | Automatic    | 2.5 kWh      | Power    | White      | Black      | 208 HP     | 2.5 L        | 4              | FWD       | 17 in | 123ABC| Used      | Well maintained| Sunroof | Yes          | $20,000| 123-456-7890| 2024-08-18 12:00:00|
| https://example.com/2  | 2018 | Honda | Civic | LX           | 45,000 km| Coupe     | Gasoline   | Manual       | -            | Manual   | Red        | Gray       | 158 HP     | 2.0 L        | 4              | FWD       | 16 in | 456DEF| Used      | No accidents  | Leather | No           | $15,500| 987-654-3210| 2024-08-18 12:00:00|
| https://example.com/3  | 2021 | Ford  | F-150 | XLT          | 15,000 mi| Truck     | Diesel     | Automatic    | -            | Power    | Blue       | Black      | 250 HP     | 3.0 L        | 6              | 4WD       | 18 in | 789GHI| New       | Fully loaded  | Towing  | Yes          | $30,000| 555-123-4567| 2024-08-18 12:00:00|

## Features

- **Data Extraction:** Extracts key details about vehicles, including make, model, year, engine specifications, and more.
- **Custom Vehicle Class:** Uses a Python class (`Vehicle`) to store and organize the extracted data.
- **Optimized Data Handling:** Supports multithreading or multiprocessing to efficiently handle large volumes of HTTP requests.
- **Dynamic URL Handling:** Implements classes and methods to handle dynamic URL templates and parameters.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/RobertArustamyan/AutoDataMiner.git
    cd AutoDataMiner
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Update the cookies and headers of requests. Information you can get using curl requests.
Find the line showed in the picture and copy CURL.
![](Images/img.png)

2. Run the scraper:

    ```bash
    python main.py
    ```

3. The scraped data will be stored in the CSV.

## Vehicle Class

The `Vehicle` class is used to store the following attributes:

- `vehicleUrl` Url link of the car.
- `year` Year car was produced.
- `make` Make of car.
- `model` Model of car.
- `modification` Modification of car.
- `distance` Distance the car was driven.
- `bodyClass` Body type of car.
- `engineType` Engine type of car.
- `transmission` Transmission type of car.
- `batteryPower` Battery power of electric car.
- `steering` Steering type (right, left).
- `outerColor` Car color.
- `innerColor` Interior color of car.
- `horsepower` Power of engine in hp.
- `engineVolume` Volume of engine.
- `cylinderNumber` Number of cylinders of engine.
- `driveType` Drive type of car.
- `tire` Tire size of car,
- `vin` Vin number of car.
- `condition` Condition of car.
- `description` Description the owner gave.
- `options` Options of car the owner gave.
- `customsClear` Shows if car is custom clear (true, false).
- `price` Price of car in USD.
- `phone` Phone number of owner.
- `parsedTime` Time data was parsed.

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any inquiries or issues, please contact [RobertArustamyan](mailto:robertarustamyan2@gmail.com).
