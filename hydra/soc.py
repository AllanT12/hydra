import socket

from PyQt5.QtCore import QRunnable, pyqtSlot


class Sock(QRunnable):
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    raw_data = None
    @pyqtSlot()
    def run(self):
        self.raw_data, addr = self.s.recvfrom(65565)
