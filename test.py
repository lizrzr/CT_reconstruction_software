from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLabel, QFileDialog, QProgressBar, QMenu, QMenuBar, QStatusBar, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

class CTReconstructionSystem(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Menu bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction('Load Image', self.loadImage)
        fileMenu.addAction('Exit', self.close)

        # Status bar
        self.statusBar().showMessage('Ready')

        # Central widget
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        hbox = QHBoxLayout()

        # Image displays
        self.imageLabel1 = QLabel(self)
        self.imageLabel1.setPixmap(QPixmap())
        hbox.addWidget(self.imageLabel1)

        self.imageLabel2 = QLabel(self)
        self.imageLabel2.setPixmap(QPixmap())
        hbox.addWidget(self.imageLabel2)

        self.imageLabel3 = QLabel(self)
        self.imageLabel3.setPixmap(QPixmap())
        hbox.addWidget(self.imageLabel3)

        vbox = QVBoxLayout()

        # Text input
        self.textEdit = QTextEdit()
        vbox.addWidget(self.textEdit)

        # SOD and SDD input
        self.sodInput = QLineEdit()
        self.sodInput.setPlaceholderText('SOD')
        vbox.addWidget(self.sodInput)

        self.sddInput = QLineEdit()
        self.sddInput.setPlaceholderText('SDD')
        vbox.addWidget(self.sddInput)

        # Progress bar
        self.progressBar = QProgressBar(self)
        vbox.addWidget(self.progressBar)

        # Buttons
        self.btn1 = QPushButton('Start Reconstruction', self)
        self.btn1.clicked.connect(self.startReconstruction)
        vbox.addWidget(self.btn1)

        hbox.addLayout(vbox)

        centralWidget.setLayout(hbox)

        self.setWindowTitle('CT Reconstruction System')

        
        self.setGeometry(300, 300, 800, 600)
        self.show()

    def loadImage(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', './')
        if fname:
            self.imageLabel1.setPixmap(QPixmap(fname))
            self.imageLabel2.setPixmap(QPixmap(fname))
            self.imageLabel3.setPixmap(QPixmap(fname))

    def startReconstruction(self):
        # Add your reconstruction code here
        # Update the progress bar as the reconstruction progresses
        pass

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = CTReconstructionSystem()
    sys.exit(app.exec_())