#user interface
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

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

#button
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        
        super(Main,self).__init__(parent)
        
        self.setupUi(self)
        self.setFixedSize(1366,768)
        self.label_7 = QLabel
        
        #self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        self.ts = time.strftime("%A, %d %B")
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()
        
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText("Dpu_website")
        self.pushButton.setFont(QFont('Arial', 30))
        self.pushButton.setGeometry(QtCore.QRect(50,200,375,80))
        self.pushButton.clicked.connect(Dpu_clicked)
        self.pushButton.setStyleSheet("color:white")
        self.pushButton.setStyleSheet("background-image : url(./lib/tuse.png); border : 2px solid blue")
# user interface buttons keys
def Run_clicked():
   print("vaibhav")

def Stop_clicked():
   exit()

def Dpu_clicked():
   exit()
   
if __name__ == "__main__":
    #startup()
    #wishMe()
    #convert_size(1)
    #system_stats()  
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
  




