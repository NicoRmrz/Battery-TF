from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot, QObject, QSize

# Imports from made files
from GUI_Stylesheets import GUI_Stylesheets

GUI_Style = GUI_Stylesheets()
# --------------------------------------------------------------------------------------------------------------
# --------------------------------- Button handlers Class ----------------------------------------------------
# -------------------------------------------------------------------------------------------------------------- 
class handlers(QObject):
	
	 # Initializes the necessary objects into the slider class for control
    def __init__(self, relay1_40, relay1_60, relay1_500, relay1_1k, relay2_40, relay2_60, relay2_500, relay2_1k, 
            GPIO_ch1, GPIO_ch2):
        super(handlers, self).__init__()
        self.relay1_40 = relay1_40
        self.relay1_60 = relay1_60
        self.relay1_500 = relay1_500
        self.relay1_1k = relay1_1k
        self.relay2_40 = relay2_40
        self.relay2_60 = relay2_60
        self.relay2_500 = relay2_500
        self.relay2_1k = relay2_1k
        self.GPIO_ch1 = GPIO_ch1
        self.GPIO_ch2 = GPIO_ch2
		
    def ch1Buttons(self, sel): 
        if sel == "40H":
            self.relay1_40.setStyleSheet(GUI_Style.statusBarButton)
        elif sel == "40L":
            self.relay1_40.setStyleSheet(GUI_Style.buttonPressed)
        elif sel == "60H":
            self.relay1_60.setStyleSheet(GUI_Style.statusBarButton)
        elif sel == "60L":
            self.relay1_60.setStyleSheet(GUI_Style.buttonPressed)
        elif sel == "500H":
            self.relay1_500.setStyleSheet(GUI_Style.statusBarButton)
        elif sel == "500L":
            self.relay1_500.setStyleSheet(GUI_Style.buttonPressed)
        elif sel == "1kH":
            self.relay1_1k.setStyleSheet(GUI_Style.statusBarButton)		
        elif sel == "1kL":
            self.relay1_1k.setStyleSheet(GUI_Style.buttonPressed)		
            
    def ch2Buttons(self, sel): 
        if sel == "40H":
            self.relay2_40.setStyleSheet(GUI_Style.statusBarButton)
        elif sel == "40L":
            self.relay2_40.setStyleSheet(GUI_Style.buttonPressed)
        elif sel == "60H":
            self.relay2_60.setStyleSheet(GUI_Style.statusBarButton)
        elif sel == "60L":
            self.relay2_60.setStyleSheet(GUI_Style.buttonPressed)
        elif sel == "500H":
            self.relay2_500.setStyleSheet(GUI_Style.statusBarButton)
        elif sel == "500L":
            self.relay2_500.setStyleSheet(GUI_Style.buttonPressed)
        elif sel == "1kH":
            self.relay2_1k.setStyleSheet(GUI_Style.statusBarButton)		
        elif sel == "1kL":
            self.relay2_1k.setStyleSheet(GUI_Style.buttonPressed)		

