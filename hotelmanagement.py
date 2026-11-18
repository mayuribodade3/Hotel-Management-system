booking = {}

while True:
    print("========== HOTEL MANAGEMENT SYSTEM ==========")
    print("1. Add Booking")
    print("2. Display All Bookings")
    print("3. Search Booking")
    print("4. Update Booking")
    print("5. Delete Booking")
    print("6. Exit")

    choice = int(input("Hey user, please enter your choice: "))

    match choice:

        case 1:
            print("========== ADD BOOKING ==========")

            bookingId = int(input("Enter Booking ID: "))

            if bookingId in booking:
                print("Booking ID already exists")

            else:
                name = input("Enter Customer Name: ")
                roomNo = int(input("Enter Room Number: "))
                roomType = input("Enter Room Type: ")
                days = int(input("Enter Number of Days: "))
                phone = input("Enter Phone Number: ")

                booking[bookingId] = {
                    "name": name,
                    "roomNo": roomNo,
                    "roomType": roomType,
                    "days": days,
                    "phone": phone
                }

                print("Booking added successfully!")

        case 2:
            print("========== DISPLAY BOOKINGS ==========")

            if len(booking) == 0:
                print("No booking records found ")

            else:
                for bookingId, details in booking.items():
                    print("Booking ID:", bookingId)
                    print("Customer Name:", details["name"])
                    print("Room Number:", details["roomNo"])
                    print("Room Type:", details["roomType"])
                    print("Number of Days:", details["days"])
                    print("Phone Number:", details["phone"])
                    print("=" * 20)

        case 3:
            print("========== SEARCH BOOKING ==========")

            bookingId = int(input("Enter Booking ID: "))

            if bookingId in booking:
                print("Booking Found")
                print("Customer Name:", booking[bookingId]["name"])
                print("Room Number:", booking[bookingId]["roomNo"])
                print("Room Type:", booking[bookingId]["roomType"])
                print("Number of Days:", booking[bookingId]["days"])
                print("Phone Number:", booking[bookingId]["phone"])

            else:
                print("Booking ID not found")

        case 4:
            print("========== UPDATE BOOKING ==========")

            bookingId = int(input("Enter Booking ID to update: "))

            if bookingId in booking:
                name = input("Enter Updated Customer Name: ")
                roomNo = int(input("Enter Updated Room Number: "))
                roomType = input("Enter Updated Room Type: ")
                days = int(input("Enter Updated Number of Days: "))
                phone = input("Enter Updated Phone Number: ")

                booking[bookingId]["name"] = name
                booking[bookingId]["roomNo"] = roomNo
                booking[bookingId]["roomType"] = roomType
                booking[bookingId]["days"] = days
                booking[bookingId]["phone"] = phone

                print("Booking updated successfully!")

            else:
                print("Booking ID not found")

        case 5:
            print("========== DELETE BOOKING ==========")

            bookingId = int(input("Enter Booking ID to delete: "))

            if bookingId in booking:
                booking.pop(bookingId)
                print("Booking deleted successfully!")

            else:
                print("Booking ID not found")

        case 6:
            print("Thank you for using Hotel Management System!")
            break

        case _:
            print("Invalid choice! Please try again.")