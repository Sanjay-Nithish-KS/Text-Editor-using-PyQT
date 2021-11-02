import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TextEditor(QMainWindow):
   def __init__(self, parent = None):
      super(TextEditor, self).__init__(parent)

      menu_bar = self.menuBar()
      
      self.label = QLabel(self)
      self.label.setGeometry(0,0,300,300)

      self.add_menu(menu_bar)
      self.setGeometry(0,0,500,500)
      self.setWindowTitle("Text Editor")
      self.setWindowIcon(QIcon('logo.png'))
   
   def add_menu(self,menu_bar):
      """
      Add Menu to the Text Editor Window
      """
      # File Menu
      file = menu_bar.addMenu("File")
      file.addAction("New")
      # Open Menu
      open = file.addAction("Open")
      open.setShortcut("Ctrl+O")
      # Save Menu
      save = QAction("Save",self)
      save.setShortcut("Ctrl+S")
      file.addAction(save)
      # Edit Menu 
      edit = file.addMenu("Edit")
      edit.addAction("copy")
      edit.addAction("paste")
      # Quit Menu
      quit = QAction("Quit",self) 
      file.addAction(quit)

      file.triggered[QAction].connect(self.processtrigger)

   def processtrigger(self,q):
      if q.text() == "Open":
         file_name = QFileDialog.getOpenFileName(self, 'Open file')[0]
         file_content = open(file_name).read()
         self.label.setText(file_content)
         self.label.move(50,20)

      elif q.text() == "Quit":
         sys.exit()

      else:
         print(f"{q.text()}")
      