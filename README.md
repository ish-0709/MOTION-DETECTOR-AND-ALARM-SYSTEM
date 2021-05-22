# MOTION-DETECTOR-AND-ALARM-SYSTEM

A motion sensor project that detects motion and sounds an alarm accordingly. This software system is designed in Python that constantly monitors an environment using a camera and sounds an alarm and even records images of the motion taking place as soon as it takes place.

# Description
•The user first needs to manually set a security code.
•The motion detector algorithm now constantly monitors the environment to check for any movement.
•When the camera detects an object, it triggers the alarm which says “Object detected” and also a green frame is formed around the new entry.
•When the camera detects a human, it triggers the alarm which says “Human Detected. What is the password?” and also a blue frame is formed around the new entry.
•Now using speech to text the password spoken by the human is detected, if it matches the security code the door lock opens and if an intruder is detected then the information is sent to the user via mail.

# Requirements
## Functional Requirements
1) Acquiring object images
2) Acquiring face images 
3) Processing face images 
4) Face detection 
5) Automation
6) Sending mails
7) Speech to text recognition
8) Text to speech recognition

## Non-Functional Requirements
1) Security – Unauthorized person should not be able to change the password, that responsibility is in the user’s hand.
2) Maintenance – Cameras used, Microphone used and usual regular updates
3) Portability - To ensure portability, the system will be developed in PYTHON language.

## Hardware Requirements

1) Processor – i3 (or any greater version)
2) Hard Disk – 5 GB
3) Memory – 1GB RAM
4) Internet – For sending mail to the user
5) Webcam
6) Microphone


## Software Requirements

1) Operating System: Windows 10 / Linux 
2) PyCharm
3) Coding Language: Python
4) Library: 
5) OpenCV 
6) Pandas
7) Pyttsx3 
8) Datetime
9) Speech recognition
10) smtplib
