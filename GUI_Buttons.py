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

