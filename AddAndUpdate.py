import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow
import Kapychino
from PyQt5 import uic


class AddCoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setWindowTitle('Редактор')
        self.btn_add.clicked.connect(self.add_coffee)
        self.btn_update.clicked.connect(self.update_coffee)
        self.close_form.clicked.connect(self.close_my)

    def close_my(self):
        self.my = Kapychino.CoffeeApp()
        self.my.show()
        AddCoffeeApp().hide()
        self.hide()

    def add_coffee(self):
        try:
            self.error_label.setText('')
            con = sqlite3.connect('coffee.sqlite')
            cur = con.cursor()
            total = len(cur.execute("""SELECT * FROM inf_coffee""").fetchall())
            result = cur.execute(f'''INSERT INTO inf_coffee(id, Variety_name, Roast_degree, 
            Ground_beans, Flavor_description, Price, Packing_volume) VALUES('{total + 1}', '{self.name.text()}', 
            '{self.stepen.text()}', '{self.mol.text()}', '{self.ground.text()}', '{self.price.text()}', 
            '{self.volume.text()}')''').fetchall()
            con.commit()
            con.close()
        except sqlite3.OperationalError:
            self.error_label.setText('Not all fields are filled or correct')

    def update_coffee(self):
        try:
            con = sqlite3.connect('coffee.sqlite')
            cur = con.cursor()
            cur.execute(f"""UPDATE inf_coffee
            SET '{self.my_pow.text()}' = '{self.my_rename.text()}'
            WHERE id = '{self.id_my.text()}'""")
            con.commit()
            con.close()
        except sqlite3.OperationalError:
            self.error_label.setText('Not all fields are filled or correct')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddCoffeeApp()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())