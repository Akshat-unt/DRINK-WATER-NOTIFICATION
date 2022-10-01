import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


def timer(interval, times):
    import time
    from plyer import notification

    for _ in range(times):
        time.sleep(interval)
        notification.notify(
            title="Please Drink Water Now",
            message="Drinking water is good for your health. "
                    "Drinking adequate water can prevent dehydration and keep your body working properly. "
                    "It can also help you lose weight and boost your energy.",
            app_icon="water.ico",
            timeout=12
        )

# a program that reminds you to drink water every x minutes for y times
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Drink Water Notification'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Create widget
        self.label1 = QLabel(
            'Enter the number of minutes you want to be reminded to drink water')
        self.label2 = QLabel(
            'Enter the number of times you want to be reminded to drink water')
        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.button = QPushButton('Start', self)
        self.button.setToolTip('This is an example button')
        self.button.move(100, 70)
        self.button.clicked.connect(self.on_click)

            # Create a grid layout
        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.textbox1, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.textbox2, 1, 1)
        layout.addWidget(self.button, 2, 0)

            # Set the layout
        self.setLayout(layout)

            # Show the app
        self.show()

    @pyqtSlot()
    def on_click(self):
        interval = int(self.textbox1.text())
        times = int(self.textbox2.text())
        timer(interval, times)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
