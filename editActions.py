from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def copyAction(editor_window):
	editor_window.text_area.copy()

def pasteAction(editor_window):
	editor_window.text_area.paste()

def cutAction(editor_window):
	editor_window.text_area.cut()

def undoAction(editor_window):
	editor_window.text_area.undo()

def redoAction(editor_window):
	editor_window.text_area.redo()

def selectAllAction(editor_window):
	editor_window.text_area.selectAll()
