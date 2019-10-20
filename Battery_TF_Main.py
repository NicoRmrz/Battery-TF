import datetime
import os
import time
import sys
import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QCheckBox, QTextEdit, QStatusBar, \
    QProgressBar, QSizePolicy, QAbstractItemView, QWidget, QTabWidget, QHBoxLayout, QVBoxLayout, QSlider
from PyQt5.QtGui import QPixmap, QIcon, QFont, QTextCursor, QPalette, QImage, QBrush, QImage
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot, QObject, QSize
import RPi.GPIO as GPIO


# imports from user made files
from GUI_Stylesheets import GUI_Stylesheets
from GUI_Buttons import Send_Command_Button, Logo_Button, Relay_1_40_Ohm, Relay_1_60_Ohm, Relay_1_500_Ohm, Relay_1_1k_Ohm, \
        Relay_2_40_Ohm, Relay_2_60_Ohm, Relay_2_500_Ohm, Relay_2_1k_Ohm
from buttonHandler import handlers
from GPIO_thread1 import GPIO_Ch1_Thread
from GPIO_thread2 import GPIO_Ch2_Thread

# Current version of application - Update for new builds
appVersion = "1.0"  # Update version

# Icon Image locations
Main_path = os.getcwd() + "/"
Icon_Path = Main_path + "/Logo/logo.png"

# Instantiate style sheets for GUI Objects
GUI_Style = GUI_Stylesheets()

#BCM chip pinout
Relay1_40 = 7
Relay1_60 = 12
Relay1_500 = 16
Relay1_1k = 20
Relay2_40 = 21
Relay2_60 = 13
Relay2_500 = 19
Relay2_1k = 26


# --------------------------------------------------------------------------------------------------------------
# --------------------------------- Main Window Class ----------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
class Window(QMainWindow):

    # Initialization of the GUI
    def __init__(self):
        super(Window, self).__init__()
        # ~ self.setGeometry(50, 50, 1100, 750)
        self.setWindowTitle("Battery TF")
        self.setStyleSheet(GUI_Style.mainWindow)
        # ~ self.setMinimumSize(1100, 750)
        self.setWindowIcon(QIcon(Icon_Path))

        # --------------------------------------------------------------
        # -------------------- Initialize  -----------------------------
        # --------------------------------------------------------------
	# GPIO Configuration
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Relay1_40,  GPIO.OUT)
        GPIO.setup(Relay1_60,  GPIO.OUT)
        GPIO.setup(Relay1_500,  GPIO.OUT)
        GPIO.setup(Relay1_1k,  GPIO.OUT)
        GPIO.setup(Relay2_40,  GPIO.OUT)
        GPIO.setup(Relay2_60,  GPIO.OUT)
        GPIO.setup(Relay2_500,  GPIO.OUT)
        GPIO.setup(Relay2_1k,  GPIO.OUT)

        # --------------------------------------------------------------
        # ---------------- Instantiate All Threads  --------------------
        # --------------------------------------------------------------
        self.GPIO_ch1 = GPIO_Ch1_Thread(GPIO)
        self.GPIO_ch2 = GPIO_Ch2_Thread(GPIO)

        # --------------------------------------------------------------
        # ---------------- Start All Threads ---------------------------
        # --------------------------------------------------------------
        self.GPIO_ch1.start()
        self.GPIO_ch2.start()

        # --------------------------------------------------------------
        # ---------------- Create Main Widget --------------------------
        # --------------------------------------------------------------
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # --------------------------------------------------------------
        # ---------------- Create Tabs ---------------------------------
        # --------------------------------------------------------------
        self.tabWidget()

        # --------------------------------------------------------------
        # -------------- Create Bottom Status Bar-----------------------
        # --------------------------------------------------------------
        self.StatusBar()
        self.setStatusBar(self.statusBar)

        # --------------------------------------------------------------
        # ------------- Create Main Window Layouts ---------------------
        # --------------------------------------------------------------
        # Instantiate GUI objects
        self.MainTitle()
        
        self.Console_Log()
        self.MainLogoButton()
        self.inputCommandPrompt()
        self.sendCommandButton()

        # Add title/ logo to the main title layout
        Main_Title_Layout = QHBoxLayout()
        Main_Title_Layout.addWidget(self.Logo_btn, 0, Qt.AlignRight)
        Main_Title_Layout.addWidget(self.MainTitleText, 0, Qt.AlignLeft)
        Main_Title_Layout.setSpacing(20)
        Main_Title_Layout.setContentsMargins(0, 0, 50, 0)

        # Layout command prompt and send button
        promptLayout = QHBoxLayout()
        promptLayout.addWidget(self.commandPrompt)
        promptLayout.addWidget(self.send_btn)
        promptLayout.setSpacing(20)

        # Layout right side of GUI window
        commandWindowLayout = QVBoxLayout()
        commandWindowLayout.addLayout(promptLayout)
        commandWindowLayout.addWidget(self.ConsoleLog)
        commandWindowLayout.setSpacing(20)

        # Create Layout for tab widget and console window
        horizontalWindow_layout = QHBoxLayout()
        horizontalWindow_layout.addWidget(self.MyTabs)
        horizontalWindow_layout.addLayout(commandWindowLayout)
        horizontalWindow_layout.setSpacing(20)

        # Add tabs and video stream to main window layout
        Full_Window_layout = QVBoxLayout()
        Full_Window_layout.addLayout(Main_Title_Layout)
        Full_Window_layout.addLayout(horizontalWindow_layout)
        Full_Window_layout.setSpacing(20)
        Full_Window_layout.setContentsMargins(20, 20, 20, 20)

        # --------------------------------------------------------------
        # ------------- Create Battery 1 Tab Layout --------------------
        # --------------------------------------------------------------
        # Instantiate Battery 1 GUI Objects
        self.remainingCapaAlarm_1()
        self.batteryMode_1()
        self.voltage_1()
        self.current_1()
        self.averageCurrent_1()
        self.relativeStatOfCharge_1()
        self.absoluteStatOfCharge_1()
        self.remainingCapacity_1()
        self.fullChargeCapacity_1()
        self.runTimeToEmpty_1()
        self.averageTimeToEmpty_1()
        self.averageTimeToFull_1()
        self.chargingCurrent_1()
        self.chargingVoltage_1()
        self.Battery_Status_1()
        self.Cycle_Count_1()
        self.Serial_Number_1()
        self.Device_Name_1()
        self.Cell_Voltage4_1()
        self.Cell_Voltage3_1()
        self.Cell_Voltage2_1()
        self.Cell_Voltage1_1()
  
        # Arrange Layout to go on Battery 1 tab
        vertical_battery1_LeftLayout = QVBoxLayout()
        vertical_battery1_LeftLayout.addLayout(self.battMode_Layout1)
        vertical_battery1_LeftLayout.addLayout(self.serialNumLayout1)
        vertical_battery1_LeftLayout.addLayout(self.deviceNameLayout1)
        vertical_battery1_LeftLayout.addLayout(self.charging_Current_Layout1)
        vertical_battery1_LeftLayout.addLayout(self.charging_Voltag_Layout1)
        vertical_battery1_LeftLayout.addLayout(self.batteryStatusLayout1)
        vertical_battery1_LeftLayout.addLayout(self.cycleCountLayout1)
        vertical_battery1_LeftLayout.addLayout(self.cellVoltage4_Layout1)
        vertical_battery1_LeftLayout.addLayout(self.cellVoltage3_Layout1)
        vertical_battery1_LeftLayout.addLayout(self.cellVoltage2_Layout1)
        vertical_battery1_LeftLayout.addLayout(self.cellVoltage1_Layout1)
        vertical_battery1_LeftLayout.setSpacing(10)

        vertical_battery1_RightLayout = QVBoxLayout()
        vertical_battery1_RightLayout.addLayout(self.remCapAlarm_Layout1)
        vertical_battery1_RightLayout.addLayout(self.voltage_Layout1)
        vertical_battery1_RightLayout.addLayout(self.current_Layout1)
        vertical_battery1_RightLayout.addLayout(self.avgCurr_Layout1)
        vertical_battery1_RightLayout.addLayout(self.relStateCharge_Layout1)
        vertical_battery1_RightLayout.addLayout(self.absStateCharge_Layout1)
        vertical_battery1_RightLayout.addLayout(self.remCap_Layout1)
        vertical_battery1_RightLayout.addLayout(self.fullCharge_Layout1)
        vertical_battery1_RightLayout.addLayout(self.runTimeToEmpty_Layout1)
        vertical_battery1_RightLayout.addLayout(self.avgTimeToEmpty_Layout1)
        vertical_battery1_RightLayout.addLayout(self.avgTimeToFull_Layout1)
        vertical_battery1_RightLayout.setSpacing(10)

        battery1Tab_layout = QHBoxLayout()
        battery1Tab_layout.addLayout(vertical_battery1_LeftLayout)
        battery1Tab_layout.addLayout(vertical_battery1_RightLayout)
        battery1Tab_layout.setSpacing(12)

        # Add final layout to main tab layout
        self.Battery1_Tab.setLayout(battery1Tab_layout)

        # --------------------------------------------------------------
        # ------------- Create Battery 2 Tab Layout --------------------
        # --------------------------------------------------------------
        # Instantiate Battery 2 GUI Objects
        self.remainingCapaAlarm_2()
        self.batteryMode_2()
        self.voltage_2()
        self.current_2()
        self.averageCurrent_2()
        self.relativeStatOfCharge_2()
        self.absoluteStatOfCharge_2()
        self.remainingCapacity_2()
        self.fullChargeCapacity_2()
        self.runTimeToEmpty_2()
        self.averageTimeToEmpty_2()
        self.averageTimeToFull_2()
        self.chargingCurrent_2()
        self.chargingVoltage_2()
        self.Battery_Status_2()
        self.Cycle_Count_2()
        self.Serial_Number_2()
        self.Device_Name_2()
        self.Cell_Voltage4_2()
        self.Cell_Voltage3_2()
        self.Cell_Voltage2_2()
        self.Cell_Voltage1_2()

        # Arrange Layout to go on Battery 2 tab
        vertical_battery2_LeftLayout = QVBoxLayout()
        vertical_battery2_LeftLayout.addLayout(self.battMode_Layout2)
        vertical_battery2_LeftLayout.addLayout(self.serialNumLayout2)
        vertical_battery2_LeftLayout.addLayout(self.deviceNameLayout2)
        vertical_battery2_LeftLayout.addLayout(self.charging_Current_Layout2)
        vertical_battery2_LeftLayout.addLayout(self.charging_Voltag_Layout2)
        vertical_battery2_LeftLayout.addLayout(self.batteryStatusLayout2)
        vertical_battery2_LeftLayout.addLayout(self.cycleCountLayout2)
        vertical_battery2_LeftLayout.addLayout(self.cellVoltage4_Layout2)
        vertical_battery2_LeftLayout.addLayout(self.cellVoltage3_Layout2)
        vertical_battery2_LeftLayout.addLayout(self.cellVoltage2_Layout2)
        vertical_battery2_LeftLayout.addLayout(self.cellVoltage1_Layout2)
        vertical_battery2_LeftLayout.setSpacing(10)

        vertical_battery2_RightLayout = QVBoxLayout()
        vertical_battery2_RightLayout.addLayout(self.remCapAlarm_Layout2)
        vertical_battery2_RightLayout.addLayout(self.voltage_Layout2)
        vertical_battery2_RightLayout.addLayout(self.current_Layout2)
        vertical_battery2_RightLayout.addLayout(self.avgCurr_Layout2)
        vertical_battery2_RightLayout.addLayout(self.relStateCharge_Layout2)
        vertical_battery2_RightLayout.addLayout(self.absStateCharge_Layout2)
        vertical_battery2_RightLayout.addLayout(self.remCap_Layout2)
        vertical_battery2_RightLayout.addLayout(self.fullCharge_Layout2)
        vertical_battery2_RightLayout.addLayout(self.runTimeToEmpty_Layout2)
        vertical_battery2_RightLayout.addLayout(self.avgTimeToEmpty_Layout2)
        vertical_battery2_RightLayout.addLayout(self.avgTimeToFull_Layout2)
        vertical_battery2_RightLayout.setSpacing(10)

        battery2Tab_layout = QHBoxLayout()
        battery2Tab_layout.addLayout(vertical_battery2_LeftLayout)
        battery2Tab_layout.addLayout(vertical_battery2_RightLayout)
        battery2Tab_layout.setSpacing(12)

        # Add final layout to main tab layout
        self.Battery2_Tab.setLayout(battery2Tab_layout)

        # --------------------------------------------------------------
        # ------------ Add Final Layout to Main Window -----------------
        # --------------------------------------------------------------
        # Set Main window layout to GUI central Widget
        self.centralWidget().setLayout(Full_Window_layout)
        self.centralWidget().isWindow()


        self.handleButtons()
        
        # Connect Signals
        self.GPIO_ch1.doneFlag1.connect(self.handle.ch1Buttons)
        self.GPIO_ch2.doneFlag2.connect(self.handle.ch2Buttons)
        
        # Display GUI Objects
        # ~ self.show()
        #~ self.showFullScreen()

        self.showMaximized()
    # --------------------------------------------------------------------------------------------------------------
    # ----------------------------- GUI Objects/ Functions ---------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------
    # ------------------- Keyboard Key Functions -----------------------
    # ------------------------------------------------------------------
    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Return:  # Send button
            self.send_btn.Un_Click()
    # ------------------------------------------------------------------
    # ------------------- Handlers -------------------------------------
    # ------------------------------------------------------------------
    def handleButtons(self):
            self.handle = handlers(self.relay1_40, self.relay1_60, self.relay1_500, self.relay1_1k, 
            self.relay2_40, self.relay2_60, self.relay2_500, self.relay2_1k, 
            self.GPIO_ch1, self.GPIO_ch2)
        
    # ------------------------------------------------------------------
    # ------------------- Main Title Function --------------------------
    # ------------------------------------------------------------------
    def MainTitle(self):
        self.MainTitleText = QLabel(self)
        self.MainTitleText.setText("Battery Test Fixture")
        self.MainTitleText.setStyleSheet(GUI_Style.mainTitle)

    def MainLogoButton(self):
        self.Logo_btn = Logo_Button(self, "", self.ConsoleLog)
        self.Logo_btn.setStyleSheet(GUI_Style.startButton)
        self.Logo_btn.pressed.connect(self.Logo_btn.On_Click)
        self.Logo_btn.released.connect(self.Logo_btn.Un_Click)
        self.Logo_btn.setIcon(QIcon(Icon_Path))
        self.Logo_btn.setIconSize(QSize(300, 80))
    # ------------------------------------------------------------------
    # -------------------  Create Console Log --------------------------
    # ------------------------------------------------------------------
    def Console_Log(self):
        self.ConsoleLog = QTextEdit(self)
        #self.ConsoleLog.setMaximumHeight(100)
        self.ConsoleLog.setStyleSheet(GUI_Style.consoleLog)
        self.ConsoleLog.setPlaceholderText("Console Log")
        self.ConsoleLog.setReadOnly(True)
        self.ConsoleLog.setLineWrapMode(True)
        self.ConsoleLog.setAlignment(Qt.AlignTop)
    # ------------------------------------------------------------------
    # ----------------  Create Input Command Prompt --------------------
    # ------------------------------------------------------------------
    def inputCommandPrompt(self):
        self.commandPrompt = QLineEdit(self)
        self.commandPrompt.setStyleSheet(GUI_Style.commandBox)
        self.commandPrompt.setPlaceholderText("Enter Command")
    # ------------------------------------------------------------------
    # -------------------  Create Send Button --------------------------
    # ------------------------------------------------------------------
    def sendCommandButton(self):
        self.send_btn = Send_Command_Button(self, "Send", self.ConsoleLog, self.commandPrompt)
        self.send_btn.setMaximumSize(125, 30)
        self.send_btn.setMinimumSize(125, 30)
        self.send_btn.setStyleSheet(GUI_Style.sendButton)
        self.send_btn.pressed.connect(self.send_btn.On_Click)
        self.send_btn.released.connect(self.send_btn.Un_Click)
    # ------------------------------------------------------------------
    # --------------------- Create Tab Widget --------------------------
    # ------------------------------------------------------------------
    def tabWidget(self):
        self.MyTabs = QTabWidget()
        self.MyTabs.setStyleSheet(GUI_Style.tabs)
        self.MyTabs.setMaximumWidth(500)

        # Create each individual tabs
        self.Battery1_Tab = QWidget()
        self.Battery2_Tab = QWidget()

        # Add Tabs and Tab Icon to tab widget
        self.MyTabs.addTab(self.Battery1_Tab, ' Battery 1')
        self.MyTabs.addTab(self.Battery2_Tab, ' Battery 2')
    # ------------------------------------------------------------------
    # ----------- Create Battery 1 Tab GUI Objects  --------------------
    # ------------------------------------------------------------------
    def remainingCapaAlarm_1(self):
        # create label
        self.remCapAlarm1 = QLabel(self)
        self.remCapAlarm1.setText("Remaining Capacity Alarm")
        self.remCapAlarm1.setStyleSheet(GUI_Style.nameLabel)
        self.remCapAlarm1.setWordWrap(True)
   
        # create input box
        self.remCapAlarmBox1 = QLineEdit(self)
        self.remCapAlarmBox1.setStyleSheet(GUI_Style.updateField)
        self.remCapAlarmBox1.setMaximumWidth(50)

        # create layout
        self.remCapAlarm_Layout1 = QHBoxLayout()
        self.remCapAlarm_Layout1.addWidget(self.remCapAlarm1)
        self.remCapAlarm_Layout1.addWidget(self.remCapAlarmBox1)


    def batteryMode_1(self):
         # create label
        self.battMode1 = QLabel(self)
        self.battMode1.setText("Battery Mode")
        self.battMode1.setStyleSheet(GUI_Style.nameLabel)
        self.battMode1.setWordWrap(True)
        
        # create input box
        self.battModeBox1 = QLineEdit(self)
        self.battModeBox1.setStyleSheet(GUI_Style.updateField)
        self.battModeBox1.setMaximumWidth(50)

        # create layout
        self.battMode_Layout1 = QHBoxLayout()
        self.battMode_Layout1.addWidget(self.battMode1)
        self.battMode_Layout1.addWidget(self.battModeBox1)

    def voltage_1(self):
         # create label
        self.voltage1 = QLabel(self)
        self.voltage1.setText("Voltage")
        self.voltage1.setStyleSheet(GUI_Style.nameLabel)
        self.voltage1.setWordWrap(True)
        
        # create input box
        self.voltageBox1 = QLineEdit(self)
        self.voltageBox1.setStyleSheet(GUI_Style.updateField)
        self.voltageBox1.setMaximumWidth(50)

        # create layout
        self.voltage_Layout1 = QHBoxLayout()
        self.voltage_Layout1.addWidget(self.voltage1)
        self.voltage_Layout1.addWidget(self.voltageBox1)

    def current_1(self):
        # create label
        self.current1 = QLabel(self)
        self.current1.setText("Current")
        self.current1.setStyleSheet(GUI_Style.nameLabel)
        self.current1.setWordWrap(True)
   
        # create input box
        self.currentBox1 = QLineEdit(self)
        self.currentBox1.setStyleSheet(GUI_Style.updateField)
        self.currentBox1.setMaximumWidth(50)

        # create layout
        self.current_Layout1 = QHBoxLayout()
        self.current_Layout1.addWidget(self.current1)
        self.current_Layout1.addWidget(self.currentBox1)

    def averageCurrent_1(self):
        # create label
        self.avgCurr1 = QLabel(self)
        self.avgCurr1.setText("Average Current")
        self.avgCurr1.setStyleSheet(GUI_Style.nameLabel)
        self.avgCurr1.setWordWrap(True)
   
        # create input box
        self.avgCurrBox1 = QLineEdit(self)
        self.avgCurrBox1.setStyleSheet(GUI_Style.updateField)
        self.avgCurrBox1.setMaximumWidth(50)

        # create layout
        self.avgCurr_Layout1 = QHBoxLayout()
        self.avgCurr_Layout1.addWidget(self.avgCurr1)
        self.avgCurr_Layout1.addWidget(self.avgCurrBox1)

    def relativeStatOfCharge_1(self):
        # create label
        self.relStateCharge1 = QLabel(self)
        self.relStateCharge1.setText("Relative State Of Charge")
        self.relStateCharge1.setStyleSheet(GUI_Style.nameLabel)
        self.relStateCharge1.setWordWrap(True)
       
       # create input box
        self.relStateChargeBox1 = QLineEdit(self)
        self.relStateChargeBox1.setStyleSheet(GUI_Style.updateField)
        self.relStateChargeBox1.setMaximumWidth(50)

        # create layout
        self.relStateCharge_Layout1 = QHBoxLayout()
        self.relStateCharge_Layout1.addWidget(self.relStateCharge1)
        self.relStateCharge_Layout1.addWidget(self.relStateChargeBox1)

    def absoluteStatOfCharge_1(self):
        # create label
        self.absStateCharge1 = QLabel(self)
        self.absStateCharge1.setText("Absolute State Of Charge")
        self.absStateCharge1.setStyleSheet(GUI_Style.nameLabel)
        self.absStateCharge1.setWordWrap(True)
   
        # create input box
        self.absStateChargeBox1 = QLineEdit(self)
        self.absStateChargeBox1.setStyleSheet(GUI_Style.updateField)
        self.absStateChargeBox1.setMaximumWidth(50)

        # create layout
        self.absStateCharge_Layout1 = QHBoxLayout()
        self.absStateCharge_Layout1.addWidget(self.absStateCharge1)
        self.absStateCharge_Layout1.addWidget(self.absStateChargeBox1)

    def remainingCapacity_1(self):
        # create label
        self.remainingCapacity1 = QLabel(self)
        self.remainingCapacity1.setText("Remaining Capacity")
        self.remainingCapacity1.setStyleSheet(GUI_Style.nameLabel)
        self.remainingCapacity1.setWordWrap(True)
   
        # create input box
        self.remainingCapacityBox1 = QLineEdit(self)
        self.remainingCapacityBox1.setStyleSheet(GUI_Style.updateField)
        self.remainingCapacityBox1.setMaximumWidth(50)

        # create layout
        self.remCap_Layout1 = QHBoxLayout()
        self.remCap_Layout1.addWidget(self.remainingCapacity1)
        self.remCap_Layout1.addWidget(self.remainingCapacityBox1)

    def fullChargeCapacity_1(self):
        # create label
        self.fullChargeCapacity1 = QLabel(self)
        self.fullChargeCapacity1.setText("Full Charge Capacity")
        self.fullChargeCapacity1.setStyleSheet(GUI_Style.nameLabel)
        self.fullChargeCapacity1.setWordWrap(True)
   
        # create input box
        self.fullChargeCapacityBox1 = QLineEdit(self)
        self.fullChargeCapacityBox1.setStyleSheet(GUI_Style.updateField)
        self.fullChargeCapacityBox1.setMaximumWidth(50)

        # create layout
        self.fullCharge_Layout1 = QHBoxLayout()
        self.fullCharge_Layout1.addWidget(self.fullChargeCapacity1)
        self.fullCharge_Layout1.addWidget(self.fullChargeCapacityBox1)

    def runTimeToEmpty_1(self):
        # create label
        self.runTimeToEmpty1 = QLabel(self)
        self.runTimeToEmpty1.setText("Run Time To Empty")
        self.runTimeToEmpty1.setStyleSheet(GUI_Style.nameLabel)
        self.runTimeToEmpty1.setWordWrap(True)
   
        # create input box
        self.runTimeToEmptyBox1 = QLineEdit(self)
        self.runTimeToEmptyBox1.setStyleSheet(GUI_Style.updateField)
        self.runTimeToEmptyBox1.setMaximumWidth(50)

        # create layout
        self.runTimeToEmpty_Layout1 = QHBoxLayout()
        self.runTimeToEmpty_Layout1.addWidget(self.runTimeToEmpty1)
        self.runTimeToEmpty_Layout1.addWidget(self.runTimeToEmptyBox1)

    def averageTimeToEmpty_1(self):
        # create label
        self.avgTimeToEmpty1 = QLabel(self)
        self.avgTimeToEmpty1.setText("Average Time To Empty")
        self.avgTimeToEmpty1.setStyleSheet(GUI_Style.nameLabel)
        self.avgTimeToEmpty1.setWordWrap(True)
   
        # create input box
        self.avgTimeToEmptyBox1 = QLineEdit(self)
        self.avgTimeToEmptyBox1.setStyleSheet(GUI_Style.updateField)
        self.avgTimeToEmptyBox1.setMaximumWidth(50)

        # create layout
        self.avgTimeToEmpty_Layout1 = QHBoxLayout()
        self.avgTimeToEmpty_Layout1.addWidget(self.avgTimeToEmpty1)
        self.avgTimeToEmpty_Layout1.addWidget(self.avgTimeToEmptyBox1)

    def averageTimeToFull_1(self):
        # create label
        self.avgTimeToFull1 = QLabel(self)
        self.avgTimeToFull1.setText("Average Time To Full")
        self.avgTimeToFull1.setStyleSheet(GUI_Style.nameLabel)
        self.avgTimeToFull1.setWordWrap(True)
        self.avgTimeToFull1.setWordWrap(True)
   
        # create input box
        self.avgTimeToFullBox1 = QLineEdit(self)
        self.avgTimeToFullBox1.setStyleSheet(GUI_Style.updateField)
        self.avgTimeToFullBox1.setMaximumWidth(50)

        # create layout
        self.avgTimeToFull_Layout1 = QHBoxLayout()
        self.avgTimeToFull_Layout1.addWidget(self.avgTimeToFull1)
        self.avgTimeToFull_Layout1.addWidget(self.avgTimeToFullBox1)     
        
    def chargingCurrent_1(self):
        # create label
        self.chargingCurrent1 = QLabel(self)
        self.chargingCurrent1.setText("Charging Current")
        self.chargingCurrent1.setStyleSheet(GUI_Style.nameLabel)
        self.chargingCurrent1.setWordWrap(True)
   
        # create input box
        self.chargingCurrentBox1 = QLineEdit(self)
        self.chargingCurrentBox1.setStyleSheet(GUI_Style.updateField)
        self.chargingCurrentBox1.setMaximumWidth(50)

        # create layout
        self.charging_Current_Layout1 = QHBoxLayout()
        self.charging_Current_Layout1.addWidget(self.chargingCurrent1)
        self.charging_Current_Layout1.addWidget(self.chargingCurrentBox1)          

    def chargingVoltage_1(self):
        # create label
        self.chargingVoltage1 = QLabel(self)
        self.chargingVoltage1.setText("Charging Voltage")
        self.chargingVoltage1.setStyleSheet(GUI_Style.nameLabel)
        self.chargingVoltage1.setWordWrap(True)
   
        # create input box
        self.chargingVoltageBox1 = QLineEdit(self)
        self.chargingVoltageBox1.setStyleSheet(GUI_Style.updateField)
        self.chargingVoltageBox1.setMaximumWidth(50)

        # create layout
        self.charging_Voltag_Layout1 = QHBoxLayout()
        self.charging_Voltag_Layout1.addWidget(self.chargingVoltage1)
        self.charging_Voltag_Layout1.addWidget(self.chargingVoltageBox1)

    def Battery_Status_1(self):
        # create label
        self.batteryStatus1 = QLabel(self)
        self.batteryStatus1.setText("Battery Status")
        self.batteryStatus1.setStyleSheet(GUI_Style.nameLabel)
        self.batteryStatus1.setWordWrap(True)
   
        # create input box
        self.batteryStatusBox1 = QLineEdit(self)
        self.batteryStatusBox1.setStyleSheet(GUI_Style.updateField)
        self.batteryStatusBox1.setMaximumWidth(50)

        # create layout
        self.batteryStatusLayout1 = QHBoxLayout()
        self.batteryStatusLayout1.addWidget(self.batteryStatus1)
        self.batteryStatusLayout1.addWidget(self.batteryStatusBox1)

    def Cycle_Count_1(self):
        # create label
        self.cycleCount1 = QLabel(self)
        self.cycleCount1.setText("Cycle Count")
        self.cycleCount1.setStyleSheet(GUI_Style.nameLabel)
        self.cycleCount1.setWordWrap(True)
   
        # create input box
        self.cycleCountBox1 = QLineEdit(self)
        self.cycleCountBox1.setStyleSheet(GUI_Style.updateField)
        self.cycleCountBox1.setMaximumWidth(50)

        # create layout
        self.cycleCountLayout1 = QHBoxLayout()
        self.cycleCountLayout1.addWidget(self.cycleCount1)
        self.cycleCountLayout1.addWidget(self.cycleCountBox1)
        
    def Serial_Number_1(self):
        # create label
        self.serNum1 = QLabel(self)
        self.serNum1.setText("Serial Number")
        self.serNum1.setStyleSheet(GUI_Style.nameLabel)
        self.serNum1.setWordWrap(True)
   
        # create input box
        self.serNumBox1 = QLineEdit(self)
        self.serNumBox1.setStyleSheet(GUI_Style.updateField)
        self.serNumBox1.setMaximumWidth(50)

        # create layout
        self.serialNumLayout1 = QHBoxLayout()
        self.serialNumLayout1.addWidget(self.serNum1)
        self.serialNumLayout1.addWidget(self.serNumBox1)
                
    def Device_Name_1(self):
        # create label
        self.devName1 = QLabel(self)
        self.devName1.setText("Device Name")
        self.devName1.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.devNameBox1 = QLineEdit(self)
        self.devNameBox1.setStyleSheet(GUI_Style.updateField)
        self.devNameBox1.setMaximumWidth(50)

        # create layout
        self.deviceNameLayout1 = QHBoxLayout()
        self.deviceNameLayout1.addWidget(self.devName1)
        self.deviceNameLayout1.addWidget(self.devNameBox1)
                   
    def Cell_Voltage4_1(self):
        # create label
        self.cellVolt4_1 = QLabel(self)
        self.cellVolt4_1.setText("Cell Voltage 4")
        self.cellVolt4_1.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.cellVolt4Box1 = QLineEdit(self)
        self.cellVolt4Box1.setStyleSheet(GUI_Style.updateField)
        self.cellVolt4Box1.setMaximumWidth(50)

        # create layout
        self.cellVoltage4_Layout1 = QHBoxLayout()
        self.cellVoltage4_Layout1.addWidget(self.cellVolt4_1)
        self.cellVoltage4_Layout1.addWidget(self.cellVolt4Box1)
          
    def Cell_Voltage3_1(self):
        # create label
        self.cellVolt3_1 = QLabel(self)
        self.cellVolt3_1.setText("Cell Voltage 3")
        self.cellVolt3_1.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.cellVolt3Box1 = QLineEdit(self)
        self.cellVolt3Box1.setStyleSheet(GUI_Style.updateField)
        self.cellVolt3Box1.setMaximumWidth(50)

        # create layout
        self.cellVoltage3_Layout1 = QHBoxLayout()
        self.cellVoltage3_Layout1.addWidget(self.cellVolt3_1)
        self.cellVoltage3_Layout1.addWidget(self.cellVolt3Box1)
                         
    def Cell_Voltage2_1(self):
        # create label
        self.cellVolt2_1 = QLabel(self)
        self.cellVolt2_1.setText("Cell Voltage 2")
        self.cellVolt2_1.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.cellVolt2Box1 = QLineEdit(self)
        self.cellVolt2Box1.setStyleSheet(GUI_Style.updateField)
        self.cellVolt2Box1.setMaximumWidth(50)

        # create layout
        self.cellVoltage2_Layout1 = QHBoxLayout()
        self.cellVoltage2_Layout1.addWidget(self.cellVolt2_1)
        self.cellVoltage2_Layout1.addWidget(self.cellVolt2Box1)
                       
    def Cell_Voltage1_1(self):
        # create label
        self.cellVolt1_1 = QLabel(self)
        self.cellVolt1_1.setText("Cell Voltage 1")
        self.cellVolt1_1.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.cellVolt1Box1 = QLineEdit(self)
        self.cellVolt1Box1.setStyleSheet(GUI_Style.updateField)
        self.cellVolt1Box1.setMaximumWidth(50)

        # create layout
        self.cellVoltage1_Layout1 = QHBoxLayout()
        self.cellVoltage1_Layout1.addWidget(self.cellVolt1_1)
        self.cellVoltage1_Layout1.addWidget(self.cellVolt1Box1)
   
    ## ------------------------------------------------------------------
    ## ----------- Create Battery 2 Tab GUI Objects  --------------------
    ## ------------------------------------------------------------------
    def remainingCapaAlarm_2(self):
        # create label
        self.remCapAlarm2 = QLabel(self)
        self.remCapAlarm2.setText("Remaining Capacity Alarm")
        self.remCapAlarm2.setStyleSheet(GUI_Style.nameLabel)
        self.remCapAlarm2.setWordWrap(True)
   
        # create input box
        self.remCapAlarmBox2 = QLineEdit(self)
        self.remCapAlarmBox2.setStyleSheet(GUI_Style.updateField)
        self.remCapAlarmBox2.setMaximumWidth(50)

        # create layout
        self.remCapAlarm_Layout2 = QHBoxLayout()
        self.remCapAlarm_Layout2.addWidget(self.remCapAlarm2)
        self.remCapAlarm_Layout2.addWidget(self.remCapAlarmBox2)

    def batteryMode_2(self):
         # create label
        self.battMode2 = QLabel(self)
        self.battMode2.setText("Battery Mode")
        self.battMode2.setStyleSheet(GUI_Style.nameLabel)
        
        # create input box
        self.battModeBox2 = QLineEdit(self)
        self.battModeBox2.setStyleSheet(GUI_Style.updateField)
        self.battModeBox2.setMaximumWidth(50)

        # create layout
        self.battMode_Layout2 = QHBoxLayout()
        self.battMode_Layout2.addWidget(self.battMode2)
        self.battMode_Layout2.addWidget(self.battModeBox2)

    def voltage_2(self):
         # create label
        self.voltage2 = QLabel(self)
        self.voltage2.setText("Voltage")
        self.voltage2.setStyleSheet(GUI_Style.nameLabel)
        
        # create input box
        self.voltageBox2 = QLineEdit(self)
        self.voltageBox2.setStyleSheet(GUI_Style.updateField)
        self.voltageBox2.setMaximumWidth(50)

        # create layout
        self.voltage_Layout2 = QHBoxLayout()
        self.voltage_Layout2.addWidget(self.voltage2)
        self.voltage_Layout2.addWidget(self.voltageBox2)

    def current_2(self):
        # create label
        self.current2 = QLabel(self)
        self.current2.setText("Current")
        self.current2.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.currentBox2 = QLineEdit(self)
        self.currentBox2.setStyleSheet(GUI_Style.updateField)
        self.currentBox2.setMaximumWidth(50)

        # create layout
        self.current_Layout2 = QHBoxLayout()
        self.current_Layout2.addWidget(self.current2)
        self.current_Layout2.addWidget(self.currentBox2)

    def averageCurrent_2(self):
        # create label
        self.avgCurr2 = QLabel(self)
        self.avgCurr2.setText("Average Current")
        self.avgCurr2.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.avgCurrBox2 = QLineEdit(self)
        self.avgCurrBox2.setStyleSheet(GUI_Style.updateField)
        self.avgCurrBox2.setMaximumWidth(50)

        # create layout
        self.avgCurr_Layout2 = QHBoxLayout()
        self.avgCurr_Layout2.addWidget(self.avgCurr2)
        self.avgCurr_Layout2.addWidget(self.avgCurrBox2)

    def relativeStatOfCharge_2(self):
        # create label
        self.relStateCharge2 = QLabel(self)
        self.relStateCharge2.setText("Relative State Of Charge")
        self.relStateCharge2.setStyleSheet(GUI_Style.nameLabel)
        self.relStateCharge2.setWordWrap(True)
       
       # create input box
        self.relStateChargeBox2 = QLineEdit(self)
        self.relStateChargeBox2.setStyleSheet(GUI_Style.updateField)
        self.relStateChargeBox2.setMaximumWidth(50)

        # create layout
        self.relStateCharge_Layout2 = QHBoxLayout()
        self.relStateCharge_Layout2.addWidget(self.relStateCharge2)
        self.relStateCharge_Layout2.addWidget(self.relStateChargeBox2)

    def absoluteStatOfCharge_2(self):
        # create label
        self.absStateCharge2 = QLabel(self)
        self.absStateCharge2.setText("Absolute State Of Charge")
        self.absStateCharge2.setStyleSheet(GUI_Style.nameLabel)
        self.absStateCharge2.setWordWrap(True)
   
        # create input box
        self.absStateChargeBox2 = QLineEdit(self)
        self.absStateChargeBox2.setStyleSheet(GUI_Style.updateField)
        self.absStateChargeBox2.setMaximumWidth(50)

        # create layout
        self.absStateCharge_Layout2 = QHBoxLayout()
        self.absStateCharge_Layout2.addWidget(self.absStateCharge2)
        self.absStateCharge_Layout2.addWidget(self.absStateChargeBox2)

    def remainingCapacity_2(self):
        # create label
        self.remainingCapacity2 = QLabel(self)
        self.remainingCapacity2.setText("Remaining Capacity")
        self.remainingCapacity2.setStyleSheet(GUI_Style.nameLabel)
        self.remainingCapacity2.setWordWrap(True)
   
        # create input box
        self.remainingCapacityBox2 = QLineEdit(self)
        self.remainingCapacityBox2.setStyleSheet(GUI_Style.updateField)
        self.remainingCapacityBox2.setMaximumWidth(50)

        # create layout
        self.remCap_Layout2 = QHBoxLayout()
        self.remCap_Layout2.addWidget(self.remainingCapacity2)
        self.remCap_Layout2.addWidget(self.remainingCapacityBox2)

    def fullChargeCapacity_2(self):
        # create label
        self.fullChargeCapacity2 = QLabel(self)
        self.fullChargeCapacity2.setText("Full Charge Capacity")
        self.fullChargeCapacity2.setStyleSheet(GUI_Style.nameLabel)
        self.fullChargeCapacity2.setWordWrap(True)
   
        # create input box
        self.fullChargeCapacityBox2 = QLineEdit(self)
        self.fullChargeCapacityBox2.setStyleSheet(GUI_Style.updateField)
        self.fullChargeCapacityBox2.setMaximumWidth(50)

        # create layout
        self.fullCharge_Layout2 = QHBoxLayout()
        self.fullCharge_Layout2.addWidget(self.fullChargeCapacity2)
        self.fullCharge_Layout2.addWidget(self.fullChargeCapacityBox2)

    def runTimeToEmpty_2(self):
        # create label
        self.runTimeToEmpty2 = QLabel(self)
        self.runTimeToEmpty2.setText("Run Time To Empty")
        self.runTimeToEmpty2.setStyleSheet(GUI_Style.nameLabel)
        self.runTimeToEmpty2.setWordWrap(True)
   
        # create input box
        self.runTimeToEmptyBox2 = QLineEdit(self)
        self.runTimeToEmptyBox2.setStyleSheet(GUI_Style.updateField)
        self.runTimeToEmptyBox2.setMaximumWidth(50)

        # create layout
        self.runTimeToEmpty_Layout2 = QHBoxLayout()
        self.runTimeToEmpty_Layout2.addWidget(self.runTimeToEmpty2)
        self.runTimeToEmpty_Layout2.addWidget(self.runTimeToEmptyBox2)

    def averageTimeToEmpty_2(self):
        # create label
        self.avgTimeToEmpty2 = QLabel(self)
        self.avgTimeToEmpty2.setText("Average Time To Empty")
        self.avgTimeToEmpty2.setStyleSheet(GUI_Style.nameLabel)
        self.avgTimeToEmpty2.setWordWrap(True)
   
        # create input box
        self.avgTimeToEmptyBox2 = QLineEdit(self)
        self.avgTimeToEmptyBox2.setStyleSheet(GUI_Style.updateField)
        self.avgTimeToEmptyBox2.setMaximumWidth(50)

        # create layout
        self.avgTimeToEmpty_Layout2 = QHBoxLayout()
        self.avgTimeToEmpty_Layout2.addWidget(self.avgTimeToEmpty2)
        self.avgTimeToEmpty_Layout2.addWidget(self.avgTimeToEmptyBox2)

    def averageTimeToFull_2(self):
        # create label
        self.avgTimeToFull2 = QLabel(self)
        self.avgTimeToFull2.setText("Average Time To Full")
        self.avgTimeToFull2.setStyleSheet(GUI_Style.nameLabel)
        self.avgTimeToFull2.setWordWrap(True)
   
        # create input box
        self.avgTimeToFullBox2 = QLineEdit(self)
        self.avgTimeToFullBox2.setStyleSheet(GUI_Style.updateField)
        self.avgTimeToFullBox2.setMaximumWidth(50)

        # create layout
        self.avgTimeToFull_Layout2 = QHBoxLayout()
        self.avgTimeToFull_Layout2.addWidget(self.avgTimeToFull2)
        self.avgTimeToFull_Layout2.addWidget(self.avgTimeToFullBox2)     
        
    def chargingCurrent_2(self):
        # create label
        self.chargingCurrent2 = QLabel(self)
        self.chargingCurrent2.setText("Charging Current")
        self.chargingCurrent2.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.chargingCurrentBox2 = QLineEdit(self)
        self.chargingCurrentBox2.setStyleSheet(GUI_Style.updateField)
        self.chargingCurrentBox2.setMaximumWidth(50)

        # create layout
        self.charging_Current_Layout2 = QHBoxLayout()
        self.charging_Current_Layout2.addWidget(self.chargingCurrent2)
        self.charging_Current_Layout2.addWidget(self.chargingCurrentBox2)          

    def chargingVoltage_2(self):
        # create label
        self.chargingVoltage2 = QLabel(self)
        self.chargingVoltage2.setText("Charging Voltage")
        self.chargingVoltage2.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.chargingVoltageBox2 = QLineEdit(self)
        self.chargingVoltageBox2.setStyleSheet(GUI_Style.updateField)
        self.chargingVoltageBox2.setMaximumWidth(50)

        # create layout
        self.charging_Voltag_Layout2 = QHBoxLayout()
        self.charging_Voltag_Layout2.addWidget(self.chargingVoltage2)
        self.charging_Voltag_Layout2.addWidget(self.chargingVoltageBox2)

    def Battery_Status_2(self):
        # create label
        self.batteryStatus2 = QLabel(self)
        self.batteryStatus2.setText("Battery Status")
        self.batteryStatus2.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.batteryStatusBox2 = QLineEdit(self)
        self.batteryStatusBox2.setStyleSheet(GUI_Style.updateField)
        self.batteryStatusBox2.setMaximumWidth(50)

        # create layout
        self.batteryStatusLayout2 = QHBoxLayout()
        self.batteryStatusLayout2.addWidget(self.batteryStatus2)
        self.batteryStatusLayout2.addWidget(self.batteryStatusBox2)

    def Cycle_Count_2(self):
        # create label
        self.cycleCount2 = QLabel(self)
        self.cycleCount2.setText("Cycle Count")
        self.cycleCount2.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.cycleCountBox2 = QLineEdit(self)
        self.cycleCountBox2.setStyleSheet(GUI_Style.updateField)
        self.cycleCountBox2.setMaximumWidth(50)

        # create layout
        self.cycleCountLayout2 = QHBoxLayout()
        self.cycleCountLayout2.addWidget(self.cycleCount2)
        self.cycleCountLayout2.addWidget(self.cycleCountBox2)
        
    def Serial_Number_2(self):
        # create label
        self.serNum2 = QLabel(self)
        self.serNum2.setText("Serial Number")
        self.serNum2.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.serNumBox2 = QLineEdit(self)
        self.serNumBox2.setStyleSheet(GUI_Style.updateField)
        self.serNumBox2.setMaximumWidth(50)

        # create layout
        self.serialNumLayout2 = QHBoxLayout()
        self.serialNumLayout2.addWidget(self.serNum2)
        self.serialNumLayout2.addWidget(self.serNumBox2)
                
    def Device_Name_2(self):
        # create label
        self.devName2 = QLabel(self)
        self.devName2.setText("Device Name")
        self.devName2.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.devNameBox2 = QLineEdit(self)
        self.devNameBox2.setStyleSheet(GUI_Style.updateField)
        self.devNameBox2.setMaximumWidth(50)

        # create layout
        self.deviceNameLayout2 = QHBoxLayout()
        self.deviceNameLayout2.addWidget(self.devName2)
        self.deviceNameLayout2.addWidget(self.devNameBox2)
                   
    def Cell_Voltage4_2(self):
        # create label
        self.cellVolt4_2 = QLabel(self)
        self.cellVolt4_2.setText("Cell Voltage 4")
        self.cellVolt4_2.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.cellVolt4Box2 = QLineEdit(self)
        self.cellVolt4Box2.setStyleSheet(GUI_Style.updateField)
        self.cellVolt4Box2.setMaximumWidth(50)

        # create layout
        self.cellVoltage4_Layout2 = QHBoxLayout()
        self.cellVoltage4_Layout2.addWidget(self.cellVolt4_2)
        self.cellVoltage4_Layout2.addWidget(self.cellVolt4Box2)
          
    def Cell_Voltage3_2(self):
        # create label
        self.cellVolt3_2 = QLabel(self)
        self.cellVolt3_2.setText("Cell Voltage 3")
        self.cellVolt3_2.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.cellVolt3Box2 = QLineEdit(self)
        self.cellVolt3Box2.setStyleSheet(GUI_Style.updateField)
        self.cellVolt3Box2.setMaximumWidth(50)

        # create layout
        self.cellVoltage3_Layout2 = QHBoxLayout()
        self.cellVoltage3_Layout2.addWidget(self.cellVolt3_2)
        self.cellVoltage3_Layout2.addWidget(self.cellVolt3Box2)
                         
    def Cell_Voltage2_2(self):
        # create label
        self.cellVolt2_2 = QLabel(self)
        self.cellVolt2_2.setText("Cell Voltage 2")
        self.cellVolt2_2.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.cellVolt2Box2 = QLineEdit(self)
        self.cellVolt2Box2.setStyleSheet(GUI_Style.updateField)
        self.cellVolt2Box2.setMaximumWidth(50)

        # create layout
        self.cellVoltage2_Layout2 = QHBoxLayout()
        self.cellVoltage2_Layout2.addWidget(self.cellVolt2_2)
        self.cellVoltage2_Layout2.addWidget(self.cellVolt2Box2)
                       
    def Cell_Voltage1_2(self):
        # create label
        self.cellVolt1_2 = QLabel(self)
        self.cellVolt1_2.setText("Cell Voltage 1")
        self.cellVolt1_2.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.cellVolt1Box2 = QLineEdit(self)
        self.cellVolt1Box2.setStyleSheet(GUI_Style.updateField)
        self.cellVolt1Box2.setMaximumWidth(50)

        # create layout
        self.cellVoltage1_Layout2 = QHBoxLayout()
        self.cellVoltage1_Layout2.addWidget(self.cellVolt1_2)
        self.cellVoltage1_Layout2.addWidget(self.cellVolt1Box2)

    # ------------------------------------------------------------------
    # ---------------- Create Status Bar Widgets -----------------------
    # ------------------------------------------------------------------
    def StatusBar(self):
        self.statusBar = QStatusBar()
        self.statusBar.setStyleSheet(GUI_Style.statusBarWhite)
        
        self.relay1_40 = Relay_1_40_Ohm(self, "40\u03A9 Relay 1", self.GPIO_ch1)
        self.relay1_40.setStyleSheet(GUI_Style.statusBarButton)
        self.relay1_40.pressed.connect(self.relay1_40.On_Click)
        self.relay1_40.released.connect(self.relay1_40.Un_Click)
        
        self.relay1_60 = Relay_1_60_Ohm(self, "60\u03A9 Relay 1", self.GPIO_ch1)
        self.relay1_60.setStyleSheet(GUI_Style.statusBarButton)
        self.relay1_60.pressed.connect(self.relay1_60.On_Click)
        self.relay1_60.released.connect(self.relay1_60.Un_Click)
        
        self.relay1_500 = Relay_1_500_Ohm(self, "500\u03A9 Relay 1", self.GPIO_ch1)
        self.relay1_500.setStyleSheet(GUI_Style.statusBarButton)
        self.relay1_500.pressed.connect(self.relay1_500.On_Click)
        self.relay1_500.released.connect(self.relay1_500.Un_Click)
        
        self.relay1_1k = Relay_1_1k_Ohm(self, "1k\u03A9 Relay 1", self.GPIO_ch1)
        self.relay1_1k.setStyleSheet(GUI_Style.statusBarButton)
        self.relay1_1k.pressed.connect(self.relay1_1k.On_Click)
        self.relay1_1k.released.connect(self.relay1_1k.Un_Click)
        
        self.relay2_40 = Relay_2_40_Ohm(self, "40\u03A9 Relay 2", self.GPIO_ch2)
        self.relay2_40.setStyleSheet(GUI_Style.statusBarButton)
        self.relay2_40.pressed.connect(self.relay2_40.On_Click)
        self.relay2_40.released.connect(self.relay2_40.Un_Click)
        
        self.relay2_60 = Relay_2_60_Ohm(self, "60\u03A9 Relay 2", self.GPIO_ch2)
        self.relay2_60.setStyleSheet(GUI_Style.statusBarButton)
        self.relay2_60.pressed.connect(self.relay2_60.On_Click)
        self.relay2_60.released.connect(self.relay2_60.Un_Click)
        
        self.relay2_500 = Relay_2_500_Ohm(self, "500\u03A9 Relay 2", self.GPIO_ch2)
        self.relay2_500.setStyleSheet(GUI_Style.statusBarButton)
        self.relay2_500.pressed.connect(self.relay2_500.On_Click)
        self.relay2_500.released.connect(self.relay2_500.Un_Click)
        
        self.relay2_1k = Relay_2_1k_Ohm(self, "1k\u03A9 Relay 2", self.GPIO_ch2)
        self.relay2_1k.setStyleSheet(GUI_Style.statusBarButton)
        self.relay2_1k.pressed.connect(self.relay2_1k.On_Click)
        self.relay2_1k.released.connect(self.relay2_1k.Un_Click)

        self.statusBar.addPermanentWidget(self.relay1_40, 0)
        self.statusBar.addPermanentWidget(self.relay1_60, 0)
        self.statusBar.addPermanentWidget(self.relay1_500, 0)
        self.statusBar.addPermanentWidget(self.relay1_1k, 0)
        self.statusBar.addPermanentWidget(self.relay2_40, 0)
        self.statusBar.addPermanentWidget(self.relay2_60, 0)
        self.statusBar.addPermanentWidget(self.relay2_500, 0)
        self.statusBar.addPermanentWidget(self.relay2_1k, 0)

        self.statusBar.showMessage("Starting Up... ", 4000)

    # ------------------------------------------------------------------
    # ----------- Close All Threads at app closure ---------------------
    # ------------------------------------------------------------------
    # Stop all threads when GUI is closed
    def closeEvent(self, *args, **kwargs):
      #  self.RPICaptureThread.Set_Exit_Program(True)
       # self.RPICaptureThread.wait(100)
        
        GPIO.cleanup()


# ----------------------------------------------------------------------
# -------------------- MAIN LOOP ---------------------------------------
# ----------------------------------------------------------------------
def run():
    # Run the application
    app = QApplication(sys.argv)
    # Create GUI
    GUI = Window()
    # Exit
    sys.exit(app.exec())


# Main code
if __name__ == "__main__":
    run()

