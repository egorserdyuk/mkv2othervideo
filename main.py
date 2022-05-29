import sys
from PyQt5 import QtWidgets

from ui import design


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):  # Initialize the class of UI
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
