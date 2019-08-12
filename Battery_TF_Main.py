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
from GUI_Buttons import Send_Command_Button

# Current version of application - Update for new builds
appVersion = "1.0"  # Update version

# Icon Image locations
Main_path = os.getcwd() + "/"

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
        #self.setWindowIcon(QIcon(Icon_Path))

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
        self.ConsoleLog()
        self.inputCommandPrompt()
        self.sendCommandButton()

        # Add title/ logo to the main title layout
        Main_Title_Layout = QHBoxLayout()
       # Main_Title_Layout.addWidget(self.Logo_btn)
        Main_Title_Layout.addWidget(self.MainTitleText, 0, Qt.AlignLeft)
        Main_Title_Layout.setSpacing(10)

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


        # Create Layout to go on Battery 1 tab
        vertical_battery1_layout = QVBoxLayout()

        # Add buttons, console log and progress bar to layout
        #vertical_battery1_layout.addWidget(self.stp_rec_btn, 0, Qt.AlignCenter)
        vertical_battery1_layout.setSpacing(30)
        vertical_battery1_layout.setContentsMargins(0, 20, 0, 0)

        # Add home vertical layout to main tab layout
        self.Battery1_Tab.setLayout(vertical_battery1_layout)

        # --------------------------------------------------------------
        # ------------- Create Battery 2 Tab Layout --------------------
        # --------------------------------------------------------------
        # Instantiate Battery 2 GUI Objects

        # Create Layout to go on Battery 2 tab
        vertical_battery2_layout = QVBoxLayout()

        # Add buttons, console log and progress bar to layout
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
    # Function to send command when a key is pressed
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
    # ------------------------------------------------------------------
    # -------------------  Create Console Log --------------------------
    # ------------------------------------------------------------------
    def ConsoleLog(self):
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

