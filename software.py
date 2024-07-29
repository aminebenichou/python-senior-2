# to install pyqt5 run the following command in your terminal
# pip install PyQt5
# if you are using vscode press ctrl + J to open terminal
# from db imports are the functions we created in our db.py file
# functools is an already installed library with python
# for any informations contact ceo@dokkitdz.com
from functools import partial
from PyQt5 import QtWidgets
from db import insertItem, retrieveItems, editItem, deleteItem
app = QtWidgets.QApplication([])


class MainWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        # super.init is required
        super().__init__()
        
        
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
    # inserting items to db 
    def add_item(self):
        insertItem(self.title.text())
        self.refresh()
        self.title.clear()
    # editing items from db it requires id and the data you pass data should be a string
    def edit_item(self, itemid):
        editItem(data=self.title.text(), itemid=itemid)
        self.refresh()
        self.title.clear()

    # gets items from db and creates buttons with the labels 
    # we used partial function to make it easy to send params to the connected functions
    def display_items(self):
        items = retrieveItems()
        for item in items:
            edit_btn = QtWidgets.QPushButton("Edit")
            self.right_layout.addWidget(QtWidgets.QLabel(item[1]))
            self.right_layout.addWidget(edit_btn)
            edit_btn.clicked.connect(partial(self.edit_item, item[0]))
            delete_btn = QtWidgets.QPushButton("Delete")
            self.right_layout.addWidget(delete_btn)
            delete_btn.clicked.connect(partial(self.delete_item, item[0]))

    # clears all items and displays them again this only works with the right layout
    def refresh(self):
        # this for statement counts all of the widgets in the rightlayout
        for i in reversed(range(self.right_layout.count())):
            # the line under is to delete eachitem in the right layout 
            self.right_layout.itemAt(i).widget().deleteLater()
        
        self.display_items()
    # deleting items from db 
    # the item argument should be an integer
    def delete_item(self, item):
        deleteItem(item)
        self.refresh()
widget = MainWindow()
widget.resize(800, 600)
widget.show()

app.exec_()