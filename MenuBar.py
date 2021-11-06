"""
	MenuBar Module

	MenuBar Module provides functions to create a menubar and add actions to the
	menu items.

	Usage:
		
		import MenuBar
		menu_bar = MenuBar.add_menu(TextEditor object)

"""


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import fileActions
from editActions import *
from FindReplaceWindow import FindReplaceWindow

def add_menu(editor_window):
	"""
  	Add Menu to the Text Editor Window
  	"""
  	# File Menu
	menu_bar = editor_window.menuBar()
	file = menu_bar.addMenu("&File")
	# New Menu
	new = file.addAction("&New")
	new.setShortcut("Ctrl+N")
	editor_window.new = new
	# Open Menu
	mopen = file.addAction("&Open")
	mopen.setShortcut("Ctrl+O")
	editor_window.mopen = mopen
	# Save Menu
	save = QAction("&Save",editor_window)
	save.setShortcut("Ctrl+S")
	file.addAction(save)
	editor_window.save = save
	# Save as Menu
	save_as = QAction("&Save as",editor_window)
	save_as.setShortcut("Ctrl+Shift+S")
	file.addAction(save_as)
	# Quit Menu
	quit = QAction("Quit",editor_window) 
	file.addAction(quit)

	# Edit Menu 
	edit = menu_bar.addMenu("&Edit")
	# Copy
	copy = edit.addAction("&Copy")
	copy.setShortcut("Ctrl+C")
	editor_window.copy = copy
	# Cut
	cut = edit.addAction("&Cut")
	cut.setShortcut("Ctrl+X")
	editor_window.cut = cut
	# Paste
	paste = edit.addAction("&Paste")
	paste.setShortcut("Ctrl+V")
	editor_window.paste = paste
	# Undo
	undo = edit.addAction("&Undo")
	undo.setShortcut("Ctrl+Z")
	editor_window.undo = undo
	# Redo
	redo = edit.addAction("&Redo")
	redo.setShortcut("Ctrl+Y")
	editor_window.redo = redo
	# Select All
	redo = edit.addAction("&Select All")
	redo.setShortcut("Ctrl+A")

	# Find Menu
	find_menu = menu_bar.addMenu("&Find")
	# Copy
	find = find_menu.addAction("&Find")
	find.setShortcut("Ctrl+F")
	# Cut
	replace = find_menu.addAction("&Replace")
	replace.setShortcut("Ctrl+H")

	file.triggered[QAction].connect(editor_window.fileAction)
	edit.triggered[QAction].connect(editor_window.editAction)
	find_menu.triggered[QAction].connect(editor_window.findAction)

	return menu_bar

def fileAction(editor_window,action):
	"""
		Adds actions to the menu items of file menu
	"""
	if action.text() == "&Open":
		fileActions.openAction(editor_window)

	elif action.text() == "&New":
		fileActions.newAction(editor_window)
		
	elif action.text() == "&Save as":
		fileActions.saveAsAction(editor_window)

	elif action.text() == "&Save":
		fileActions.saveAction(editor_window)

	elif action.text() == "&Quit":
		sys.exit()

	else:
		print(action.text)

def editAction(editor_window,action):
	"""
		Adds actions to the menu items of edit menu
	"""
	if action.text() == "&Copy":
		copyAction(editor_window)

	elif action.text() == "&Paste":
		pasteAction(editor_window)

	elif action.text() == "&Cut":
		cutAction(editor_window)

	elif action.text() == "&Undo":
		undoAction(editor_window)

	elif action.text() == "&Redo":
		redoAction(editor_window)
	
	elif action.text() == "&Select All":
		selectAllAction(editor_window)

def findAction(editor_window,action):
	"""
		Adds actions to the menu items of find menu
	"""
	if action.text() == "&Find":
		editor_window.find = FindReplaceWindow("find",editor_window)
		
	elif action.text() == "&Replace":
		editor_window.replace = FindReplaceWindow("replace",editor_window)

