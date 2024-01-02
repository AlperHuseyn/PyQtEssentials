"""This module sets up a GUI with a 'Proceed' button to accept a license agreement."""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QWidget):
    """
    This MainWindow class creates a basic user interface with a single 'Proceed' button. 
    When clicked, the button opens a message box that prompts the user to agree to the 
    license terms before proceeding.    
    """
    def __init__(self):
        """Initialize the main window."""
        super().__init__()

        self.setWindowTitle('License Agreement')
        self.resize(320, 200)

        # Setup the 'Proceed' button with geometry and event handler
        self.pushButtonStart = QPushButton('Proceed', self)
        self.pushButtonStart.setGeometry(220, 100, 100, 100)
        self.pushButtonStart.clicked.connect(self.programAgreementHandler)
        
        # Setup a checkbox for user to choose to launch the app
        self.checkBoxLaunch = QCheckBox('Launch app', self)
        self.checkBoxLaunch.move(10, 150)
        self.checkBoxLaunch.toggled.connect(self.checkBoxLaunchHandler)
        
    def programAgreementHandler(self):
        """     
        Displays a message box to the user with the license agreement information when the 
        'Proceed' button is clicked. The user can choose to agree (Ok) or abort the action.
        """
        ret = QMessageBox.information(self, 'User agreement choice', 'By clicking "Ok" you agree to the license agreement', QMessageBox.Ok|QMessageBox.Abort)
        
        if (ret == QMessageBox.Ok):
            print('User agreed.')
        else:
            print('Aborted.')
            
    def checkBoxLaunchHandler(self, checked):
        """
        Handler for the checkbox state change. Currently, this is a placeholder that can be 
        expanded to implement additional functionality when the checkbox is toggled.
        """
        pass
            
app = QApplication(sys.argv)

mainWindow = MainWindow()
mainWindow.show()

app.exec()
