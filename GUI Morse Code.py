import sys

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.label = QLabel('Enter some text to translate into Morse Code:', self)
        self.lineInput = QLineEdit(self)
        self.buttonEncode = QPushButton('Encode', self)
        self.buttonClear = QPushButton('Clear', self)
        self.response = QLabel("", self)
        self.title = "Morse Code Encoder"
        font = QFont("Times New Roman", 14, 60, False)
        self.setFont(font)

        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(23, 33, 53))
        self.palette.setColor(QPalette.WindowText, Qt.lightGray)
        self.palette.setColor(QPalette.ButtonText, Qt.black)

        self.setPalette(self.palette)
        self.create_translator()

    def create_translator(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 600, 260)

        self.label.move(100, 10)
        self.label.resize(360, 40)
        self.label.setStyleSheet("color: whitesmoke;")

        self.lineInput.move(140, 50)
        self.lineInput.resize(255, 40)

        self.response.move(20, 140)
        self.response.resize(1024, 80)
        self.response.setMaximumWidth(500)
        self.response.setStyleSheet("border: 1px solid black; color: whitesmoke;")
        self.response.setWordWrap(True)

        self.buttonEncode.move(120, 100)

        self.buttonClear.move(360, 100)
        self.buttonClear.resize(60, 30)
        self.buttonClear.setStyleSheet("background-color: rgb(180,20,40);")

        self.buttonClear.clicked.connect(self.evt_clear)
        self.buttonEncode.clicked.connect(self.evt_click)
        self.show()

    @pyqtSlot()
    def evt_click(self):
        morse = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '..-.',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '.-.',
            's': '...',
            't': '-',
            'u': '..-',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----',
            '.': '.-.-.-',
            ',': '--..--',
            '?': '..--..',
            "'": '.----.',
            '/': '-..-.',
            '(': '-.--.',
            ')': '-.--.-',
            '&': '.-...',
            ':': '---...',
            ';': '-.-.-.',
            '=': '-...-',
            '+': '.-.-.',
            '-': '-....-',
            '_': '..--.-',
            '"': '.-..-.',
            '$': '...-..-',
            '!': '-.-.--',
            '@': '.--.-.',
            ' ': '/',
        }
        new_list = []
        raw_sentence = self.lineInput.text()
        if raw_sentence != "":
            sentence = raw_sentence.lower()
            sentence_list = list(sentence)
            for c in sentence_list:
                for k, v in morse.items():
                    if c == k:
                        new_list += v + "   "
            morse_translation = ''.join(new_list)

            self.response.setText(f"'{raw_sentence}'" + " translates to:\n" + morse_translation)
            self.lineInput.setText("")

    def evt_clear(self):
        self.lineInput.setText("")
        self.response.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
