import sqlite3

conn = sqlite3.connect('ITS.db')
print("Databse connection successfull")

conn.execute('''CREATE TABLE IF NOT EXISTS "Vehicle"(
  "VehicleID" INTEGER NOT NULL,
  "RegistrationID" TEXT NOT NULL,
  "Manufacturer" TEXT NOT NULL,
  "Model" TEXT NOT NULL,
  "Color" TEXT NOT NULL,
  "CurrentOdometer" INT NOT NULL,
  "PassengerCapacity" INT NOT NULL,
  "Avalaible" BOOLEAN NOT NULL,
  PRIMARY KEY("VehicleID"));'''
)

print("Table Vehicle succesfully created")

conn.execute('''CREATE TABLE IF NOT EXISTS "Language"(
  "LanguageCode" CHAR(2) NOT NULL,
  "LanguageName" TEXT NOT NULL,
  PRIMARY KEY("LanguageCode"));'''
)

print("Table Language succesfully created")

conn.execute('''CREATE TABLE IF NOT EXISTS "Country"(
  "CountryCode" CHAR(2) NOT NULL,
  "CountryName" TEXT NOT NULL,
  "MostFrequentlySpokenLanguage" CHAR(2) NOT NULL,
  PRIMARY KEY("CountryCode"),
  CONSTRAINT "Language_Country"
    FOREIGN KEY ("MostFrequentlySpokenLanguage")
      REFERENCES "Language" ("LanguageCode"));'''
)

print("Table Country succesfully created")

conn.execute('''CREATE TABLE IF NOT EXISTS "Official"(
  "OfficialID" INTEGER NOT NULL,
  "CityID" CHAR(8) NOT NULL,
  "Name" TEXT NOT NULL,
  "Role" TEXT NOT NULL,
  "PreferredLanguage" CHAR(2) NOT NULL,
  "CountryCode" CHAR(2) NOT NULL,
  PRIMARY KEY("OfficialID"),
  CONSTRAINT "Language_Official"
    FOREIGN KEY ("PreferredLanguage") REFERENCES "Language" ("LanguageCode"),
  CONSTRAINT "Country_Official"
    FOREIGN KEY ("CountryCode") REFERENCES "Country" ("CountryCode"));'''
)

print("Table Official succesfully created")

conn.execute('''CREATE TABLE IF NOT EXISTS "Driver"(
  "DriverID" INTEGER NOT NULL,
  "LicenseNumber" CHAR(18) NOT NULL,
  "Name" TEXT NOT NULL,
  "ClearanceLevel" INT NOT NULL,
  "FATLLevel" INT,
  "FATLQualificationDate" DATE,
  "STLVTLevel" INT,
  "STLVTQualificationDate" DATE,
  "STLVTCertifyingAuthority" TEXT,
  "PreferredLanguage" NCHAR NOT NULL,
  PRIMARY KEY("DriverID"),
  CONSTRAINT "Language_Driver"
    FOREIGN KEY ("PreferredLanguage") REFERENCES "Language" ("LanguageCode"));'''
)

print("Table Driver succesfully created")

conn.execute('''CREATE TABLE IF NOT EXISTS "Location"(
  "LocationID" INTEGER NOT NULL,
  "Name" TEXT NOT NULL,
  "Address" TEXT NOT NULL,
  "Type" TEXT NOT NULL,
  PRIMARY KEY("LocationID"));'''
)

print("Table Location succesfully created")

conn.execute('''CREATE TABLE IF NOT EXISTS "Booking"(
  "Reference" TEXT NOT NULL,
  "StartTime" DATETIME NOT NULL,
  "EndTime" DATETIME NOT NULL,
  "StartOdometer" INTEGER NOT NULL,
  "EndOdometer" INTEGER NOT NULL,
  "OfficialID" INTEGER NOT NULL,
  "DriverID" INTEGER NOT NULL,
  "VehicleID" INTEGER NOT NULL,
  "PickupLocationID" INTEGER NOT NULL,
  "DropOffLocationID" INTEGER NOT NULL,
  PRIMARY KEY("Reference"),
  CONSTRAINT "Vehicle_Booking"
    FOREIGN KEY ("VehicleID") REFERENCES "Vehicle" ("VehicleID"),
  CONSTRAINT "Driver_Booking"
    FOREIGN KEY ("DriverID") REFERENCES "Driver" ("DriverID"),
  CONSTRAINT "Official_Booking"
    FOREIGN KEY ("OfficialID") REFERENCES "Official" ("OfficialID"),
  CONSTRAINT "Location_Booking"
    FOREIGN KEY ("PickupLocationID") REFERENCES "Location" ("LocationID"),
  CONSTRAINT "Location_Booking"
    FOREIGN KEY ("DropOffLocationID") REFERENCES "Location" ("LocationID"));'''
)

print("Table Booking succesfully created")

conn.execute('''CREATE TABLE IF NOT EXISTS "VehicleAction"(
  "ActionID" INTEGER NOT NULL,
  "VehicleID" INTEGER NOT NULL,
  "Type" CHARACTER NOT NULL,
  "Odometer" INT NOT NULL,
  "FinalCost" INT NOT NULL,
  "Description" TEXT NOT NULL,
  "Date" DATE NOT NULL,
  PRIMARY KEY("ActionID"),
  CONSTRAINT "Vehicle_VehicleAction"
    FOREIGN KEY ("VehicleID") REFERENCES "Vehicle" ("VehicleID"));'''
)

print("Table VehicleAction succesfully created")
