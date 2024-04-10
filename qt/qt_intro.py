from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
# processing system arguments 
import sys

# QtApplication in an instance
app = QApplication(sys.argv)

# creates the application window
window = QMainWindow()

# set title of the app's window
window.setWindowTitle("My first window Widget")
window.show()

# create button 
button = QPushButton("Randomize")

# set the button on central position in the app
window.setCentralWidget(button)


if __name__ == "__main__":
    # starts the event app
    app.exec()