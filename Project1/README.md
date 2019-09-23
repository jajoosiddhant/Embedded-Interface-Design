# EID-Project-1
  
This project was completed under the course Embedded Interface Design at University of Colorado, Boulder under the guidance of Professor Bruce Montgomery in September 2019.
  
## Authors: Siddhant Jajoo and Satya Mehta  

## Installation Instructions 
 Run below commands to install all the libraries and dependancies to required for this project. 
    
***Python Installation***
- sudo apt-get update
- sudo apt-get upgrade
- sudo apt-get install python3-dev python3-pip
  
***Adafruit DHT22 Sensor Installation***
- sudo python3 -m pip install --upgrade pip setuptools wheel
- sudo pip3 install Adafruit_DHT
  
***MySQL Installation***
- pip install MySQL-python
- sudo apt-get install mysql-client
- sudo apt-get install mariadb-server
- sudo apt-get install mariadb-client

***PyQT Installation***
- sudo apt-get install qt5-default pyqt5-dev-pyqt5-dev-tools
- sudo apt-get install qttools-dev-tools

The folder consists of two .py files: app.py and test.py. test.py is the gui module which has been imported into app.py.  
In order to run the application type this command: `python3 app.py` from the source directory.

## Project Work

The GUI consists of pushbuttons with the following functionalities:
- Status Box: All the display messages are displayed in the status box according to the button pressed in the GUI.
- Refresh: This button would fetch immediate temperature and humidity values from the DHT22 sensor and display it in the Status box of the GUI without updating the database.
- Radio Button: On selecting the appropriate radio button, the temperature units in the entire GUI are changed from Celsius to Fahrenheit and vice versa.
- Temperature Graph: This button would fetch 10 latest temperature values from the database and plot a graph of temperature values in Celsius or Fahrenheit (depending on the status of radio buttons) vs Time.
- Humidity Graph: This button would fetch 10 latest humidity values from the database and plot a graph of humidity values (percentage) (depending on the status of radio buttons) vs Time.
- Double Spin Box for Temperature and Humidity: These spin boxes are used as an input box for threshold values of Temperature and Humidity to display an alarm message if the temperature and humidity values cross their thresholds respectively. The threshold values are modified automatically if the radio button status is changed from Celsius to Fahrenheit and vice versa. The threshold calculation is done instantaneously as the values are changed and the alarm message is displayed in the Status Box.
- Timer: A timer has been implemented which would fetch tempertaure and humidity values from the DHT22 sensor, check threshold values for alarm display and update the values in the database every 15 seconds.

-> Siddhant Jajoo - Pyqt5 work and Integration  
-> Satya Mehta - Mysql, Matplotlib and Integration. 

## Project Additions
- Conversion from Celsius to Fahrenheit and vice versa by clicking on the respective radio button.
- Displaying Alarm text message as soon as the threshold is changed in addition to checking every 15 seconds and also at pressing      refresh button on the GUI.  


## References
- https://github.com/adafruit/DHT-sensor-library - Adafruit library for DHT22 sensor.
- https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/ - Adafruit Sensor Installation
