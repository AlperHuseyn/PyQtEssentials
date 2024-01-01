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

        self.pushButtonStart = QPushButton('Proceed', self)
        self.pushButtonStart.setGeometry(10, 10, 100, 100)
        self.pushButtonStart.clicked.connect(self.programAgreementHandler)

        
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
            
app = QApplication(sys.argv)

mainWindow = MainWindow()
mainWindow.show()

app.exec()
