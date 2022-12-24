from PySide6.QtWidgets import QApplication, QWidget
# processing system arguments 
import sys

# QtApplication in an instance
app = QApplication(sys.argv)

# creates the application window
window = QWidget()
window.show()

if __name__ == "__main__":
    # starts the event app
    app.exec()