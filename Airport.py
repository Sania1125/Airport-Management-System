import uuid

class Passenger:
    def __init__(self, name, passport_number):
        self.id = str(uuid.uuid4())
        self.name = name
        self.passport_number = passport_number

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "passport_number": self.passport_number
        }


class Flight:
    def __init__(self, flight_number, origin, destination, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.capacity = capacity
        self.passengers = []

    def book_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            return f"✔ Seat booked for {passenger.name}"
        return "❌ Flight full!"

    def show_manifest(self):
        return [p.name for p in self.passengers]

    def to_dict(self):
        return {
            "flight_number": self.flight_number,
            "origin": self.origin,
            "destination": self.destination,
            "capacity": self.capacity,
            "passenger_count": len(self.passengers)
        }
