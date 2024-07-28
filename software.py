from functools import partial
from PyQt5 import QtWidgets
from db import insertItem, retrieveItems, editItem
app = QtWidgets.QApplication([])


class MainWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        print(retrieveItems())
        
        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.left_layout = QtWidgets.QVBoxLayout()
        self.right_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.right_layout)
        
        self.title = QtWidgets.QLineEdit()
        self.add_btn = QtWidgets.QPushButton("Add Item")
        self.add_btn.clicked.connect(self.add_item)

        self.left_layout.addWidget(self.title)
        self.left_layout.addWidget(self.add_btn)
        self.display_items()
    def add_item(self):
        insertItem(self.title.text())
    def edit_item(self, itemid):
        editItem(data=self.title.text(), itemid=itemid)
    def display_items(self):
        items = retrieveItems()
        for item in items:
            edit_btn = QtWidgets.QPushButton("Edit")
            self.right_layout.addWidget(QtWidgets.QLabel(item[1]))
            self.right_layout.addWidget(edit_btn)
            edit_btn.clicked.connect(partial(self.edit_item, item[0]))

widget = MainWindow()
widget.resize(800, 600)
widget.show()

app.exec_()