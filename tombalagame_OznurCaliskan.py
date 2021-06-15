
##
# @file tombalagame_OznurCaliskan.py
#
# @brief Object Oriented Programming II 2021 Spring Course Project: Tombala Game Project
#
# @mainpage TOMBALA GAME PROJECT
#
# @section description_tombalagame_OznurCaliskan Description
# Tombala Game project designed in Qt Designer and converted to Python script.
# The Python code has been improved and object oriented programming features are used in the user-defined classes.
#
# @section libraries_tombalagame_OznurCaliskan Libraries/Modules
# NumPy library
# PyQt5 library
#
# @section notes_tombalagame_OznurCaliskan Notes
# This project is a Tombala Game for two players.
# User can write player's names and select colors for each player's cards.
# By clicking Initialize Cards button the cards will be set and user can start picking numbers.
# When the player's cards have the same numbers as picked number, this will be indicated.
# Player's scores set as when the user hits first bingo gets 10 points, second bingo gets 20 points and when all numbers are completed in card gets 40 points.
#
# @section author_tombalagame_OznurCaliskan Author(s)
# - Created by Öznur Çalışkan on 05/08/2021.
# - Finished by Öznur Çalışkan on 06/05/2021.
#
# Copyright (c) 2021 Öznur Çalışkan.  All rights reserved.

##Imports NumPy and PyQt5 library
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QDesktopWidget, QDateTimeEdit

## Ui_MainWindow class.
#
#  This class is implemented for Qt GUI.
class Ui_MainWindow(object):
    
    ## Setup Ui method to set all the widgets on the GUI
    #  @param self The object pointer.
    #  @param MainWindow The created window on Qt Designer.
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(575, 362)
        MainWindow.move(100,100)
        self.ui = Ui_MainWindow()
        
        ## Sets central widget. 
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(9)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(170, 0, 127);\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_28.setTextFormat(QtCore.Qt.AutoText)
        self.label_28.setScaledContents(True)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_4.addWidget(self.label_28, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_29.setFont(font)
        self.label_29.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_29.setStyleSheet("color: rgb(111, 0, 167);\n"
"background-color: rgb(170, 170, 255);")
        self.label_29.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout.addWidget(self.label_29)
        
        self.label_59 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("color: rgb(111, 0, 167);\n"
"background-color: rgb(170, 170, 255);")
        self.label_59.setText("")
        self.label_59.setObjectName("label_59")
        self.horizontalLayout.addWidget(self.label_59)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        self.label_48 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_48.setText("")
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.gridLayout_3.addWidget(self.label_48, 2, 5, 1, 1)
        
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 1, 3, 1, 1)
        
        self.label_46 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_46.setText("")
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.gridLayout_3.addWidget(self.label_46, 2, 1, 1, 1)
        
        self.label_53 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_53.setText("")
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.gridLayout_3.addWidget(self.label_53, 1, 6, 1, 1)
        
        self.label_47 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_47.setText("")
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.gridLayout_3.addWidget(self.label_47, 2, 3, 1, 1)
        
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 1, 5, 1, 1)
        
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_50.setText("")
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.gridLayout_3.addWidget(self.label_50, 0, 3, 1, 1)
        
        self.label_45 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_45.setText("")
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.gridLayout_3.addWidget(self.label_45, 1, 2, 1, 1)
        
        self.label_52 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_52.setText("")
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.gridLayout_3.addWidget(self.label_52, 1, 4, 1, 1)
        
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 1, 1, 1)
        
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 1, 7, 1, 1)
        
        self.label_49 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_49.setText("")
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.gridLayout_3.addWidget(self.label_49, 2, 7, 1, 1)
        
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 1, 8, 1, 1)
        
        self.label_65 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_65.setFont(font)
        self.label_65.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.label_65.setAlignment(QtCore.Qt.AlignCenter)
        self.label_65.setObjectName("label_65")
        self.gridLayout_3.addWidget(self.label_65, 2, 8, 1, 1)
        
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)
        
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 2, 2, 1, 1)
        
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 0, 2, 1, 1)
        
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 0, 4, 1, 1)
        
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)
        
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 2, 4, 1, 1)
        
        self.label_64 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_64.setFont(font)
        self.label_64.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.label_64.setObjectName("label_64")
        self.gridLayout_3.addWidget(self.label_64, 0, 7, 1, 1)
        
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 2, 6, 1, 1)
        
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 0, 6, 1, 1)
        
        self.label_51 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_51.setText("")
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.gridLayout_3.addWidget(self.label_51, 0, 5, 1, 1)
        
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_44.setText("")
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout_3.addWidget(self.label_44, 0, 1, 1, 1)
        
        self.label_54 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_54.setText("")
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.gridLayout_3.addWidget(self.label_54, 0, 8, 1, 1)
        
        self.label_55 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_55.setText("")
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.gridLayout_3.addWidget(self.label_55, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(111, 0, 167);\n"
"background-color: rgb(170, 170, 255);")
        self.label_30.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_30.setScaledContents(False)
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_2.addWidget(self.label_30)
        
        self.label_60 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("color: rgb(111, 0, 167);\n"
"background-color: rgb(170, 170, 255);")
        self.label_60.setText("")
        self.label_60.setObjectName("label_60")
        self.horizontalLayout_2.addWidget(self.label_60)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        
        self.label_66 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_66.setAlignment(QtCore.Qt.AlignCenter)
        self.label_66.setObjectName("label_66")
        self.gridLayout_2.addWidget(self.label_66, 2, 7, 1, 1)
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 9, 1, 1)
        
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_34.setText("")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_2.addWidget(self.label_34, 2, 4, 1, 1)
        
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_38.setText("")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 2, 6, 1, 1)
        
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_40.setText("")
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout_2.addWidget(self.label_40, 2, 8, 1, 1)
        
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 9, 1, 1)
        
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 5, 1, 1)
        
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 7, 1, 1)
        
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 5, 1, 1)
        
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 6, 1, 1)
        
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_36.setText("")
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_2.addWidget(self.label_36, 1, 5, 1, 1)
        
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 0, 8, 1, 1)
        
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_39.setText("")
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout_2.addWidget(self.label_39, 1, 7, 1, 1)
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        
        self.label_56 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setObjectName("label_56")
        self.gridLayout_2.addWidget(self.label_56, 1, 8, 1, 1)
        
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_31.setText("")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 0, 1, 1, 1)
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 4, 1, 1)
        
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_37.setText("")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_2.addWidget(self.label_37, 0, 6, 1, 1)
        
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_41.setText("")
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout_2.addWidget(self.label_41, 0, 9, 1, 1)
        
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_35.setText("")
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_2.addWidget(self.label_35, 0, 4, 1, 1)
        
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_32.setText("")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_2.addWidget(self.label_32, 2, 1, 1, 1)
        
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_42.setText("")
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout_2.addWidget(self.label_42, 1, 0, 1, 1)
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)
        
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 2, 1, 1)
        
        self.label_43 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.label_43.setText("")
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.gridLayout_2.addWidget(self.label_43, 1, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 1, 0, 5, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.label_57 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("color: rgb(111, 0, 167);\n"
"background-color: rgb(170, 170, 255);")
        self.label_57.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_57.setObjectName("label_57")
        self.verticalLayout.addWidget(self.label_57)
        
        self.label_58 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("color: rgb(111, 0, 167);\n"
"background-color: rgb(170, 170, 255);")
        self.label_58.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_58.setObjectName("label_58")
        self.verticalLayout.addWidget(self.label_58)
        self.gridLayout_4.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        
        self.label_67 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_67.setFont(font)
        self.label_67.setStyleSheet("color: rgb(111, 0, 167);\n"
"background-color: rgb(170, 170, 255);")
        self.label_67.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_67.setObjectName("label_67")
        self.verticalLayout_6.addWidget(self.label_67)
        
        self.label_68 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_68.setFont(font)
        self.label_68.setStyleSheet("color: rgb(111, 0, 167);\n"
"background-color: rgb(170, 170, 255);")
        self.label_68.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_68.setObjectName("label_68")
        self.verticalLayout_6.addWidget(self.label_68)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox)
        self.comboBox.activated[str].connect(self.onActivated)
        
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_2)
        self.comboBox_2.activated[str].connect(self.onActivated1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 2, 1, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(218, 108, 163);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.buttonPick)
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(218, 108, 163);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buttonInitialize)
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 3, 1, 1, 2)
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(243, 121, 182);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        self.label_61 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("color: rgb(111, 0, 167);\n"
"background-color: rgb(170, 170, 255);")
        self.label_61.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_61.setObjectName("label_61")
        self.verticalLayout_4.addWidget(self.label_61)
        
        self.label_62 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("color: rgb(111, 0, 167);\n"
"background-color: rgb(170, 170, 255);")
        self.label_62.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_62.setObjectName("label_62")
        self.verticalLayout_4.addWidget(self.label_62)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        self.label_70 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_70.setFont(font)
        self.label_70.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"color: rgb(110, 0, 165);")
        self.label_70.setObjectName("label_70")
        self.label_70.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_5.addWidget(self.label_70)
        self.label_70.setText(str(0))
        
        self.label_71 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_71.setFont(font)
        self.label_71.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"color: rgb(110, 0, 165);")
        self.label_71.setObjectName("label_71")
        self.label_71.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_5.addWidget(self.label_71)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.label_71.setText(str(0))
        
        self.label_63 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_63.setWordWrap(True);
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("color: rgb(111, 0, 167);\n"
"background-color: rgb(170, 170, 255);")
        self.label_63.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.gridLayout.addWidget(self.label_63, 1, 0, 1, 2)
        self.gridLayout_4.addWidget(self.frame, 5, 1, 1, 2)
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 255);\n"
"background-color: rgb(255, 255, 127);")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 4, 1, 1, 1)
        
        self.label_69 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy)
        self.label_69.setMinimumSize(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_69.setFont(font)
        self.label_69.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(170, 0, 255);")
        self.label_69.setAlignment(QtCore.Qt.AlignCenter)
        self.label_69.setObjectName("label_69")
        self.gridLayout_4.addWidget(self.label_69, 4, 2, 1, 1)
        
        ## Sets main window.
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 18))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.setShortcut('Ctrl+Q')
        self.actionQuit.triggered.connect(qApp.quit)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.lineEdit.textChanged['QString'].connect(self.label_59.setText)
        self.lineEdit_2.textChanged['QString'].connect(self.label_60.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        ## @var initialize_button
        #  a class variable for initialize button
        self.initialize_button = self.pushButton
        
        ## @var card1
        #  a class variable for player 1's card
        self.card1 = np.empty([3,5])
        
        ## @var card2
        #  a class variable for player 2's card
        self.card2 = np.empty([3,5])
        
        ## @var initial_card
        #  a class variable for empty cards in the first place
        self.initial_card = np.empty([3,5])
        
        ## @var unique_card_1
        #  a class variable for player 1's unique and sorted card
        self.unique_card_1 = np.empty([3,5])
        
        ## @var unique_card_2
        #  a class variable for player 2's unique and sorted card
        self.unique_card_2 = np.empty([3,5])
        
        ## @var button
        #  a class variable for pick numbers button
        self.button = self.pushButton_2
        
        ## @var picked
        #  a class variable for picked number
        self.picked = 0
        
        ## @var bag
        #  a class variable for list of random numbers to be picked
        self.bag = []
        self.row1_card1 = []
        self.row2_card1 = []
        self.row3_card1 = []
        self.row1_card2 = []
        self.row2_card2 = []
        self.row3_card2 = []
        self.point_card1 = 0
        self.point_card2 = 0
        self.row1_1 = 0
        self.row2_1 = 0
        self.row3_1 = 0
        self.row1_2 = 0
        self.row2_2 = 0
        self.row3_2 = 0
        self.win = 0
        
        self.card1_labels=[self.label_15,self.label_18,self.label_19,self.label_27,self.label_64,
                           self.label_16,self.label_24,self.label_25,self.label_26,self.label_20,
                           self.label_17,self.label_21,self.label_22,self.label_23,self.label_65]
        self.card2_labels=[self.label_3,self.label_7,self.label_8,self.label_11,self.label_33,
                           self.label_4,self.label_6,self.label_10,self.label_56,self.label_9,
                           self.label_5,self.label_12,self.label_13,self.label_66,self.label_14]
        
        ## @var card
        #  a class variable for calling Card base class and initialize cards
        self.card = Card(self.initial_card,self.card1,self.card2,self.unique_card_1,self.unique_card_2)
        
        ## @var pick
        #  a class variable for calling PickNumber base class and implement picked number
        self.pick = PickNumber(self.picked,self.bag)
        
        ## @var check
        #  a class variable for calling Check subclass and check the cards
        self.check = Check(self.initial_card,self.card1,self.card2,self.unique_card_1,self.unique_card_2,self.picked,self.bag,self.row1_card1,self.row2_card1,self.row3_card1,self.row1_card2,self.row2_card2,self.row3_card2,self.point_card1,self.point_card2,self.row1_1,self.row2_1,self.row3_1,self.row1_2,self.row2_2,self.row3_2,self.win)
    
    ## retranslateUi method utilized by Qt GUI to set widget's names displaying on GUI.
    #  @param self The object pointer.
    #  @param MainWindow The created window on Qt Designer
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_28.setText(_translate("MainWindow", "WELCOME TO TOMBALA GAME"))
        self.label_29.setText(_translate("MainWindow", "PLAYER 1\'s NAME:   "))
        self.label_24.setText(_translate("MainWindow", " "))
        self.label_25.setText(_translate("MainWindow", " "))
        self.label_16.setText(_translate("MainWindow", " "))
        self.label_26.setText(_translate("MainWindow", " "))
        self.label_20.setText(_translate("MainWindow", " "))
        self.label_65.setText(_translate("MainWindow", " "))
        self.label_17.setText(_translate("MainWindow", " "))
        self.label_21.setText(_translate("MainWindow", " "))
        self.label_18.setText(_translate("MainWindow", " "))
        self.label_19.setText(_translate("MainWindow", " "))
        self.label_15.setText(_translate("MainWindow", " "))
        self.label_22.setText(_translate("MainWindow", " "))
        self.label_64.setText(_translate("MainWindow", " "))
        self.label_23.setText(_translate("MainWindow", " "))
        self.label_27.setText(_translate("MainWindow", " "))
        self.label_30.setText(_translate("MainWindow", "PLAYER 2\'s NAME:   "))
        self.label_4.setText(_translate("MainWindow", " "))
        self.label_5.setText(_translate("MainWindow", " "))
        self.label_66.setText(_translate("MainWindow", " "))
        self.label_9.setText(_translate("MainWindow", " "))
        self.label_14.setText(_translate("MainWindow", " "))
        self.label_8.setText(_translate("MainWindow", " "))
        self.label_11.setText(_translate("MainWindow", " "))
        self.label_13.setText(_translate("MainWindow", " "))
        self.label_10.setText(_translate("MainWindow", " "))
        self.label_33.setText(_translate("MainWindow", " "))
        self.label_3.setText(_translate("MainWindow", " "))
        self.label_56.setText(_translate("MainWindow", " "))
        self.label_6.setText(_translate("MainWindow", " "))
        self.label_7.setText(_translate("MainWindow", " "))
        self.label_12.setText(_translate("MainWindow", " "))
        self.label_57.setText(_translate("MainWindow", "PLAYER 1\'s name:"))
        self.label_58.setText(_translate("MainWindow", "PLAYER 2\'s name:"))
        self.label_67.setText(_translate("MainWindow", "Select color for Card1:"))
        self.label_68.setText(_translate("MainWindow", "Select color for Card2:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Pink"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Orange"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Green"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Purple"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Pink"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Orange"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Green"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Purple"))
        self.pushButton_2.setText(_translate("MainWindow", "PICK NUMBER"))
        self.pushButton.setText(_translate("MainWindow", "INITIALIZE CARDS"))
        self.label_61.setText(_translate("MainWindow", "PLAYER 1\'s Score:"))
        self.label_62.setText(_translate("MainWindow", "PLAYER 2\'s Score:"))
        self.label_63.setText(_translate("MainWindow", "Waiting for the start"))
        self.label_2.setText(_translate("MainWindow", "Picked Number:"))
        self.menuMenu.setTitle(_translate("MainWindow", "Exit"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
    
    ## onActivated method utilized by Qt GUI to get player 1's card color selection from combo box then set and display it on GUI.
    #  @param self The object pointer.
    #  @param text The user's selection from combo box
    def onActivated(self,text):
        self.choice=text
        #Setting the card color selection for player 1.
        if self.choice=="Pink":
            for x in self.card1_labels:
                x.setStyleSheet("background-color: rgb(243, 121, 182);")  
        elif self.choice=="Orange":
            for x in self.card1_labels:
                x.setStyleSheet("background-color: rgb(255, 170, 0);")   
        elif self.choice=="Green":
            for x in self.card1_labels:
                x.setStyleSheet("background-color: rgb(85, 255, 0);")      
        elif self.choice=="Purple":
            for x in self.card1_labels:
                x.setStyleSheet("background-color: rgb(170, 0, 255);")
    
    ## onActivated1 method utilized by Qt GUI to get player 2's card color selection from combo box then set and display it on GUI.
    #  @param self The object pointer.
    #  @param text The user's selection from combo box
    def onActivated1(self,text):
        self.choice=text
        #Setting the card color selection for player 2.
        if self.choice=="Pink":
            for x in self.card2_labels:
                x.setStyleSheet("background-color: rgb(243, 121, 182);")  
        elif self.choice=="Orange":
            for x in self.card2_labels:
                x.setStyleSheet("background-color: rgb(255, 170, 0);")   
        elif self.choice=="Green":
            for x in self.card2_labels:
                x.setStyleSheet("background-color: rgb(85, 255, 0);")      
        elif self.choice=="Purple":
            for x in self.card2_labels:
                x.setStyleSheet("background-color: rgb(170, 0, 255);")
            
    ## Button initialize method utilized by Qt GUI to set each player's cards then display the cards on GUI.
    #  @param self The object pointer.
    def buttonInitialize(self):
        self.label_63.setText("Good luck!")
        self.initial_card = self.card.get_initial_card()
        self.card.set_initialize_card(self.card1,self.card2)
        self.card.set_unique_sorted_card(self.card1,self.card2)
        self.unique_card_1 = self.card.get_unique_sorted_card_1()
        self.unique_card_2 = self.card.get_unique_sorted_card_2()
        
        self.card1_label=[[self.label_15,self.label_18,self.label_19,self.label_27,self.label_64],
                           [self.label_16,self.label_24,self.label_25,self.label_26,self.label_20],
                           [self.label_17,self.label_21,self.label_22,self.label_23,self.label_65]]
        
        self.card2_label=[[self.label_3,self.label_7,self.label_8,self.label_11,self.label_33],
                           [self.label_4,self.label_6,self.label_10,self.label_56,self.label_9],
                           [self.label_5,self.label_12,self.label_13,self.label_66,self.label_14]]
        #Setting the players' cards numbers on their places on GUI.
        for i in range(3):
                for j in range(5):
                        self.card1_label[i][j].raise_()
                        self.card2_label[i][j].raise_()
                        self.card1_label[i][j].setText(str(self.unique_card_1[i][j]))
                        self.card2_label[i][j].setText(str(self.unique_card_2[i][j]))

    ## Button pick method utilized by Qt GUI to pick number and check cards then display them on GUI.
    #  @param self The object pointer.    
    def buttonPick(self):
        self.label_63.setText("Keep it up!")
        self.check.check_cards(self.unique_card_1,self.unique_card_2,self.picked,self.bag,self.row1_card1,self.row2_card1,self.row3_card1,self.row1_card2,self.row2_card2,self.row3_card2,self.point_card1,self.point_card2,self.row1_1,self.row2_1,self.row3_1,self.row1_2,self.row2_2,self.row3_2,self.win)
        self.picked = self.check.picked_num
        self.point_card1 = self.check.point_card1
        self.check.unique_sorted_card_1 = self.unique_card_1
        self.check.unique_sorted_card_2 = self.unique_card_2
        self.point_card2 = self.check.point_card2
        self.win = self.check.win
        self.bag = self.check.bag
        self.label_69.setText(str(self.picked))
        
        #Setting the GUI for picked number, first bingo, second bingo and winner scores and texts for player 1.
        for x in np.nditer(self.unique_card_1):
            for i in self.card1_labels:
                if str(self.picked) == i.text() and x == self.picked:
                    i.setStyleSheet("background-color: rgb(255, 0, 0);")
            if self.point_card1 == 10 and self.point_card2 == 0:
                self.label_70.setText(str(10))
                self.label_63.setText("Player 1 it's FIRST BINGO!")
            if self.point_card1 == 20 and (self.point_card2 == 0 or self.point_card2 == 10):
                self.label_70.setText(str(20))
                self.label_63.setText("Player 1 it's SECOND BINGO!")
            if self.point_card1 == 40 and (self.point_card2 == 0 or self.point_card2 == 10 or self.point_card2 == 20):
                self.label_63.setText("PLAYER 1 IS THE WINNER!(YOU CAN QUIT)")
                self.label_70.setText(str(40))
        #Setting the GUI for picked number, first bingo, second bingo and winner scores and texts for player 2.
        for y in np.nditer(self.unique_card_2):
            for i in self.card2_labels:
                if str(self.picked) == i.text() and y == self.picked:
                    i.setStyleSheet("background-color: rgb(255, 0, 0);")
            if self.point_card2 == 10 and self.point_card1 == 0:
                self.label_71.setText(str(10))
                self.label_63.setText("Player 2 it's FIRST BINGO!")
            if self.point_card2 == 20 and (self.point_card1 == 0 or self.point_card1 == 10):
                self.label_71.setText(str(20))
                self.label_63.setText("Player 2 it's SECOND BINGO!")
            if self.point_card2 == 40 and (self.point_card1 == 0 or self.point_card1 == 10 or self.point_card1 == 20):
                self.label_63.setText("PLAYER 2 IS THE WINNER!(YOU CAN QUIT)")
                self.label_71.setText(str(40))

## Card base class.
#
#  Defines the base class utilized for implementation of player cards.                    
class Card:
    
    ## The constructor for Card base class.
    #  @param self The object pointer.
    #  @param card_zeros The initial card with zeros.
    #  @param card_1 The player 1's card with random numbers.
    #  @param card_2 The player 2's card with random numbers.
    #  @param unique_sorted_card_1 The player 1's card with sorted unique random numbers.
    #  @param unique_sorted_card_2 The player 2's card with sorted unique random numbers.
    def __init__(self,card_zeros,card_1,card_2,unique_sorted_card_1,unique_sorted_card_2):
        self.card_zeros = card_zeros
        self.card_1 = card_1
        self.card_2 = card_2
        self.unique_sorted_card_1 = unique_sorted_card_1
        self.unique_sorted_card_2 = unique_sorted_card_2
    
    ## Set initial card method initializes player card's all numbers with zeros.   
    def set_initial_card(self,card_zeros):
        self.card_zeros = np.zeros([3,5])
    
    ## Set initialize card method initializes player card's all numbers with random numbers.
    def set_initialize_card(self,card_1,card_2):
        self.card_1 = np.random.choice(np.arange(1, 91), replace=False, size=(3, 5))
        self.card_2 = np.random.choice(np.arange(1, 91), replace=False, size=(3, 5))
    
    ## Set unique sorted card method initializes player card's all numbers with sorted unique numbers.
    def set_unique_sorted_card(self,card_1,card_2):
        self.sorted_card_1 = np.sort(self.card_1, axis=1)
        self.sorted_card_2 = np.sort(self.card_2, axis=1)
        self.unique_sorted_card_1 = np.unique(self.sorted_card_1,axis=1)
        self.unique_sorted_card_2 = np.unique(self.sorted_card_2,axis=1)
    
    ## Get initial card method to reach player cards with zeros.  
    def get_initial_card(self):
        return self.card_zeros
    
    ## Get unique sorted card 1 method to reach player 1's card with sorted unique numbers.
    def get_unique_sorted_card_1(self):
        return self.unique_sorted_card_1
    
    ## Get unique sorted card 2 method to reach player 2's card with sorted unique numbers.
    def get_unique_sorted_card_2(self):
        return self.unique_sorted_card_2
    
## PickNumber base class.
#
#  Defines the base class utilized for picking numbers.
class PickNumber:
    
    ## The constructor for PickNumber base class.
    #  @param self The object pointer.
    #  @param picked_num The picked number.
    #  @param bag The list of numbers to be picked.
    def __init__(self,picked_num,bag):
        self.picked_num = picked_num    
        self.bag = list(bag)
    
    ## Set picked number method to implement random picked numbers.   
    def set_picked_num(self,bag,picked_num):
        if self.bag==[]:
            for i in range(1,90):
                self.bag.append(i)
        self.picked_num = np.random.choice(self.bag)
        self.bag.remove(self.picked_num)
    
    ## Get picked number method to get random picked number.  
    def get_picked_number(self):
        return self.picked_num

## Check subclass.
#
#  Defines the subclass utilized for checking both player's card inherited from Card and PickNumber base classes.
class Check(Card,PickNumber):
    
    ## The constructor for Check subclass
    #  @param self The object pointer.
    #  @param card_zeros The initial card with zeros.
    #  @param card_1 The player 1's card with random numbers.
    #  @param card_2 The player 2's card with random numbers.
    #  @param unique_sorted_card_1 The player 1's card with sorted unique random numbers.
    #  @param unique_sorted_card_2 The player 2's card with sorted unique random numbers.
    #  @param picked_num The picked number.
    #  @param bag The list of numbers to be picked.
    #  @param row1_card1 The first row of player 1's card.
    #  @param row2_card1 The second row of player 1's card.
    #  @param row3_card1 The third row of player 1's card.
    #  @param row1_card2 The first row of player 2's card.
    #  @param row2_card2 The second row of player 2's card.
    #  @param row3_card2 The third row of player 2's card.
    #  @param point_card1 The score of player 1.
    #  @param point_card2 The score of player 2.
    #  @param row1_1 The flag for completing all numbers in first row of player 1's card.
    #  @param row2_1 The flag for completing all numbers in second row of player 1's card.
    #  @param row3_1 The flag for completing all numbers in third row of player 1's card.
    #  @param row1_2 The flag for completing all numbers in first row of player 2's card.
    #  @param row2_2 The flag for completing all numbers in second row of player 2's card.
    #  @param row3_2 The flag for completing all numbers in third row of player 2's card.
    #  @param win The flag for the player who completed all numbers in its card, the winner.
    def __init__(self,card_zeros,card_1,card_2,unique_sorted_card_1,unique_sorted_card_2,picked_num,bag,row1_card1,row2_card1,row3_card1,row1_card2,row2_card2,row3_card2,point_card1,point_card2,row1_1,row2_1,row3_1,row1_2,row2_2,row3_2,win):
        Card.__init__(self,card_zeros,card_1,card_2,unique_sorted_card_1,unique_sorted_card_2)
        PickNumber.__init__(self,picked_num,bag)
        self.row1_card1 = []
        self.row2_card1 = []
        self.row3_card1 = []
        self.row1_card2 = []
        self.row2_card2 = []
        self.row3_card2 = []
        self.point_card1 = 0
        self.point_card2 = 0
        self.row1_1 = 0
        self.row2_1 = 0
        self.row3_1 = 0
        self.row1_2 = 0
        self.row2_2 = 0
        self.row3_2 = 0
        self.win = 0
    
    ## Check cards method to check if picked number matches with any number in player's cards and check first bingo, second bingo in player's cards each rows and check winner.
    def check_cards(self,unique_sorted_card_1,unique_sorted_card_2,picked_num,bag,row1_card1,row2_card1,row3_card1,row1_card2,row2_card2,row3_card2,point_card1,point_card2,row1_1,row2_1,row3_1,row1_2,row2_2,row3_2,win):
        self.unique_sorted_card_1 = Card.get_unique_sorted_card_1(self)
        self.unique_sorted_card_2 = Card.get_unique_sorted_card_2(self)
        PickNumber.set_picked_num(self,bag,picked_num)
        #Checking card 1
        for x in np.nditer(self.unique_sorted_card_1):
            if x == self.picked_num:
                #Checking card 1's first row
                for y in self.unique_sorted_card_1[0,:]:
                    if y == self.picked_num:
                        self.row1_card1.append(y)
                if sorted(self.row1_card1) == sorted(list(self.unique_sorted_card_1[0,:])):
                    self.row1_1 = 1
                if self.row1_1==1 and self.point_card2==0 and self.point_card1==0:
                    self.point_card1 = 10
                #Checking card 1's second row
                for z in self.unique_sorted_card_1[1,:]:
                    if z == self.picked_num:
                        self.row2_card1.append(z)
                if sorted(self.row2_card1) == sorted(list(self.unique_sorted_card_1[1,:])):
                    self.row2_1 = 1
                if self.row2_1==1 and self.point_card2==0 and self.point_card1==0:
                    self.point_card1 = 10
                #Checking card 1's third row    
                for t in self.unique_sorted_card_1[2,:]:
                    if t == self.picked_num:
                        self.row3_card1.append(t)
                if sorted(self.row3_card1) == sorted(list(self.unique_sorted_card_1[2,:])):
                    self.row3_1 = 1
                if self.row3_1==1 and self.point_card2==0 and self.point_card1==0:
                    self.point_card1 = 10
                #Setting points for second bingo and winner    
                if ((self.row1_1==1 and self.row2_1==1) or (self.row1_1==1 and self.row3_1==1) or (self.row2_1==1 and self.row3_1==1)) and (self.point_card2==0 or self.point_card2==10):
                    self.point_card1 = 20
                if self.row1_1==1 and self.row2_1==1 and self.row3_1==1 and (self.point_card2==0 or self.point_card2==10 or self.point_card2==20):
                    self.point_card1 = 40
                    self.win = 1
        #Checking card 2            
        for x in np.nditer(self.unique_sorted_card_2):
            if x == self.picked_num:
                #Checking card 2's first row
                for y in self.unique_sorted_card_2[0,:]:
                    if y == self.picked_num:
                        self.row1_card2.append(y)
                if sorted(self.row1_card2) == sorted(list(self.unique_sorted_card_2[0,:])):
                    self.row1_2 = 1
                if self.row1_2==1 and self.point_card1==0 and self.point_card2==0:
                    self.point_card2 = 10
                #Checking card 2's second row    
                for z in self.unique_sorted_card_2[1,:]:
                    if z == self.picked_num:
                        self.row2_card2.append(z)
                if sorted(self.row2_card2) == sorted(list(self.unique_sorted_card_2[1,:])):
                    self.row2_2 = 1
                if self.row2_2==1 and self.point_card1==0 and self.point_card2==0:
                    self.point_card2 = 10
                #Checking card 2's third row    
                for t in self.unique_sorted_card_2[2,:]:
                    if t == self.picked_num:
                        self.row3_card2.append(t)
                if sorted(self.row3_card2) == sorted(list(self.unique_sorted_card_2[2,:])):
                    self.row3_2 = 1
                if self.row3_2==1 and self.point_card1==0 and self.point_card2==0:
                    self.point_card2 = 10
                #Setting points for second bingo and winner     
                if ((self.row1_2==1 and self.row2_2==1) or (self.row1_2==1 and self.row3_2==1) or (self.row2_2==1 and self.row3_2==1)) and (self.point_card1==0 or self.point_card1==10):
                    self.point_card2 = 20
                if self.row1_2==1 and self.row2_2==1 and self.row3_2==1 and (self.point_card1==0 or self.point_card1==10 or self.point_card1==20):
                    self.point_card2 = 40
                    self.win = 1
    