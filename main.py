import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Эспрессо')
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM inf_coffee""").fetchall()
        self.table.setColumnCount(7)
        self.table.setRowCount(len(result))
        for elem in result:
            print(elem)
        x = 0
        for elem in result:
            y = 0
            for i in elem:
                self.table.setItem(x, y, QTableWidgetItem(str(i)))
                print('g')
                y += 1
            x += 1
        self.table.resizeColumnsToContents()
        con.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
