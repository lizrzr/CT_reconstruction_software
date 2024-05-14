from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QProgressBar, QTextEdit
from Ui_MainWindow import Ui_MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())