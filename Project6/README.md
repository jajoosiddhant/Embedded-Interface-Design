# EID-Project-6 - MAGIC WAND
  
This project was completed under the course Embedded Interface Design at University of Colorado, Boulder under the guidance of Professor Bruce Montgomery in September 2019.
  
## Authors: Siddhant Jajoo, Satya Mehta, Vatsal Sheth  

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
  
  

***AWS Python SDK Intsallation***
- sudo pip install AWSIoTPythonSDK

***AWS Account is required for this project and should have services like IoT Core, SQS, SNS enabled and authorized.***

## Project Work


### Project Issues Faced

  
->Satya Mehta -   
->Siddhant Jajoo - 
->Vatsal Sheth - 



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
