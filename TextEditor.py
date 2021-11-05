import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MenuBar,TextArea,FindReplaceWindow
from PyQt5 import QtWidgets

class TextEditor(QMainWindow):
   def __init__(self, parent = None):
      super(TextEditor, self).__init__(parent)

      self.menu_bar = MenuBar.add_menu(self)

      self.text_area = TextArea.add_text_area(self)
      self.text_area.textChanged.connect(self.textChanged)

      self.setGeometry(0,0,500,500)
      self.setWindowTitle("Text Editor")
      self.setWindowIcon(QIcon('logo.png'))
      self.setStyleSheet("font:25px;")
      #self.menu_bar.setStyleSheet("background-color:white;color:black")
      #background-color:rgba(48,56,65,255)

   def resizeEvent(self, event):
      menu_bar_height = self.menuBar().height()
      text_editor_width = self.width()
      text_editor_height = self.height()

      self.text_area.setGeometry(
         0, 
         menu_bar_height,
         text_editor_width,
         text_editor_height - menu_bar_height
      )

   def fileAction(self,action):
      MenuBar.fileAction(self,action)

   def editAction(self,action):
      MenuBar.editAction(self,action)

   def findAction(self,action):
      MenuBar.findAction(self,action)

   def textChanged(self):
      editor_window_title = self.windowTitle()
      
      if editor_window_title[-1] != "*":
         self.setWindowTitle(
               self.windowTitle() + " *"
            )
      