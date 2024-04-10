from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStatusBar, QWidget
import sys

class buttonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Button Holder app")
        
        button = QPushButton("Push me")
        
        self.setCentralWidget(button)
app = QApplication(sys.argv)

window = buttonHolder()

window.show()

app.exec()