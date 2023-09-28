1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Mohd-Saddam/car_parking
    ```

2. Navigate to the project directory:

    ```bash
    cd carParking
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

5. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```
6. Run the program:
   ```bash
      python calculateParking.py
   ```
8. Output data from terminal:
  ```
Maximum cars that can be parked: 16
Car with license plate ABC0001 parked successfully in spot 15
Car with license plate ABC0002 parked successfully in spot 0
Car with license plate ABC0003 parked successfully in spot 7
Car with license plate ABC0004 parked successfully in spot 4
Car with license plate ABC0005 parked successfully in spot 11
Car with license plate ABC0006 parked successfully in spot 13
Car with license plate ABC0007 parked successfully in spot 12
Car with license plate ABC0008 parked successfully in spot 9
Car with license plate ABC0009 parked successfully in spot 1
Car with license plate ABC0010 parked successfully in spot 10
Car with license plate ABC0011 parked successfully in spot 6
Car with license plate ABC0012 parked successfully in spot 3
Car with license plate ABC0013 parked successfully in spot 14
Car with license plate ABC0014 parked successfully in spot 8
Car with license plate ABC0015 parked successfully in spot 5
Car with license plate ABC0016 parked successfully in spot 2
Data stored in S3: s3://parking-bucket-data/parking_data/parking_lot_1600_ft2_20230928225844.json
Data stored in JSON file and uploaded to S3.
 ```
 ```
{
    "Spot 0": "Car with license plate ABC0001",
    "Spot 1": "Car with license plate ABC0002",
    "Spot 2": "Car with license plate ABC0003",
    "Spot 3": "Car with license plate ABC0004",
    "Spot 4": "Car with license plate ABC0005",
    "Spot 5": "Car with license plate ABC0006",
    "Spot 6": "Car with license plate ABC0007",
    "Spot 7": "Car with license plate ABC0008",
    "Spot 8": "Car with license plate ABC0009",
    "Spot 9": "Car with license plate ABC0010",
    "Spot 10": "Car with license plate ABC0011",
    "Spot 11": "Car with license plate ABC0012",
    "Spot 12": "Car with license plate ABC0013",
    "Spot 13": "Car with license plate ABC0014",
    "Spot 14": "Car with license plate ABC0015",
    "Spot 15": "Car with license plate ABC0016"
}
```
9. Bucket data screenshot
    ```
    <img width="1402" alt="Screenshot 2023-09-28 at 11 09 12 PM" src="https://github.com/Mohd-Saddam/car_parking/assets/50014573/50654784-9595-4f40-9b1d-f41e06ef41f8">

    ```
