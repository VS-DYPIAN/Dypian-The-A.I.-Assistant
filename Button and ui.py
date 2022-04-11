# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
import time
from imageio import imopen
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType  
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui")) 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("D.Y.P.I.A.N ")
  
        # setting geometry
        self.setGeometry(100, 100, 600, 400)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
    # method for widgets
    def UiComponents(self):
  
        # creating a push button
        Run = QPushButton("Run", self)
        Exit = QPushButton("Stop", self)
        # setting geometry of button
        Run.setGeometry(10,30,100,40)
        Exit.setGeometry(10,60,100,40)
  
  
        # adding action to a button
        Run.clicked.connect(self.Run)
        Exit.clicked.connect(self.Stop)
       
        #background
        self.setStyleSheet("background-image : url(./lib/tuse.png); border : 2px solid blue")
        Run.setStyleSheet("background-color: red");
        
        

        Exit.setStyleSheet("background-color:red");
    # action method
    def Run(self):
         print("Command")
    def Stop(self):
         exit()
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())