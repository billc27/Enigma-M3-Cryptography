from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigmam3 import EnigmaM3

# Rotor
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")

# Reflector
UKW_B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

class Ui_MainWindow(object):
    def center(self, MainWindow):
        qr = MainWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)

        MainWindow.setStyleSheet(
            """
            background-color: #181719;
            color: white;
            """
        )

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        # Create main vertical layout
        self.main_vlayout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Create title horizontal layout
        self.title_hlayout = QtWidgets.QHBoxLayout()
        self.main_vlayout.addLayout(self.title_hlayout)

        # Title Label
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        
        self.label_6.setFixedWidth(200)
        self.label_6.setFixedHeight(50)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setStyleSheet(
            """
            border-radius: 5%;
            background-color: #5b5c5e;
            font-weight: bold;
            """
        )
        self.title_hlayout.addStretch(1)
        self.title_hlayout.addWidget(self.label_6)
        self.title_hlayout.addStretch(1)

        # Create content horizontal layout
        self.content_hlayout = QtWidgets.QHBoxLayout()
        self.main_vlayout.addLayout(self.content_hlayout)
        
        # Create left side vertical layout
        self.left_vlayout = QtWidgets.QVBoxLayout()
        
        self.left_vlayout.setContentsMargins(40, 30, 0, 0)
        self.content_hlayout.addLayout(self.left_vlayout)
        

        # Create rotor grid layout
        self.rotor_gridlayout = QtWidgets.QGridLayout()
        
        self.left_vlayout.addLayout(self.rotor_gridlayout)
        

        # Rotor Configuration Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setStyleSheet(
            """
            font-weight: 500;
            """
        )
        
        self.rotor_gridlayout.addWidget(self.label, 0, 0, 1, 4)

        # Rotor 1 Label
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
    
        self.rotor_gridlayout.addWidget(self.label_4, 1, 0)

        # Rotor 1 Choice
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setStyleSheet(
            """
            background-color: #5b5c5e;
            """
        )
        self.rotor_gridlayout.addWidget(self.comboBox, 1, 1)

        # Rotor 1 Initial Position
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.setStyleSheet(
            """
            background-color: #767674;
            """
        )
        for i in range(26):
            self.comboBox_4.addItem("")
        self.rotor_gridlayout.addWidget(self.comboBox_4, 1, 2)

        # Rotor 1 Ring Setting
        self.comboBox_7 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.setStyleSheet(
            """
            background-color: #5b5c5e;
            """
        )
        for i in range(26):
            self.comboBox_7.addItem("")
        self.rotor_gridlayout.addWidget(self.comboBox_7, 1, 3)

        # Rotor 2 Label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        
        self.rotor_gridlayout.addWidget(self.label_2, 2, 0)

        # Rotor 2 Choice
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setStyleSheet(
            """
            background-color: #5b5c5e;
            """
        )
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.rotor_gridlayout.addWidget(self.comboBox_2, 2, 1)

        # Rotor 2 Initial Position
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.setStyleSheet(
            """
            background-color: #767674;
            """
        )
        for i in range(26):
            self.comboBox_5.addItem("")
        self.rotor_gridlayout.addWidget(self.comboBox_5, 2, 2)

        # Rotor 2 Ring Setting
        self.comboBox_8 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.setStyleSheet(
            """
            background-color: #5b5c5e;
            """
        )
        for i in range(26):
            self.comboBox_8.addItem("")
        self.rotor_gridlayout.addWidget(self.comboBox_8, 2, 3)

        # Rotor 3 Label
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        
        self.rotor_gridlayout.addWidget(self.label_3, 3, 0)

        # Rotor 3 Choice
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.setStyleSheet(
            """
            background-color: #5b5c5e;
            """
        )
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.rotor_gridlayout.addWidget(self.comboBox_3, 3, 1)

        # Rotor 3 Initial Position
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.setStyleSheet(
            """
            background-color: #767674;
            """
        )
        for i in range(26):
            self.comboBox_6.addItem("")
        self.rotor_gridlayout.addWidget(self.comboBox_6, 3, 2)

        # Rotor 3 Ring Setting
        self.comboBox_9 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.setStyleSheet(
            """
            background-color: #5b5c5e;
            """
        )
        for i in range(26):
            self.comboBox_9.addItem("")
        self.rotor_gridlayout.addWidget(self.comboBox_9, 3, 3)

        # Plugboard Label
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet(
            """
            
            font-weight: 500;
            """
        )
        
        self.left_vlayout.addWidget(self.label_5)

        # Plugboard Input Box
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        plugboard = self.textEdit.toPlainText()
        self.left_vlayout.addWidget(self.textEdit)

        # Start Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFixedHeight(40)
        self.pushButton.setStyleSheet(
            """
            QPushButton {
                background-color: #767674;
                border-radius: 5%;
            }
            QPushButton:hover {
                background-color: #9e9e9e;
            }
            """
        )

        

        self.left_vlayout.addWidget(self.pushButton)


        # Create right side vertical layout
        self.right_vlayout = QtWidgets.QVBoxLayout()
        self.content_hlayout.addLayout(self.right_vlayout)

        # Input Box Label
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.right_vlayout.setContentsMargins(60, 30, 40, 0)
        self.right_vlayout.addWidget(self.label_8)

        # Input Box
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.right_vlayout.addWidget(self.lineEdit)

        # Result Box Label
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.label_9.setContentsMargins(0, 25, 0, 0)
        self.right_vlayout.addWidget(self.label_9)

        # Result Box
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.right_vlayout.addWidget(self.textBrowser)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.center(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.encrypt_message)

    def encrypt_message(self):
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # Get rotor choices
        rotor1_choice = self.comboBox.currentText()
        print("Rotor 1 Choice:", rotor1_choice)
        
        rotor2_choice = self.comboBox_2.currentText()
        print("Rotor 2 Choice:", rotor2_choice)
        rotor3_choice = self.comboBox_3.currentText()
        print("Rotor 3 Choice:", rotor3_choice)

        # Get rotor initial positions
        rotor1_initial_position = self.comboBox_4.currentText()
        print("Rotor 1 Initial Position:", rotor1_initial_position)
        rotor2_initial_position = self.comboBox_5.currentText()
        print("Rotor 2 Initial Position:", rotor2_initial_position)
        rotor3_initial_position = self.comboBox_6.currentText()
        print("Rotor 3 Initial Position:", rotor3_initial_position)

        rotor_initial_position = rotor1_initial_position + rotor2_initial_position + rotor3_initial_position
        print("Rotor Initial Position:", rotor_initial_position)

        # Get rotor ring settings
        rotor1_ring_setting = (alphabets.find(self.comboBox_7.currentText()))+1
        print("Rotor 1 Ring:", rotor1_ring_setting)
        rotor2_ring_setting = (alphabets.find(self.comboBox_8.currentText()))+1
        print("Rotor 2 Ring:", rotor2_ring_setting)
        rotor3_ring_setting = (alphabets.find(self.comboBox_9.currentText()))+1
        print("Rotor 3 Ring:", rotor3_ring_setting)

        rotor_ring_settings = (rotor1_ring_setting, rotor2_ring_setting, rotor3_ring_setting)
        print("Rotor Ring Settings:", rotor_ring_settings)

        # Get plugboard settings
        plugboard_settings = self.textEdit.toPlainText().split(',')
        print("Plugboard Settings:", plugboard_settings)

        # Set up Enigma M3 machine
        kb = Keyboard()
        
        if (plugboard_settings == ['']):
            pb = Plugboard([])
        else:
            pb = Plugboard(plugboard_settings)

        def get_rotor_obj(name):
            if (name == "I"):
                return I
            elif (name == "II"):
                return II
            elif (name == "III"):
                return III

        enigma = EnigmaM3(UKW_B, get_rotor_obj(rotor1_choice), get_rotor_obj(rotor2_choice), get_rotor_obj(rotor3_choice), pb, kb)
        enigma.set_keys(rotor_initial_position)
        enigma.set_rings(rotor_ring_settings)
        
        # Get message
        message = self.lineEdit.text()
        print("Message:", message)
        
        # Encrypt message
        c_text = ""
        for letter in message:
            c_text += enigma.encrypt(letter)
        
        # Display encrypted text
        self.textBrowser.setText(c_text)
        print("Encrypted Message:", c_text)
        print("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label_2.setText(_translate("MainWindow", "Rotor 2:"))
        self.label_3.setText(_translate("MainWindow", "Rotor 3:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "I"))
        self.comboBox.setItemText(1, _translate("MainWindow", "II"))
        self.comboBox.setItemText(2, _translate("MainWindow", "III"))
        self.label_4.setText(_translate("MainWindow", "Rotor 1:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "I"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "II"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "III"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "I"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "II"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "III"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "B"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "C"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "D"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "E"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "F"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "G"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "H"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "I"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "J"))
        self.comboBox_4.setItemText(10, _translate("MainWindow", "K"))
        self.comboBox_4.setItemText(11, _translate("MainWindow", "L"))
        self.comboBox_4.setItemText(12, _translate("MainWindow", "M"))
        self.comboBox_4.setItemText(13, _translate("MainWindow", "N"))
        self.comboBox_4.setItemText(14, _translate("MainWindow", "O"))
        self.comboBox_4.setItemText(15, _translate("MainWindow", "P"))
        self.comboBox_4.setItemText(16, _translate("MainWindow", "Q"))
        self.comboBox_4.setItemText(17, _translate("MainWindow", "R"))
        self.comboBox_4.setItemText(18, _translate("MainWindow", "S"))
        self.comboBox_4.setItemText(19, _translate("MainWindow", "T"))
        self.comboBox_4.setItemText(20, _translate("MainWindow", "U"))
        self.comboBox_4.setItemText(21, _translate("MainWindow", "V"))
        self.comboBox_4.setItemText(22, _translate("MainWindow", "W"))
        self.comboBox_4.setItemText(23, _translate("MainWindow", "X"))
        self.comboBox_4.setItemText(24, _translate("MainWindow", "Y"))
        self.comboBox_4.setItemText(25, _translate("MainWindow", "Z"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "B"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "C"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "D"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "E"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "F"))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "G"))
        self.comboBox_5.setItemText(7, _translate("MainWindow", "H"))
        self.comboBox_5.setItemText(8, _translate("MainWindow", "I"))
        self.comboBox_5.setItemText(9, _translate("MainWindow", "J"))
        self.comboBox_5.setItemText(10, _translate("MainWindow", "K"))
        self.comboBox_5.setItemText(11, _translate("MainWindow", "L"))
        self.comboBox_5.setItemText(12, _translate("MainWindow", "M"))
        self.comboBox_5.setItemText(13, _translate("MainWindow", "N"))
        self.comboBox_5.setItemText(14, _translate("MainWindow", "O"))
        self.comboBox_5.setItemText(15, _translate("MainWindow", "P"))
        self.comboBox_5.setItemText(16, _translate("MainWindow", "Q"))
        self.comboBox_5.setItemText(17, _translate("MainWindow", "R"))
        self.comboBox_5.setItemText(18, _translate("MainWindow", "S"))
        self.comboBox_5.setItemText(19, _translate("MainWindow", "T"))
        self.comboBox_5.setItemText(20, _translate("MainWindow", "U"))
        self.comboBox_5.setItemText(21, _translate("MainWindow", "V"))
        self.comboBox_5.setItemText(22, _translate("MainWindow", "W"))
        self.comboBox_5.setItemText(23, _translate("MainWindow", "X"))
        self.comboBox_5.setItemText(24, _translate("MainWindow", "Y"))
        self.comboBox_5.setItemText(25, _translate("MainWindow", "Z"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "B"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "C"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "D"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "E"))
        self.comboBox_6.setItemText(5, _translate("MainWindow", "F"))
        self.comboBox_6.setItemText(6, _translate("MainWindow", "G"))
        self.comboBox_6.setItemText(7, _translate("MainWindow", "H"))
        self.comboBox_6.setItemText(8, _translate("MainWindow", "I"))
        self.comboBox_6.setItemText(9, _translate("MainWindow", "J"))
        self.comboBox_6.setItemText(10, _translate("MainWindow", "K"))
        self.comboBox_6.setItemText(11, _translate("MainWindow", "L"))
        self.comboBox_6.setItemText(12, _translate("MainWindow", "M"))
        self.comboBox_6.setItemText(13, _translate("MainWindow", "N"))
        self.comboBox_6.setItemText(14, _translate("MainWindow", "O"))
        self.comboBox_6.setItemText(15, _translate("MainWindow", "P"))
        self.comboBox_6.setItemText(16, _translate("MainWindow", "Q"))
        self.comboBox_6.setItemText(17, _translate("MainWindow", "R"))
        self.comboBox_6.setItemText(18, _translate("MainWindow", "S"))
        self.comboBox_6.setItemText(19, _translate("MainWindow", "T"))
        self.comboBox_6.setItemText(20, _translate("MainWindow", "U"))
        self.comboBox_6.setItemText(21, _translate("MainWindow", "V"))
        self.comboBox_6.setItemText(22, _translate("MainWindow", "W"))
        self.comboBox_6.setItemText(23, _translate("MainWindow", "X"))
        self.comboBox_6.setItemText(24, _translate("MainWindow", "Y"))
        self.comboBox_6.setItemText(25, _translate("MainWindow", "Z"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "B"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "C"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "D"))
        self.comboBox_7.setItemText(4, _translate("MainWindow", "E"))
        self.comboBox_7.setItemText(5, _translate("MainWindow", "F"))
        self.comboBox_7.setItemText(6, _translate("MainWindow", "G"))
        self.comboBox_7.setItemText(7, _translate("MainWindow", "H"))
        self.comboBox_7.setItemText(8, _translate("MainWindow", "I"))
        self.comboBox_7.setItemText(9, _translate("MainWindow", "J"))
        self.comboBox_7.setItemText(10, _translate("MainWindow", "K"))
        self.comboBox_7.setItemText(11, _translate("MainWindow", "L"))
        self.comboBox_7.setItemText(12, _translate("MainWindow", "M"))
        self.comboBox_7.setItemText(13, _translate("MainWindow", "N"))
        self.comboBox_7.setItemText(14, _translate("MainWindow", "O"))
        self.comboBox_7.setItemText(15, _translate("MainWindow", "P"))
        self.comboBox_7.setItemText(16, _translate("MainWindow", "Q"))
        self.comboBox_7.setItemText(17, _translate("MainWindow", "R"))
        self.comboBox_7.setItemText(18, _translate("MainWindow", "S"))
        self.comboBox_7.setItemText(19, _translate("MainWindow", "T"))
        self.comboBox_7.setItemText(20, _translate("MainWindow", "U"))
        self.comboBox_7.setItemText(21, _translate("MainWindow", "V"))
        self.comboBox_7.setItemText(22, _translate("MainWindow", "W"))
        self.comboBox_7.setItemText(23, _translate("MainWindow", "X"))
        self.comboBox_7.setItemText(24, _translate("MainWindow", "Y"))
        self.comboBox_7.setItemText(25, _translate("MainWindow", "Z"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "B"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "C"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "D"))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "E"))
        self.comboBox_8.setItemText(5, _translate("MainWindow", "F"))
        self.comboBox_8.setItemText(6, _translate("MainWindow", "G"))
        self.comboBox_8.setItemText(7, _translate("MainWindow", "H"))
        self.comboBox_8.setItemText(8, _translate("MainWindow", "I"))
        self.comboBox_8.setItemText(9, _translate("MainWindow", "J"))
        self.comboBox_8.setItemText(10, _translate("MainWindow", "K"))
        self.comboBox_8.setItemText(11, _translate("MainWindow", "L"))
        self.comboBox_8.setItemText(12, _translate("MainWindow", "M"))
        self.comboBox_8.setItemText(13, _translate("MainWindow", "N"))
        self.comboBox_8.setItemText(14, _translate("MainWindow", "O"))
        self.comboBox_8.setItemText(15, _translate("MainWindow", "P"))
        self.comboBox_8.setItemText(16, _translate("MainWindow", "Q"))
        self.comboBox_8.setItemText(17, _translate("MainWindow", "R"))
        self.comboBox_8.setItemText(18, _translate("MainWindow", "S"))
        self.comboBox_8.setItemText(19, _translate("MainWindow", "T"))
        self.comboBox_8.setItemText(20, _translate("MainWindow", "U"))
        self.comboBox_8.setItemText(21, _translate("MainWindow", "V"))
        self.comboBox_8.setItemText(22, _translate("MainWindow", "W"))
        self.comboBox_8.setItemText(23, _translate("MainWindow", "X"))
        self.comboBox_8.setItemText(24, _translate("MainWindow", "Y"))
        self.comboBox_8.setItemText(25, _translate("MainWindow", "Z"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "B"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "C"))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "D"))
        self.comboBox_9.setItemText(4, _translate("MainWindow", "E"))
        self.comboBox_9.setItemText(5, _translate("MainWindow", "F"))
        self.comboBox_9.setItemText(6, _translate("MainWindow", "G"))
        self.comboBox_9.setItemText(7, _translate("MainWindow", "H"))
        self.comboBox_9.setItemText(8, _translate("MainWindow", "I"))
        self.comboBox_9.setItemText(9, _translate("MainWindow", "J"))
        self.comboBox_9.setItemText(10, _translate("MainWindow", "K"))
        self.comboBox_9.setItemText(11, _translate("MainWindow", "L"))
        self.comboBox_9.setItemText(12, _translate("MainWindow", "M"))
        self.comboBox_9.setItemText(13, _translate("MainWindow", "N"))
        self.comboBox_9.setItemText(14, _translate("MainWindow", "O"))
        self.comboBox_9.setItemText(15, _translate("MainWindow", "P"))
        self.comboBox_9.setItemText(16, _translate("MainWindow", "Q"))
        self.comboBox_9.setItemText(17, _translate("MainWindow", "R"))
        self.comboBox_9.setItemText(18, _translate("MainWindow", "S"))
        self.comboBox_9.setItemText(19, _translate("MainWindow", "T"))
        self.comboBox_9.setItemText(20, _translate("MainWindow", "U"))
        self.comboBox_9.setItemText(21, _translate("MainWindow", "V"))
        self.comboBox_9.setItemText(22, _translate("MainWindow", "W"))
        self.comboBox_9.setItemText(23, _translate("MainWindow", "X"))
        self.comboBox_9.setItemText(24, _translate("MainWindow", "Y"))
        self.comboBox_9.setItemText(25, _translate("MainWindow", "Z"))
        self.label.setText(_translate("MainWindow", "Rotor Configuration (Rotor - Initial Position - Ring Settings)"))
        self.label_5.setText(_translate("MainWindow", "Plugboard"))
        self.label_6.setText(_translate("MainWindow", "ENIGMA - M3"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt;\">Your Text</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt;\">Result</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
