import datetime
import os
import time
import sys
import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QCheckBox, QTextEdit, QStatusBar, \
    QProgressBar, QSizePolicy, QAbstractItemView, QWidget, QTabWidget, QHBoxLayout, QVBoxLayout, QSlider
from PyQt5.QtGui import QPixmap, QIcon, QFont, QTextCursor, QPalette, QImage, QBrush, QImage
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot, QObject, QSize

# imports from user made files
from GUI_Stylesheets import GUI_Stylesheets
from GUI_Buttons import Send_Command_Button, Logo_Button

# Current version of application - Update for new builds
appVersion = "1.0"  # Update version

# Icon Image locations
Main_path = os.getcwd() + "/"
Icon_Path = Main_path + "/Logo/logo.png"

# Instantiate style sheets for GUI Objects
GUI_Style = GUI_Stylesheets()

# --------------------------------------------------------------------------------------------------------------
# --------------------------------- Main Window Class ----------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
class Window(QMainWindow):

    # Initialization of the GUI
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 900, 600)
        self.setWindowTitle("Battery TF v" + appVersion)
        self.setStyleSheet(GUI_Style.mainWindow)
        self.setMinimumSize(900, 600)
        self.setWindowIcon(QIcon(Icon_Path))

        # --------------------------------------------------------------
        # -------------------- Initialize  -----------------------------
        # --------------------------------------------------------------


        # --------------------------------------------------------------
        # ---------------- Instantiate All Threads  --------------------
        # --------------------------------------------------------------


        # --------------------------------------------------------------
        # ---------------- Start All Threads ---------------------------
        # --------------------------------------------------------------


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
        Main_Title_Layout.setContentsMargins(0, 0, 350, 0)

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
  
        # Create main Layout to go on Battery 1 tab
        vertical_battery1_layout = QVBoxLayout()
        vertical_battery1_layout.addLayout(self.remCapAlarm_Layout1)
        vertical_battery1_layout.addLayout(self.battMode_Layout1)
        vertical_battery1_layout.addLayout(self.voltage_Layout1)
        vertical_battery1_layout.addLayout(self.current_Layout1)
        vertical_battery1_layout.addLayout(self.avgCurr_Layout1)
        vertical_battery1_layout.addLayout(self.relStateCharge_Layout1)
        vertical_battery1_layout.addLayout(self.absStateCharge_Layout1)
        vertical_battery1_layout.addLayout(self.remCap_Layout1)
        vertical_battery1_layout.addLayout(self.fullCharge_Layout1)
        vertical_battery1_layout.addLayout(self.runTimeToEmpty_Layout1)
        vertical_battery1_layout.addLayout(self.avgTimeToEmpty_Layout1)
        vertical_battery1_layout.addLayout(self.avgTimeToFull_Layout1)
        vertical_battery1_layout.addLayout(self.charging_Current_Layout1)
        vertical_battery1_layout.addLayout(self.charging_Voltag_Layout1)
        vertical_battery1_layout.setSpacing(0)
        vertical_battery1_layout.setContentsMargins(0, 0, 0, 0)

        # Add home vertical layout to main tab layout
        self.Battery1_Tab.setLayout(vertical_battery1_layout)

        # --------------------------------------------------------------
        # ------------- Create Battery 2 Tab Layout --------------------
        # --------------------------------------------------------------
        # Instantiate Battery 2 GUI Objects



        # Create Layout to go on Battery 2 tab
        vertical_battery2_layout = QVBoxLayout()
        vertical_battery2_layout.setSpacing(30)
        vertical_battery2_layout.setContentsMargins(0, 20, 0, 0)

        # Add home vertical layout to main tab layout
        self.Battery2_Tab.setLayout(vertical_battery2_layout)

        # --------------------------------------------------------------
        # ------------ Add Final Layout to Main Window -----------------
        # --------------------------------------------------------------
        # Set Main window layout to GUI central Widget
        self.centralWidget().setLayout(Full_Window_layout)
        self.centralWidget().isWindow()

        # Display GUI Objects
        self.show()
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
        self.Logo_btn.setIconSize(QSize(80, 80))
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
        self.MyTabs.setMaximumWidth(400)

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
   
        # create input box
        self.remCapAlarmBox1 = QLineEdit(self)
        self.remCapAlarmBox1.setStyleSheet(GUI_Style.updateField)
        self.remCapAlarmBox1.setMaximumWidth(50)

        # create layout
        self.remCapAlarm_Layout1 = QHBoxLayout()
        self.remCapAlarm_Layout1.addWidget(self.remCapAlarm1)
        self.remCapAlarm_Layout1.addWidget(self.remCapAlarmBox1,0, Qt.AlignLeft)

    def batteryMode_1(self):
         # create label
        self.battMode1 = QLabel(self)
        self.battMode1.setText("Battery Mode")
        self.battMode1.setStyleSheet(GUI_Style.nameLabel)
        
        # create input box
        self.battModeBox1 = QLineEdit(self)
        self.battModeBox1.setStyleSheet(GUI_Style.updateField)
        self.battModeBox1.setMaximumWidth(50)

        # create layout
        self.battMode_Layout1 = QHBoxLayout()
        self.battMode_Layout1.addWidget(self.battMode1)
        self.battMode_Layout1.addWidget(self.battModeBox1, 0 , Qt.AlignLeft)

    def voltage_1(self):
         # create label
        self.voltage1 = QLabel(self)
        self.voltage1.setText("Voltage")
        self.voltage1.setStyleSheet(GUI_Style.nameLabel)
        
        # create input box
        self.voltageBox1 = QLineEdit(self)
        self.voltageBox1.setStyleSheet(GUI_Style.updateField)
        self.voltageBox1.setMaximumWidth(50)

        # create layout
        self.voltage_Layout1 = QHBoxLayout()
        self.voltage_Layout1.addWidget(self.voltage1)
        self.voltage_Layout1.addWidget(self.voltageBox1, 0 , Qt.AlignLeft)

    def current_1(self):
        # create label
        self.current1 = QLabel(self)
        self.current1.setText("Current")
        self.current1.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.currentBox1 = QLineEdit(self)
        self.currentBox1.setStyleSheet(GUI_Style.updateField)
        self.currentBox1.setMaximumWidth(50)

        # create layout
        self.current_Layout1 = QHBoxLayout()
        self.current_Layout1.addWidget(self.current1)
        self.current_Layout1.addWidget(self.currentBox1, 0 , Qt.AlignLeft)

    def averageCurrent_1(self):
        # create label
        self.avgCurr1 = QLabel(self)
        self.avgCurr1.setText("Average Current")
        self.avgCurr1.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.avgCurrBox1 = QLineEdit(self)
        self.avgCurrBox1.setStyleSheet(GUI_Style.updateField)
        self.avgCurrBox1.setMaximumWidth(50)

        # create layout
        self.avgCurr_Layout1 = QHBoxLayout()
        self.avgCurr_Layout1.addWidget(self.avgCurr1)
        self.avgCurr_Layout1.addWidget(self.avgCurrBox1, 0 , Qt.AlignLeft)

    def relativeStatOfCharge_1(self):
        # create label
        self.relStateCharge1 = QLabel(self)
        self.relStateCharge1.setText("Relative State Of Charge")
        self.relStateCharge1.setStyleSheet(GUI_Style.nameLabel)
       
       # create input box
        self.relStateChargeBox1 = QLineEdit(self)
        self.relStateChargeBox1.setStyleSheet(GUI_Style.updateField)
        self.relStateChargeBox1.setMaximumWidth(50)

        # create layout
        self.relStateCharge_Layout1 = QHBoxLayout()
        self.relStateCharge_Layout1.addWidget(self.relStateCharge1)
        self.relStateCharge_Layout1.addWidget(self.relStateChargeBox1, 0 , Qt.AlignLeft)

    def absoluteStatOfCharge_1(self):
        # create label
        self.absStateCharge1 = QLabel(self)
        self.absStateCharge1.setText("Absolute State Of Charge")
        self.absStateCharge1.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.absStateChargeBox1 = QLineEdit(self)
        self.absStateChargeBox1.setStyleSheet(GUI_Style.updateField)
        self.absStateChargeBox1.setMaximumWidth(50)

        # create layout
        self.absStateCharge_Layout1 = QHBoxLayout()
        self.absStateCharge_Layout1.addWidget(self.absStateCharge1)
        self.absStateCharge_Layout1.addWidget(self.absStateChargeBox1, 0 , Qt.AlignLeft)

    def remainingCapacity_1(self):
        # create label
        self.remainingCapacity1 = QLabel(self)
        self.remainingCapacity1.setText("Remaining Capacity")
        self.remainingCapacity1.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.remainingCapacityBox1 = QLineEdit(self)
        self.remainingCapacityBox1.setStyleSheet(GUI_Style.updateField)
        self.remainingCapacityBox1.setMaximumWidth(50)

        # create layout
        self.remCap_Layout1 = QHBoxLayout()
        self.remCap_Layout1.addWidget(self.remainingCapacity1)
        self.remCap_Layout1.addWidget(self.remainingCapacityBox1, 0 , Qt.AlignLeft)

    def fullChargeCapacity_1(self):
        # create label
        self.fullChargeCapacity1 = QLabel(self)
        self.fullChargeCapacity1.setText("Full Charge Capacity")
        self.fullChargeCapacity1.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.fullChargeCapacityBox1 = QLineEdit(self)
        self.fullChargeCapacityBox1.setStyleSheet(GUI_Style.updateField)
        self.fullChargeCapacityBox1.setMaximumWidth(50)

        # create layout
        self.fullCharge_Layout1 = QHBoxLayout()
        self.fullCharge_Layout1.addWidget(self.fullChargeCapacity1)
        self.fullCharge_Layout1.addWidget(self.fullChargeCapacityBox1, 0 , Qt.AlignLeft)

    def runTimeToEmpty_1(self):
        # create label
        self.runTimeToEmpty1 = QLabel(self)
        self.runTimeToEmpty1.setText("Run Time To Empty")
        self.runTimeToEmpty1.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.runTimeToEmptyBox1 = QLineEdit(self)
        self.runTimeToEmptyBox1.setStyleSheet(GUI_Style.updateField)
        self.runTimeToEmptyBox1.setMaximumWidth(50)

        # create layout
        self.runTimeToEmpty_Layout1 = QHBoxLayout()
        self.runTimeToEmpty_Layout1.addWidget(self.runTimeToEmpty1)
        self.runTimeToEmpty_Layout1.addWidget(self.runTimeToEmptyBox1, 0 , Qt.AlignLeft)

    def averageTimeToEmpty_1(self):
        # create label
        self.avgTimeToEmpty1 = QLabel(self)
        self.avgTimeToEmpty1.setText("Average Time To Empty")
        self.avgTimeToEmpty1.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.avgTimeToEmptyBox1 = QLineEdit(self)
        self.avgTimeToEmptyBox1.setStyleSheet(GUI_Style.updateField)
        self.avgTimeToEmptyBox1.setMaximumWidth(50)

        # create layout
        self.avgTimeToEmpty_Layout1 = QHBoxLayout()
        self.avgTimeToEmpty_Layout1.addWidget(self.avgTimeToEmpty1)
        self.avgTimeToEmpty_Layout1.addWidget(self.avgTimeToEmptyBox1, 0 , Qt.AlignLeft)

    def averageTimeToFull_1(self):
        # create label
        self.avgTimeToFull1 = QLabel(self)
        self.avgTimeToFull1.setText("Average Time To Full")
        self.avgTimeToFull1.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.avgTimeToFullBox1 = QLineEdit(self)
        self.avgTimeToFullBox1.setStyleSheet(GUI_Style.updateField)
        self.avgTimeToFullBox1.setMaximumWidth(50)

        # create layout
        self.avgTimeToFull_Layout1 = QHBoxLayout()
        self.avgTimeToFull_Layout1.addWidget(self.avgTimeToFull1)
        self.avgTimeToFull_Layout1.addWidget(self.avgTimeToFullBox1, 0 , Qt.AlignLeft)     
        
    def chargingCurrent_1(self):
        # create label
        self.chargingCurrent1 = QLabel(self)
        self.chargingCurrent1.setText("Charging Current")
        self.chargingCurrent1.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.chargingCurrentBox1 = QLineEdit(self)
        self.chargingCurrentBox1.setStyleSheet(GUI_Style.updateField)
        self.chargingCurrentBox1.setMaximumWidth(50)

        # create layout
        self.charging_Current_Layout1 = QHBoxLayout()
        self.charging_Current_Layout1.addWidget(self.chargingCurrent1)
        self.charging_Current_Layout1.addWidget(self.chargingCurrentBox1, 0 , Qt.AlignLeft)          

    def chargingVoltage_1(self):
        # create label
        self.chargingVoltage1 = QLabel(self)
        self.chargingVoltage1.setText("Charging Voltage")
        self.chargingVoltage1.setStyleSheet(GUI_Style.nameLabel)
   
        # create input box
        self.chargingVoltageBox1 = QLineEdit(self)
        self.chargingVoltageBox1.setStyleSheet(GUI_Style.updateField)
        self.chargingVoltageBox1.setMaximumWidth(50)

        # create layout
        self.charging_Voltag_Layout1 = QHBoxLayout()
        self.charging_Voltag_Layout1.addWidget(self.chargingVoltage1)
        self.charging_Voltag_Layout1.addWidget(self.chargingVoltageBox1, 0 , Qt.AlignLeft)

    # ------------------------------------------------------------------
    # ----------- Create Battery 2 Tab GUI Objects  --------------------
    # ------------------------------------------------------------------


    # ------------------------------------------------------------------
    # ---------------- Create Status Bar Widgets -----------------------
    # ------------------------------------------------------------------
    def StatusBar(self):
        self.statusBar = QStatusBar()
        self.statusBar.setStyleSheet(GUI_Style.statusBarWhite)

        self.batt1 = QLabel()
        self.batt1.setMinimumSize(50, 12)
        self.batt1.setStyleSheet(GUI_Style.statusBar_widgets)
        self.batt1.setText("| Battery 1")
        self.batt1.setAlignment(Qt.AlignCenter)

        self.batt2 = QLabel()
        self.batt2.setMinimumSize(50, 12)
        self.batt2.setStyleSheet(GUI_Style.statusBar_widgets)
        self.batt2.setText("| Battery 2")
        self.batt2.setAlignment(Qt.AlignCenter)

        self.statusBar.addPermanentWidget(self.batt1, 0)
        self.statusBar.addPermanentWidget(self.batt2, 0)

        self.statusBar.showMessage("Starting Up... ", 4000)

    # ------------------------------------------------------------------
    # ----------- Close All Threads at app closure ---------------------
    # ------------------------------------------------------------------
    # Stop all threads when GUI is closed
    def closeEvent(self, *args, **kwargs):
      #  self.RPICaptureThread.Set_Exit_Program(True)
       # self.RPICaptureThread.wait(100)
        pass

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

