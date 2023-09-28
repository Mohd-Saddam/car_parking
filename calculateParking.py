import random
import json
from datetime import datetime
import boto3
from botocore.exceptions import NoCredentialsError

class Car:
    def __init__(self, license_plate):
        """
        Initialize a Car instance with a given license plate.

        Args:
            license_plate (str): The license plate of the car.
        """
        if not isinstance(license_plate, str) or len(license_plate) != 7:
            raise ValueError("License plate must be a 7-digit string.")
        self.license_plate = license_plate

    def __str__(self):
        """
        Convert the Car instance to a string representation.

        Returns:
            str: A string representation of the car.
        """
        return f"Car with license plate {self.license_plate}"

class ParkingLot:
    def __init__(self, square_footage, spot_size=(8, 12)):
        """
        Initialize a ParkingLot instance.

        Args:
            square_footage (int): The square footage of the parking lot.
            spot_size (tuple): The size of a parking spot in feet (width, length).
        """
        if square_footage <= 0:
            raise ValueError("Square footage must be a positive value.")
        if not isinstance(spot_size, tuple) or len(spot_size) != 2:
            raise ValueError("Spot size must be a tuple of (width, length).")

        self.square_footage = square_footage
        self.spot_size = spot_size
        self.calculate_max_cars()
        self.parking_lot = [None] * self.max_cars
        self.parked_cars = []

    def calculate_max_cars(self):
        """
        Calculate the maximum number of cars that can fit in the parking lot.
        """
        spot_area = self.spot_size[0] * self.spot_size[1]
        self.max_cars = self.square_footage // spot_area

    def find_empty_spot(self):
        """
        Find an empty parking spot in the parking lot.

        Returns:
            int or None: The index of an empty spot or None if the parking lot is full.
        """
        if None in self.parking_lot:
            empty_spots = [i for i, car in enumerate(self.parking_lot) if car is None]
            return random.choice(empty_spots) if empty_spots else None
        return None

    def park_car(self, car):
        """
        Park a car in the parking lot.

        Args:
            car (Car): The Car instance to be parked.

        Returns:
            str: A message indicating whether the car was parked successfully or not.
        """
        if not isinstance(car, Car):
            raise ValueError("Invalid car object.")

        empty_spot = self.find_empty_spot()
        if empty_spot is not None:
            self.parking_lot[empty_spot] = car
            self.parked_cars.append(car)
            return f"{car} parked successfully in spot {empty_spot}"
        return f"{car} was not parked successfully. Parking lot is full."

    def create_json(self):
        """
        Create a JSON file to store parking data and upload it to an S3 bucket.
        """
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        json_filename = f"parking_lot_{self.square_footage}_ft2_{timestamp}.json"

        data = {}
        for i, car in enumerate(self.parked_cars):
            data[f"Spot {i}"] = str(car)

        with open(json_filename, "w") as json_file:
            json.dump(data, json_file, indent=4)

        # Upload the JSON file to an S3 bucket
        s3_bucket_name = "your_bucket_name"  # Replace with your S3 bucket name
        s3_object_key = f"parking_data/{json_filename}"  # The key (path) in the bucket
        # Replace 'YOUR_ACCESS_KEY' and 'YOUR_SECRET_KEY' with your AWS credentials
        aws_access_key = 'YOUR_ACCESS_KEY'
        aws_secret_key = 'YOUR_SECRET_KEY'

        try:
            s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
            s3.upload_file(json_filename, s3_bucket_name, s3_object_key)
            print(f"Data stored in S3: s3://{s3_bucket_name}/{s3_object_key}")
        except FileNotFoundError:
            print(f"The file {json_filename} was not found.")
        except NoCredentialsError:
            print("AWS credentials not available or incorrect.")
        except Exception as e:
            print(f"Error uploading file: {str(e)}")

def main():
    square_footage = 1600  # Change this to the desired square footage
    try:
        parking_lot = ParkingLot(square_footage)
        print(f"Maximum cars that can be parked: {parking_lot.max_cars}")
        cars = [Car(f"ABC{str(i).zfill(4)}") for i in range(1, parking_lot.max_cars + 1)]

        for car in cars:
            result = parking_lot.park_car(car)
            print(result)

        parking_lot.create_json()
        print(f"Data stored in JSON file and uploaded to S3.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
