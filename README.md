Smart Gate Pass & QR Code Utility System
This repository hosts a suite of Python-based terminal applications designed for physical access control management and
secure data encoding/decoding using QR codes.
1. Smart Gate Pass System ( gate_pass_system.py )
A file-based utility for managing staff/student entries and exits. It implements custom business logic to control access based
on specific dates and days of the week.
Key Features
Persistent Logging: Records entry and exit events (ID, name, purpose, timestamps) to a local text file
( gate_pass_records.txt ).
Active Tracking: Uses a simple placeholder ( - ) to identify individuals who have entered but not yet logged their exit.
Custom Access Control: Restricts gate pass issuance based on date validation, allowing access only on:
Sundays
The 2nd and 4th Saturdays of the month.
Special purpose days (Option 2 in the initial menu).
Record Management: Includes functions to view all records, search by ID, and delete records entirely.
2. QR Code Utility App ( qr_code_app.py )
A standalone tool for converting data into QR codes and securely decoding them.
Key Features
QR Code Generation: Converts raw text, a URL, or the contents of an entire .txt file into a high-quality PNG image.
QR Code Decoding: Utilizes computer vision ( cv2 ) to scan an image file and extract the hidden text or data, saving
the result to an output text file.
Prerequisites
Both applications require Python 3.x and the following libraries:
Application Library Purpose
qr_code_app.py qrcode Core QR code generation.
qr_code_app.py Pillow (PIL) Image handling for code generation.
qr_code_app.py opencv-python (cv2) Image scanning and decoding.
Both datetime , os Standard system libraries.
Installation
1. Clone the Repository:
git clone [your-repo-link]
cd [your-repo-name]
2. Install Dependencies: You must install the following libraries to use the QR code functionality:
pip install qrcode pillow opencv-python
(Note: Use pip3 if you have multiple Python versions installed.)
Usage
Running the Gate Pass System
The system begins with an access check based on the current date:
python gate_pass_system.py
Running the QR Code Utility
This app provides a menu for generating or decoding operations:
python qr_code_app.py
