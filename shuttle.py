class ShuttleService:
    def __init__(self):
        self.bookings = []

    def book_shuttle(self, customer_name, pickup_location, dropoff_location, distance):
        fare = self.calculate_fare(distance)
        booking = {
            'customer_name': customer_name,
            'pickup_location': pickup_location,
            'dropoff_location': dropoff_location,
            'distance': distance,
            'fare': fare
        }
        self.bookings.append(booking)
        return booking

    def calculate_fare(self, distance):
        # Example fare calculation: $5 per mile
        base_fare = 5
        return base_fare * distance

    def generate_invoice(self, booking):
        invoice = f"""
        ============================
        INVOICE
        ============================
        Customer Name: {booking['customer_name']}
        Pickup Location: {booking['pickup_location']}
        Dropoff Location: {booking['dropoff_location']}
        Distance: {booking['distance']} miles
        Fare: ${booking['fare']}
        ============================
        Thank you for choosing our shuttle service!
        """
        return invoice


# Example usage
if __name__ == "__main__":
    shuttle_service = ShuttleService()

    # Book a shuttle
    booking = shuttle_service.book_shuttle(
        customer_name="John Doe",
        pickup_location="123 Main St",
        dropoff_location="456 Elm St",
        distance=10
    )

    # Generate and print invoice
    invoice = shuttle_service.generate_invoice(booking)
    print(invoice)
