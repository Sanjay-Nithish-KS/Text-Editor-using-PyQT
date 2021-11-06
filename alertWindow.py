"""
	alertWindow module

	alerWindow module provides function to show error
	message in a window.
"""


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def createAlert(editor_window,message):
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("Error")
	msg.setInformativeText(message)
	msg.setWindowTitle("Error")
	msg.setGeometry(500,500,300,300)
	msg.exec_()