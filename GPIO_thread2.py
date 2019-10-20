import time
from time import sleep
import datetime
import os
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
import RPi.GPIO as GPIO

Relay2_40 = 21
Relay2_60 = 13
Relay2_500 = 19
Relay2_1k = 26
                
# --------------------------------------------------------------------------------------------------------------
# ----------------------------------- VIdeo Stream Thread Class ------------------------------------------------
# --------------------------------------------------------------------------------------------------------------   
class GPIO_Ch2_Thread(QThread):
	doneFlag2 = pyqtSignal(str) 
    
	def __init__(self, GPIO):
		QThread.__init__(self)
		self.exitProgram = False
		self.set40 = False
		self.set60 = False
		self.set500 = False
		self.set1k = False
		self.GPIO = GPIO
        
    #Sets up the program to exit when the main window is shutting down
	def Set_Exit_Program(self, exiter):
		self.exitProgram = exiter
		
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
			if self.set40 == True:
				if self.GPIO.input(Relay2_40) == 0:
					self.GPIO.output(Relay2_40, GPIO.HIGH)
					self.doneFlag2.emit("40H")

				else: 
					self.GPIO.output(Relay2_40, GPIO.LOW)
					self.doneFlag2.emit("40L")

				print(GPIO.input(Relay2_40))
				
				self.set40 = False
			
			if self.set60 == True:
				if self.GPIO.input(Relay2_60) == 0:
					self.GPIO.output(Relay2_60, GPIO.HIGH)
					self.doneFlag2.emit("60H")

				else: 
					self.GPIO.output(Relay2_60, GPIO.LOW)
					self.doneFlag2.emit("60L")

				print(GPIO.input(Relay2_60))
				self.set60 = False
			
			if self.set500 == True:
				if self.GPIO.input(Relay2_500) == 0:
					self.GPIO.output(Relay2_500, GPIO.HIGH)
					self.doneFlag2.emit("500H")

				else: 
					self.GPIO.output(Relay2_500, GPIO.LOW)
					self.doneFlag2.emit("500L")
				print(GPIO.input(Relay2_500))

				self.set500 = False
			
			if self.set1k == True:
				if self.GPIO.input(Relay2_1k) == 0:
					self.GPIO.output(Relay2_1k, GPIO.HIGH)
					self.doneFlag2.emit("1kH")

				else: 
					self.GPIO.output(Relay2_1k, GPIO.LOW)
					self.doneFlag2.emit("1kL")				
				print(GPIO.input(Relay2_1k))
				self.set1k = False
			
			if(self.exitProgram == True):
				self.exitProgram = False
				break
            
			time.sleep(0.01)

