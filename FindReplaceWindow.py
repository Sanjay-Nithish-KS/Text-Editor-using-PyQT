"""
	FindReplaceWindow Class

	The Class FindReplace is used to create find or find and replace
	window.

	Usage:
		import FindReplaceWindow
		FindReplaceWindow.FindReplaceWindow(action,TextEditor object)
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from findReplaceActions import *

class FindReplaceWindow(QWidget):
	def __init__(self,action,editor_window,parent = None):
		super(FindReplaceWindow,self).__init__(parent)
		self.action = action
		self.editor_window = editor_window
		self.editor_window.last_match = None
		if action == "find":
			self.createFindLayout()
			self.setWindowTitle("Find")
			self.show()

		else:
			self.createReplaceLayout()
			self.setWindowTitle("Find & Replace")
			self.show()

	def createFindLayout(self):
		"""
			createFindLayout creates a find window.
		"""
		window = self.editor_window
		#Layouts
		verticalLayout = QVBoxLayout()
		horizontalLayout1 = QHBoxLayout()
		horizontalLayout2 = QHBoxLayout()

		# Widgets
		window.find_text_box = QLineEdit(self)
		window.find_next_button = QPushButton("Next")
		window.find_prev_button = QPushButton("Previous")
		window.find_button = QPushButton("Find")

		# Adding Widgets to Horizontal Layout
		horizontalLayout1.addWidget(QLabel("Find  : "))
		horizontalLayout1.addWidget(window.find_text_box,Qt.AlignCenter)
		horizontalLayout1.addStretch(2)
		horizontalLayout2.addWidget(window.find_button,Qt.AlignCenter)
		horizontalLayout2.addWidget(window.find_prev_button,Qt.AlignCenter)
		horizontalLayout2.addWidget(window.find_next_button,Qt.AlignCenter)
		
		# Adding Horizontal Layout to Vertu=ical Layout
		verticalLayout.addLayout(horizontalLayout1,Qt.AlignCenter)
		verticalLayout.addLayout(horizontalLayout2,Qt.AlignCenter)

		# Event
		window.find_button.clicked.connect(lambda: findAction(window))

		self.setLayout(verticalLayout)
		self.setGeometry(100,100,400,200)

	def createReplaceLayout(self):
		"""
			createReplaceLayout creates a find and replace window.
		"""
		window = self.editor_window
		# Layouts
		verticalLayout = QVBoxLayout()
		horizontalLayout1 = QHBoxLayout()
		horizontalLayout2 = QHBoxLayout()
		horizontalLayout3 = QHBoxLayout()
		horizontalLayout4 = QHBoxLayout()

		# Widgets
		window.find_text_box = QLineEdit(self)
		window.replace_text_box = QLineEdit(self)
		window.find_next_button = QPushButton("Next")
		window.find_prev_button = QPushButton("Previous")
		window.find_button = QPushButton("Find")
		window.replace_button = QPushButton("Replace")
		window.replace_all_button = QPushButton("Replace All")

		# Adding Widgets to Horzontal Layout
		horizontalLayout1.addWidget(QLabel("Find  : "))
		horizontalLayout1.addWidget(window.find_text_box,Qt.AlignCenter)
		horizontalLayout1.addStretch(2)
		horizontalLayout2.addWidget(QLabel("Replace  : "))
		horizontalLayout2.addWidget(window.replace_text_box,Qt.AlignCenter)
		horizontalLayout2.addStretch(2)
		horizontalLayout3.addWidget(window.find_button,Qt.AlignCenter)
		horizontalLayout3.addWidget(window.find_prev_button,Qt.AlignCenter)
		horizontalLayout3.addWidget(window.find_next_button,Qt.AlignCenter)
		horizontalLayout4.addWidget(window.replace_button,Qt.AlignCenter)
		horizontalLayout4.addWidget(window.replace_all_button,Qt.AlignCenter)

		# Adding Horizontal Layout to Vertical Layout
		verticalLayout.addLayout(horizontalLayout1,Qt.AlignCenter)
		verticalLayout.addLayout(horizontalLayout2,Qt.AlignCenter)
		verticalLayout.addLayout(horizontalLayout3,Qt.AlignCenter)
		verticalLayout.addLayout(horizontalLayout4,Qt.AlignCenter)

		# Events
		window.find_button.clicked.connect(lambda: findAction(window))
		window.replace_button.clicked.connect(lambda: replaceAction(window))
		window.replace_all_button.clicked.connect(lambda: replaceAllAction(window))

		self.setLayout(verticalLayout)
		self.setGeometry(100,100,400,200)

