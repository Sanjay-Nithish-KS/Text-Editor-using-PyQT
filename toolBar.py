"""
	toolBar module

	toolBar module provides function to create a tool bar
	for the text editor.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import resources

def add_tool_bar(editor_window):
	file_toolbar = editor_window.addToolBar("File")
	file_toolbar.addAction(editor_window.new)
	file_toolbar.addAction(editor_window.mopen)
	file_toolbar.addAction(editor_window.save)

	edit_toolbar = editor_window.addToolBar("Edit")
	edit_toolbar.addAction(editor_window.copy)
	edit_toolbar.addAction(editor_window.paste)
	edit_toolbar.addAction(editor_window.cut)
	edit_toolbar.addAction(editor_window.undo)
	edit_toolbar.addAction(editor_window.redo)

	add_icons(editor_window)

	editor_window.file_toolbar = file_toolbar
	editor_window.edit_toolbar = edit_toolbar

	file_toolbar.setMovable(False)
	edit_toolbar.setMovable(False)

def add_icons(editor_window):
	"""
		add_icons adds icons for the menus in the tool bar and menu bar.
	"""
	editor_window.new.setIcon(QIcon(":new_icon"))
	editor_window.copy.setIcon(QIcon(":copy_icon"))
	editor_window.paste.setIcon(QIcon(":paste_icon"))
	editor_window.mopen.setIcon(QIcon(":open_icon"))
	editor_window.cut.setIcon(QIcon(":cut_icon"))
	editor_window.save.setIcon(QIcon(":save_icon"))
	editor_window.undo.setIcon(QIcon(":undo_icon"))
	editor_window.redo.setIcon(QIcon(":redo_icon"))