# helpers.py
from datetime import datetime
import logging

# Configure basic logging
logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_action(message: str):
    """
    Logs a given action/message with timestamp.
    """
    logging.info(message)
    print(f"[LOG] {message}")

def current_datetime():
    """
    Returns the current date and time in a readable format.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def flight_summary(flight):
    """
    Returns a readable summary of a flight object.
    """
    return f"Flight {flight.flight_number} | {flight.origin} ➝ {flight.destination} | Capacity: {flight.capacity} | Booked: {len(flight.passengers)}"
