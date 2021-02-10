import sys
import platform
import os
import gspread
import pandas as pd
import subprocess
from pathlib import Path

import json


from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


# IMPORT FUNCTIONS
from Source import *

# GUI FILE

from ui_main import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.DF = pd.DataFrame([])

        ## TOP
        ########################################################################

        self.ui.BtnLoadDf.clicked.connect(lambda: DataFunc.get_data(self))


        ## PAGES
        ########################################################################
       
        # PAGE 1
        self.ui_page1 = Ui_Page1(self)

        # PAGE 2
        self.ui.Btn_Menu_2.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.Btn_Menu_3.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_3))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())