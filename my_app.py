from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 

from instr import *
from second_win import *
     
class MainWin(QWidget):
   def __init__(self):
       ''' the window which the greeting is located in '''
       super().__init__()


       # creating and configuring graphic elements:
       self.initUI()


       #establishes connections between elements
       self.connects()


       # sets what the window will look like (label, size, location)
       self.set_appear()


       # start:
       self.show()


   def initUI(self):
       ''' creates graphic elements '''
       self.btn_next = QPushButton(txt_next, self)
       self.hello_text = QLabel(txt_hello)
       self.instruction = QLabel(txt_instruction)


       self.layout_line = QVBoxLayout()
       self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
       self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
       self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)         
       self.setLayout(self.layout_line)
  
   def next_click(self):
       self.tw = TestWin()
       self.hide()


   def connects(self):
       self.btn_next.clicked.connect(self.next_click)


   ''' sets what the window will look like (label, size, location) '''
   def set_appear(self):
       self.setWindowTitle(txt_title)
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
       self.show()

app = QApplication([])
mw = MainWin()
app.exec_()
