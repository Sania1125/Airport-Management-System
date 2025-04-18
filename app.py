from airport import Flight, Passenger

def main():
    flight1 = Flight("PK303", "Karachi", "Lahore", 2)

    print(flight1.to_dict())

    # Add passengers
    p1 = Passenger("Ali Raza", "PAK123")
    p2 = Passenger("Sana Khan", "PAK456")
    p3 = Passenger("John Smith", "PAK789")

    print(flight1.book_passenger(p1))
    print(flight1.book_passenger(p2))
    print(flight1.book_passenger(p3))  # Should be rejected

    print("Passenger Manifest:", flight1.show_manifest())

if __name__ == "__main__":
    main()
