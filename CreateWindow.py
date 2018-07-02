import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, \
     QPushButton,   QLabel , QComboBox
import pyqtgraph as pg
from PyQt5 import QtGui, QtCore


class Create(QMainWindow):

    def __init__(self):
        super().__init__()

        # self.initUI()

    def CreateUI(self):
        self.Layout = pg.LayoutWidget()
        self.LayoutInfo = pg.LayoutWidget()
        self.LayoutButton = pg.LayoutWidget()

        self.setGeometry(100, 100, 300, 200)

        self.setWindowTitle('Create Contact')
        self.setCentralWidget(self.Layout)


        # Create label Name
        self.NameLabel = QLabel()
        self.NameLabel.setText("Name")

        self.NameText = QtGui.QLineEdit() #QPlainTextEdit()

        # Create label age
        self.AgeLabel = QLabel()
        self.AgeLabel.setText("Age")

        self.AgeText = QtGui.QLineEdit()

        # Create label mobile
        self.MobileLabel = QLabel()
        self.MobileLabel.setText("Mobile")


        self.MobileText =QtGui.QLineEdit()
        self.MobileText.setValidator(QtGui.QIntValidator())
        # self.MobileText.textChanged.connect(self.validation)

        # Create label Gender
        self.GenderLabel = QLabel()
        self.GenderLabel.setText("Gender")

        self.GenderText = QtGui.QLineEdit()


        # Create label Address
        self.AddressLabel = QLabel()
        self.AddressLabel.setText("Address")

        self.AdderssText = QtGui.QLineEdit()


        # Create label Group
        self.GroupLabel = QLabel()
        self.GroupLabel.setText("Group")

        # self.GroupText = QtGui.QLineEdit()
        self.GroupText = QComboBox()
        self.GroupText.addItem("Default")
        self.GroupText.addItem("Business")

        # Delete Button Tab 1
        self.SaveButton = QPushButton()
        self.SaveButton.setText("Save")

        # 'Name', 'Age', 'Mobile', 'Gender', 'Address'

        self.LayoutInfo.addWidget(self.NameLabel,0,0)
        self.LayoutInfo.addWidget(self.NameText,0,1)

        self.LayoutInfo.addWidget(self.AgeLabel, 1, 0)
        self.LayoutInfo.addWidget(self.AgeText, 1, 1)

        self.LayoutInfo.addWidget(self.MobileLabel, 2, 0)
        self.LayoutInfo.addWidget(self.MobileText, 2, 1)

        self.LayoutInfo.addWidget(self.GenderLabel, 3, 0)
        self.LayoutInfo.addWidget(self.GenderText, 3, 1)

        self.LayoutInfo.addWidget(self.AddressLabel, 4, 0)
        self.LayoutInfo.addWidget(self.AdderssText, 4, 1)

        self.LayoutInfo.addWidget(self.GroupLabel, 5, 0)
        self.LayoutInfo.addWidget(self.GroupText, 5, 1)

        self.LayoutButton.addWidget(self.SaveButton, 0, 0)

        self.Layout.addWidget(self.LayoutInfo, 0, 0)
        self.Layout.addWidget(self.LayoutButton, 1, 0)

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    UI = Create()
    sys.exit(app.exec_())