import sys


from interface.form import *
from random import randint
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import time


class MyWin(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.get_started)
        self.ui.pushButton_2.clicked.connect(sys.exit)
        self.ui.commandLinkButton.clicked.connect(self.ui.textEdit.clear)
        self.setWindowIcon(QIcon('interface/icon.ico'))
    def get_started(self):
        sorting = self.ui.cb.currentText()
        if sorting == "Сортировка вставками":
            self.insertion_sorting_solo()
        elif sorting == "Сортировка Шелла":
            self.shell_1()
        elif sorting == "С.Ш. с использованием посл. Кнута":
            self.shell_2()

    def data_gen(self):
        list = []
        for i in range(0, int(self.ui.doubleSpinBox.value())):
            list.append(randint(0, 100000))

        return list

    def insertion_sorting_solo(self):
        arr = self.data_gen()
        self.ui.textEdit.insertPlainText("Исходная последовательность: \t" + ", ".join(map(str, arr)) + "\n")
        start = time.time()
        for index in range(1, len(arr)):
            value = arr[index]
            i = index - 1
            while i >= 0:
                if value < arr[i]:
                    arr[i + 1] = arr[i]
                    arr[i] = value
                    i -= 1
                else:
                    break
            self.ui.textEdit.insertPlainText("\t\t\t" + ", ".join(map(str, arr)) + "\n")
        finish = time.time()
        self.ui.textEdit.insertPlainText("Полученный список: \t\t" + ", ".join(map(str, arr)) + "\n\n")
        self.ui.timelabel.setText("Затраченное время: %.6f c" % (finish - start))

    def shell_1(self):
        def shell_insertion(array, low, gap):
            for i in range(low + gap, len(array), gap):
                tmp = array[i]
                pos = i
                while pos >= gap and array[pos - gap] > tmp:
                    array[pos] = array[pos - gap]
                    pos = pos - gap
                array[pos] = tmp

        start = time.time()
        array = self.data_gen()
        self.ui.textEdit.insertPlainText("Исходная последовательность: \t" + ", ".join(map(str, array)) + "\n")
        gap = len(array) // 2
        while gap > 0:
            for i in range(gap):
                shell_insertion(array, i, gap)
            self.ui.textEdit.insertPlainText(
                'После сортировки массива с шагом ' + str(gap) + ': \t' + ", ".join(map(str, array)) + "\n")
            gap //= 2
        finish = time.time()
        self.ui.timelabel.setText("Затраченное время: %.6f c" % (finish - start))
        self.ui.textEdit.insertPlainText("Итоговый отсортированный массив:  \t" + ", ".join(map(str, array)) + "\n\n")

    def shell_2(self):
        def shell_insertion(array, low, gap):
            for i in range(low + gap, len(array), gap):
                tmp = array[i]
                pos = i
                while pos >= gap and array[pos - gap] > tmp:
                    array[pos] = array[pos - gap]
                    pos = pos - gap
                array[pos] = tmp

        start = time.time()
        array = self.data_gen()
        self.ui.textEdit.insertPlainText("Исходная последовательность: \t" + ", ".join(map(str, array)) + "\n")
        gap_list = []

        for i in range(1, 20):
            gap_list.append(int(0.5 * (3 ** i - 1)))
        if len(array) == 2:
            gap = 1
        for i in gap_list:
            if i <= len(array) // 3:
                gap = i

        while gap > 0:
            for i in range(gap):
                shell_insertion(array, i, gap)
            self.ui.textEdit.insertPlainText(
                'После сортировки массива с шагом ' + str(gap) + ': \t' + ", ".join(map(str, array)) + "\n")
            gap //= 3
        finish = time.time()
        self.ui.timelabel.setText("Затраченное время: %.6f c" % (finish - start))
        self.ui.textEdit.insertPlainText("Итоговый отсортированный массив:  \t" + ", ".join(map(str, array)) + "\n\n")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
