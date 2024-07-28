from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])


class MainWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("To do App")
        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.left_layout = QtWidgets.QVBoxLayout()
        self.right_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.right_layout)
        
        self.title = QtWidgets.QLineEdit()
        self.add_btn = QtWidgets.QPushButton("Add Item")
        self.edit_btn = QtWidgets.QPushButton("Edit")
        self.add_btn.clicked.connect(self.add_item)

        self.left_layout.addWidget(self.title)
        self.left_layout.addWidget(self.add_btn)
        self.right_layout.addWidget(self.edit_btn)

    def add_item(self):
        print("hello")

widget = MainWindow()
widget.resize(800, 600)
widget.show()

app.exec_()