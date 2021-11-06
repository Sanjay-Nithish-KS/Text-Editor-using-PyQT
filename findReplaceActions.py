"""
	findReplaceActions Module

	findReplaceActions module provided functions to set actions to find and
	find and replace menu.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import re

last_match = None

def findAction(editor_window):
	text_to_find = editor_window.find_text_box.text()
	text = editor_window.text_area.toPlainText()
	pattern = re.compile(text_to_find)
	last_match = editor_window.last_match
	start = last_match.start() + 1 if last_match else 0
	last_match = pattern.search(text,start)
	if last_match:
		start = last_match.start()
		end = last_match.end()
		moveCursor(editor_window,start,end)
	else:
		editor_window.text_area.moveCursor(QTextCursor.End)
	editor_window.last_match = last_match
 
def replaceAction(editor_window):
	cursor = editor_window.text_area.textCursor()
	replace_text = editor_window.replace_text_box.text()
	last_match = editor_window.last_match
	if last_match and cursor.hasSelection():
		cursor.insertText(replace_text)
		editor_window.text_area.setTextCursor(cursor)

def replaceAllAction(editor_window):
	editor_window.last_match = None
	findAction(editor_window)
	while editor_window.last_match:
		replaceAction(editor_window)
		findAction(editor_window)

def moveCursor(editor_window,start,end):
	cursor = editor_window.text_area.textCursor()
	cursor.setPosition(start)
	cursor.movePosition(QTextCursor.Right,QTextCursor.KeepAnchor,end - start)
	editor_window.text_area.setTextCursor(cursor)
	