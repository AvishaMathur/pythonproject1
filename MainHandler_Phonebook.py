import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QTableWidget, \
    QTableWidgetItem, QLayout, QPushButton,QHeaderView, QTabWidget, QWidget
from PyQt5.QtGui import QIcon
import pyqtgraph as pg
from CreateWindow import Create
from PyQt5 import QtGui, QtCore



class MainHandler(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = pg.LayoutWidget()
        self.tab2 = pg.LayoutWidget()
        self.tabs.resize(300, 200)

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(200, 200, 450, 500)

        self.setWindowTitle('Phone Book')
        self.setCentralWidget(self.tabs)

        # Table Tab 1
        self.tableWidgetContactTab1 = QTableWidget()
        # self.tableWidgetContactTab1.setRowCount(2)
        self.tableWidgetContactTab1.setColumnCount(6)
        self.tableWidgetContactTab1.setHorizontalHeaderLabels(['Name', 'Age', 'Mobile', 'Gender', 'Address', 'Group'])
        self.tableWidgetContactTab1.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidgetContactTab1.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

        self.ContactListDefault = []
        self.ContactListDefault.append("Avisha")
        self.ContactListDefault.append("25")
        self.ContactListDefault.append("1234567890")
        self.ContactListDefault.append("Female")
        self.ContactListDefault.append("Jodhpur")
        self.ContactListDefault.append("Default")

        self.ContactListDefault2 = []
        self.ContactListDefault2.append("XYZ")
        self.ContactListDefault2.append("25")
        self.ContactListDefault2.append("1234247890")
        self.ContactListDefault2.append("Female")
        self.ContactListDefault2.append("Jodhpur")
        self.ContactListDefault2.append("Business")

        self.RowCount=0

        self.tableWidgetContactTab1.insertRow(self.RowCount)

        # chkBoxItem = QtGui.QTableWidgetItem()
        # chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        # chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
        # self.tableWidgetContactTab1.setItem(self.RowCount, 0, chkBoxItem)
        for col in range(0, 6):

            itemstr=str(self.ContactListDefault[col])
            item = QtGui.QTableWidgetItem(itemstr)

            # item.setFlags(QtCore.Qt.ItemIsUserCheckable |
            #               QtCore.Qt.ItemIsEnabled)


            self.tableWidgetContactTab1.setItem(self.RowCount, col, item)
            self.tableWidgetContactTab1.item(self.RowCount, col).setBackground(QtGui.QColor(255, 255, 153))
            # self.tableWidgetContactTab1.setItem(self.RowCount, col + 1, item)
            # item_1.setCheckState(QtCore.Qt.Unchecked)

        self.RowCount +=1



        self.tableWidgetContactTab1.insertRow(self.RowCount)

        # chkBoxItem = QtGui.QTableWidgetItem()
        # chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        # chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
        # self.tableWidgetContactTab1.setItem(self.RowCount, 0, chkBoxItem)

        for col in range(0, 6):
            item=str(self.ContactListDefault2[col])
            # self.tableWidgetContactTab1.setItem(self.RowCount,col+1,QTableWidgetItem( item))
            self.tableWidgetContactTab1.setItem(self.RowCount, col, QTableWidgetItem(item))
            self.tableWidgetContactTab1.item(self.RowCount, col).setBackground(QtGui.QColor(255, 255, 153))
        self.RowCount += 1


        # self.tableWidgetContactTab1.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableWidgetContactTab1.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        # Layout Tab 1
        self.ButtonlayoutContactTab1 = pg.LayoutWidget()

        # Create Button Tab 1
        self.CreateButton = QPushButton()
        self.CreateButton.setText("Create")
        self.CreateButton.clicked.connect(self.CreateDetails)

        # Update Button Tab 1
        self.EditButton = QPushButton()
        self.EditButton.setText("Edit")
        self.EditButton.clicked.connect(self.EditDetails)

        # Update Button Tab 1
        self.UpdateButton = QPushButton()
        self.UpdateButton.setText("Update")
        self.UpdateButton.clicked.connect(self.UpdateDetails)
        self.UpdateButton.setEnabled(False)

        # Delete Button Tab 1
        self.DeleteButton = QPushButton()
        self.DeleteButton.setText("Delete")
        self.DeleteButton.clicked.connect(self.DeleteDetails)
        # self.DeleteButton.setEnabled(False)

        # Tab 1
        self.ButtonlayoutContactTab1.addWidget(self.CreateButton)
        self.ButtonlayoutContactTab1.addWidget(self.EditButton)
        self.ButtonlayoutContactTab1.addWidget(self.UpdateButton)
        self.ButtonlayoutContactTab1.addWidget(self.DeleteButton)



        # Businss Group-----------------------------------------------------------------------------------
        self.RowCount_Group=0
        # Table Tab 2
        self.tableWidgetGroupTab2 = QTableWidget()
        # self.tableWidgetGroupTab2.setRowCount(1)
        self.tableWidgetGroupTab2.setColumnCount(5)
        self.tableWidgetGroupTab2.setHorizontalHeaderLabels(['Name', 'Age', 'Mobile', 'Gender', 'Address'])
        self.tableWidgetGroupTab2.setEditTriggers(QTableWidget.NoEditTriggers)

        self.tableWidgetGroupTab2.insertRow(self.RowCount_Group)

        for col in range(0, 6):
            item = str(self.ContactListDefault2[col])
            self.tableWidgetGroupTab2.setItem(self.RowCount_Group, col, QTableWidgetItem(item))
        self.RowCount_Group += 1


        # self.tableWidgetGroupTab2.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableWidgetGroupTab2.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)

        # Tab 1
        self.tab1.addWidget(self.tableWidgetContactTab1,0,0)
        self.tab1.addWidget(self.ButtonlayoutContactTab1, 1,0)

        # Tab 2
        self.tab2.addWidget(self.tableWidgetGroupTab2, 0, 0)



        # Add tabs
        self.tabs.addTab(self.tab1, "Contact List")
        self.tabs.addTab(self.tab2, "Business Group")

        self.show()

    def CreateDetails(self):

        self.AddContact = Create()
        self.AddContact.CreateUI()
        self.AddContact.SaveButton.clicked.connect(self.saveDetails)

    def saveDetails(self):
        try:
            # 'Name', 'Age', 'Mobile', 'Gender', 'Address'

            self.ContactList=[]
            NameText = self.AddContact.NameText.text() #.toPlainText()
            AgeText = self.AddContact.AgeText.text()
            MobileText = self.AddContact.MobileText.text()
            GenderText = self.AddContact.GenderText.text()
            AddressText = self.AddContact.AdderssText.text()
            GroupText= self.AddContact.GroupText.currentText()

            self.ContactList.append(NameText)
            self.ContactList.append(AgeText)
            self.ContactList.append(MobileText)
            self.ContactList.append(GenderText)
            self.ContactList.append(AddressText)
            self.ContactList.append(GroupText)

            self.tableWidgetContactTab1.insertRow(self.RowCount)
            # chkBoxItem = QtGui.QTableWidgetItem()
            # chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            # chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            # self.tableWidgetContactTab1.setItem(self.RowCount, 0, chkBoxItem)

            for col in range(0, 6):
                item = str(self.ContactList[col])
                # self.tableWidgetContactTab1.setItem(self.RowCount, col+1, QTableWidgetItem(item))
                self.tableWidgetContactTab1.setItem(self.RowCount, col, QTableWidgetItem(item))
                self.tableWidgetContactTab1.item(self.RowCount, col).setBackground(QtGui.QColor(255, 255, 153))
            self.RowCount += 1

            # print(GroupText)
            if GroupText == "Business":
                print(GroupText)
                self.tableWidgetGroupTab2.insertRow(self.RowCount_Group)
                for col in range(0, 5):
                    item = str(self.ContactList[col])
                    self.tableWidgetGroupTab2.setItem(self.RowCount_Group, col, QTableWidgetItem(item))
                self.RowCount_Group += 1


            self.AddContact.close()
            # print(self.ContactList)

        except Exception as e:
            print(e.args[0])


    def EditDetails(self):
        self.tableWidgetContactTab1.setEditTriggers(QTableWidget.AllEditTriggers)
        self.EditButton.setEnabled(False)
        self.UpdateButton.setEnabled(True)

    def UpdateDetails(self):
        self.tableWidgetContactTab1.setEditTriggers(QTableWidget.NoEditTriggers)
        self.EditButton.setEnabled(True)
        self.UpdateButton.setEnabled(False)

        self.updateGroupList()

    def DeleteDetails(self):
        try:
            self.index_list = []
            self.rowList = []

            for model_index in self.tableWidgetContactTab1.selectionModel().selectedRows():
                self.index = QtCore.QPersistentModelIndex(model_index)
                self.index_list.append(self.index)

                self.row = self.index.row()
                self.rowList.append(self.row)
                print(self.rowList)

            # To add name of contact in list which are deleted
            Namelist = []
            for row in self.rowList:
                QTableWidgetItemGroup = self.tableWidgetContactTab1.item(row,5)
                group =  QTableWidgetItemGroup.text()

                if group == "Business":
                    QTableWidgetItemName = self.tableWidgetContactTab1.item(row, 0)
                    name= QTableWidgetItemName.text()
                    print(name)
                    Namelist.append(name)
                    print(Namelist)

            # Check and Delete from Group table also
            self.RowCount_Group=self.tableWidgetGroupTab2.rowCount()
            for row in range(0, self.RowCount_Group):
                nameitem = self.tableWidgetGroupTab2.item(row,0)
                name = nameitem.text()

                for Delname in Namelist:
                    if Delname == name:
                        self.tableWidgetGroupTab2.removeRow(row)
                        self.RowCount_Group -= 1

            # Delete seleced row  from Contact table
            for self.index in self.index_list:
                self.tableWidgetContactTab1.removeRow(self.index.row())
                self.RowCount -= 1


        except Exception as e:
            print(e.args[0])

    def updateGroupList(self):
        try:
            self.Updatelist = []
            for row in range(0,self.RowCount):
                QTableWidgetItemContact = self.tableWidgetContactTab1.item(row, 5)
                group = QTableWidgetItemContact.text()
                if group == "Business":
                    for col in range(0, 5):
                        self.Updatelist.append(self.tableWidgetContactTab1.item(row, col).text())
            print( self.Updatelist)


            #clear and update group list
            self.tableWidgetGroupTab2.clear()
            self.tableWidgetGroupTab2.setHorizontalHeaderLabels(['Name', 'Age', 'Mobile', 'Gender', 'Address'])
            self.tableWidgetGroupTab2.setEditTriggers(QTableWidget.NoEditTriggers)

            self.RowCount_Group=0
            lengthRow= int((len( self.Updatelist))/5)
            colNum = 0
            # if lengthRow != 0:
                # self.tableWidgetGroupTab2.insertRow(self.RowCount_Group)
            for row in range(1, lengthRow+1):
                # self.tableWidgetGroupTab2.insertRow(self.RowCount_Group)
                # self.RowCount_Group += 1

                for col in range(colNum, 5*row):
                    item = str( self.Updatelist[col])
                    self.tableWidgetGroupTab2.setItem(self.RowCount_Group, col, QTableWidgetItem(item))
                colNum+=5
                # self.RowCount_Group += 1


        except Exception as e:
            print(e.args[0])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    UI = MainHandler()
    sys.exit(app.exec_())