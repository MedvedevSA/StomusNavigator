# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(978, 671)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top = QFrame(self.main_frame)
        self.Top.setObjectName(u"Top")
        self.Top.setMaximumSize(QSize(16777215, 50))
        self.Top.setFrameShape(QFrame.StyledPanel)
        self.Top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(871, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.lbl_cur_pj = QLabel(self.Top)
        self.lbl_cur_pj.setObjectName(u"lbl_cur_pj")
        self.lbl_cur_pj.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.lbl_cur_pj)


        self.verticalLayout.addWidget(self.Top)

        self.body = QFrame(self.main_frame)
        self.body.setObjectName(u"body")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.body)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.left_menu = QFrame(self.body)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(90, 16777215))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.Btn_Menu_1 = QPushButton(self.left_menu)
        self.Btn_Menu_1.setObjectName(u"Btn_Menu_1")
        self.Btn_Menu_1.setMinimumSize(QSize(0, 60))

        self.verticalLayout_2.addWidget(self.Btn_Menu_1)

        self.Btn_Menu_2 = QPushButton(self.left_menu)
        self.Btn_Menu_2.setObjectName(u"Btn_Menu_2")
        self.Btn_Menu_2.setMinimumSize(QSize(0, 60))

        self.verticalLayout_2.addWidget(self.Btn_Menu_2)

        self.Btn_Menu_3 = QPushButton(self.left_menu)
        self.Btn_Menu_3.setObjectName(u"Btn_Menu_3")
        self.Btn_Menu_3.setMinimumSize(QSize(0, 60))

        self.verticalLayout_2.addWidget(self.Btn_Menu_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.left_menu)

        self.Pages_Widget = QStackedWidget(self.body)
        self.Pages_Widget.setObjectName(u"Pages_Widget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_5 = QVBoxLayout(self.page_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.page_1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 200))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(120, 150))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.rBtn_1_machine = QRadioButton(self.frame)
        self.rBtn_1_machine.setObjectName(u"rBtn_1_machine")
        self.rBtn_1_machine.setMinimumSize(QSize(0, 30))
        self.rBtn_1_machine.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_3.addWidget(self.rBtn_1_machine)

        self.rBtn_2_machine = QRadioButton(self.frame)
        self.rBtn_2_machine.setObjectName(u"rBtn_2_machine")
        self.rBtn_2_machine.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.rBtn_2_machine)

        self.rBtn_3_machine = QRadioButton(self.frame)
        self.rBtn_3_machine.setObjectName(u"rBtn_3_machine")
        self.rBtn_3_machine.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.rBtn_3_machine)


        self.horizontalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(250, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lbl_cur_info = QLabel(self.frame_2)
        self.lbl_cur_info.setObjectName(u"lbl_cur_info")
        self.lbl_cur_info.setGeometry(QRect(30, 10, 231, 41))
        self.lbl_cur_info.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(150, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.Btn_curOpenPj = QPushButton(self.frame_3)
        self.Btn_curOpenPj.setObjectName(u"Btn_curOpenPj")
        self.Btn_curOpenPj.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.Btn_curOpenPj)

        self.Btn_curOpenDraw = QPushButton(self.frame_3)
        self.Btn_curOpenDraw.setObjectName(u"Btn_curOpenDraw")
        self.Btn_curOpenDraw.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.Btn_curOpenDraw)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.verticalSpacer_3 = QSpacerItem(20, 166, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.frame_6 = QFrame(self.page_1)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 200))
        self.frame_6.setMaximumSize(QSize(16777215, 300))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidget = QTableWidget(self.frame_6)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        if (self.tableWidget.rowCount() < 20):
            self.tableWidget.setRowCount(20)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(3)

        self.horizontalLayout_5.addWidget(self.tableWidget)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 20))

        self.verticalLayout_6.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 20))

        self.verticalLayout_6.addWidget(self.pushButton_2)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.Pages_Widget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.checkBox = QCheckBox(self.page_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(200, 150, 70, 17))
        self.buttonBox = QDialogButtonBox(self.page_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(240, 310, 156, 23))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.Pages_Widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.Pages_Widget.addWidget(self.page_3)

        self.horizontalLayout_2.addWidget(self.Pages_Widget)


        self.verticalLayout.addWidget(self.body)


        self.horizontalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 978, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Pages_Widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_cur_pj.setText(QCoreApplication.translate("MainWindow", u"Cur_PJ", None))
        self.Btn_Menu_1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Btn_Menu_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Btn_Menu_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.rBtn_1_machine.setText(QCoreApplication.translate("MainWindow", u"#1 Nexturn", None))
        self.rBtn_2_machine.setText(QCoreApplication.translate("MainWindow", u"#2 Nexturn", None))
        self.rBtn_3_machine.setText(QCoreApplication.translate("MainWindow", u"#3 Tsugami", None))
        self.lbl_cur_info.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041d\u0430 N \u0441\u0442\u0430\u043d\u043a\u0435:</p><p>AN-ZEN-D6.0-WELDING-HOLDER</p></body></html>", None))
        self.Btn_curOpenPj.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.Btn_curOpenDraw.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0430 \u0441 \u0447\u0435\u0440\u0442\u0435\u0436\u043e\u043c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
    # retranslateUi
