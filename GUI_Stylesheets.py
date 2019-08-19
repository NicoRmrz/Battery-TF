from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot, QObject, QSize

# --------------------------------------------------------------------------------------------------------------
# --------------------------------- GUI setStylesheet Class ----------------------------------------------------
# -------------------------------------------------------------------------------------------------------------- 
class GUI_Stylesheets(QObject):
	
	 # Initializes the necessary objects into the slider class for control
    def __init__(self):
        super(GUI_Stylesheets, self).__init__()


        self.mainWindow = ("background-color: rgba(49, 51, 53, 240);")
		
        self.mainTitle =	("font: bold 35px Verdana; "
							"color: rgba(8, 139, 174, 200); "
							"background-color: rgba(18,151,147,0);"
							)
		
        self.tabs = 	("QTabWidget::pane {border-top: 1px solid white;} "
						"QTabWidget::tab-bar {left: 5px;} "
						"QTabBar::tab {background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
							"stop: 0 #E1E1E1, "
							"stop: 0.4 #DDDDDD, "
							"stop: 0.5 #D8D8D8, "
							"stop: 1.0 #D3D3D3); "
							"border: 2px solid #C4C4C3; "
							"border-bottom-color: #C2C7CB; "
							"border-top-left-radius: 4px; "
							"border-top-right-radius: 4px; "
							"min-width: 0px; "
							"padding: 2px;} "
						"QTabBar::tab:selected, "
						"QTabBar::tab:hover {background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
							"stop: 0 #fafafa, "
							"stop: 0.4 #f4f4f4, "
							"stop: 0.5 #e7e7e7, "
							"stop: 1.0 #fafafa);} "
						"QTabBar::tab:selected {border-color: #9B9B9B; "
							"border-bottom-color: #C2C7CB;} "
						"QTabBar::tab:!selected {margin-top: 2px;} "
						"QTabBar::tab:selected {margin-left: -4px; "
							"margin-right: -4px;} "
						"QTabBar::tab:first:selected {margin-left: 0;} "
						"QTabBar::tab:last:selected {margin-right: 0;} "
						"QTabBar::tab:only-one {margin: 0;}"
						)
		

		
        self.statusBarWhite = ("QStatusBar { background: #313335;"
										"color:white;} "

							"QStatusBar::item {border: 1px solid #313335; "
								"border-radius: 3px; }"
							)

							
        self.statusBar_widgets	= (	"QLabel {border: none; "
								"background-color: qlineargradient(spread:pad x1:0.45, y1:0.3695, x2:0.427, y2:0, "
								"stop:0 rgba(242, 242, 242, 0), "
								"stop:1 rgba(242,242,242, 0)); "						
								"font: 20 px; "
								"font-weight: lighter; "
								"color: white; }"			
							)

		
        self.consoleLog	=	("font: 12px Verdana; "
							"background-color: qlineargradient(spread:pad x1:0.45, y1:0.3695, x2:0.427, y2:0, "
								"stop:0 rgba(242,242,242, 0), "
								"stop:1 rgba(242,242,242, 0));"
								"color: white; "
								"border: none;"
							)

        self.commandBox = 	("font: 16px Verdana; "
                              "background-color: qlineargradient(spread:pad x1:0.45, y1:0.3695, x2:0.427, y2:0, "
                                  "stop:0 rgba(242, 242, 242, 240), "
                                  "stop:1 rgba(255,255,255,255))"
                              )

        self.sendButton = ("font: bold 12px Verdana; "
                           "background-color: qlineargradient(spread:pad x1:0.45, y1:0.3695, x2:0.427, y2:0, "
                                "stop:0 rgba(88, 139, 174, 240), "
                                "stop:1 rgba(255,255,255,255)); "
                           "border-style: outset; "
                           "border-radius: 4px; "
                           "border-width: 1px; "
                           "border-color: white; "
                           "padding: 4px"
                           )

        self.buttonPressed = ("font: bold 12px Verdana; "
							  "background-color: qlineargradient(spread:pad x1:0.45, y1:0.3695, x2:0.427, y2:0, "
							  "stop:0 rgba(213, 213, 213, 240), "
							  "stop:1 rgba(255,255,255,255)); "
							  "border-style: outset; "
							  "border-radius: 4px; "
							  "border-width: 1px; "
							  "border-color: white; "
							  "padding: 4px"
							  )

        self.startButton = 	("font: bold 12px Verdana; "
							"background-color: qlineargradient(spread:pad x1:0.45, y1:0.3695, x2:0.427, y2:0, "
								"stop:0 rgba(242, 242, 242, 0), "
								"stop:1 rgba(255,255,255,0)); "
								"border-style: outset; "
								"border-radius: 4px"
							)
        
        self.nameLabel = ("font: bold 10px Verdana; "
							"color: white; "
							"background-color: rgba(18,151,147,0);"
							)

        self.updateField = ("font: 10px Verdana; "
                            "color: black; "
                            #"border: 1px; "
                            
                              "background-color: qlineargradient(spread:pad x1:0.45, y1:0.3695, x2:0.427, y2:0, "
                                  "stop:0 rgba(242, 242, 242, 255), "
                                  "stop:1 rgba(255,255,255,255))"
                              )