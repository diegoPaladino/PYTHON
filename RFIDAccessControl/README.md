# RFIDAccessControl

## Introduction
RFIDAccessControl is a Python-based project designed to manage access control for residential doors using RFID technology. The system reads RFID tags and grants or denies access based on pre-approved RFID IDs.

## List of Necessary Materials
- Raspberry Pi
- RFID-RC522 Module
- Relay Module
- Jumper wires
- Breadboard
- Python 3.x
- `RPi.GPIO` and `mfrc522` Python libraries

## Project Purpose
The purpose of this project is to provide a secure and efficient way to control access to a residential door using RFID technology. This project is ideal for homeowners looking to enhance the security of their property by implementing a personalized access control system.

## Pros and Cons

### Pros
- Enhances home security
- Easy to use and manage
- Customizable to accept multiple RFID tags
- Low-cost implementation

### Cons
- Requires basic knowledge of electronics and programming
- Limited to the range of the RFID reader

## General Guidelines

### Installation
1. Set up your Raspberry Pi with the necessary OS and Python installed.
2. Connect the RFID-RC522 module to the Raspberry Pi using jumper wires.
3. Connect the relay module to control the door lock mechanism.
4. Install the required Python libraries:
    ```sh
    pip install RPi.GPIO
    pip install mfrc522
    ```

### Usage
1. Modify the `valid_rfid_ids` list in the code to include your valid RFID tags.
2. Run the `RFIDAccessControl` script:
    ```sh
    python RFIDAccessControl.py
    ```
3. Hold an RFID tag near the reader to test access control.

### Troubleshooting
- Ensure all connections are secure and correctly configured.
- Verify that the RFID module and relay are functioning properly.
- Check for any errors in the script and refer to the error messages for debugging.

## License
This project is open-source and free to use under the MIT License.
