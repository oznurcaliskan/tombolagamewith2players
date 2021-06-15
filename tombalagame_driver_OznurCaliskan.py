##
# @file tombalagame_OznurCaliskan.py
#
# @brief Tombala Game Driver Code
#
# @section author_tombalagame_OznurCaliskan Author(s)
# - Created by Öznur Çalışkan on 05/08/2021.
# - Finished by Öznur Çalışkan on 06/05/2021.
#
# Copyright (c) 2021 Öznur Çalışkan.  All rights reserved.

##Imports NumPy and PyQt5 library
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon
from tombalagame_OznurCaliskan import Ui_MainWindow
import sys

## mywindow class.
#
#  This class is implemented for Qt GUI.
class mywindow(QtWidgets.QMainWindow):
    
    ## The constructor for mywindow class.
    #  @param self The object pointer.
    def __init__(self):
        super(mywindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Tombala Game')
        self.setWindowIcon(QIcon('icon.png')) 
        self.initUI()
    
    ## initUI method to set window.
    #  @param self The object pointer.    
    def initUI(self):               
        self.resize(250, 150)    
        self.center()
        self.show()
        
    ## center method to set widget in the center.
    #  @param self The object pointer.    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    ## closeEvent method to set close event.
    #  @param self The object pointer.
    #  @param event The event.    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()  
        
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())