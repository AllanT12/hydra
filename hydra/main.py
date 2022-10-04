import string
import struct
import sys
import socket
import _thread
from getmac import get_mac_address
from PyQt5 import QtWidgets, QtCore
from sniffer import Ui_mainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(window)
    window.show()
    app.exec_()
    sys.exit()








