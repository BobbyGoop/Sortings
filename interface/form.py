# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(891, 478)
        Frame.setMinimumSize(QtCore.QSize(891, 478))
        Frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Frame.setWindowIcon(icon)
        Frame.setWindowOpacity(1.0)
        Frame.setAutoFillBackground(False)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gridLayout_2 = QtWidgets.QGridLayout(Frame)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cb = QtWidgets.QComboBox(Frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb.setFont(font)
        self.cb.setObjectName("cb")
        self.cb.addItem("")
        self.cb.addItem("")
        self.cb.addItem("")
        self.gridLayout_2.addWidget(self.cb, 1, 11, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(140, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(40, 25))
        self.pushButton.setSizeIncrement(QtCore.QSize(0, 10))
        self.pushButton.setBaseSize(QtCore.QSize(15, 0))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 5, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy)
        self.doubleSpinBox.setMinimumSize(QtCore.QSize(25, 0))
        self.doubleSpinBox.setMaximumSize(QtCore.QSize(110, 25))
        self.doubleSpinBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.doubleSpinBox.setWrapping(True)
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setMaximum(9999999999.0)
        self.doubleSpinBox.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSpinBox.setProperty("value", 4.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_2.addWidget(self.doubleSpinBox, 0, 4, 1, 4)
        self.label = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.gridLayout_2.addWidget(self.commandLinkButton, 5, 11, 1, 1)
        self.label_2 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 11, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 869, 328))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit.setLineWidth(0)
        self.textEdit.setMidLineWidth(0)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setReadOnly(True)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setTabStopDistance(86.0)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 2, 0, 2, 12)
        self.label_3 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 3)
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(140, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(40, 25))
        self.pushButton_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_2.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 5, 1, 1, 1)
        self.timelabel = QtWidgets.QLabel(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timelabel.sizePolicy().hasHeightForWidth())
        self.timelabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.timelabel.setFont(font)
        self.timelabel.setObjectName("timelabel")
        self.gridLayout_2.addWidget(self.timelabel, 6, 0, 1, 5)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Сортировка"))
        self.cb.setItemText(0, _translate("Frame", "Сортировка вставками"))
        self.cb.setItemText(1, _translate("Frame", "Сортировка Шелла"))
        self.cb.setItemText(2, _translate("Frame", "С.Ш. с использованием посл. Кнута"))
        self.pushButton.setText(_translate("Frame", "Запустить программу"))
        self.label.setText(_translate("Frame", "Введите колличество элементов последовательности:"))
        self.commandLinkButton.setText(_translate("Frame", "Очистить поле"))
        self.label_2.setText(_translate("Frame", "Выберите метод сортировки:"))
        self.textEdit.setHtml(_translate("Frame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Franklin Gothic Book\'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Frame", "Результаты сортировки:"))
        self.pushButton_2.setText(_translate("Frame", "Выход"))
        self.timelabel.setText(_translate("Frame", "Затраченное время:"))
