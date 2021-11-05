import re
from PyQt5.QtGui import *

class FileDisplay():
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
		file_content = open(file_path).read()
		self.editor_window.text_area.setPlainText(file_content)

	def displayImageFile(self,file_path):
		self.editor_window.text_area.setPlainText("")
		document = self.editor_window.text_area.document()
		cursor = QTextCursor(document)
		position = cursor.position()
		cursor.insertImage(file_path)
