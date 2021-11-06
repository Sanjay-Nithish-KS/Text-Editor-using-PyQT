"""
   TextEditor Class

   Desciption:
      Creation of the GUI of the text editor is implemented bu this class.
      It inherits the QMainWindow class.

   Overrided Functions:
      1. resizeEvent()
      2. closeEvent()

   Usage:

      import TextEditor
      text_editor = TextEditor.TextEditor()

"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MenuBar,TextArea,FindReplaceWindow
from PyQt5 import QtWidgets
import toolBar

class TextEditor(QMainWindow):
   def __init__(self, parent = None):
      super(TextEditor, self).__init__(parent)

      self.menu_bar = MenuBar.add_menu(self)

      self.text_area = TextArea.add_text_area(self)
      self.text_area.textChanged.connect(self.textChanged)
      self.text_area.cursorPositionChanged.connect(self.cursorPositionChanged)

      toolBar.add_tool_bar(self)

      self.setGeometry(0,0,500,500)
      self.setWindowTitle("Text Editor")
      self.setWindowIcon(QIcon('logo.png'))
      self.statusBar = QStatusBar(self)
      self.setStatusBar(self.statusBar)

      self.setStyle()

   def setStyle(self):
      """
         Sets style for the belo components
         1. TextEdit
         2. Menu Bar
         3. Tool Bar
         4. Status Bar
      """
      self.statusBar.setStyleSheet("font:20px")
      self.setStyleSheet("font:25px;")
      self.text_area.setStyleSheet("""
                        selection-background-color: rgba(255,211,67,255);
                        border-color:black;
                        selection-color:black;
                        font:20px;
      """)
      self.menu_bar.setStyleSheet("padding:5px")
      self.file_toolbar.setStyleSheet("padding:5px;padding-right:8px;")
      self.edit_toolbar.setStyleSheet("padding:5px;padding-right:8px;")
      self.text_area.setAttribute(Qt.WA_StyledBackground) 

   def resizeEvent(self, event):
      """
         resizeEvent
         This is a Overrided Method.

         Used to resize the text area when the text editor 
         is resized.
      """
      menu_bar_height = self.menuBar().height()
      text_editor_width = self.width()
      text_editor_height = self.height()
      toolbar_height = self.file_toolbar.height()
      statusbar_height = self.statusBar.height()

      self.text_area.setGeometry(
         0, 
         menu_bar_height + toolbar_height,
         text_editor_width,
         text_editor_height - menu_bar_height - toolbar_height - statusbar_height
      )

   def fileAction(self,action):
      MenuBar.fileAction(self,action)

   def editAction(self,action):
      MenuBar.editAction(self,action)

   def findAction(self,action):
      MenuBar.findAction(self,action)

   def textChanged(self):
      """
         Text Changed
         This function changes the title of the window when the 
         file is Modified.
      """
      editor_window_title = self.windowTitle()
      
      if editor_window_title[-1] != "*":
         self.setWindowTitle(
               self.windowTitle() + " *"
            )

   def cursorPositionChanged(self):
      """
         Used to set the Line Number and the Column number in the status bar according to the 
         cursor position
      """
      cursor = self.text_area.textCursor()
      line_no = cursor.blockNumber()
      col_no = cursor.columnNumber()
      self.statusBar.showMessage("Line "+str(line_no)+", Column "+str(col_no))

   def closeEvent(self,event):
      """
         Used to ask user confirmation when a text editor is closed wihout saving
         a file
      """
      title = self.windowTitle()
      if title[-1] == "*":
         msg = 'Are you sure you want to close the Text Editor without Saving the file?'
         reply = QMessageBox.question(self, 'Window Close',msg,
                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
         if reply == QMessageBox.Yes:
            sys.exit()
         else:
            event.ignore()
   