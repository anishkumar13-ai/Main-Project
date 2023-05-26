class Package:
    def __init__(self, name, flights, hotels, activities):
        self.name = name
        self.flights = flights
        self.hotels = hotels
        self.activities = activities

    def calculate_total_cost(self):
        total_cost = sum([item.price for item in self.flights + self.hotels + self.activities])
        return total_cost


class Flight:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Hotel:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Activity:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Booking:
    def __init__(self, customer, package):
        self.customer = customer
        self.package = package

    def calculate_total_cost(self):
        return self.package.calculate_total_cost()

    def display_booking_details(self):
        print("Booking Details:")
        print("Customer:", self.customer.name)
        print("Package:", self.package.name)
        print("Total Cost:", self.calculate_total_cost())


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class PaymentInfo:
    def __init__(self, card_number, card_holder, expiration_date, cvv):
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiration_date = expiration_date
        self.cvv = cvv


class PackageManagement:
    def __init__(self):
        self.packages = []
        self.bookings = []

    def create_package(self):
        name = input("Enter package name: ")
        flights = []
        hotels = []
        activities = []

        add_flights = input("Add flights to the package? (y/n): ")
        while add_flights.lower() == "y":
            flight_name = input("Enter flight name: ")
            flight_price = float(input("Enter flight price: "))
            flight = Flight(flight_name, flight_price)
            flights.append(flight)
            add_flights = input("Add another flight? (y/n): ")

        add_hotels = input("Add hotels to the package? (y/n): ")
        while add_hotels.lower() == "y":
            hotel_name = input("Enter hotel name: ")
            hotel_price = float(input("Enter hotel price: "))
            hotel = Hotel(hotel_name, hotel_price)
            hotels.append(hotel)
            add_hotels = input("Add another hotel? (y/n): ")

        add_activities = input("Add activities to the package? (y/n): ")
        while add_activities.lower() == "y":
            activity_name = input("Enter activity name: ")
            activity_price = float(input("Enter activity price: "))
            activity = Activity(activity_name, activity_price)
            activities.append(activity)
            add_activities = input("Add another activity? (y/n): ")

        package = Package(name, flights, hotels, activities)
        self.packages.append(package)
        print("Package created successfully!")

    def modify_package(self):
        package_name = input("Enter package name to modify: ")
        found_package = None
        for package in self.packages:
            if package.name == package_name:
                found_package = package
                break

        if found_package:
            choice = input("What do you want to modify? (1. Flights, 2. Hotels, 3. Activities): ")
            if choice == "1":
                found_package.flights = self._modify_components(found_package.flights, Flight)
            elif choice == "2":
                found_package.hotels = self._modify_components(found_package.hotels, Hotel)
            elif choice == "3":
                found_package.activities = self._modify_components(found_package.activities, Activity)
            else:
                print("Invalid choice.")
        else:
            print("Package not found.")

    def _modify_components(self, components, component_class):
        modified_components = components.copy()

        action = input("Add or remove? (add/remove): ")
        if action == "add":
            component_name = input("Enter component name: ")
            component_price = float(input("Enter component price: "))
            component = component_class(component_name, component_price)
            modified_components.append(component)
        elif action == "remove":
            component_name = input("Enter component name to remove: ")
            found_component = None
            for component in modified_components:
                if component.name == component_name:
                    found_component = component
                    break
            if found_component:
                modified_components.remove(found_component)
            else:
                print("Component not found.")

        return modified_components

    def browse_packages(self):
        print("Available Packages:")
        for package in self.packages:
            print(f"Package Name: {package.name}")
            print("Flights:")
            for flight in package.flights:
                print(f"- {flight.name}: ${flight.price}")
            print("Hotels:")
            for hotel in package.hotels:
                print(f"- {hotel.name}: ${hotel.price}")
            print("Activities:")
            for activity in package.activities:
                print(f"- {activity.name}: ${activity.price}")
            print("")

    def search_package(self):
        keyword = input("Enter keyword to search for package: ")
        found_packages = []
        for package in self.packages:
            if keyword.lower() in package.name.lower():
                found_packages.append(package)

        if found_packages:
            print(f"Found {len(found_packages)} package(s) matching '{keyword}':")
            for package in found_packages:
                print(f"Package Name: {package.name}")
                print("Flights:")
                for flight in package.flights:
                    print(f"- {flight.name}: ${flight.price}")
                print("Hotels:")
                for hotel in package.hotels:
                    print(f"- {hotel.name}: ${hotel.price}")
                print("Activities:")
                for activity in package.activities:
                    print(f"- {activity.name}: ${activity.price}")
                print("")
        else:
            print("No packages found.")

    def create_booking(self):
        package_name = input("Enter package name for the booking: ")
        customer_name = input("Enter customer name: ")
        customer_email = input("Enter customer email: ")

        found_package = None
        for package in self.packages:
            if package.name == package_name:
                found_package = package
                break

        if found_package:
            customer = Customer(customer_name, customer_email)
            booking = Booking(customer, found_package)
            self.bookings.append(booking)
            print("Booking created successfully!")
        else:
            print("Package not found.")

    def view_bookings(self):
        if self.bookings:
            print("All Bookings:")
            for booking in self.bookings:
                booking.display_booking_details()
                print("-------------------------")
        else:
            print("No bookings found.")

    def modify_booking(self):
        if self.bookings:
            customer_email = input("Enter customer email for the booking to modify: ")

            found_booking = None
            for booking in self.bookings:
                if booking.customer.email == customer_email:
                    found_booking = booking
                    break

            if found_booking:
                choice = input("What do you want to modify? (1. Package, 2. Customer): ")
                if choice == "1":
                    package_name = input("Enter new package name: ")

                    found_package = None
                    for package in self.packages:
                        if package.name == package_name:
                            found_package = package
                            break

                    if found_package:
                        found_booking.package = found_package
                        print("Package modified successfully!")
                    else:
                        print("Package not found.")
                elif choice == "2":
                    new_customer_name = input("Enter new customer name: ")
                    found_booking.customer.name = new_customer_name
                    print("Customer name modified successfully!")
                else:
                    print("Invalid choice.")
            else:
                print("Booking not found.")
        else:
            print("No bookings found.")

    def delete_booking(self):
        if self.bookings:
            customer_email = input("Enter customer email for the booking to delete: ")

            found_booking = None
            for booking in self.bookings:
                if booking.customer.email == customer_email:
                    found_booking = booking
                    break

            if found_booking:
                self.bookings.remove(found_booking)
                print("Booking deleted successfully!")
            else:
                print("Booking not found.")
        else:
            print("No bookings found.")


def main():
    package_management = PackageManagement()

    while True:
        print("1. Create Package")
        print("2. Modify Package")
        print("3. Browse Packages")
        print("4. Search Package")
        print("5. Create Booking")
        print("6. View Bookings")
        print("7. Modify Booking")
        print("8. Delete Booking")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            package_management.create_package()
        elif choice == "2":
            package_management.modify_package()
        elif choice == "3":
            package_management.browse_packages()
        elif choice == "4":
            package_management.search_package()
        elif choice == "5":
            package_management.create_booking()
        elif choice == "6":
            package_management.view_bookings()
        elif choice == "7":
            package_management.modify_booking()
        elif choice == "8":
            package_management.delete_booking()
        elif choice == "9":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
