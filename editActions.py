"""
	editActions Module

	The editActions Module provides functions to set the actions to
	menu items of the edit Menu. 
	
"""


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def copyAction(editor_window):
	editor_window.text_area.copy()
	setStatus(editor_window,"Copied the Selected Text")

def pasteAction(editor_window):
	editor_window.text_area.paste()
	setStatus(editor_window,"Pasted the Text")

def cutAction(editor_window):
	editor_window.text_area.cut()
	setStatus(editor_window,"Selected Text has been Cut")

def undoAction(editor_window):
	editor_window.text_area.undo()
	setStatus(editor_window,"Undo operation carried out")

def redoAction(editor_window):
	editor_window.text_area.redo()
	setStatus(editor_window,"Redo operation carried out")

def selectAllAction(editor_window):
	editor_window.text_area.selectAll()
	setStatus(editor_window,"Selected All the Text ")

def setStatus(editor_window,msg):
	"""
		Appends the given message to the status bar
	"""
	status = editor_window.statusBar.currentMessage()
	editor_window.statusBar.showMessage(status + " | " + msg)