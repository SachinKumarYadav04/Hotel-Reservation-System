import cgi
import mysql.connector  
requests = cgi.FieldStorage()
# Get the form data from the POST request
room_type = requests.getvalue('room_type')
number_of_rooms = requests.getvalue('number_of_rooms')
check_in_date = requests.getvalue('check_in_date')
check_out_date = requests.getvalue('check_out_date')
guest_name = requests.getvalue('guest_name')
guest_email = requests.getvalue('guest_email')
guest_phone = requests.getvalue('guest_phone')
# Check if the form is valid
if (room_type and number_of_rooms and check_in_date and check_out_date and guest_name and guest_email and guest_phone):
    # Create a new hotel booking object
    hotel_booking = HotelBooking()
    # Set the room type
    hotel_booking.setRoomType(room_type)
    # Set the number of rooms
    hotel_booking.setNumberOfRooms(number_of_rooms)
    # Set the check-in date
    hotel_booking.setCheckInDate(check_in_date)
    # Set the check-out date
    hotel_booking.setCheckOutDate(check_out_date)
    # Set the guest name
    hotel_booking.setGuestName(guest_name)
    # Set the guest email
    hotel_booking.setGuestEmail(guest_email)
    # Set the guest phone
    hotel_booking.setGuestPhone(guest_phone)
    # Save the hotel booking
    hotel_booking.save()
   # Send a confirmation email to the guest
confirmation_message = "Thank you for booking a hotel room at our hotel. Your booking has been confirmed."

# Print the confirmation message (for testing)
print(confirmation_message)
myconn = mysql.connector.connect(host = "127.0.0.1", user = "root",passwd = "Anushka@25", database = "bookingdb1")  
c=myconn.cursor()
hotel_insert="""INSERT INTO `bookingdb1`.`hotel booking`
(`Room type`,
`Number of room`,
`Check In Date`,
`CheckOut Date`,
`Guest Name`,
`Guest EmailId`,
`Guest Phone`)
VALUES (%s, %s, %s,%s, %s, %s, %s)"""

data=[(1,2,'2023-08-22','2023-08-22','SACHIN','SAC15@gmail.com',9876532101)]
c.executemany(hotel_insert, data)
myconn.commit()
myconn.close
  



