import sqlite3

conn = sqlite3.connect('ITS.db')
print("Databse connection successfull")

languages = [
    ("EN", "English"),
    ("KR", "Korean"),
    ("FR", "French")
]

conn.executemany('''INSERT INTO "Language" ("LanguageCode", "LanguageName") VALUES (?, ?);''', languages)
conn.commit()

print("Table Language succesfully filled")

countries = [
    ("KR", "South Korea", "KR"),
    ("EN", "England", "EN"),
    ("FR", "France", "FR")
]

conn.executemany('''INSERT INTO "Country" ("CountryCode", "CountryName", "MostFrequentlySpokenLanguage") VALUES (?, ?, ?);''', countries)
conn.commit()

print("Table Country succesfully filled")

officials = [
    ("INCHEON", "Clement Monteiro", "Coach", "KR", "KR"),
    ("INCHEON", "Cyprien Singez", "Journalist", "FR", "FR"),
]

conn.executemany('''INSERT INTO "Official" ("CityID", "Name", "Role", "PreferredLanguage", "CountryCode") VALUES (?, ?, ?, ?, ?);''', officials)
conn.commit()

print("Table Official succesfully filled")

drivers = [
    ("azerty123456789", "Clément Monteiro", 3, "KR")
]

conn.executemany('''INSERT INTO "Driver" ("LicenseNumber", "Name", "ClearanceLevel", "PreferredLanguage") VALUES (?, ?, ?, ?);''', drivers)
conn.commit()

print("Table Driver succesfully filled")

locations = [
    ("Incheon Airport", "Incheon Airport", "Airport"),
    ("Incheon Bus Terminal", "Incheon Bus Terminal", "Bus Terminal"),
    ("Jeju Airport", "Jeju Airport", "Airport")
]

conn.executemany('''INSERT INTO "Location" ("Name", "Address", "Type") VALUES (?, ?, ?);''', locations)
conn.commit()

print("Table Location succesfully filled")

vehicles = [
    ("AA-123-AA", "Tesla", "Model Y", "BLue", 10, 5, False),
    ("AA-123-AA", "Toyota", "Prius", "White", 10000, 5, True),
    ("CC-123-CC", "Renaud", "Clio", "Black", 100000, 4, True)
]

conn.executemany('''INSERT INTO "Vehicle" ("RegistrationID", "Manufacturer", "Model", "Color", "CurrentOdometer", "PassengerCapacity", "Avalaible") VALUES (?, ?, ?, ?, ?, ?, ?);''', vehicles)
conn.commit()

print("Table Vehicle succesfully filled")

vehicleActions = [
    ("R", 1, 10000, 1000, "Repair because of damage", "2023-10-21"),
    ("M", 2, 10, 1000, "Battery replacement", "2023-10-21")
]

conn.executemany('''INSERT INTO "VehicleAction" ("Type", "VehicleID", "Odometer", "FinalCost", "Description", "Date") VALUES (?, ?, ?, ?, ?, ?);''', vehicleActions)
conn.commit()

print("Table VehicleAction succesfully filled")

bookings = [
    ("azerty123456789", "2023-10-21 10:00:00", "2023-10-21 11:00:00", 10000, 10010, 1, 1, 1, 1, 2),
    ("987654321ytreza", "2023-10-21 08:00:00", "2023-10-21 12:00:00", 10, 20, 2, 1, 2, 2, 3)
]

conn.executemany('''INSERT INTO "Booking" ("Reference", "StartTime", "EndTime", "StartOdometer", "EndOdometer", "OfficialID", "DriverID", "VehicleID", "PickupLocationID", "DropOffLocationID") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', bookings)
conn.commit()

print("Table Booking succesfully filled")
