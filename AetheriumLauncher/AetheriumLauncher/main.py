from launcher.ui import LauncherUI
from PySide6.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LauncherUI()
    window.show()
    sys.exit(app.exec())
