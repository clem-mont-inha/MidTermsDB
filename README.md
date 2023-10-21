# Entity-Relationship Diagram (ERD) for ITS Database

This report provides an overview of the Entity-Relationship Diagram (ERD) for the "ITS" (Intelligent Transportation System) database, which has been created using a SQLite database schema. The database contains multiple tables that represent various aspects of the transportation system, including vehicles, drivers, officials, languages, countries, bookings, locations, and vehicle actions.

## Database Schema

The ERD for the "ITS" database consists of the following tables:

### Vehicle
- **VehicleID (PK)**: Unique identifier for each vehicle.
- RegistrationID: The registration ID of the vehicle.
- Manufacturer: The manufacturer of the vehicle.
- Model: The model of the vehicle.
- Color: The color of the vehicle.
- CurrentOdometer: The current odometer reading of the vehicle.
- PassengerCapacity: The maximum passenger capacity of the vehicle.
- Available: A boolean indicating whether the vehicle is available for booking.

### Language
- **LanguageCode (PK)**: A two-character code representing the language.
- LanguageName: The name of the language.

### Country
- **CountryCode (PK)**: A two-character code representing the country.
- CountryName: The name of the country.
- MostFrequentlySpokenLanguage: A foreign key referencing the Language table, indicating the most frequently spoken language in the country.

### Official
- **OfficialID (PK)**: Unique identifier for each official.
- CityID: A character code representing the city where the official is assigned.
- Name: The name of the official.
- Role: The role or position of the official.
- PreferredLanguage: A foreign key referencing the Language table, indicating the official's preferred language.
- CountryCode: A foreign key referencing the Country table, indicating the country where the official is assigned.

### Driver
- **DriverID (PK)**: Unique identifier for each driver.
- LicenseNumber: The license number of the driver.
- Name: The name of the driver.
- ClearanceLevel: The clearance level of the driver.
- FATLLevel: The level of the First Aid and Traffic Law Training.
- FATLQualificationDate: The date of qualification for FATL.
- STLVTLevel: The level of Safe Transport of Live Veterinary Tissue (STLVT) training.
- STLVTQualificationDate: The date of qualification for STLVT.
- STLVTCertifyingAuthority: The authority certifying the STLVT qualification.
- PreferredLanguage: A foreign key referencing the Language table, indicating the driver's preferred language.

### Location
- **LocationID (PK)**: Unique identifier for each location.
- Name: The name of the location.
- Address: The address of the location.
- Type: The type of location.

### Booking
- **Reference (PK)**: A unique reference for each booking.
- StartTime: The start time of the booking.
- EndTime: The end time of the booking.
- StartOdometer: The vehicle's odometer reading at the start of the booking.
- EndOdometer: The vehicle's odometer reading at the end of the booking.
- OfficialID: A foreign key referencing the Official table, indicating the official responsible for the booking.
- DriverID: A foreign key referencing the Driver table, indicating the driver assigned to the booking.
- VehicleID: A foreign key referencing the Vehicle table, indicating the vehicle used for the booking.
- PickupLocationID: A foreign key referencing the Location table, indicating the pickup location.
- DropOffLocationID: A foreign key referencing the Location table, indicating the drop-off location.

### VehicleAction
- **ActionID (PK)**: Unique identifier for each vehicle action.
- VehicleID: A foreign key referencing the Vehicle table, indicating the vehicle associated with the action.
- Type: The type of vehicle action.
- Odometer: The vehicle's odometer reading at the time of the action.
- FinalCost: The final cost associated with the action.
- Description: A description of the action.
- Date: The date on which the action took place.

## Relationships

The ERD includes the following relationships between tables:

- A foreign key relationship between the `Country` table and the `Language` table, where `Country.MostFrequentlySpokenLanguage` references `Language.LanguageCode`.

- Two foreign key relationships for the `Official` table: one with the `Language` table (`Official.PreferredLanguage` references `Language.LanguageCode`) and one with the `Country` table (`Official.CountryCode` references `Country.CountryCode`).

- A foreign key relationship for the `Driver` table with the `Language` table (`Driver.PreferredLanguage` references `Language.LanguageCode`).

- Multiple foreign key relationships for the `Booking` table: one with the `Vehicle` table (`Booking.VehicleID` references `Vehicle.VehicleID`), one with the `Driver` table (`Booking.DriverID` references `Driver.DriverID`), one with the `Official` table (`Booking.OfficialID` references `Official.OfficialID`), and two with the `Location` table (`Booking.PickupLocationID` and `Booking.DropOffLocationID` both reference `Location.LocationID`).

- A foreign key relationship for the `VehicleAction` table with the `Vehicle` table (`VehicleAction.VehicleID` references `Vehicle.VehicleID`).

This ERD outlines the structure and relationships of the tables in the "ITS" database, providing a comprehensive view of the data model for the intelligent transportation system.