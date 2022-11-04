import sys
from PySide6 import QtWidgets

from ui import main_window


class App(QtWidgets.QMainWindow, main_window.Ui_MainWindow):  # Initialize the class of UI
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
