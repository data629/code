import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget

class Ui_Photolabel(object):
    def setupUi(self, Photolabel):
        Photolabel.setObjectName("Photolabel")
        Photolabel.resize(514, 600)
        self.centralwidget = QtWidgets.QWidget(Photolabel)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 260, 121, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 320, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 150, 91, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 150, 55, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(310, 290, 55, 16))
        self.label_9.setObjectName("label_9")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(310, 310, 181, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(310, 340, 91, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(310, 400, 131, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(310, 370, 171, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(310, 430, 121, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 390, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 420, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 490, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.Photolabel_10 = QtWidgets.QLabel(self.centralwidget)
        self.Photolabel_10.setGeometry(QtCore.QRect(310, 10, 151, 101))
        self.Photolabel_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Photolabel_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Photolabel_10.setText("")
        self.Photolabel_10.setScaledContents(True)
        self.Photolabel_10.setAlignment(QtCore.Qt.AlignCenter)
        self.Photolabel_10.setObjectName("Photolabel_10")
        self.UploadPhotopushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.UploadPhotopushButton_2.setGeometry(QtCore.QRect(310, 120, 93, 28))
        self.UploadPhotopushButton_2.setObjectName("UploadPhotopushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 100, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 160, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 220, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 280, 113, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 340, 113, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(310, 170, 181, 111))
        self.lineEdit_7.setObjectName("lineEdit_7")
        Photolabel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Photolabel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 26))
        self.menubar.setObjectName("menubar")
        self.menuCV = QtWidgets.QMenu(self.menubar)
        self.menuCV.setObjectName("menuCV")
        Photolabel.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Photolabel)
        self.statusbar.setObjectName("statusbar")
        Photolabel.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCV.menuAction())

        self.retranslateUi(Photolabel)
        QtCore.QMetaObject.connectSlotsByName(Photolabel)

    def retranslateUi(self, Photolabel):
        _translate = QtCore.QCoreApplication.translate
        Photolabel.setWindowTitle(_translate("Photolabel", "CV"))
        self.label.setText(_translate("Photolabel", "Name"))
        self.label_2.setText(_translate("Photolabel", "Lastname"))
        self.label_3.setText(_translate("Photolabel", "Status"))
        self.label_4.setText(_translate("Photolabel", "Education"))
        self.label_5.setText(_translate("Photolabel", "Employment Hustory"))
        self.label_6.setText(_translate("Photolabel", "Languages"))
        self.label_8.setText(_translate("Photolabel", "Details"))
        self.label_9.setText(_translate("Photolabel", "Skills"))
        self.checkBox.setText(_translate("Photolabel", "Effective Time Managment"))
        self.checkBox_2.setText(_translate("Photolabel", "Adaptability"))
        self.checkBox_4.setText(_translate("Photolabel", "Teamwork skills"))
        self.checkBox_5.setText(_translate("Photolabel", "Communication Skills"))
        self.checkBox_3.setText(_translate("Photolabel", "Responsibility"))
        self.radioButton.setText(_translate("Photolabel", "Male"))
        self.radioButton_2.setText(_translate("Photolabel", "Female"))
        self.pushButton.setText(_translate("Photolabel", "Submit"))
        self.UploadPhotopushButton_2.setText(_translate("Photolabel", "Upload Photo"))
        self.menuCV.setTitle(_translate("Photolabel", "CV"))



class CVApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Photolabel()
        self.ui.setupUi(self)
        self.setWindowTitle("CV")
        self.ui.UploadPhotopushButton_2.clicked.connect(self.upload_photo)
        self.ui.pushButton.clicked.connect(self.save_cv_data)
        self.photo_path = None
        self.ui.lineEdit.setPlaceholderText("შეიყვანეთ სახელი")
        self.ui.lineEdit_2.setPlaceholderText("შეიყვანეთ გვარი")
        self.ui.lineEdit_3.setPlaceholderText("შეიყვანეთ სტატუსი")
        self.ui.lineEdit_4.setPlaceholderText("შეიყვანეთ განათლება")
        self.ui.lineEdit_5.setPlaceholderText("შეიყვანეთ სამუშაო გამოცდილება")
        self.ui.lineEdit_6.setPlaceholderText("შეიყვანეთ ენები")
        self.ui.lineEdit_7.setPlaceholderText("მოკლე აღწერა/დეტალები")


    def upload_photo(self):
        """ფოტოს ასატვირთი ფუნქცია."""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self,
                                                   "აირჩიეთ ფოტო",
                                                   "",
                                                   "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)",
                                                   options=options)
        if file_path:
            self.photo_path = file_path
            pixmap = QtGui.QPixmap(self.photo_path)
            if not pixmap.isNull():
                self.ui.Photolabel_10.setPixmap(pixmap)
                print(f"ფოტო ატვირთულია: {self.photo_path}")
            else:
                QMessageBox.warning(self, "შეცდომა", "ფოტოს ჩატვირთვა ვერ მოხერხდა. შესაძლოა ფაილი დაზიანებულია ან არასწორი ფორმატისაა.")
                self.photo_path = None
        else:
            self.photo_path = None

    def save_cv_data(self):
        """CV მონაცემების TXT ფაილში შენახვის ფუნქცია."""
        cv_data = []


        cv_data.append("--- პირადი ინფორმაცია ---")
        cv_data.append(f"სახელი: {self.ui.lineEdit.text()}")
        cv_data.append(f"გვარი: {self.ui.lineEdit_2.text()}")
        cv_data.append(f"სტატუსი: {self.ui.lineEdit_3.text()}")
        cv_data.append(f"განათლება: {self.ui.lineEdit_4.text()}")
        cv_data.append(f"დასაქმების ისტორია: {self.ui.lineEdit_5.text()}")
        cv_data.append(f"ენები: {self.ui.lineEdit_6.text()}")
        cv_data.append(f"დეტალები: {self.ui.lineEdit_7.text()}")



        cv_data.append("\n--- სქესი ---")
        if self.ui.radioButton.isChecked():
            cv_data.append("სქესი: მამრობითი")
        elif self.ui.radioButton_2.isChecked():
            cv_data.append("სქესი: მდედრობითი")
        else:
            cv_data.append("სქესი: არ არის მითითებული")


        cv_data.append("\n--- უნარები ---")
        skills = []
        if self.ui.checkBox.isChecked():
            skills.append(self.ui.checkBox.text())
        if self.ui.checkBox_2.isChecked():
            skills.append(self.ui.checkBox_2.text())
        if self.ui.checkBox_5.isChecked():
            skills.append(self.ui.checkBox_5.text())
        if self.ui.checkBox_4.isChecked():
            skills.append(self.ui.checkBox_4.text())
        if self.ui.checkBox_3.isChecked():
            skills.append(self.ui.checkBox_3.text())

        if skills:
            cv_data.append("უნარები: " + ", ".join(skills))
        else:
            cv_data.append("უნარები: არ არის არჩეული")


        cv_data.append("\n--- ფოტო ---")
        if self.photo_path:
            cv_data.append(f"ფოტოს გზა: {self.photo_path}")
        else:
            cv_data.append("ფოტო: არ არის ატვირთული")


        file_name = "my_cv_data.txt"
        try:
            with open(file_name, "w", encoding="utf-8") as f:
                for line in cv_data:
                    f.write(line + "\n")
            QMessageBox.information(self, "წარმატება", f"CV მონაცემები წარმატებით შენახულია '{file_name}' ფაილში.")
            print(f"CV მონაცემები შენახულია: {file_name}")
        except Exception as e:
            QMessageBox.critical(self, "შეცდომა", f"მონაცემების შენახვა ვერ მოხერხდა:\n{e}")
            print(f"მონაცემების შენახვის შეცდომა: {e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CVApp()
    window.show()
    sys.exit(app.exec_())