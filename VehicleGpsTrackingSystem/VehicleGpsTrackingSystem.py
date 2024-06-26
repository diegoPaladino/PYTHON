# VehicleGpsTrackingSystem.py

import requests
import time

class Vehicle:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.latitude = None
        self.longitude = None

    def update_location(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"Vehicle {self.name} (ID: {self.id}) is at latitude {self.latitude} and longitude {self.longitude}"

class GpsTracker:
    def __init__(self, tracking_url):
        self.tracking_url = tracking_url
        self.vehicles = {}

    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.id] = vehicle

    def fetch_vehicle_location(self, vehicle_id):
        response = requests.get(f"{self.tracking_url}/{vehicle_id}")
        if response.status_code == 200:
            data = response.json()
            return data['latitude'], data['longitude']
        else:
            print(f"Failed to fetch location for vehicle {vehicle_id}")
            return None, None

    def update_all_locations(self):
        for vehicle_id, vehicle in self.vehicles.items():
            latitude, longitude = self.fetch_vehicle_location(vehicle_id)
            if latitude is not None and longitude is not None:
                vehicle.update_location(latitude, longitude)

    def display_all_locations(self):
        for vehicle in self.vehicles.values():
            print(vehicle)

if __name__ == "__main__":
    # Sample tracking URL
    TRACKING_URL = "http://example.com/api/vehicle"

    # Initialize the GPS tracker
    gps_tracker = GpsTracker(TRACKING_URL)

    # Add vehicles to be tracked
    gps_tracker.add_vehicle(Vehicle(1, "Truck 1"))
    gps_tracker.add_vehicle(Vehicle(2, "Van 1"))
    gps_tracker.add_vehicle(Vehicle(3, "Car 1"))

    while True:
        gps_tracker.update_all_locations()
        gps_tracker.display_all_locations()
        time.sleep(10)  # Wait for 10 seconds before the next update
