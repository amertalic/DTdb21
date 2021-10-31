# DTdb21

It's a custom data cleaning tool for a large amount of data stored in multiple Excel files.

This data needs to be extracted, cleaned, verified and stored in a postgreSQL table. 

## Data and data type

Most of the data are simple strings. These strings need to be extracted and reformatted correctly and then stored.
Sometimes one field wil be broken down into more fields. For example name_surname filed needs to be broken into name and surname filed.

### Microchip
A microchip implant is an identifying integrated circuit placed under the skin of an animal. The chip, about the size of a large grain of rice, uses passive radio-frequency identification (RFID) technology, and is also known as a PIT (passive integrated transponder) tag. Standard pet microchips are typically 11–13 mm long (approximately 1⁄2 inch) and 2 mm in diameter.

Beside simple data there is unique data that is not correctly entered into the Excel table when it was created. 
For example a microchip number is a 15 digit long string that was entered as a digit and lost its "0" at the beginning, 
or a letter (or some other character) were added so the cell was recognized as a text cell and the beginning "0" will not be lost.
