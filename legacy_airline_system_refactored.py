from datetime import datetime, timedelta
import logging

MAX_SEATS = 150

# Configure logging
logging.basicConfig(level=logging.INFO)

class FlightManager:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight_number, origin, destination, departure_time, duration_minutes, aircraft_type):
        flight = {
            'flight_number': flight_number,
            'origin': origin,
            'destination': destination,
            'departure_time': departure_time,
            'arrival_time': departure_time + timedelta(minutes=duration_minutes),
            'aircraft_type': aircraft_type,
            'seats_available': MAX_SEATS
        }
        self.flights.append(flight)
        logging.info(f"Flight {flight_number} added.")
        return flight


class PassengerManager:
    def __init__(self):
        self.passengers = []

    def register_passenger(self, name, passport_number):
        passenger = {
            'name': name,
            'passport_number': passport_number,
            'registered_on': datetime.now()
        }
        self.passengers.append(passenger)
        logging.info(f"Passenger '{name}' registered.")
        return passenger


class CrewManager:
    def __init__(self):
        self.crew_members = []

    def assign_crew_member(self, name, role, flight_number):
        crew = {
            'name': name,
            'role': role,
            'assigned_flight': flight_number
        }
        self.crew_members.append(crew)
        logging.info(f"Crew member '{name}' assigned to flight {flight_number}.")
        return crew


class BookingManager:
    def __init__(self, flights, passengers):
        self.bookings = []
        self.flights = flights
        self.passengers = passengers

    def book_flight(self, passport_number, flight_number):
        passenger = next((p for p in self.passengers if p['passport_number'] == passport_number), None)
        flight = next((f for f in self.flights if f['flight_number'] == flight_number), None)

        if not passenger or not flight:
            logging.error("Passenger or Flight not found.")
            return

        if flight['seats_available'] <= 0:
            logging.error("No seats available on this flight.")
            return

        booking = {
            'passenger': passenger,
            'flight': flight,
            'booking_date': datetime.now(),
            'seat_number': 151 - flight['seats_available']
        }

        flight['seats_available'] -= 1
        self.bookings.append(booking)
        logging.info(f"Booking successful for {passenger['name']} on flight {flight['flight_number']}.")


class AirlineSystem:
    def __init__(self):
        self.flight_manager = FlightManager()
        self.passenger_manager = PassengerManager()
        self.crew_manager = CrewManager()
        self.booking_manager = BookingManager(self.flight_manager.flights, self.passenger_manager.passengers)

    def flight_summary(self, flight_number):
        flight = next((f for f in self.flight_manager.flights if f['flight_number'] == flight_number), None)

        if not flight:
            logging.error("Flight not found.")
            return

        crew = [c for c in self.crew_manager.crew_members if c['assigned_flight'] == flight_number]
        booked_passengers = [b['passenger']['name'] for b in self.booking_manager.bookings if b['flight']['flight_number'] == flight_number]

        logging.info(f"Flight {flight_number} from {flight['origin']} to {flight['destination']}:")
        logging.info(f"Departure: {flight['departure_time']} | Arrival: {flight['arrival_time']}")
        logging.info("Crew Members:")
        for c in crew:
            logging.info(f" - {c['name']} ({c['role']})")
        logging.info("Booked Passengers:")
        for name in booked_passengers:
            logging.info(f" - {name}")



if __name__ == '__main__':
    airline_system = AirlineSystem()
    flight = airline_system.flight_manager.add_flight("AI101", "New York", "London", datetime(2025, 5, 1, 18, 0), 420, "Boeing 777")
    passenger_1 = airline_system.passenger_manager.register_passenger("Alice Johnson", "P1234567")
    passenger_2 = airline_system.passenger_manager.register_passenger("Bob Lee", "P2345678")
    crew_1 = airline_system.crew_manager.assign_crew_member("Captain Morgan", "Pilot", "AI101")
    crew_2 = airline_system.crew_manager.assign_crew_member("Dana Scott", "Flight Attendant", "AI101")
    airline_system.booking_manager.book_flight("P1234567", "AI101")
    airline_system.booking_manager.book_flight("P2345678", "AI101")
    airline_system.flight_summary("AI101")
