from time import sleep
import os
import time
from time import sleep
import sys

# Import GUI
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QCheckBox, QLineEdit, QLabel, QCheckBox, QTextEdit, \
    QProgressBar, QAbstractScrollArea, QAbstractSlider, QScrollBar, QComboBox, QFrame
from PyQt5.QtGui import QPixmap, QIcon, QFont, QPalette, QImage, QBrush, QTextCursor, QTextOption
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot, QObject, QSize

# Imports from made files
from GUI_Stylesheets import GUI_Stylesheets

GUI_Style = GUI_Stylesheets()

# --------------------------------------------------------------------------------------------------------------
# --------------------------------- Send QPushButton Class -----------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
class Send_Command_Button(QPushButton):
    sendCommand = None
    console_log = None
    log = None
    final_Str = None

    # Initializes the necessary objects into the button class for control
    def __init__(self, window, text, consoleLog, inputCommand):
        super(Send_Command_Button, self).__init__()
        self.setText(text)
        self.setParent(window)
        self.console_log = consoleLog
        self.sendCommand = inputCommand

    # Function call for the click event
    def On_Click(self):
        # Button turns grey
        self.setStyleSheet(GUI_Style.buttonPressed)

    # Function call for the Un_click event
    def Un_Click(self):
        self.writeToConsoleLog(self.sendCommand.text())
        self.sendCommand.setText("")
        self.Reset_GUI()

    def writeToConsoleLog(self, input_textbox):
        old_text = self.console_log.toPlainText()
        full_text = old_text + '\n' + input_textbox
        self.console_log.setText(full_text)  # write ESG feedback to ESG window
        self.console_log.setWordWrapMode(QTextOption.WordWrap)
        self.console_log.moveCursor(QTextCursor.End)

    # Resets the necessary objects when the test is reran
    def Reset_GUI(self):
        # Change button back to normal
        self.setStyleSheet(GUI_Style.sendButton)
# --------------------------------------------------------------------------------------------------------------
# --------------------------------- Secret/ Logo QPushButton Class ---------------------------------------------
# --------------------------------------------------------------------------------------------------------------
class Logo_Button(QPushButton):     
    old_window = None
    new_window = None
    NIGHT_MODE = False

    # Initializes the necessary objects into the button class for control
    def __init__(self, window, text, consoleLog):
        super(Logo_Button, self).__init__()
        self.setText(text)
        self.setParent(window)
        self.mainWindow = window
        self.LargeTextBox = consoleLog

    # Function call for the click event
    def On_Click(self):
        pass

    # Function call for the Un_click event
    def Un_Click(self):
        if self.NIGHT_MODE != True:
            self.Night_Mode()
            self.NIGHT_MODE = True

        elif self.NIGHT_MODE != False:
            self.Regular_Mode()
            self.NIGHT_MODE = False
            
    # Night Mode
    def Night_Mode(self):
        pass
        
    # Regular Mode
    def Regular_Mode(self):
        pass
        
     # Function call to write to Console Log
    def WriteToConsole(self, new_input):
        self.old_window = self.large_textbox.toPlainText()
        self.new_window = self.old_window + '\n' + new_input
        self.large_textbox.setText(self.new_window)
        self.large_textbox.moveCursor(QTextCursor.End)
# --------------------------------------------------------------------------------------------------------------
# --------------------------------- 40 Ohm Relay 1 QPushButton Class -------------------------------------------
# --------------------------------------------------------------------------------------------------------------
class Relay_1_40_Ohm(QPushButton):     

    # Initializes the necessary objects into the button class for control
    def __init__(self, window, text, gpioThread):
        super(Relay_1_40_Ohm, self).__init__()
        self.setText(text)
        self.setParent(window)
        self.mainWindow = window
        self.gpioThread = gpioThread

    # Function call for the click event
    def On_Click(self):
        self.setStyleSheet(GUI_Style.buttonPressed)

    # Function call for the Un_click event
    def Un_Click(self):
        self.gpioThread.Set_40Ohm(True)
# --------------------------------------------------------------------------------------------------------------
# --------------------------------- 60 Ohm Relay 1 QPushButton Class -------------------------------------------
# --------------------------------------------------------------------------------------------------------------
class Relay_1_60_Ohm(QPushButton):     

    # Initializes the necessary objects into the button class for control
    def __init__(self, window, text, gpioThread):
        super(Relay_1_60_Ohm, self).__init__()
        self.setText(text)
        self.setParent(window)
        self.mainWindow = window
        self.gpioThread = gpioThread

    # Function call for the click event
    def On_Click(self):
        self.setStyleSheet(GUI_Style.buttonPressed)

    # Function call for the Un_click event
    def Un_Click(self):
        self.gpioThread.Set_60Ohm(True)
# --------------------------------------------------------------------------------------------------------------
# --------------------------------- 500 Ohm Relay 1 QPushButton Class ------------------------------------------
# --------------------------------------------------------------------------------------------------------------
class Relay_1_500_Ohm(QPushButton):     

    # Initializes the necessary objects into the button class for control
    def __init__(self, window, text, gpioThread):
        super(Relay_1_500_Ohm, self).__init__()
        self.setText(text)
        self.setParent(window)
        self.mainWindow = window
        self.gpioThread = gpioThread

    # Function call for the click event
    def On_Click(self):
        self.setStyleSheet(GUI_Style.buttonPressed)

    # Function call for the Un_click event
    def Un_Click(self):
        self.gpioThread.Set_500Ohm(True)
# --------------------------------------------------------------------------------------------------------------
# --------------------------------- 1k Ohm Relay 1 QPushButton Class -------------------------------------------
# --------------------------------------------------------------------------------------------------------------
class Relay_1_1k_Ohm(QPushButton):     

    # Initializes the necessary objects into the button class for control
    def __init__(self, window, text, gpioThread):
        super(Relay_1_1k_Ohm, self).__init__()
        self.setText(text)
        self.setParent(window)
        self.mainWindow = window
        self.gpioThread = gpioThread

    # Function call for the click event
    def On_Click(self):
        self.setStyleSheet(GUI_Style.buttonPressed)

    # Function call for the Un_click event
    def Un_Click(self):
        self.gpioThread.Set_1kOhm(True)
        self.Reset_GUI()
            
    # Resets the necessary objects when the test is reran
    def Reset_GUI(self):
        # Change button back to normal
        self.setStyleSheet(GUI_Style.statusBarButton)
# --------------------------------------------------------------------------------------------------------------
# --------------------------------- 40 Ohm Relay 2 QPushButton Class -------------------------------------------
# --------------------------------------------------------------------------------------------------------------
class Relay_2_40_Ohm(QPushButton):     

    # Initializes the necessary objects into the button class for control
    def __init__(self, window, text, gpioThread):
        super(Relay_2_40_Ohm, self).__init__()
        self.setText(text)
        self.setParent(window)
        self.mainWindow = window
        self.gpioThread = gpioThread

    # Function call for the click event
    def On_Click(self):
        self.setStyleSheet(GUI_Style.buttonPressed)

    # Function call for the Un_click event
    def Un_Click(self):
        self.gpioThread.Set_40Ohm(True)
# --------------------------------------------------------------------------------------------------------------
# --------------------------------- 60 Ohm Relay 2 QPushButton Class -------------------------------------------
# --------------------------------------------------------------------------------------------------------------
class Relay_2_60_Ohm(QPushButton):     

    # Initializes the necessary objects into the button class for control
    def __init__(self, window, text, gpioThread):
        super(Relay_2_60_Ohm, self).__init__()
        self.setText(text)
        self.setParent(window)
        self.mainWindow = window
        self.gpioThread = gpioThread

    # Function call for the click event
    def On_Click(self):
        self.setStyleSheet(GUI_Style.buttonPressed)

    # Function call for the Un_click event
    def Un_Click(self):
        self.gpioThread.Set_60Ohm(True)
            
    # Resets the necessary objects when the test is reran
    def Reset_GUI(self):
        # Change button back to normal
        self.setStyleSheet(GUI_Style.statusBarButton)
# --------------------------------------------------------------------------------------------------------------
# --------------------------------- 500 Ohm Relay 2 QPushButton Class ------------------------------------------
# --------------------------------------------------------------------------------------------------------------
class Relay_2_500_Ohm(QPushButton):     

    # Initializes the necessary objects into the button class for control
    def __init__(self, window, text, gpioThread):
        super(Relay_2_500_Ohm, self).__init__()
        self.setText(text)
        self.setParent(window)
        self.mainWindow = window
        self.gpioThread = gpioThread

    # Function call for the click event
    def On_Click(self):
        self.setStyleSheet(GUI_Style.buttonPressed)

    # Function call for the Un_click event
    def Un_Click(self):
        self.gpioThread.Set_500Ohm(True)
# --------------------------------------------------------------------------------------------------------------
# --------------------------------- 1k Ohm Relay 2 QPushButton Class -------------------------------------------
# --------------------------------------------------------------------------------------------------------------
class Relay_2_1k_Ohm(QPushButton):     

    # Initializes the necessary objects into the button class for control
    def __init__(self, window, text, gpioThread):
        super(Relay_2_1k_Ohm, self).__init__()
        self.setText(text)
        self.setParent(window)
        self.mainWindow = window
        self.gpioThread =gpioThread

    # Function call for the click event
    def On_Click(self):
        self.setStyleSheet(GUI_Style.buttonPressed)

    # Function call for the Un_click event
    def Un_Click(self):
        self.gpioThread.Set_1kOhm(True)

        
