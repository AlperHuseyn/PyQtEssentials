"""This module provides a basic GUI with start and stop buttons using PyQt5."""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QWidget):
    """
    Main window class with start and stop buttons.

    This class creates a GUI with 'Start' and 'Stop' buttons. Clicking 'Start'
    disables itself and enables the 'Stop' button. Clicking 'Stop' reverses this.
    """
    def __init__(self):
        """Initialize the main window with two buttons."""
        super().__init__()

        self.setWindowTitle('setEnable')

        self.pushButtonStart = QPushButton('Start', self)
        self.pushButtonStart.setGeometry(10, 10, 100, 100)
        self.pushButtonStart.clicked.connect(self.programStartedHandler)

        self.pushButtonStop = QPushButton('Stop', self)
        self.pushButtonStop.setGeometry(130, 10, 130, 100)
        self.pushButtonStop.setEnabled(False)
        self.pushButtonStop.clicked.connect(self.programStoppedHandler)

    def programStartedHandler(self):
        """Handle the 'Start' button click event."""
        self.pushButtonStart.setEnabled(False)
        self.pushButtonStop.setEnabled(True)
        print('Program started...')

    def programStoppedHandler(self):
        """Handle the 'Stop' button click event."""
        self.pushButtonStart.setEnabled(True)
        self.pushButtonStop.setEnabled(False)
        print('Program stopped...')

app = QApplication(sys.argv)

mainWindow = MainWindow()
mainWindow.show()

app.exec()
