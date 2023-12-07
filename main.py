from logic import *

def main() -> None:
    """
    This is the main function for the entire project.
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()