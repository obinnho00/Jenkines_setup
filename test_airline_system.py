import unittest
from legacy_airline_system_refactored import AirlineSystem

class TestAirlineSystem(unittest.TestCase):

    def setUp(self):
        self.system = AirlineSystem()

    def test_add_flight(self):
        self.system.flight_manager.add_flight("AI101", "New York", "London", "2025-05-01 18:00", 420, "Boeing 777")
        flight = self.system.flight_manager.flights[0]
        self.assertEqual(flight['flight_number'], "AI101")
        self.assertEqual(flight['origin'], "New York")
        self.assertEqual(flight['destination'], "London")

    def test_register_passenger(self):
        self.system.passenger_manager.register_passenger("Alice Johnson", "P1234567")
        passenger = self.system.passenger_manager.passengers[0]
        self.assertEqual(passenger['name'], "Alice Johnson")
        self.assertEqual(passenger['passport_number'], "P1234567")

    def test_book_flight(self):
        self.system.passenger_manager.register_passenger("Bob Lee", "P2345678")
        self.system.flight_manager.add_flight("AI102", "San Francisco", "Tokyo", "2025-06-01 15:00", 360, "Airbus A380")
        self.system.booking_manager.book_flight("P2345678", "AI102")
        
        booking = self.system.booking_manager.bookings[0]
        self.assertEqual(booking['passenger']['name'], "Bob Lee")
        self.assertEqual(booking['flight']['flight_number'], "AI102")
        
    def test_flight_summary(self):
        self.system.flight_manager.add_flight("AI103", "Paris", "Berlin", "2025-07-01 10:00", 180, "Boeing 747")
        self.system.passenger_manager.register_passenger("John Doe", "P567890")
        self.system.booking_manager.book_flight("P567890", "AI103")
        summary = self.system.flight_summary("AI103")
        self.assertIn("Flight AI103 from Paris to Berlin:", summary)

if __name__ == '__main__':
    unittest.main()
