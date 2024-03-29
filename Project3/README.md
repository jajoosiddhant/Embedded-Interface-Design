# EID-Project-3
  
This project was completed under the course Embedded Interface Design at University of Colorado, Boulder under the guidance of Professor Bruce Montgomery in September 2019.
  
## Authors: Siddhant Jajoo, Satya Mehta  

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

***Tornado Installation***
- sudo pip install tornado

***NodeJS Installation***
- curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
- restart your terminal
- nvm -version should return 0.34.0
- nvm install node
- nvm install 10.16.3

***NodeJS Mysql Installation***
- npm install mysql
- npm install websocket (in the working directory)
- nm init -y (in the working directory)
This project is built on the project-1. The Tornado webscket code is added into the main application code but it is executed onto the different thread. Hence, it runs independently. 

***AWS Python SDK Intsallation***
- sudo pip install AWSIoTPythonSDK

***AWS Account is required for this project and should have services like IoT Core, SQS, SNS enabled and authorized.***
## Project Work

## Project-1
The GUI consists of pushbuttons with the following functionalities:
- Status Box: All the display messages are displayed in the status box according to the button pressed in the GUI.
- Refresh: This button would fetch immediate temperature and humidity values from the DHT22 sensor and display it in the Status box of the GUI without updating the database.
- Radio Button: On selecting the appropriate radio button, the temperature units in the entire GUI are changed from Celsius to Fahrenheit and vice versa.
- Temperature Graph: This button would fetch 10 latest temperature values from the database and plot a graph of temperature values in Celsius or Fahrenheit (depending on the status of radio buttons) vs Time.
- Humidity Graph: This button would fetch 10 latest humidity values from the database and plot a graph of humidity values (percentage) (depending on the status of radio buttons) vs Time.
- Double Spin Box for Temperature and Humidity: These spin boxes are used as an input box for threshold values of Temperature and Humidity to display an alarm message if the temperature and humidity values cross their thresholds respectively. The threshold values are modified automatically if the radio button status is changed from Celsius to Fahrenheit and vice versa. The threshold calculation is done instantaneously as the values are changed and the alarm message is displayed in the Status Box.
- Timer: A timer has been implemented which would fetch tempertaure and humidity values from the DHT22 sensor, check threshold values for alarm display and update the values in the database every 15 seconds.

## Project1 Additions
- Conversion from Celsius to Fahrenheit and vice versa by clicking on the respective radio button.
- Displaying Alarm text message as soon as the threshold is changed in addition to checking every 15 seconds and also at pressing      refresh button on the GUI.  

-> Siddhant Jajoo - Pyqt5 work and Integration  
-> Satya Mehta - Mysql, Matplotlib and Integration. 

## Project2 Additions
Project 2 Additons - 1) HTML CLient website 2) NodeJs Server 3) Tornado Server.
- Find the AWS development account in the folder.
- The HTML page establishes WebSocket communications woth both the Tornado Webserver and NodeJS Webserver.
- CSS has been used to refine the HTML webpage.
- NodeJs and Tornado act as the Webserver to store timestamp, temperature and humidity data.

1) HTML CLient Website
- Refresh Button: This pushbutton fetches the latest temperature and Humidity values along with the timestamp fom the tornado web server which has been integrated with the python application and PyQt5 GUI developed during Project 1. If it fails to acquire the current values or the DHT22 does not respond, an error is returned to the HTML page for diplay.
- Fetch Database: This pushbutton fetches the latest temperature and humidity values along with the timestamp that has been stored in the mysql webserver.
- Radio Button: There are two radio buttons -> Celsius and Fahrenheit which converts the temperature unit to the appropriate temperature unit selected in the entire webpage.
- Test Network: This pushbutton fetches the last 10 Temperature and Humidity values along with timestamp from the Tornado webserver and NodeJs server. It also notes the start, stop and execution time to fetch all the data and displays it on the HTML website.
- Temperature Graph: This pushbutton fetches the last 10 temeperature values from the Tornado Webserver and creates a graph. 
- Humidity Graph: This pushbutton fetches the last 10 humidity values from the Tornado Webserver and creates a graph.


-> Siddhant Jajoo - Node JS Web Socket, Integration  
-> Satya Mehta - Tornado Web Socket, Integration
-> Vatsal Sheth - Html webpage, Integration

## Project3 Additions. 
- Data push handler which is initialized as MQTT client and it sends messages to AWS server using AWSIoTPython SDK. 
- The JSON string include keys like Alert, Temperature, Temperature Alert level, Temperature alert trigger, humidity, humidity alert     level, humidity alert trigger.
- The AWS account should be created and should have services enabled. 
- In this project we require IoT Core, SQS, SNS, Lambda services enabled.
- The Lambda function created is linked with IoT core under AWS settings and hence whenever there are new MQTT messages the Lambda     function is invoked.
- The lambda function is used to parse the data from the MQTT message. (JSON string). 
- If the message is an alert type than the SNS is used to send a sms which includes all information to a phone number. 

### HTML CLient Website
- The client website has additional three buttons which are used to fetch data from AWS SQS queue.
- SQS-Single: This pushbutton fetches the latest data from the AWS queue and deletes the data from queue as well and displays it in the form of a table with contents timestamp, temperature (Celsius or Fahrenheit) and humidity values.  
- SQS-All: This pushbutton fetches 20 latest data from the AWS queue and deletes the entire data available in the queue as well and displays the 20 latest values in the form of a table with contents timestamp, temperature (Celsius or Fahrenheit) and humidity values.
- SQS-Count:  This pushbutton retrieves the current Message count in the AWS queue and displays it in a text box in the status window. The count is also updated in the textbox on pressing the SQS-Client and SQS-All push buttons.


### Project Issues Faced
- Implementing the settings required for AWS account.
- Creating the table to fetch latest 20 values and not the old 20 values.  
  
  

->Satya Mehta - AWS IoT Initialization, SNS, Lambda Function, Data push handler.  
->Siddhant Jajoo - AWS Lambda modifcations, HTML Web page, AWs SQS




## References
- https://github.com/adafruit/DHT-sensor-library - Adafruit library for DHT22 sensor.
- https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/ - Adafruit Sensor Installation
- https://www.w3schools.com/nodejs/nodejs_mysql.asp - Node.js talking to MySQL
- https://www.pubnub.com/blog/nodejs-websocket-programming-examples/ - Node.js WebServer example
- https://os.mbed.com/cookbook/Websockets-Server - Python-Tornado-HTML example
- http://www.tornadoweb.org/en/stable/
- https://wiki.python.org/moin/WebServers - Many other choices, many levels of complexity
- https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html - AWS IoT Initialization.
- https://techblog.calvinboey.com/raspberrypi-aws-iot-python/ - Raspberry Pi AWS IoT SDK example
- https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-making-api-requests.html - SQS with HTTP Get, Set Request
- https://docs.aws.amazon.com/lambda/latest/dg/with-sns-example.html - Using Lambda with SNS
