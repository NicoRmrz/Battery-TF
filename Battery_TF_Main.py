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
        self.remainingCapaAlarmBox_1()
        self.batteryMode_1()
        self.batteryModeBox_1()
        self.averageCurrent_1()
        self.averageCurrentBox_1()

        # Create Layout to go on Battery 1 tab
        remCapAlarm_Layout1 = QHBoxLayout()
        remCapAlarm_Layout1.addWidget(self.remCapAlarm1)
        remCapAlarm_Layout1.addWidget(self.remCapAlarmBox1,0, Qt.AlignLeft)
        remCapAlarm_Layout1.setSpacing(0)
        remCapAlarm_Layout1.setContentsMargins(0, 0, 0, 0)

        # Create Layout to go on Battery 1 tab
        battMode_Layout1 = QHBoxLayout()
        battMode_Layout1.addWidget(self.battMode1)
        battMode_Layout1.addWidget(self.battModeBox1, 0 , Qt.AlignLeft)
        battMode_Layout1.setSpacing(0)
        battMode_Layout1.setContentsMargins(0, 0, 0, 0)

        # Create Layout to go on Battery 1 tab
        avgCurr_Layout1 = QHBoxLayout()
        avgCurr_Layout1.addWidget(self.avgCurr1)
        avgCurr_Layout1.addWidget(self.avgCurrBox1, 0 , Qt.AlignLeft)
        avgCurr_Layout1.setSpacing(0)
        avgCurr_Layout1.setContentsMargins(0, 0, 0, 0)

        # Create main Layout to go on Battery 1 tab
        vertical_battery1_layout = QVBoxLayout()
        vertical_battery1_layout.addLayout(remCapAlarm_Layout1)
        vertical_battery1_layout.addLayout(battMode_Layout1)
        vertical_battery1_layout.addLayout(avgCurr_Layout1)
        vertical_battery1_layout.setSpacing(10)
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
        self.remCapAlarm1 = QLabel(self)
        self.remCapAlarm1.setText("Remaining Capacity Alarm")
        self.remCapAlarm1.setStyleSheet(GUI_Style.nameLabel)
   
    def remainingCapaAlarmBox_1(self):
        self.remCapAlarmBox1 = QLineEdit(self)
        self.remCapAlarmBox1.setStyleSheet(GUI_Style.updateField)
        self.remCapAlarmBox1.setMaximumWidth(50)

    def batteryMode_1(self):
        self.battMode1 = QLabel(self)
        self.battMode1.setText("Battery Mode")
        self.battMode1.setStyleSheet(GUI_Style.nameLabel)
   
    def batteryModeBox_1(self):
        self.battModeBox1 = QLineEdit(self)
        self.battModeBox1.setStyleSheet(GUI_Style.updateField)
        self.battModeBox1.setMaximumWidth(50)

    def averageCurrent_1(self):
        self.avgCurr1 = QLabel(self)
        self.avgCurr1.setText("Average Current")
        self.avgCurr1.setStyleSheet(GUI_Style.nameLabel)
   
    def averageCurrentBox_1(self):
        self.avgCurrBox1 = QLineEdit(self)
        self.avgCurrBox1.setStyleSheet(GUI_Style.updateField)
        self.avgCurrBox1.setMaximumWidth(50)

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

