from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QMainWindow, QRadioButton, QMessageBox
import sys




class X(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(300,350)

        self.grid = QGridLayout()
        self.h_lay = QHBoxLayout()
        self.h_str_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()
        self.msg = QMessageBox()
        self.msg.setWindowTitle("RESULT")

        self.btn1 = QPushButton("")
        self.btn2 = QPushButton("")
        self.btn3 = QPushButton("")
        self.btn4 = QPushButton("")
        self.btn5 = QPushButton("")
        self.btn6 = QPushButton("")
        self.btn7 = QPushButton("")
        self.btn8 = QPushButton("")
        self.btn9 = QPushButton("")

        self.lst = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]
        index = 0

        self.counter = 1

        self.str_style = """QPushButton {
            color:red;
            background-color:white;
            border:1px solid black;
            border-radius:50%;
            font: bold 12pt;}"""

        for i in range(3):
            for j in range(3):
                self.grid.addWidget(self.lst[index], i, j)
                self.lst[index].setFixedSize(96,70)
                self.lst[index].setStyleSheet(self.str_style)
                index+=1

        self.reset_btn = QPushButton("RESET")
        self.reset_btn.clicked.connect(self.res)

        self.close_btn = QPushButton("CLOSE")
        self.close_btn.clicked.connect(self.close)

        self.label_navbat = QLabel("  >>>>>   X")
        self.label_navbat.setStyleSheet("font: bold 16pt Arial;")

        self.h_str_lay.addStretch()
        self.h_str_lay.addWidget(self.label_navbat)
        self.h_str_lay.addStretch()


        self.h_lay.addWidget(self.reset_btn)
        self.h_lay.addWidget(self.close_btn)

        self.v_main_lay.addLayout(self.grid)
        self.v_main_lay.addLayout(self.h_str_lay)
        self.v_main_lay.addLayout(self.h_lay)
        
        self.setLayout(self.v_main_lay)

        self.btn1.clicked.connect(lambda: self.clicker(self.btn1))
        self.btn2.clicked.connect(lambda: self.clicker(self.btn2))
        self.btn3.clicked.connect(lambda: self.clicker(self.btn3))
        self.btn4.clicked.connect(lambda: self.clicker(self.btn4))
        self.btn5.clicked.connect(lambda: self.clicker(self.btn5))
        self.btn6.clicked.connect(lambda: self.clicker(self.btn6))
        self.btn7.clicked.connect(lambda: self.clicker(self.btn7))
        self.btn8.clicked.connect(lambda: self.clicker(self.btn8))
        self.btn9.clicked.connect(lambda: self.clicker(self.btn9))

    
    def disable(self):
        for i in self.lst:
            i.setDisabled(True)

    
    def win(self, a: QPushButton, b: QPushButton, c: QPushButton):
        str_style = """QPushButton {
            color:floralwhite;
            background-color:darkgreen;
            border:1px solid black;
            border-radius:50%;
            font: bold 12pt;}"""

        a.setStyleSheet(str_style)
        b.setStyleSheet(str_style)
        c.setStyleSheet(str_style)
        
        self.disable()

        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText(a.text()+" is WINNER")
        self.msg.buttonClicked.connect(self.res)

        self.msg.exec_()
    
    def checkWin(self):
        if self.btn1.text() != "" and self.btn1.text()==self.btn2.text() and self.btn1.text() == self.btn3.text():
            self.win(self.btn1, self.btn2, self.btn3)
        
        if self.btn4.text() != "" and self.btn4.text()==self.btn5.text() and self.btn4.text() == self.btn6.text():
            self.win(self.btn4, self.btn5, self.btn6)

        if self.btn7.text() != "" and self.btn7.text()==self.btn8.text() and self.btn7.text() == self.btn9.text():
            self.win(self.btn7, self.btn8, self.btn9)

        if self.btn1.text() != "" and self.btn1.text()==self.btn4.text() and self.btn1.text() == self.btn7.text():
            self.win(self.btn1, self.btn4, self.btn7)

        if self.btn2.text() != "" and self.btn2.text()==self.btn5.text() and self.btn2.text() == self.btn8.text():
            self.win(self.btn2, self.btn5, self.btn8)
        
        if self.btn3.text() != "" and self.btn3.text()==self.btn6.text() and self.btn3.text() == self.btn9.text():
            self.win(self.btn3, self.btn6, self.btn9)

        if self.btn1.text() != "" and self.btn1.text()==self.btn5.text() and self.btn1.text() == self.btn9.text():
            self.win(self.btn1, self.btn5, self.btn9)
        
        if self.btn7.text() != "" and self.btn7.text()==self.btn3.text() and self.btn7.text() == self.btn5.text():
            self.win(self.btn7, self.btn3, self.btn5)
        
        if self.counter==10:
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("DRAW")
            self.msg.buttonClicked.connect(self.res)
            self.msg.exec_()

    def res(self):
        for i in self.lst:
            i.setEnabled(True)
            i.setText("")
            i.setStyleSheet(self.str_style)
        self.counter = 1
        self.label_navbat.setText("  >>>>>   X")

    def clicker(self, btn):
        if self.counter % 2 != 0:
            btn.setText("X")
            self.label_navbat.setText("  >>>>>   O")
        else:
            btn.setText("O")
            self.label_navbat.setText("  >>>>>   X")

        self.counter+=1
        btn.setEnabled(False)

        self.checkWin()

        

        





class O(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(300,350)

        self.grid = QGridLayout()
        self.h_lay = QHBoxLayout()
        self.h_str_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()
        self.msg = QMessageBox()
        self.msg.setWindowTitle("RESULT")

        self.btn1 = QPushButton("")
        self.btn2 = QPushButton("")
        self.btn3 = QPushButton("")
        self.btn4 = QPushButton("")
        self.btn5 = QPushButton("")
        self.btn6 = QPushButton("")
        self.btn7 = QPushButton("")
        self.btn8 = QPushButton("")
        self.btn9 = QPushButton("")

        self.lst = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]
        index = 0

        self.counter = 1

        self.str_style = """QPushButton {
            color:red;
            background-color:white;
            border:1px solid black;
            border-radius:50%;
            font: bold 12pt;}"""

        for i in range(3):
            for j in range(3):
                self.grid.addWidget(self.lst[index], i, j)
                self.lst[index].setFixedSize(96,70)
                self.lst[index].setStyleSheet(self.str_style)
                index+=1

        self.reset_btn = QPushButton("RESET")
        self.reset_btn.clicked.connect(self.res)

        self.close_btn = QPushButton("CLOSE")
        self.close_btn.clicked.connect(self.close)

        self.label_navbat = QLabel("  >>>>>   O")
        self.label_navbat.setStyleSheet("font: bold 16pt Arial;")

        self.h_str_lay.addStretch()
        self.h_str_lay.addWidget(self.label_navbat)
        self.h_str_lay.addStretch()


        self.h_lay.addWidget(self.reset_btn)
        self.h_lay.addWidget(self.close_btn)

        self.v_main_lay.addLayout(self.grid)
        self.v_main_lay.addLayout(self.h_str_lay)
        self.v_main_lay.addLayout(self.h_lay)
        
        self.setLayout(self.v_main_lay)

        self.btn1.clicked.connect(lambda: self.clicker(self.btn1))
        self.btn2.clicked.connect(lambda: self.clicker(self.btn2))
        self.btn3.clicked.connect(lambda: self.clicker(self.btn3))
        self.btn4.clicked.connect(lambda: self.clicker(self.btn4))
        self.btn5.clicked.connect(lambda: self.clicker(self.btn5))
        self.btn6.clicked.connect(lambda: self.clicker(self.btn6))
        self.btn7.clicked.connect(lambda: self.clicker(self.btn7))
        self.btn8.clicked.connect(lambda: self.clicker(self.btn8))
        self.btn9.clicked.connect(lambda: self.clicker(self.btn9))

    
    def disable(self):
        for i in self.lst:
            i.setDisabled(True)

    
    def win(self, a: QPushButton, b: QPushButton, c: QPushButton):
        str_style = """QPushButton {
            color:floralwhite;
            background-color:darkgreen;
            border:1px solid black;
            border-radius:50%;
            font: bold 12pt;}"""

        a.setStyleSheet(str_style)
        b.setStyleSheet(str_style)
        c.setStyleSheet(str_style)
        
        self.disable()

        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText(a.text()+" is WINNER")
        self.msg.buttonClicked.connect(self.res)

        self.msg.exec_()
    
    def checkWin(self):
        if self.btn1.text() != "" and self.btn1.text()==self.btn2.text() and self.btn1.text() == self.btn3.text():
            self.win(self.btn1, self.btn2, self.btn3)
        
        if self.btn4.text() != "" and self.btn4.text()==self.btn5.text() and self.btn4.text() == self.btn6.text():
            self.win(self.btn4, self.btn5, self.btn6)

        if self.btn7.text() != "" and self.btn7.text()==self.btn8.text() and self.btn7.text() == self.btn9.text():
            self.win(self.btn7, self.btn8, self.btn9)

        if self.btn1.text() != "" and self.btn1.text()==self.btn4.text() and self.btn1.text() == self.btn7.text():
            self.win(self.btn1, self.btn4, self.btn7)

        if self.btn2.text() != "" and self.btn2.text()==self.btn5.text() and self.btn2.text() == self.btn8.text():
            self.win(self.btn2, self.btn5, self.btn8)
        
        if self.btn3.text() != "" and self.btn3.text()==self.btn6.text() and self.btn3.text() == self.btn9.text():
            self.win(self.btn3, self.btn6, self.btn9)

        if self.btn1.text() != "" and self.btn1.text()==self.btn5.text() and self.btn1.text() == self.btn9.text():
            self.win(self.btn1, self.btn5, self.btn9)
        
        if self.btn7.text() != "" and self.btn7.text()==self.btn3.text() and self.btn7.text() == self.btn5.text():
            self.win(self.btn7, self.btn3, self.btn5)
        
        if self.counter==10:
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("DRAW")
            self.msg.buttonClicked.connect(self.res)
            self.msg.exec_()

    def res(self):
        for i in self.lst:
            i.setEnabled(True)
            i.setText("")
            i.setStyleSheet(self.str_style)
        self.counter = 1
        self.label_navbat.setText("  >>>>>   O")

    def clicker(self, btn):
        if self.counter % 2 != 0:
            btn.setText("O")
            self.label_navbat.setText("  >>>>>   X")
        else:
            btn.setText("X")
            self.label_navbat.setText("  >>>>>   O")

        self.counter+=1
        btn.setEnabled(False)

        self.checkWin()

        

  







class MyOX(QMainWindow):
    def __init__(self):
        super().__init__()

        self.Q_Widget = QWidget()

        self.Main_Label = QLabel("CHOOSE")
        self.Red_Label = QLabel("")

        self.O_Button = QRadioButton("O")

        self.X_Button = QRadioButton("X")

        self.Start_B = QPushButton("START")
        self.Start_B.clicked.connect(self.check)


        self.Q_V_Layout = QVBoxLayout()

        self.Q_H_Layout = QHBoxLayout()
        self.Q_H_for_Label = QHBoxLayout()

        self.R_for = QHBoxLayout()

        self.R_for.addStretch()
        self.R_for.addWidget(self.Red_Label)
        self.R_for.addStretch()

        self.Q_H_for_Label.addStretch()
        self.Q_H_for_Label.addWidget(self.Main_Label)
        self.Q_H_for_Label.addStretch()

        self.Q_V_Layout.addStretch()

        self.Q_H_Layout.addStretch()
        self.Q_H_Layout.addWidget(self.O_Button)
        self.Q_H_Layout.addWidget(self.X_Button)
        self.Q_H_Layout.addStretch()

        self.Q_V_Layout.addLayout(self.Q_H_for_Label)
        self.Q_V_Layout.addStretch()
        self.Q_V_Layout.addLayout(self.Q_H_Layout)

        self.Q_V_Layout.addLayout(self.R_for)
        self.Q_V_Layout.addStretch()

        self.Q_V_Layout.addStretch()
        self.Q_V_Layout.addWidget(self.Start_B)

        self.Q_Widget.setLayout(self.Q_V_Layout)

        self.setCentralWidget(self.Q_Widget)


    def check(self):
        if self.X_Button.isChecked():
            self.X_OBJ = X()
            self.X_OBJ.show()
            self.close()

        elif self.O_Button.isChecked():
            self.O_OBJ = O()
            self.O_OBJ.show() 
            self.close()   


        elif not self.O_Button.isChecked() and  not self.X_Button.isChecked():
            self.Red_Label.setText("You have not selected anything!")
            self.Red_Label.setStyleSheet("background-color:red; color: white")





app = QApplication(sys.argv)
Game_OX = MyOX()
Game_OX.show()
Game_OX.setGeometry(500,200,700,600)
Game_OX.setWindowTitle("Tic-Tak-Toe")
app.exec_()
