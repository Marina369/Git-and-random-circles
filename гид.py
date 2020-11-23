import sys
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QColor
from random import choice
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.colors = ['mediumorchid', 'blueviolet', 'navy', 'royalblue', 'deeppink', 'red', 'black',
                       'darkslategrey', 'limegreen', 'darkgreen', 'yellow', 'darkorange', 'orange']

    def initUI(self):
        self.setGeometry(200, 200, 700, 700)
        self.setWindowTitle('Git и случайные окружности')

        self.pushButton = QPushButton('тык сюда', self)
        self.pushButton.move(310, 310)
        self.pushButton.resize(80, 80)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(choice(self.colors)))
        x = random.randint(0, 660)
        y = random.randint(0, 530)
        d = random.randint(10, 150)
        qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
