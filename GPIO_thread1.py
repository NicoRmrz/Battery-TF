import time
from time import sleep
import datetime
import os
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
import RPi.GPIO as GPIO

Relay1_40 = 7
Relay1_60 = 12
Relay1_500 = 16
Relay1_1k = 20
# --------------------------------------------------------------------------------------------------------------
# ----------------------------------- GPIO Channel 1 Thread Class ------------------------------------------------
# --------------------------------------------------------------------------------------------------------------   
class GPIO_Ch1_Thread(QThread):
	doneFlag1 = pyqtSignal(str) 
    
	def __init__(self, GPIO):
		QThread.__init__(self)
		self.exitProgram = False
		self.set40 = False
		self.set60 = False
		self.set500 = False
		self.set1k = False
		self.GPIO = GPIO
		self.setLow = False
	
    #Sets up the program to exit when the main window is shutting down
	def Set_Exit_Program(self, exiter):
		self.exitProgram = exiter
		
	#Sets all GPIO pins Low
	def	setAllLow(self, state):
		self.setLow = state
		
	# Set 40 ohm load
	def Set_40Ohm(self, state):
		self.set40 = state
		
	# Set 60 ohm load
	def Set_60Ohm(self, state):
		self.set60 = state
		
	# Set 500 ohm load
	def Set_500Ohm(self, state):
		self.set500 = state
		
	# Set 1k ohm load
	def Set_1kOhm(self, state):
		self.set1k = state
        
	def run(self):
		self.setPriority(QThread.HighestPriority)

		while (1):
			if self.setLow == True:
				self.GPIO.output(Relay1_40, GPIO.LOW)
				self.GPIO.output(Relay1_60, GPIO.LOW)
				self.GPIO.output(Relay1_500, GPIO.LOW)
				self.GPIO.output(Relay1_1k, GPIO.LOW)
				self.setLow = False
				
			if self.set40 == True:
				if self.GPIO.input(Relay1_40) == 0:
					self.GPIO.output(Relay1_40, GPIO.HIGH)
					self.GPIO.output(Relay1_60, GPIO.LOW)
					self.GPIO.output(Relay1_500, GPIO.LOW)
					self.GPIO.output(Relay1_1k, GPIO.LOW)
					self.doneFlag1.emit("40H")
					self.doneFlag1.emit("60L")
					self.doneFlag1.emit("500L")
					self.doneFlag1.emit("1kL")					

				else: 
					self.GPIO.output(Relay1_40, GPIO.LOW)
					self.doneFlag1.emit("40L")

				print(GPIO.input(Relay1_40))
				
				self.set40 = False
			
			if self.set60 == True:
				if self.GPIO.input(Relay1_60) == 0:
					self.GPIO.output(Relay1_60, GPIO.HIGH)
					self.GPIO.output(Relay1_40, GPIO.LOW)
					self.GPIO.output(Relay1_500, GPIO.LOW)
					self.GPIO.output(Relay1_1k, GPIO.LOW)
					self.doneFlag1.emit("60H")
					self.doneFlag1.emit("40L")
					self.doneFlag1.emit("500L")
					self.doneFlag1.emit("1kL")

				else: 
					self.GPIO.output(Relay1_60, GPIO.LOW)
					self.doneFlag1.emit("60L")

				print(GPIO.input(Relay1_60))
				self.set60 = False
			
			if self.set500 == True:
				if self.GPIO.input(Relay1_500) == 0:
					self.GPIO.output(Relay1_500, GPIO.HIGH)
					self.GPIO.output(Relay1_40, GPIO.LOW)
					self.GPIO.output(Relay1_60, GPIO.LOW)
					self.GPIO.output(Relay1_1k, GPIO.LOW)
					self.doneFlag1.emit("500H")
					self.doneFlag1.emit("40L")
					self.doneFlag1.emit("60L")
					self.doneFlag1.emit("1kL")

				else: 
					self.GPIO.output(Relay1_500, GPIO.LOW)
					self.doneFlag1.emit("500L")
				print(GPIO.input(Relay1_500))

				self.set500 = False
			
			if self.set1k == True:
				if self.GPIO.input(Relay1_1k) == 0:
					self.GPIO.output(Relay1_1k, GPIO.HIGH)
					self.GPIO.output(Relay1_40, GPIO.LOW)
					self.GPIO.output(Relay1_60, GPIO.LOW)
					self.GPIO.output(Relay1_500, GPIO.LOW)
					self.doneFlag1.emit("1kH")
					self.doneFlag1.emit("40L")
					self.doneFlag1.emit("60L")
					self.doneFlag1.emit("500L")

				else: 
					self.GPIO.output(Relay1_1k, GPIO.LOW)
					self.doneFlag1.emit("1kL")				
				print(GPIO.input(Relay1_1k))
				self.set1k = False
			
			if(self.exitProgram == True):
				self.exitProgram = False
				break
            
			time.sleep(0.2)

