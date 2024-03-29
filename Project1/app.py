from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import Adafruit_DHT
import MySQLdb
import datetime
import time
import matplotlib.pyplot as plt
import threading
import multitimer
from test import Ui_MainWindow
import sys
import numpy as np


__author__ = "Satya Mehta, Siddhant Jajoo"
__copyright__ = "Copyright (C) 2019 by Satya Mehta and Siddhant Jajoo"

class gui_functionality(Ui_MainWindow):
    
    """
        gui_functionality: This class consist of all the print functions that would be
        required to display data on the GUI and to obtain temperature reading from the DHT22 sensor.
        
    """
    def print_refresh(self):
        """
        print_refresh: Reads data from the sensor and prints on the text box on the gui
        upon every button press of Refresh on the GUI.
        """
        self.plainTextEdit.appendPlainText("Obtaining Current Temperature and Humidity Values:")
        temperature, humidity = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if temperature is None and humidity is None:
            self.plainTextEdit.appendPlainText("ERROR: SENSOR IS OFFLINE\n")
            return
        current_time = datetime.datetime.now()
        self.plainTextEdit.appendPlainText("Timestamp = %s" %current_time)
        if self.fahrenheit_flag:
            temperature = (temperature * 9/5) + 32
            self.plainTextEdit.appendPlainText("Temperature = %0.2f degree Fahrenheit" %temperature)
            self.threshold_calc(temperature, humidity)
        else:
            self.plainTextEdit.appendPlainText("Temperature = %0.2f degree Celsius" %temperature)
            self.threshold_calc(temperature, humidity)
        self.plainTextEdit.appendPlainText("Humidity = %0.2f percent\n" %humidity)
        
        
    def print_interval(self, current_time, temperature, humidity):
        """
        print_interval: Used by the other functions to print the sensor data on to the GUI status window.
        """
        self.plainTextEdit.appendPlainText("Timestamp = %s" %current_time)
        if self.fahrenheit_flag:
            temperature = (temperature * 9/5) + 32
            self.plainTextEdit.appendPlainText("Temperature = %0.2f degree Fahrenheit" %temperature)
            self.threshold_calc(temperature, humidity)
        else:
            self.plainTextEdit.appendPlainText("Temperature = %0.2f degree Celsius" %temperature)
            self.threshold_calc(temperature, humidity)
        self.plainTextEdit.appendPlainText("Humidity = %0.2f percent\n" %humidity)
    
        
    def celsius_to_fahrenheit(self):
        """
        celsius_to_fahrenheit: This function is called when the Fahrenheit mode is selected on the GUI
        It sets the fahrenheit flag to 1. 
        """
        self.plainTextEdit.appendPlainText("Changing Temperature Units from Celsius to Fahrenheit!")
        self.fahrenheit_flag = 1
        self.spinbox_value = (self.doubleSpinBox_temp.value() * 9/5) + 32
        self.doubleSpinBox_temp.setValue(self.spinbox_value)
        
    def fahrenheit_to_celsius(self):
        """
        fahrenheit_to_celsius: This function is called when the Celsius mode is selected on the GUI
        It clears the fahrenheit flag to 0.
        """
        self.plainTextEdit.appendPlainText("Changing Temperature Units from Fahrenheit to Celsius!")
        self.fahrenheit_flag = 0
        self.spinbox_value = (self.doubleSpinBox_temp.value() - 32)*(5/9)
        self.doubleSpinBox_temp.setValue(self.spinbox_value)
        
    def print_temp_graph(self):
        
        """
        print_temp_graph: This function is called when the Print Temp Graph button on the GUI is pressed.
        It fetches 10 latest temperatue value from the database table and plots them on the graph.
        """
        self.plainTextEdit.appendPlainText("Refreshing Temperature Graph")
        cur.execute("SELECT temperature FROM environment ORDER BY ID DESC LIMIT 10")
        temp = cur.fetchall()
        temp_array = np.asarray(temp)
        timestamp_array = [1,2,3,4,5,6,7,8,9,10]
        #temp_array = [temp[9], temp[8], temp[7], temp[6], temp[5], temp[4], temp[3], temp[2], temp[1], temp[0]]
        if self.fahrenheit_flag:
            new_temp_array = list()
            for i in temp_array:
                new_temp_array.append((i * 9/5) + 32)
            plt.ylabel('Temperature(Fahreneit)')
            plt.plot(timestamp_array, new_temp_array)
        else:
            plt.plot(timestamp_array, temp_array)
            plt.ylabel('Temperature(C)')
        plt.xlabel('Time')
        plt.show()

    def print_hum_graph(self):
        """
        print_hum_graph: This function is called when the Print Humidity Graph button on the GUI is pressed.
        It fetches 10 latest humidity value from the database table and plots them on the graph.
        """
        self.plainTextEdit.appendPlainText("Refreshing Humidity Graph")
        cur.execute("SELECT humidity FROM environment ORDER BY ID DESC LIMIT 10")
        hum = cur.fetchall()
        hum_array = [hum[9], hum[8], hum[7], hum[6], hum[5], hum[4], hum[3], hum[2], hum[1], hum[0]]
        timestamp_array = [1,2,3,4,5,6,7,8,9,10]
        plt.plot(timestamp_array, hum_array)
        plt.ylabel('Humidity(%)')
        plt.xlabel('Time')
        plt.show()
        
    def threshold_calc(self, temperature, humidity):
        """
        threshold_calc: Checks the temperature, humidity if it crosses the threshold and prints on the GUI
        status box if the condition is true.
        """
        temparray = np.asarray(temperature)
        humarray = np.asarray(humidity)
        if temparray > self.doubleSpinBox_temp.value():
            self.plainTextEdit.appendPlainText("WARNING: Temperature exceeds Threshold ")
        
        if humarray > self.doubleSpinBox_hum.value():
            self.plainTextEdit.appendPlainText("WARNING: Humidity exceeds Threshold\n")
    
    def get_sensor_data(self):
        """
        get_sensor_data: This function is called at every 15 seconds of timer timeout.
        It gets the data from the sensor and inserts it into database.
        """
        global reads
        self.plainTextEdit.appendPlainText("\nObtaining Current Temperature and Humidity Values:")
        temperature, humidity = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        current_time = datetime.datetime.now()        
        if humidity is not None and temperature is not None:
            self.print_interval(current_time, temperature, humidity)
            sql = """INSERT INTO environment
                      (temperature,humidity,timestamp)
                      VALUES('%f', '%f', '%s')"""% (temperature, humidity, current_time)
            try:
                cur.execute(sql)
                db.commit()
            except:
                db.rollback()
        else:
            self.plainTextEdit.appendPlainText("ERROR: SENSOR IS OFFLINE\n")
        reads = reads + 1    
        if reads == 30:
            sys.exit()
            
        return temperature, humidity

    def check_database(self):
        """
        check_database: This function is called after every change in the threshold data.
        It gets the latest value from the database and calls the threshold_calc function.
        """
        
        sql = "SELECT temperature FROM environment ORDER BY ID DESC LIMIT 1"
        try:
            cur.execute(sql)
            latest_temp = cur.fetchall()
            self.latest_temp_list = np.asarray(latest_temp[0])
        except:
            db.rollback()

        sql = "SELECT humidity FROM environment ORDER BY ID DESC LIMIT 1"
        try:
            cur.execute(sql)
            latest_humidity = cur.fetchall()
        except:
            db.rollback()
        if self.fahrenheit_flag:
            self.latest_temp_list[0] = (self.latest_temp_list[0] * 9/5) + 32
            
        self.threshold_calc(self.latest_temp_list[0], latest_humidity[0])


    def __init__(self, MainWindow):
        super().__init__()
        """
        Initialization for the PyQT objects
        """
        self.setupUi(MainWindow)
        self.doubleSpinBox_temp.setValue(30)
        self.doubleSpinBox_hum.setValue(50)
        self.radioButton_celsius.setChecked(True)
        self.fahrenheit_flag = 0
        self.pushButton_refresh.clicked.connect(self.print_refresh)
        self.pushButton_temp_graph.clicked.connect(self.print_temp_graph)
        self.pushButton_hum_graph.clicked.connect(self.print_hum_graph)
        self.doubleSpinBox_temp.valueChanged.connect(self.check_database)
        self.doubleSpinBox_hum.valueChanged.connect(self.check_database)
        self.radioButton_celsius.pressed.connect(self.fahrenheit_to_celsius)
        self.radioButton_fahrenheit.pressed.connect(self.celsius_to_fahrenheit)

if __name__ == "__main__":

    """Sensor Initialization"""
    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN = 4
    reads = 0
    
    """Database initialization"""
    db = MySQLdb.connect(host= "localhost", user= "pi", passwd="letmein", db= "exampledb")
    cur = db.cursor()
    sql_command = """CREATE TABLE IF NOT EXISTS environment(
                id INT NOT NULL AUTO_INCREMENT,
                temperature  FLOAT,
                humidity FLOAT,
                timestamp CHAR(30),
                PRIMARY KEY(id))"""
    try:
        cur.execute(sql_command)
        db.commit()
        print ("Database Initialized")
    except:
        db.rollback()

    """PyQt5 initialization"""
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    mygui = gui_functionality(MainWindow)
    MainWindow.show()
    
    
    """Timer Iniitalization for 15 seconds"""
    timer = QTimer()
    timer.timeout.connect(mygui.get_sensor_data)
    timer.start(15000)
    
    
    sys.exit(app.exec_())



