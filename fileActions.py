"""
	fileActions Module

	The fileActions Module provides functions to set the actions to
	menu items of the file Menu. 
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from FileDisplay import FileDisplay
import alertWindow

def openAction(editor_window):
	file_path = QFileDialog.getOpenFileName(editor_window, 'Open file')[0]
	FileDisplay(file_path,editor_window)
	if file_path != "":
		editor_window.setWindowTitle(f"Text Editor  |  {file_path}")
		setStatus(editor_window,"Opened "+ file_path)
		

def newAction(editor_window):
	editor_window.text_area.setPlainText("")
	editor_window.setWindowTitle("Text Editor  |  untitled.txt")
	setStatus(editor_window,"New File Created")

def saveAction(editor_window):
	window_title = editor_window.windowTitle()
	file_content = editor_window.text_area.toPlainText()
	file_path = ""

	if window_title.find("untitled.txt") != -1 or window_title == "Text Editor *":
		try:
			file_path = QFileDialog.getSaveFileName(editor_window, 'Save File')[0]
			with open(file_path,"w") as file:
				file.write(file_content)
			editor_window.setWindowTitle(f"Text Editor  |  {file_path}")
			setStatus(editor_window,"Saved "+ file_path)

		except:
			alertWindow.createAlert(editor_window,'You have not chose any location to save the file')

	elif window_title.endswith(" *"):
		file_path = window_title[
						window_title.index("| ")+3:-2 # Start Index : End Index
					]
		with open(file_path,"w") as file:
			file.write(file_content)
		editor_window.setWindowTitle(f"Text Editor  |  {file_path}")
		setStatus(editor_window,"Saved "+ file_path)

	else:
		editor_window.setWindowTitle(f"Text Editor")
	
def saveAsAction(editor_window):
	file_content = editor_window.text_area.toPlainText()
	try:
		file_path = QFileDialog.getSaveFileName(editor_window, 'Save File')[0]
		with open(file_path,"w") as file:
			file.write(file_content)
		setStatus(editor_window,"Saved As "+ file_path)

	except:
		alertWindow.createAlert(editor_window,'You have not chose any location to save the file')

	editor_window.setWindowTitle(f"Text Editor  |  {file_path}")

def setStatus(editor_window,msg):
	"""
		Appends the given message to the status bar
	"""
	status = editor_window.statusBar.currentMessage()
	editor_window.statusBar.showMessage(status + " | " + msg)