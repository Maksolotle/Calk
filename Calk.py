# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calk.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSplitter,
    QWidget)
import s_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(300, 500))
        MainWindow.setMaximumSize(QSize(300, 500))
        icon = QIcon()
        icon.addFile(u":/icon/R.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: whitesmoke;\n"
"	background-color: #232323;\n"
"	font-family: Rubik;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #2c2c2c;\n"
"}\n"
"")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        self.lbl_temp.setGeometry(QRect(0, 0, 301, 131))
        self.lbl_temp.setStyleSheet(u"color: rgb(176, 176, 176);")
        self.lb_t = QLineEdit(self.centralwidget)
        self.lb_t.setObjectName(u"lb_t")
        self.lb_t.setGeometry(QRect(0, 80, 311, 71))
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_t.sizePolicy().hasHeightForWidth())
        self.lb_t.setSizePolicy(sizePolicy1)
        self.lb_t.setStyleSheet(u"font-size: 35pt")
        self.lb_t.setMaxLength(11)
        self.lb_t.setCursorPosition(1)
        self.lb_t.setReadOnly(True)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 150, 311, 351))
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy2)
        self.splitter.setOrientation(Qt.Vertical)
        self.gridLayoutWidget = QWidget(self.splitter)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.layout_buttons = QGridLayout(self.gridLayoutWidget)
        self.layout_buttons.setObjectName(u"layout_buttons")
        self.layout_buttons.setContentsMargins(0, 0, 0, 0)
        self.btn_min = QPushButton(self.gridLayoutWidget)
        self.btn_min.setObjectName(u"btn_min")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_min.sizePolicy().hasHeightForWidth())
        self.btn_min.setSizePolicy(sizePolicy3)
        self.btn_min.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_min.setStyleSheet(u"background-color: #616161")

        self.layout_buttons.addWidget(self.btn_min, 2, 4, 1, 1)

        self.btn_point = QPushButton(self.gridLayoutWidget)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy3.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy3)
        self.btn_point.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_point, 4, 3, 1, 1)

        self.btn_9 = QPushButton(self.gridLayoutWidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy3.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy3)
        self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_9.setStyleSheet(u"")

        self.layout_buttons.addWidget(self.btn_9, 1, 3, 1, 1)

        self.btn_ce = QPushButton(self.gridLayoutWidget)
        self.btn_ce.setObjectName(u"btn_ce")
        sizePolicy3.setHeightForWidth(self.btn_ce.sizePolicy().hasHeightForWidth())
        self.btn_ce.setSizePolicy(sizePolicy3)
        self.btn_ce.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ce.setStyleSheet(u"background-color: #ffa200")

        self.layout_buttons.addWidget(self.btn_ce, 0, 2, 1, 1)

        self.btn_ = QPushButton(self.gridLayoutWidget)
        self.btn_.setObjectName(u"btn_")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_.sizePolicy().hasHeightForWidth())
        self.btn_.setSizePolicy(sizePolicy4)
        self.btn_.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_.setStyleSheet(u"background-color: #616161")

        self.layout_buttons.addWidget(self.btn_, 0, 4, 1, 1)

        self.btn_5 = QPushButton(self.gridLayoutWidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy3.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy3)
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_5, 2, 2, 1, 1)

        self.btn_7 = QPushButton(self.gridLayoutWidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy3.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy3)
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_7.setStyleSheet(u"background-color: rgb(44, 44, 44);")

        self.layout_buttons.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_2 = QPushButton(self.gridLayoutWidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy3.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy3)
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_2, 3, 2, 1, 1)

        self.btn_3 = QPushButton(self.gridLayoutWidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy3.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy3)
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_3, 3, 3, 1, 1)

        self.btn_plus = QPushButton(self.gridLayoutWidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy3.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy3)
        self.btn_plus.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plus.setStyleSheet(u"background-color: #616161")

        self.layout_buttons.addWidget(self.btn_plus, 3, 4, 1, 1)

        self.btn_clear = QPushButton(self.gridLayoutWidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy3.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy3)
        self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear.setStyleSheet(u"background-color: #ffa200")

        self.layout_buttons.addWidget(self.btn_clear, 0, 0, 1, 1)

        self.btn_4 = QPushButton(self.gridLayoutWidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy3.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy3)
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_backspace = QPushButton(self.gridLayoutWidget)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy4.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy4)
        self.btn_backspace.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_backspace.setStyleSheet(u"background-color: #616161")
        icon1 = QIcon()
        icon1.addFile(u":/icon/backspace_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backspace.setIcon(icon1)
        self.btn_backspace.setIconSize(QSize(40, 40))

        self.layout_buttons.addWidget(self.btn_backspace, 0, 3, 1, 1)

        self.btn_neg = QPushButton(self.gridLayoutWidget)
        self.btn_neg.setObjectName(u"btn_neg")
        sizePolicy3.setHeightForWidth(self.btn_neg.sizePolicy().hasHeightForWidth())
        self.btn_neg.setSizePolicy(sizePolicy3)
        self.btn_neg.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_neg, 4, 0, 1, 1)

        self.btn_0 = QPushButton(self.gridLayoutWidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy3.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy3)
        self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_0, 4, 2, 1, 1)

        self.btn_1 = QPushButton(self.gridLayoutWidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy3.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy3)
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_6 = QPushButton(self.gridLayoutWidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy3.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy3)
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_6, 2, 3, 1, 1)

        self.btn_r = QPushButton(self.gridLayoutWidget)
        self.btn_r.setObjectName(u"btn_r")
        sizePolicy3.setHeightForWidth(self.btn_r.sizePolicy().hasHeightForWidth())
        self.btn_r.setSizePolicy(sizePolicy3)
        self.btn_r.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_r.setStyleSheet(u"background-color: #616161")

        self.layout_buttons.addWidget(self.btn_r, 4, 4, 1, 1)

        self.btn_x = QPushButton(self.gridLayoutWidget)
        self.btn_x.setObjectName(u"btn_x")
        sizePolicy3.setHeightForWidth(self.btn_x.sizePolicy().hasHeightForWidth())
        self.btn_x.setSizePolicy(sizePolicy3)
        self.btn_x.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_x.setStyleSheet(u"background-color: #616161")

        self.layout_buttons.addWidget(self.btn_x, 1, 4, 1, 1)

        self.btn_8 = QPushButton(self.gridLayoutWidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy3.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy3)
        self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_8, 1, 2, 1, 1)

        self.splitter.addWidget(self.gridLayoutWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calk", None))
        self.lbl_temp.setText("")
#if QT_CONFIG(tooltip)
        self.lb_t.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">0</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_min.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_min.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_point.setText(QCoreApplication.translate("MainWindow", u",", None))
#if QT_CONFIG(shortcut)
        self.btn_point.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
#if QT_CONFIG(shortcut)
        self.btn_ce.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.btn_.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_backspace.setText("")
#if QT_CONFIG(shortcut)
        self.btn_backspace.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.btn_neg.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_r.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.btn_r.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_x.setText(QCoreApplication.translate("MainWindow", u"x", None))
#if QT_CONFIG(shortcut)
        self.btn_x.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

