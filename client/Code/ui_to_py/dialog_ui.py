from PySide2 import QtCore, QtGui, QtWidgets

class Dialog_task(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Dialog_task, self).__init__(parent)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(463, 500)
        css_file = open('../Stylesheet/dialog_stylesheet.css').read()
        Dialog.setStyleSheet(css_file)

        # icon & text label
        self.clock_icon = QtWidgets.QLabel(Dialog)
        self.clock_icon.setGeometry(QtCore.QRect(30, 120, 30, 30))
        self.clock_icon.setText("")
        self.clock_icon.setPixmap(QtGui.QPixmap("../Assets/clock.png"))
        self.clock_icon.setScaledContents(True)
        self.clock_icon.setObjectName("clock_icon")

        self.location_icon = QtWidgets.QLabel(Dialog)
        self.location_icon.setGeometry(QtCore.QRect(30, 170, 30, 30))
        self.location_icon.setText("")
        self.location_icon.setPixmap(QtGui.QPixmap("../Assets/placeholder.png"))
        self.location_icon.setScaledContents(True)
        self.location_icon.setObjectName("location_icon")

        self.label_noti = QtWidgets.QLabel(Dialog)
        self.label_noti.setGeometry(QtCore.QRect(70, 265, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        self.label_noti.setFont(font)
        self.label_noti.setObjectName("label_4")

        self.label_dueto = QtWidgets.QLabel(Dialog)
        self.label_dueto.setGeometry(QtCore.QRect(150, 80, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        self.label_dueto.setFont(font)
        self.label_dueto.setObjectName("label")

        self.label_location = QtWidgets.QLabel(Dialog)
        self.label_location.setGeometry(QtCore.QRect(70, 175, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        self.label_location.setFont(font)
        self.label_location.setObjectName("label_3")

        self.label_desc = QtWidgets.QLabel(Dialog)
        self.label_desc.setGeometry(QtCore.QRect(30, 310, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        self.label_desc.setFont(font)
        self.label_desc.setObjectName("label_5")

        self.label_to_time = QtWidgets.QLabel(Dialog)
        self.label_to_time.setGeometry(QtCore.QRect(200, 125, 21, 16))

        self.label_time = QtWidgets.QLabel(Dialog)
        self.label_time.setGeometry(QtCore.QRect(70, 125, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_2")

        # lineEdit
        self.location = QtWidgets.QLineEdit(Dialog)
        self.location.setGeometry(QtCore.QRect(70, 210, 359, 28))
        self.location.setObjectName("location")

        self.from_dateEdit = QtWidgets.QDateEdit(Dialog)
        self.from_dateEdit.setGeometry(QtCore.QRect(30, 70, 110, 31))
        self.from_dateEdit.setAcceptDrops(False)
        self.from_dateEdit.setAutoFillBackground(False)
        self.from_dateEdit.setFrame(False)
        self.from_dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.from_dateEdit.setCalendarPopup(True)
        self.from_dateEdit.setObjectName("from_dateEdit")

        self.timeEdit = QtWidgets.QTimeEdit(Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(130, 120, 61, 28))
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setObjectName("timeEdit")

        self.to_timeEdit = QtWidgets.QTimeEdit(Dialog)
        self.to_timeEdit.setGeometry(QtCore.QRect(220, 120, 61, 28))
        self.to_timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.to_timeEdit.setObjectName("to_timeEdit")

        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(300, 120, 100, 28))
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")

        self.textEdit_desc = QtWidgets.QTextEdit(Dialog)
        self.textEdit_desc.setGeometry(QtCore.QRect(30, 340, 401, 114))
        self.textEdit_desc.setObjectName("textEdit")

        self.to_dateEdit = QtWidgets.QDateEdit(Dialog)
        self.to_dateEdit.setGeometry(QtCore.QRect(210, 70, 110, 31))
        self.to_dateEdit.setAcceptDrops(False)
        self.to_dateEdit.setAutoFillBackground(False)
        self.to_dateEdit.setFrame(False)
        self.to_dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.to_dateEdit.setCalendarPopup(True)
        self.to_dateEdit.setObjectName("to_dateEdit")

        self.noti_icon = QtWidgets.QLabel(Dialog)
        self.noti_icon.setGeometry(QtCore.QRect(30, 260, 30, 30))
        self.noti_icon.setText("")
        self.noti_icon.setPixmap(QtGui.QPixmap("../Assets/ring.png"))
        self.noti_icon.setScaledContents(True)
        self.noti_icon.setObjectName("noti_icon")

        self.title = QtWidgets.QLineEdit(Dialog)
        self.title.setGeometry(QtCore.QRect(30, 20, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(21)
        self.title.setFont(font)
        self.title.setObjectName("title")

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(190, 265, 161, 26))
        self.comboBox.setObjectName("comboBox")

        # btn


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.location.setPlaceholderText(QtWidgets.QApplication.translate("Dialog", "Add Location", None, -1))
        self.label_noti.setText(QtWidgets.QApplication.translate("Dialog", "Notifications", None, -1))
        self.label_dueto.setText(QtWidgets.QApplication.translate("Dialog", "due to", None, -1))
        self.label_location.setText(QtWidgets.QApplication.translate("Dialog", "Location", None, -1))
        self.radioButton.setText(QtWidgets.QApplication.translate("Dialog", "All day", None, -1))
        self.textEdit_desc.setPlaceholderText(QtWidgets.QApplication.translate("Dialog", "Add Description", None, -1))
        self.label_desc.setText(QtWidgets.QApplication.translate("Dialog", "Descriptions", None, -1))
        self.label_to_time.setText(QtWidgets.QApplication.translate("Dialog", "-", None, -1))
        # self.save_btn.setText(QtWidgets.QApplication.translate("Dialog", "CREATE", None, -1))
        self.title.setPlaceholderText(QtWidgets.QApplication.translate("Dialog", "Title", None, -1))
        self.label_time.setText(QtWidgets.QApplication.translate("Dialog", "Time", None, -1))

class Create_dialog(Dialog_task):
    def __init__(self, parent=None):
        super(Create_dialog, self).__init__(parent)

    def setupUi(self, Dialog):
        super().setupUi(Dialog)

        self.save_btn = QtWidgets.QPushButton(Dialog)
        self.save_btn.setGeometry(QtCore.QRect(330, 20, 101, 30))
        self.save_btn.setObjectName("save_btn")
        self.save_btn.setText('Create')

class Display_dialog(Dialog_task):
    def __init__(self, parent=None):
        super(Display_dialog, self).__init__(parent)

    def setupUi(self, Dialog):
        super().setupUi(Dialog)

        self.edit_btn = QtWidgets.QPushButton(Dialog)
        self.edit_btn.setGeometry(QtCore.QRect(330, 20, 101, 30))
        self.edit_btn.setObjectName("save_btn")
        self.edit_btn.setText("Edit")


class Edit_dialog(Dialog_task):
    def __init__(self, parent=None):
        super(Edit_dialog, self).__init__(parent)

    def setupUi(self, Dialog):
        super().setupUi(Dialog)

        self.save_btn = QtWidgets.QPushButton(Dialog)
        self.save_btn.setGeometry(QtCore.QRect(330, 20, 101, 30))
        self.save_btn.setObjectName("save_btn")
        self.save_btn.setText("Save")

        self.save_btn = QtWidgets.QPushButton(Dialog)
        self.save_btn.setGeometry(QtCore.QRect(330, 60, 101, 30))
        self.save_btn.setObjectName("delete_btn")
        self.save_btn.setText("Delete")
