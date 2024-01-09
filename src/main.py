"""Main module. Runs application"""


from sys import argv
from PyQt6.QtWidgets import QApplication
from windows import MainWindow


def main() -> None:
    """This function runs application"""
    app = QApplication(argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()


if __name__ == '__main__':
    main()
