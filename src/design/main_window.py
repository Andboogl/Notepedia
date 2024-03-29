# Form implementation generated from reading ui file 'design/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class MainWindowDesign(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 239)
        MainWindow.setStyleSheet('color: black;')
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 811, 241))
        self.frame.setStyleSheet("background: rgb(141, 141, 141);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(310, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.create_article = QtWidgets.QPushButton(parent=self.frame)
        self.create_article.setGeometry(QtCore.QRect(140, 70, 541, 61))
        self.create_article.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.create_article.setStyleSheet("QPushButton {\n"
"    background: rgb(108, 108, 108);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: rgb(124, 124, 124);\n"
"}")
        self.create_article.setObjectName("create_article")
        self.look_for_articles = QtWidgets.QPushButton(parent=self.frame)
        self.look_for_articles.setGeometry(QtCore.QRect(140, 140, 541, 61))
        self.look_for_articles.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.look_for_articles.setStyleSheet("QPushButton {\n"
"    background: rgb(108, 108, 108);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: rgb(124, 124, 124);\n"
"}")
        self.look_for_articles.setObjectName("look_for_articles")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NotePedia"))
        self.label.setText(_translate("MainWindow", "Головна"))
        self.create_article.setText(_translate("MainWindow", "Створити статью"))
        self.look_for_articles.setText(_translate("MainWindow", "Дивитись статьї"))
