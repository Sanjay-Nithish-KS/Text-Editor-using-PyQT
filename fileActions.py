from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from FileDisplay import FileDisplay

def openAction(editor_window):
	try:
		file_path = QFileDialog.getOpenFileName(editor_window, 'Open file')[0]
		FileDisplay(file_path,editor_window)
		editor_window.setWindowTitle(f"Text Editor  |  {file_path}")
	except:
		print("")

def newAction(editor_window):
	editor_window.text_area.setPlainText("")
	editor_window.setWindowTitle("Text Editor  |  untitled.txt")

def saveAction(editor_window):
	window_title = editor_window.windowTitle()
	file_content = editor_window.text_area.toPlainText()
	file_path = ""

	if window_title.find("untitled.txt") != -1 or window_title == "Text Editor *":
		try:
			file_path = QFileDialog.getSaveFileName(editor_window, 'Save File')[0]
			with open(file_path,"w") as file:
				file.write(file_content)
		except:
			print("")

	elif window_title.endswith(" *"):
		file_path = window_title[
						window_title.index("| ")+3:-2 # Start Index : End Index
					]
		with open(file_path,"w") as file:
			file.write(file_content)

	else:
		file_path = window.windowTitle()

	editor_window.setWindowTitle(f"Text Editor  |  {file_path}")
	
def saveAsAction(editor_window):
	file_content = editor_window.text_area.toPlainText()
	try:
		file_path = QFileDialog.getSaveFileName(editor_window, 'Save File')[0]
		with open(file_path,"w") as file:
			file.write(file_content)
	except:
		print("")
	editor_window.setWindowTitle(f"Text Editor  |  {file_path}")