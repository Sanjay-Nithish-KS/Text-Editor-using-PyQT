from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def add_text_area(editor_window):
	menu_bar_height = editor_window.menuBar().height()
	text_editor_width = editor_window.width()
	text_editor_height = editor_window.height()

	editor_window.text_area = QTextEdit(editor_window)
	editor_window.text_area.setAutoFormatting(QTextEdit.AutoAll)
	editor_window.text_area.setGeometry(
		 0, 
		 menu_bar_height,
	     text_editor_width,
	     text_editor_width - menu_bar_height
    )
	return editor_window.text_area
