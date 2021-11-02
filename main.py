import TextEditor
import sys
from PyQt5.QtWidgets import *

def main():
   app = QApplication(sys.argv)
   editor = TextEditor.TextEditor()
   editor.show()
   sys.exit(app.exec_())
   
if __name__ == '__main__':
   main()