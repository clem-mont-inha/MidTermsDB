# Entity-Relationship Diagram for ITS Database

This document offers a comprehensive exploration of the Entity-Relationship Diagram (ERD) pertaining to the "ITS" (Intelligent Transportation System) database, constructed according to a SQLite database schema. Within this database, one will find numerous tables that delineate different facets of the transportation system, encompassing categories such as vehicles, drivers, authorities, languages, countries, reservations, locations, and vehicle activities.

## Database Schema

## Vehicle
- **VehicleID (Primary Key)**: Unique identifier for each vehicle.
- RegistrationID: The registration ID of the vehicle.
- Manufacturer: The manufacturer of the vehicle.
- Model: The model of the vehicle.
- Color: The color of the vehicle.
- CurrentOdometer: The current odometer reading of the vehicle.
- PassengerCapacity: The maximum passenger capacity of the vehicle.
- Available: If the vehicle is available for booking.

## Language
- **LanguageCode (Primary Key)**: A two-character code representing the language.
- LanguageName: Language name.

## Country
- **CountryCode (Primary Key)**: A two-character code representing the country.
- CountryName: Country Name.
- MostFrequentlySpokenLanguage: A foreign key referencing the Language table, indicating the most frequently spoken language in the country.

## Official
- **OfficialID (Primary Key)**: Unique identifier for each official.
- CityID: A character code representing the city where the official is assigned.
- Name: Official name.
- Role: The role or position of the official.
- PreferredLanguage: A foreign key referencing the Language table, indicating the official's preferred language.
- CountryCode: A foreign key referencing the Country table, indicating the country where the official is assigned.

## Driver
- **DriverID (Primary Key)**: Unique identifier for each driver.
- LicenseNumber: The license number of the driver.
- Name: Driver name.
- ClearanceLevel: The clearance level of the driver.
- FATLLevel: The level of the First Aid and Traffic Law Training.
- FATLQualificationDate: The date of qualification for FATL.
- STLVTLevel: The level of Safe Transport of Live Veterinary Tissue (STLVT) training.
- STLVTQualificationDate: The date of qualification for STLVT.
- STLVTCertifyingAuthority: The authority certifying the STLVT qualification.
- PreferredLanguage: A foreign key referencing the Language table, indicating the driver's preferred language.

## Location
- **LocationID (Primary Key)**: Unique identifier for each location.
- Name: The name of the location.
- Address: The address of the location.
- Type: The type of location.

## Booking
- **Reference (Primary Key)**: A unique reference for each booking.
- StartTime: The start time of the booking.
- EndTime: The end time of the booking.
- StartOdometer: The vehicle's odometer reading at the start of the booking.
- EndOdometer: The vehicle's odometer reading at the end of the booking.
- OfficialID: A foreign key referencing the Official table, indicating the official responsible for the booking.
- DriverID: A foreign key referencing the Driver table, indicating the driver assigned to the booking.
- VehicleID: A foreign key referencing the Vehicle table, indicating the vehicle used for the booking.
- PickupLocationID: A foreign key referencing the Location table, indicating the pickup location.
- DropOffLocationID: A foreign key referencing the Location table, indicating the drop-off location.

## VehicleAction
- **ActionID (Primary Key)**: Unique identifier for each vehicle action.
- VehicleID: A foreign key referencing the Vehicle table, indicating the vehicle associated with the action.
- Type: The type of vehicle action.
- Odometer: The vehicle's odometer reading at the time of the action.
- FinalCost: The final cost associated with the action.
- Description: A description of the action.
- Date: The date on which the action took place.

## Relationships

![alt text](https://github.com/clem-mont-inha/MidTermsDB/blob/main/image.png?raw=true)
## GitHub

- [@github](https://github.com/clem-mont-inha/MidTermsDB)

