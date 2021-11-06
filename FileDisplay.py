"""
	FileDisplay Class

	The Class FileDisplay is used to display the file content in the 
	text editor's text area.
	The FileDisplay class can display both text files and image files.

	Usage:
		import FileDisplay
		FileDisplay.FileDisplay(file_path,TextEditor object)

"""


import re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import alertWindow

class FileDisplay:
	def __init__(self,file_path,editor_window):
		self.file_path = file_path
		self.editor_window = editor_window

		regex = "([^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$)"
		p = re.compile(regex)
		
		if re.search(p,file_path):
			self.displayImageFile(file_path)
		else:
			self.displayTextFile(file_path)

	def displayTextFile(self,file_path):
		"""
			displayTextFile displays text files in the text editor's 
			text area.
		"""
		try:
			file_content = open(file_path).read()
			self.editor_window.text_area.setPlainText(file_content)
		except:
			alertWindow.createAlert(alertWindow,'You have not chose any file to open')

	def displayImageFile(self,file_path):
		"""
			displayTextFile displays Image files in the text editor's 
			text area.
		"""
		self.editor_window.text_area.setPlainText("")
		document = self.editor_window.text_area.document()
		cursor = QTextCursor(document)
		position = cursor.position()
		cursor.insertImage(file_path)
