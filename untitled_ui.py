# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1274, 729)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(9)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACT"
                        "ION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #3a3a3a;\n"
"	color: #fff;\n"
"	selection-background-color: #b78620;\n"
"	selection-color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"	border: 1px solid #000;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item \n"
"{\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected \n"
"{\n"
"	background-color: rgba(183, 134, 32, 20%);\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed \n"
"{\n"
"	background-color: rgb(183, 134, 32);\n"
""
                        "	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #222;\n"
"    padding: 4px;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"   	background-color: rgb(183, 134, 32);\n"
"	height: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"	background-color: rgba(183, 134, 32, 20%);\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolBar-----*/\n"
"QToolBar\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(69, 69, 69, 255),stop"
                        ":1 rgba(58, 58, 58, 255));\n"
"	border-top: none;\n"
"	border-bottom: 1px solid #4f4f4f;\n"
"	border-left: 1px solid #4f4f4f;\n"
"	border-right: 1px solid #4f4f4f;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolBar::separator\n"
"{\n"
"	background-color: #2e2e2e;\n"
"	width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton \n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"	padding: 5px;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"	margin-left: 1px;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover\n"
"{\n"
"	background-color: rgba(183, 134, 32, 20%);\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"	\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"	border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:checked\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, "
                        "50, 255));\n"
"	border: 1px solid #222;\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"	color: #ffffff;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::flat\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgba(183, 134, 32, 20%);\n"
"	border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"	border: 1px solid #b78620;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"QPushButton::checked\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #131313;\n"
"	color : #eee;\n"
"	border: 1px solid #343434;\n"
"	border-radius: 2px;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPlainTExtEdit-----*/\n"
"QPlainTextEdit\n"
"{\n"
"	background-color: #131313;\n"
"	color : #eee;\n"
"	border: 1px solid #343434;\n"
"	border-radius: 2px;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTabBar-----*/\n"
"QTabBar::tab\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #666;\n"
"	border-bottom: none;\n"
"	padding: 5px;\n"
"	padding-lef"
                        "t: 15px;\n"
"	padding-right: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"	background-color: red;\n"
"	border: 1px solid #666;\n"
"	top: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"	margin-right: 0; \n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"	background-color: #0c0c0d;\n"
"	margin-left: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"	color: #b1b1b1;\n"
"	border-bottom-style: solid;\n"
"	background-color: #0c0c0d;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"	margin-bottom: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"	border-top-color: #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"    border: 1px solid #000;\n"
"    padding-left: 6px;\n"
"    color: #ffffff;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"	b"
                        "ackground-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #b78620;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #383838;\n"
"    color: #ffffff;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #b78620;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"\n"
"/*-----QSpinBox & QDateTimeEdit-----*/\n"
"QSpinBox,\n"
"QDateTimeEdit \n"
"{\n"
"    background"
                        "-color: #131313;\n"
"	color : #eee;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"    border-radius : 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, \n"
"QDateTimeEdit::up-button\n"
"{\n"
"	border-top-right-radius:2px;\n"
"	background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover, \n"
"QDateTimeEdit::up-button:hover\n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, \n"
"QDateTimeEdit::up-button:pressed\n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDateTimeEdit::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button, \n"
"QDateTimeEdit::down-button\n"
"{\n"
"	border-bottom-right-radius:2px;\n"
"	background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
""
                        "QSpinBox::down-button:hover, \n"
"QDateTimeEdit::down-button:hover\n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:pressed, \n"
"QDateTimeEdit::down-button:pressed\n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDateTimeEdit::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox \n"
"{\n"
"    border: 1px solid;\n"
"    border-color: #666666;\n"
"	border-radius: 5px;\n"
"    margin-top: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  \n"
"{\n"
"    background-color: transparent;\n"
"    color: #eee;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QHeaderView-----*/\n"
"QHeaderView::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2"
                        ":1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"	border: 1px solid #000;\n"
"    color: #fff;\n"
"    text-align: left;\n"
"	padding: 4px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"	border: 1px solid #000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeWidget-----*/\n"
"QTreeView\n"
"{\n"
"	show-decoration-selected: 1;\n"
"	alternate-background-color: #3a3a3a;\n"
"	selection-color: #fff;\n"
"	background-color: #2d2d2d;\n"
"	border: 1px solid gray;\n"
"	padding-top : 5px;\n"
"	color: #fff;\n"
"	font: 8pt;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected\n"
"{\n"
"	color:#fff;\n"
"	background-color: #b78620;\n"
"	border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"    background-color: #262626;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"	image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branc"
                        "h:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"	image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 83, 83, 255),stop:0.293269 rgba(81, 81, 81, 255),stop:0.634615 rgba(79, 79, 79, 255),stop:1 rgba(83, 83, 83, 255));\n"
"    border : none;\n"
"    color: white;\n"
"    show-decoration-selected: 1; \n"
"    outline: 0;\n"
"	border: 1px solid gray;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::disabled \n"
"{\n"
"	background-color: #656565;\n"
"	color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item \n"
"{\n"
"	background-color: #2d2d2d;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:alternate \n"
"{\n"
"    background-color: #3a3a3a;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected \n"
"{\n"
"	background-color: #b78620;\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"QListView::item:selected:!active \n"
"{\n"
"	background-color: #b78620;\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:active \n"
"{\n"
"	background-color: #b78620;\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #262626;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"	background-color: transparent;\n"
"    color: lightgray;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"	background-color: #b78620;\n"
"    border: 1px solid #3a546e;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"	border: 1px solid #b78620; \n"
"\n"
"}\n"
"\n"
"\n"
""
                        "QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton \n"
"{\n"
"	color: lightgray;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover \n"
"{\n"
"	background-color: lightgray;\n"
"	border: 2px solid #b78620;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked \n"
"{\n"
"	border: 2px solid #b78620;\n"
"	border-radius: 6px;\n"
"	background-color: rgba(183,134,32,20%);  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSlider-----*/\n"
"QSlider::groove:horizontal \n"
"{\n"
"	background-color: transparent;\n"
"	height: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal \n"
"{\n"
"	background-color: #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal \n"
"{\n"
"	background-color: #131313;\n"
""
                        "\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"	background-color: #b78620;\n"
"	width: 14px;\n"
"	margin-top: -6px;\n"
"	margin-bottom: -6px;\n"
"	border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover \n"
"{\n"
"	background-color: #d89e25;\n"
"	border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal:disabled \n"
"{\n"
"	background-color: #bbb;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border: 1px solid #aaa;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #3d3d3d;\n"
"    height: 15px;\n"
"    margin: 0px 16px 0 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:"
                        "1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arr"
                        "ow-left.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 16px;\n"
"	border: 1px solid #2d2d2d;\n"
"    margin: 16px 0px 16px 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"	background-color: qlinear"
                        "gradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"    border: 1px solid #666666;\n"
"    text-align: center;\n"
"	color: #000;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #b78620;\n"
"    width: 30px;\n"
"    margin: 0.5px;\n"
"\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setFont(font)
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 30, -1, -1)
        self.right_frame = QFrame(self.centralwidget)
        self.right_frame.setObjectName(u"right_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.right_frame.sizePolicy().hasHeightForWidth())
        self.right_frame.setSizePolicy(sizePolicy1)
        self.right_frame.setFrameShape(QFrame.Panel)
        self.right_frame.setFrameShadow(QFrame.Sunken)
        self.right_frame.setLineWidth(5)
        self.right_frame.setMidLineWidth(5)
        self.verticalLayout_2 = QVBoxLayout(self.right_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.customer_table = QTableWidget(self.right_frame)
        if (self.customer_table.columnCount() < 6):
            self.customer_table.setColumnCount(6)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.customer_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.customer_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.customer_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.customer_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.customer_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.customer_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.customer_table.rowCount() < 1):
            self.customer_table.setRowCount(1)
        self.customer_table.setObjectName(u"customer_table")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.customer_table.sizePolicy().hasHeightForWidth())
        self.customer_table.setSizePolicy(sizePolicy2)
        self.customer_table.setFont(font1)
        self.customer_table.setFrameShape(QFrame.NoFrame)
        self.customer_table.setAutoScrollMargin(2)
        self.customer_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.customer_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.customer_table.setTextElideMode(Qt.ElideMiddle)
        self.customer_table.setShowGrid(True)
        self.customer_table.setGridStyle(Qt.SolidLine)
        self.customer_table.setSortingEnabled(True)
        self.customer_table.setWordWrap(False)
        self.customer_table.setCornerButtonEnabled(True)
        self.customer_table.setRowCount(1)
        self.customer_table.horizontalHeader().setVisible(True)
        self.customer_table.horizontalHeader().setCascadingSectionResizes(True)
        self.customer_table.horizontalHeader().setMinimumSectionSize(68)
        self.customer_table.horizontalHeader().setDefaultSectionSize(70)
        self.customer_table.horizontalHeader().setHighlightSections(True)
        self.customer_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.customer_table.horizontalHeader().setStretchLastSection(True)
        self.customer_table.verticalHeader().setVisible(True)
        self.customer_table.verticalHeader().setCascadingSectionResizes(False)
        self.customer_table.verticalHeader().setDefaultSectionSize(30)
        self.customer_table.verticalHeader().setHighlightSections(True)
        self.customer_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.customer_table)

        self.frame_2 = QFrame(self.right_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.right_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.delete_selected_table_button = QPushButton(self.frame)
        self.delete_selected_table_button.setObjectName(u"delete_selected_table_button")

        self.horizontalLayout.addWidget(self.delete_selected_table_button)

        self.clear_table_button = QPushButton(self.frame)
        self.clear_table_button.setObjectName(u"clear_table_button")

        self.horizontalLayout.addWidget(self.clear_table_button)

        self.filter_table_button = QPushButton(self.frame)
        self.filter_table_button.setObjectName(u"filter_table_button")

        self.horizontalLayout.addWidget(self.filter_table_button)

        self.populate_table_button = QPushButton(self.frame)
        self.populate_table_button.setObjectName(u"populate_table_button")

        self.horizontalLayout.addWidget(self.populate_table_button)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalLayout_2.setStretch(0, 99)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)

        self.gridLayout_4.addWidget(self.right_frame, 0, 2, 1, 1)

        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.left_frame.sizePolicy().hasHeightForWidth())
        self.left_frame.setSizePolicy(sizePolicy3)
        self.left_frame.setLayoutDirection(Qt.LeftToRight)
        self.left_frame.setFrameShape(QFrame.Panel)
        self.left_frame.setFrameShadow(QFrame.Sunken)
        self.left_frame.setLineWidth(5)
        self.left_frame.setMidLineWidth(5)
        self.verticalLayout = QVBoxLayout(self.left_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 50, 1, 50)
        self.add_customer_label = QLabel(self.left_frame)
        self.add_customer_label.setObjectName(u"add_customer_label")
        self.add_customer_label.setFont(font1)
        self.add_customer_label.setFrameShape(QFrame.StyledPanel)
        self.add_customer_label.setFrameShadow(QFrame.Sunken)
        self.add_customer_label.setLineWidth(5)
        self.add_customer_label.setMidLineWidth(5)
        self.add_customer_label.setScaledContents(True)
        self.add_customer_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.add_customer_label)

        self.customer_entry_box = QFrame(self.left_frame)
        self.customer_entry_box.setObjectName(u"customer_entry_box")
        sizePolicy2.setHeightForWidth(self.customer_entry_box.sizePolicy().hasHeightForWidth())
        self.customer_entry_box.setSizePolicy(sizePolicy2)
        self.customer_entry_box.setFont(font)
        self.customer_entry_box.setFrameShape(QFrame.Panel)
        self.customer_entry_box.setFrameShadow(QFrame.Raised)
        self.customer_entry_box.setLineWidth(5)
        self.customer_entry_box.setMidLineWidth(5)
        self.formLayout_2 = QFormLayout(self.customer_entry_box)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.add_customer_name = QLineEdit(self.customer_entry_box)
        self.add_customer_name.setObjectName(u"add_customer_name")
        sizePolicy2.setHeightForWidth(self.add_customer_name.sizePolicy().hasHeightForWidth())
        self.add_customer_name.setSizePolicy(sizePolicy2)
        self.add_customer_name.setFont(font)
        self.add_customer_name.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.add_customer_name)

        self.add_customer_surname = QLineEdit(self.customer_entry_box)
        self.add_customer_surname.setObjectName(u"add_customer_surname")
        sizePolicy2.setHeightForWidth(self.add_customer_surname.sizePolicy().hasHeightForWidth())
        self.add_customer_surname.setSizePolicy(sizePolicy2)
        self.add_customer_surname.setFont(font)
        self.add_customer_surname.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.add_customer_surname)

        self.add_customer_phone = QLineEdit(self.customer_entry_box)
        self.add_customer_phone.setObjectName(u"add_customer_phone")
        sizePolicy2.setHeightForWidth(self.add_customer_phone.sizePolicy().hasHeightForWidth())
        self.add_customer_phone.setSizePolicy(sizePolicy2)
        self.add_customer_phone.setFont(font)
        self.add_customer_phone.setMaxLength(32767)
        self.add_customer_phone.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.add_customer_phone)

        self.add_customer_vehicle = QLineEdit(self.customer_entry_box)
        self.add_customer_vehicle.setObjectName(u"add_customer_vehicle")
        sizePolicy2.setHeightForWidth(self.add_customer_vehicle.sizePolicy().hasHeightForWidth())
        self.add_customer_vehicle.setSizePolicy(sizePolicy2)
        self.add_customer_vehicle.setFont(font)
        self.add_customer_vehicle.setAlignment(Qt.AlignCenter)
        self.add_customer_vehicle.setDragEnabled(False)

        self.formLayout_2.setWidget(4, QFormLayout.SpanningRole, self.add_customer_vehicle)

        self.add_customer_plates = QLineEdit(self.customer_entry_box)
        self.add_customer_plates.setObjectName(u"add_customer_plates")
        sizePolicy2.setHeightForWidth(self.add_customer_plates.sizePolicy().hasHeightForWidth())
        self.add_customer_plates.setSizePolicy(sizePolicy2)
        self.add_customer_plates.setFont(font)
        self.add_customer_plates.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(5, QFormLayout.SpanningRole, self.add_customer_plates)

        self.add_customer_chasis = QLineEdit(self.customer_entry_box)
        self.add_customer_chasis.setObjectName(u"add_customer_chasis")
        sizePolicy2.setHeightForWidth(self.add_customer_chasis.sizePolicy().hasHeightForWidth())
        self.add_customer_chasis.setSizePolicy(sizePolicy2)
        self.add_customer_chasis.setFont(font)
        self.add_customer_chasis.setAlignment(Qt.AlignCenter)
        self.add_customer_chasis.setDragEnabled(False)

        self.formLayout_2.setWidget(6, QFormLayout.SpanningRole, self.add_customer_chasis)

        self.save_new_customer_button = QPushButton(self.customer_entry_box)
        self.save_new_customer_button.setObjectName(u"save_new_customer_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.save_new_customer_button.sizePolicy().hasHeightForWidth())
        self.save_new_customer_button.setSizePolicy(sizePolicy4)
        self.save_new_customer_button.setFont(font)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.save_new_customer_button)

        self.cancel_new_customer_button = QPushButton(self.customer_entry_box)
        self.cancel_new_customer_button.setObjectName(u"cancel_new_customer_button")
        sizePolicy4.setHeightForWidth(self.cancel_new_customer_button.sizePolicy().hasHeightForWidth())
        self.cancel_new_customer_button.setSizePolicy(sizePolicy4)
        self.cancel_new_customer_button.setFont(font)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.cancel_new_customer_button)


        self.verticalLayout.addWidget(self.customer_entry_box)

        self.search_customer_label = QLabel(self.left_frame)
        self.search_customer_label.setObjectName(u"search_customer_label")
        self.search_customer_label.setFont(font1)
        self.search_customer_label.setFrameShape(QFrame.StyledPanel)
        self.search_customer_label.setFrameShadow(QFrame.Sunken)
        self.search_customer_label.setLineWidth(5)
        self.search_customer_label.setMidLineWidth(5)
        self.search_customer_label.setTextFormat(Qt.AutoText)
        self.search_customer_label.setScaledContents(True)
        self.search_customer_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.search_customer_label)

        self.customer_search_box = QFrame(self.left_frame)
        self.customer_search_box.setObjectName(u"customer_search_box")
        sizePolicy2.setHeightForWidth(self.customer_search_box.sizePolicy().hasHeightForWidth())
        self.customer_search_box.setSizePolicy(sizePolicy2)
        self.customer_search_box.setFont(font)
        self.customer_search_box.setLayoutDirection(Qt.LeftToRight)
        self.customer_search_box.setFrameShape(QFrame.Panel)
        self.customer_search_box.setFrameShadow(QFrame.Raised)
        self.customer_search_box.setLineWidth(5)
        self.customer_search_box.setMidLineWidth(5)
        self.formLayout_3 = QFormLayout(self.customer_search_box)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.search_customer_name = QLineEdit(self.customer_search_box)
        self.search_customer_name.setObjectName(u"search_customer_name")
        sizePolicy2.setHeightForWidth(self.search_customer_name.sizePolicy().hasHeightForWidth())
        self.search_customer_name.setSizePolicy(sizePolicy2)
        self.search_customer_name.setFont(font)
        self.search_customer_name.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(1, QFormLayout.SpanningRole, self.search_customer_name)

        self.search_customer_surname = QLineEdit(self.customer_search_box)
        self.search_customer_surname.setObjectName(u"search_customer_surname")
        sizePolicy2.setHeightForWidth(self.search_customer_surname.sizePolicy().hasHeightForWidth())
        self.search_customer_surname.setSizePolicy(sizePolicy2)
        self.search_customer_surname.setFont(font)
        self.search_customer_surname.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(2, QFormLayout.SpanningRole, self.search_customer_surname)

        self.search_customer_phone = QLineEdit(self.customer_search_box)
        self.search_customer_phone.setObjectName(u"search_customer_phone")
        sizePolicy2.setHeightForWidth(self.search_customer_phone.sizePolicy().hasHeightForWidth())
        self.search_customer_phone.setSizePolicy(sizePolicy2)
        self.search_customer_phone.setFont(font)
        self.search_customer_phone.setMaxLength(32767)
        self.search_customer_phone.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(3, QFormLayout.SpanningRole, self.search_customer_phone)

        self.search_customer_vehicle = QLineEdit(self.customer_search_box)
        self.search_customer_vehicle.setObjectName(u"search_customer_vehicle")
        sizePolicy2.setHeightForWidth(self.search_customer_vehicle.sizePolicy().hasHeightForWidth())
        self.search_customer_vehicle.setSizePolicy(sizePolicy2)
        self.search_customer_vehicle.setFont(font)
        self.search_customer_vehicle.setAlignment(Qt.AlignCenter)
        self.search_customer_vehicle.setDragEnabled(False)

        self.formLayout_3.setWidget(4, QFormLayout.SpanningRole, self.search_customer_vehicle)

        self.search_customer_plates = QLineEdit(self.customer_search_box)
        self.search_customer_plates.setObjectName(u"search_customer_plates")
        sizePolicy2.setHeightForWidth(self.search_customer_plates.sizePolicy().hasHeightForWidth())
        self.search_customer_plates.setSizePolicy(sizePolicy2)
        self.search_customer_plates.setFont(font)
        self.search_customer_plates.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(5, QFormLayout.SpanningRole, self.search_customer_plates)

        self.search_customer_chasis = QLineEdit(self.customer_search_box)
        self.search_customer_chasis.setObjectName(u"search_customer_chasis")
        sizePolicy2.setHeightForWidth(self.search_customer_chasis.sizePolicy().hasHeightForWidth())
        self.search_customer_chasis.setSizePolicy(sizePolicy2)
        self.search_customer_chasis.setFont(font)
        self.search_customer_chasis.setAlignment(Qt.AlignCenter)
        self.search_customer_chasis.setDragEnabled(False)

        self.formLayout_3.setWidget(6, QFormLayout.SpanningRole, self.search_customer_chasis)

        self.search_customer_button = QPushButton(self.customer_search_box)
        self.search_customer_button.setObjectName(u"search_customer_button")
        sizePolicy4.setHeightForWidth(self.search_customer_button.sizePolicy().hasHeightForWidth())
        self.search_customer_button.setSizePolicy(sizePolicy4)
        self.search_customer_button.setFont(font)

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.search_customer_button)

        self.cancel_search_customer_button = QPushButton(self.customer_search_box)
        self.cancel_search_customer_button.setObjectName(u"cancel_search_customer_button")
        sizePolicy4.setHeightForWidth(self.cancel_search_customer_button.sizePolicy().hasHeightForWidth())
        self.cancel_search_customer_button.setSizePolicy(sizePolicy4)
        self.cancel_search_customer_button.setFont(font)

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.cancel_search_customer_button)


        self.verticalLayout.addWidget(self.customer_search_box)

        self.emptyRowFrame = QFrame(self.left_frame)
        self.emptyRowFrame.setObjectName(u"emptyRowFrame")

        self.verticalLayout.addWidget(self.emptyRowFrame)


        self.gridLayout_4.addWidget(self.left_frame, 0, 0, 1, 1)

        self.middle_frame = QFrame(self.centralwidget)
        self.middle_frame.setObjectName(u"middle_frame")
        self.middle_frame.setMinimumSize(QSize(0, 450))
        self.middle_frame.setFrameShape(QFrame.Panel)
        self.middle_frame.setFrameShadow(QFrame.Sunken)
        self.middle_frame.setLineWidth(5)
        self.middle_frame.setMidLineWidth(5)
        self.verticalLayout_4 = QVBoxLayout(self.middle_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.user_data_frame = QFrame(self.middle_frame)
        self.user_data_frame.setObjectName(u"user_data_frame")
        self.user_data_frame.setFrameShape(QFrame.Panel)
        self.user_data_frame.setFrameShadow(QFrame.Raised)
        self.user_data_frame.setLineWidth(5)
        self.user_data_frame.setMidLineWidth(5)
        self.horizontalLayout_2 = QHBoxLayout(self.user_data_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(self.user_data_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_8 = QFrame(self.frame_3)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_8)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        font2 = QFont()
        font2.setPointSize(11)
        self.frame_5.setFont(font2)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.name_label = QLabel(self.frame_5)
        self.name_label.setObjectName(u"name_label")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.name_label.setFont(font3)
        self.name_label.setFrameShape(QFrame.NoFrame)
        self.name_label.setFrameShadow(QFrame.Plain)
        self.name_label.setLineWidth(0)
        self.name_label.setMidLineWidth(0)
        self.name_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.name_label)

        self.line = QFrame(self.frame_5)
        self.line.setObjectName(u"line")
        self.line.setFont(font2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.surname_label = QLabel(self.frame_5)
        self.surname_label.setObjectName(u"surname_label")
        self.surname_label.setFont(font3)
        self.surname_label.setFrameShape(QFrame.NoFrame)
        self.surname_label.setFrameShadow(QFrame.Plain)
        self.surname_label.setLineWidth(0)
        self.surname_label.setMidLineWidth(0)
        self.surname_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.surname_label)

        self.line_2 = QFrame(self.frame_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFont(font2)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.phone_label = QLabel(self.frame_5)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setFont(font3)
        self.phone_label.setFrameShape(QFrame.NoFrame)
        self.phone_label.setFrameShadow(QFrame.Plain)
        self.phone_label.setLineWidth(0)
        self.phone_label.setMidLineWidth(0)
        self.phone_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.phone_label)

        self.line_3 = QFrame(self.frame_5)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFont(font2)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_3)

        self.vehicle_label = QLabel(self.frame_5)
        self.vehicle_label.setObjectName(u"vehicle_label")
        self.vehicle_label.setFont(font3)
        self.vehicle_label.setFrameShape(QFrame.NoFrame)
        self.vehicle_label.setFrameShadow(QFrame.Plain)
        self.vehicle_label.setLineWidth(0)
        self.vehicle_label.setMidLineWidth(0)
        self.vehicle_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.vehicle_label)

        self.line_4 = QFrame(self.frame_5)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFont(font2)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_4)

        self.plates_label = QLabel(self.frame_5)
        self.plates_label.setObjectName(u"plates_label")
        self.plates_label.setFont(font3)
        self.plates_label.setFrameShape(QFrame.NoFrame)
        self.plates_label.setFrameShadow(QFrame.Plain)
        self.plates_label.setLineWidth(0)
        self.plates_label.setMidLineWidth(0)
        self.plates_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.plates_label)

        self.line_5 = QFrame(self.frame_5)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFont(font2)
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_5)

        self.chasis_label = QLabel(self.frame_5)
        self.chasis_label.setObjectName(u"chasis_label")
        self.chasis_label.setFont(font3)
        self.chasis_label.setFrameShape(QFrame.NoFrame)
        self.chasis_label.setFrameShadow(QFrame.Plain)
        self.chasis_label.setLineWidth(0)
        self.chasis_label.setMidLineWidth(0)
        self.chasis_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.chasis_label)

        self.line_6 = QFrame(self.frame_5)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFont(font2)
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_6)

        self.ID_label = QLabel(self.frame_5)
        self.ID_label.setObjectName(u"ID_label")
        self.ID_label.setFont(font3)
        self.ID_label.setFrameShape(QFrame.NoFrame)
        self.ID_label.setFrameShadow(QFrame.Plain)
        self.ID_label.setLineWidth(0)
        self.ID_label.setMidLineWidth(0)
        self.ID_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.ID_label)

        self.line_7 = QFrame(self.frame_5)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFont(font2)
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_7)


        self.horizontalLayout_4.addWidget(self.frame_5)

        self.line_9 = QFrame(self.frame_3)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_9)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.name_text_data = QLabel(self.frame_6)
        self.name_text_data.setObjectName(u"name_text_data")
        self.name_text_data.setFont(font3)
        self.name_text_data.setFrameShape(QFrame.NoFrame)
        self.name_text_data.setFrameShadow(QFrame.Plain)
        self.name_text_data.setLineWidth(0)
        self.name_text_data.setMidLineWidth(0)
        self.name_text_data.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.name_text_data)

        self.line_11 = QFrame(self.frame_6)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_11)

        self.surname_text_data = QLabel(self.frame_6)
        self.surname_text_data.setObjectName(u"surname_text_data")
        self.surname_text_data.setFont(font3)
        self.surname_text_data.setFrameShape(QFrame.NoFrame)
        self.surname_text_data.setFrameShadow(QFrame.Plain)
        self.surname_text_data.setLineWidth(0)
        self.surname_text_data.setMidLineWidth(0)
        self.surname_text_data.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.surname_text_data)

        self.line_12 = QFrame(self.frame_6)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_12)

        self.phone_text_data = QLabel(self.frame_6)
        self.phone_text_data.setObjectName(u"phone_text_data")
        self.phone_text_data.setFont(font3)
        self.phone_text_data.setFrameShape(QFrame.NoFrame)
        self.phone_text_data.setFrameShadow(QFrame.Plain)
        self.phone_text_data.setLineWidth(0)
        self.phone_text_data.setMidLineWidth(0)
        self.phone_text_data.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.phone_text_data)

        self.line_13 = QFrame(self.frame_6)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_13)

        self.vehicle_text_data = QLabel(self.frame_6)
        self.vehicle_text_data.setObjectName(u"vehicle_text_data")
        self.vehicle_text_data.setFont(font3)
        self.vehicle_text_data.setFrameShape(QFrame.NoFrame)
        self.vehicle_text_data.setFrameShadow(QFrame.Plain)
        self.vehicle_text_data.setLineWidth(0)
        self.vehicle_text_data.setMidLineWidth(0)
        self.vehicle_text_data.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.vehicle_text_data)

        self.line_14 = QFrame(self.frame_6)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_14)

        self.plates_text_data = QLabel(self.frame_6)
        self.plates_text_data.setObjectName(u"plates_text_data")
        self.plates_text_data.setFont(font3)
        self.plates_text_data.setFrameShape(QFrame.NoFrame)
        self.plates_text_data.setFrameShadow(QFrame.Plain)
        self.plates_text_data.setLineWidth(0)
        self.plates_text_data.setMidLineWidth(0)
        self.plates_text_data.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.plates_text_data)

        self.line_15 = QFrame(self.frame_6)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_15)

        self.chasis_text_data = QLabel(self.frame_6)
        self.chasis_text_data.setObjectName(u"chasis_text_data")
        self.chasis_text_data.setFont(font3)
        self.chasis_text_data.setFrameShape(QFrame.NoFrame)
        self.chasis_text_data.setFrameShadow(QFrame.Plain)
        self.chasis_text_data.setLineWidth(0)
        self.chasis_text_data.setMidLineWidth(0)
        self.chasis_text_data.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.chasis_text_data)

        self.line_16 = QFrame(self.frame_6)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_16)

        self.id_text_data = QLabel(self.frame_6)
        self.id_text_data.setObjectName(u"id_text_data")
        self.id_text_data.setFont(font3)
        self.id_text_data.setFrameShape(QFrame.NoFrame)
        self.id_text_data.setFrameShadow(QFrame.Plain)
        self.id_text_data.setLineWidth(0)
        self.id_text_data.setMidLineWidth(0)
        self.id_text_data.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.id_text_data)

        self.line_17 = QFrame(self.frame_6)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_17)


        self.horizontalLayout_4.addWidget(self.frame_6)

        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(3, 8)

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.line_10 = QFrame(self.user_data_frame)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_10)


        self.verticalLayout_4.addWidget(self.user_data_frame)

        self.user_work_orders_frame = QFrame(self.middle_frame)
        self.user_work_orders_frame.setObjectName(u"user_work_orders_frame")
        self.user_work_orders_frame.setFrameShape(QFrame.Panel)
        self.user_work_orders_frame.setFrameShadow(QFrame.Raised)
        self.user_work_orders_frame.setLineWidth(5)
        self.user_work_orders_frame.setMidLineWidth(5)

        self.verticalLayout_4.addWidget(self.user_work_orders_frame)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 6)

        self.gridLayout_4.addWidget(self.middle_frame, 0, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 3)
        self.gridLayout_4.setColumnStretch(1, 10)
        self.gridLayout_4.setColumnStretch(2, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.add_customer_name, self.add_customer_surname)
        QWidget.setTabOrder(self.add_customer_surname, self.add_customer_phone)
        QWidget.setTabOrder(self.add_customer_phone, self.add_customer_vehicle)
        QWidget.setTabOrder(self.add_customer_vehicle, self.add_customer_plates)
        QWidget.setTabOrder(self.add_customer_plates, self.add_customer_chasis)
        QWidget.setTabOrder(self.add_customer_chasis, self.save_new_customer_button)
        QWidget.setTabOrder(self.save_new_customer_button, self.cancel_new_customer_button)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Budget Flow", None))
        ___qtablewidgetitem = self.customer_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Ime", None));
        ___qtablewidgetitem1 = self.customer_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Prezime", None));
        ___qtablewidgetitem2 = self.customer_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Telefon", None));
        ___qtablewidgetitem3 = self.customer_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Vozilo", None));
        ___qtablewidgetitem4 = self.customer_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        self.delete_selected_table_button.setText(QCoreApplication.translate("MainWindow", u"Obri\u0161i", None))
        self.clear_table_button.setText(QCoreApplication.translate("MainWindow", u"Poni\u0161ti", None))
        self.filter_table_button.setText(QCoreApplication.translate("MainWindow", u"Filtriraj", None))
        self.populate_table_button.setText(QCoreApplication.translate("MainWindow", u"Prika\u017ei Sve", None))
        self.add_customer_label.setText(QCoreApplication.translate("MainWindow", u"Nova Mu\u0161terija", None))
        self.add_customer_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ime", None))
        self.add_customer_surname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prezime", None))
        self.add_customer_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefon", None))
        self.add_customer_vehicle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Vozilo", None))
        self.add_customer_plates.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Registracija", None))
        self.add_customer_chasis.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Broj \u0160asije", None))
        self.save_new_customer_button.setText(QCoreApplication.translate("MainWindow", u"Unos", None))
        self.cancel_new_customer_button.setText(QCoreApplication.translate("MainWindow", u"Odustani", None))
        self.search_customer_label.setText(QCoreApplication.translate("MainWindow", u"Pretraga Mu\u0161terije", None))
        self.search_customer_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ime", None))
        self.search_customer_surname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prezime", None))
        self.search_customer_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefon", None))
        self.search_customer_vehicle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Vozilo", None))
        self.search_customer_plates.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Registracija", None))
        self.search_customer_chasis.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Broj \u0160asije", None))
        self.search_customer_button.setText(QCoreApplication.translate("MainWindow", u"Tra\u017ei", None))
        self.cancel_search_customer_button.setText(QCoreApplication.translate("MainWindow", u"Odustani", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Ime:", None))
        self.surname_label.setText(QCoreApplication.translate("MainWindow", u"Prezime:", None))
        self.phone_label.setText(QCoreApplication.translate("MainWindow", u"#Telefon:", None))
        self.vehicle_label.setText(QCoreApplication.translate("MainWindow", u"Vozilo:", None))
        self.plates_label.setText(QCoreApplication.translate("MainWindow", u"#Registracija:", None))
        self.chasis_label.setText(QCoreApplication.translate("MainWindow", u"#\u0160asija:", None))
        self.ID_label.setText(QCoreApplication.translate("MainWindow", u"#ID:", None))
        self.name_text_data.setText("")
        self.surname_text_data.setText("")
        self.phone_text_data.setText("")
        self.vehicle_text_data.setText("")
        self.plates_text_data.setText("")
        self.chasis_text_data.setText("")
        self.id_text_data.setText("")
    # retranslateUi

