from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget, QFont,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
      
from instr import *


class FinalWin(QWidget):
   def __init__(self):
       ''' the window in which the survey is being conducted '''
       super().__init__()


       # creating and configuring graphic elements:
       self.initUI()


       # sets what the window will look like (label, size, location)
       self.set_appear()
      
       # start:
       self.show()


   def initUI(self):
       ''' creates graphic elements '''
       self.workh_text = QLabel(txt_workheart)
       self.index_text = QLabel(txt_index)


       self.layout_line = QVBoxLayout()
       self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
       self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)        
       self.setLayout(self.layout_line)


   ''' sets what the window will look like (label, size, location) '''
   def set_appear(self):
       self.setWindowTitle(txt_finalwin)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)
       self.setWindowTitle("Label") 
  
        # setting  the geometry of window 
       self.setGeometry(0, 0, 400, 300) 
  
        # creating a label widget 
        # by default label will display at top left corner 
       self.label_1 = QLabel('Arial font', self) 
  
        # moving position 
       self.label_1.move(100, 100) 
  
        # setting font and size 
       self.label_1.setFont(QFont('Arial', 10)) 
  
        # creating a label widget 
        # by default label will display at top left corner 
       self.label_2 = QLabel('Times font', self) 
  
        # moving position 
       self.label_2.move(100, 120) 
  
        # setting font and size 
       self.label_2.setFont(QFont('Times', 10)) 