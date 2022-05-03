from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import images
from datetime import date
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph,Image, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import mysql.connector as sql


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1421, 983)
        MainWindow.setStyleSheet("background-color:#eeedff")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.head_frame = QtWidgets.QFrame(self.centralwidget)
        self.head_frame.setGeometry(QtCore.QRect(0, 0, 1421, 91))
        self.head_frame.setStyleSheet("background-color:red;")
        self.head_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.head_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.head_frame.setObjectName("head_frame")

        self.sms_heading = QtWidgets.QLabel(self.head_frame)
        self.sms_heading.setGeometry(QtCore.QRect(510, 0, 431, 91))
        self.sms_heading.setStyleSheet("font-size: 50px; font-family: Impact; color: yellow;")
        self.sms_heading.setObjectName("sms_heading")

        self.billNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.billNumLabel.setGeometry(QtCore.QRect(20, 110, 101, 31))
        self.billNumLabel.setStyleSheet("font-size: 25px; font-family: Stencil;")
        self.billNumLabel.setObjectName("billNumLabel")

        self.billNum = QtWidgets.QLabel(self.centralwidget)
        self.billNum.setGeometry(QtCore.QRect(140, 105, 101, 41))
        self.billNum.setStyleSheet("background-color: white; font-size: 20px; color: red; margin-left: 2px;")
        self.billNum.setObjectName("billNum")

        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(1100, 110, 81, 31))
        self.dateLabel.setStyleSheet("font-size: 25px; font-family: Stencil;")
        self.dateLabel.setObjectName("dateLabel")

        self.date = QtWidgets.QDateEdit(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(1190, 100, 161, 51))
        self.date.setStyleSheet("font-size: 20px; color: blue; border: none;")
        self.date.setObjectName("date")

        self.pNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.pNameLabel.setGeometry(QtCore.QRect(110, 160, 171, 41))
        self.pNameLabel.setStyleSheet("font-size: 25px; font-family: Stencil;")
        self.pNameLabel.setObjectName("pNameLabel")

        self.pName = QtWidgets.QLineEdit(self.centralwidget)
        self.pName.setGeometry(QtCore.QRect(290, 160, 971, 41))
        self.pName.setStyleSheet("background-color:white; font-size: 22px; font-family: BODONI MT;")
        self.pName.setText("")
        self.pName.setObjectName("pName")

        self.adddressLabel = QtWidgets.QLabel(self.centralwidget)
        self.adddressLabel.setGeometry(QtCore.QRect(110, 210, 171, 41))
        self.adddressLabel.setStyleSheet("font-size: 25px; font-family: Stencil;")
        self.adddressLabel.setObjectName("adddressLabel")

        self.address = QtWidgets.QLineEdit(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(290, 210, 971, 41))
        self.address.setStyleSheet("background-color:white; font-size: 22px; font-family: BODONI MT;")
        self.address.setText("")
        self.address.setObjectName("address")

        self.pGstinLabel = QtWidgets.QLabel(self.centralwidget)
        self.pGstinLabel.setGeometry(QtCore.QRect(110, 260, 171, 41))
        self.pGstinLabel.setStyleSheet("font-size: 25px; font-family: Stencil;")
        self.pGstinLabel.setObjectName("pGstinLabel")

        self.pGstn = QtWidgets.QLineEdit(self.centralwidget)
        self.pGstn.setGeometry(QtCore.QRect(290, 260, 411, 41))
        self.pGstn.setStyleSheet("background-color:white; font-size: 22px; font-family: BODONI MT;")
        self.pGstn.setText("")
        self.pGstn.setObjectName("pGstn")

        self.mob = QtWidgets.QLineEdit(self.centralwidget)
        self.mob.setGeometry(QtCore.QRect(850, 260, 411, 41))
        self.mob.setStyleSheet("background-color:white; font-size: 22px; font-family: BODONI MT;")
        self.mob.setText("")
        self.mob.setObjectName("mob")

        self.mobLabel = QtWidgets.QLabel(self.centralwidget)
        self.mobLabel.setGeometry(QtCore.QRect(720, 260, 121, 41))
        self.mobLabel.setStyleSheet("font-size: 25px; font-family: Stencil;")
        self.mobLabel.setObjectName("mobLabel")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 320, 1331, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 350, 1361, 41))
        self.frame_2.setStyleSheet("background-color:#9dff70;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.snumLabel = QtWidgets.QLabel(self.frame_2)
        self.snumLabel.setGeometry(QtCore.QRect(10, 0, 101, 41))
        self.snumLabel.setStyleSheet("font-size: 25px; font-family: Stencil;")
        self.snumLabel.setObjectName("snumLabel")

        self.partiLabel = QtWidgets.QLabel(self.frame_2)
        self.partiLabel.setGeometry(QtCore.QRect(440, 0, 171, 41))
        self.partiLabel.setStyleSheet("font-size: 25px; font-family: Stencil;")
        self.partiLabel.setObjectName("partiLabel")

        self.qtyLabel = QtWidgets.QLabel(self.frame_2)
        self.qtyLabel.setGeometry(QtCore.QRect(960, 0, 61, 41))
        self.qtyLabel.setStyleSheet("font-size: 25px; font-family: Stencil;")
        self.qtyLabel.setObjectName("qtyLabel")

        self.rateLabel = QtWidgets.QLabel(self.frame_2)
        self.rateLabel.setGeometry(QtCore.QRect(1070, 0, 71, 41))
        self.rateLabel.setStyleSheet("font-size: 25px; font-family: Stencil;")
        self.rateLabel.setObjectName("rateLabel")

        self.amtLabel = QtWidgets.QLabel(self.frame_2)
        self.amtLabel.setGeometry(QtCore.QRect(1180, 0, 181, 41))
        self.amtLabel.setStyleSheet("font-size: 25px; font-family: Stencil;")
        self.amtLabel.setObjectName("amtLabel")

        self.snum1 = QtWidgets.QLineEdit(self.centralwidget)
        self.snum1.setGeometry(QtCore.QRect(30, 400, 71, 31))
        self.snum1.setStyleSheet("background-color: white; font-size: 15px;")
        self.snum1.setObjectName("snum1")

        self.snum2 = QtWidgets.QLineEdit(self.centralwidget)
        self.snum2.setGeometry(QtCore.QRect(30, 440, 71, 31))
        self.snum2.setStyleSheet("background-color: white; font-size: 15px;")
        self.snum2.setObjectName("snum2")

        self.snum3 = QtWidgets.QLineEdit(self.centralwidget)
        self.snum3.setGeometry(QtCore.QRect(30, 480, 71, 31))
        self.snum3.setStyleSheet("background-color: white; font-size: 15px;")
        self.snum3.setObjectName("snum3")

        self.snum5 = QtWidgets.QLineEdit(self.centralwidget)
        self.snum5.setGeometry(QtCore.QRect(30, 560, 71, 31))
        self.snum5.setStyleSheet("background-color: white; font-size: 15px;")
        self.snum5.setObjectName("snum5")

        self.snum4 = QtWidgets.QLineEdit(self.centralwidget)
        self.snum4.setGeometry(QtCore.QRect(30, 520, 71, 31))
        self.snum4.setStyleSheet("background-color: white; font-size: 15px;")
        self.snum4.setObjectName("snum4")

        self.snum6 = QtWidgets.QLineEdit(self.centralwidget)
        self.snum6.setGeometry(QtCore.QRect(30, 600, 71, 31))
        self.snum6.setStyleSheet("background-color: white; font-size: 15px;")
        self.snum6.setObjectName("snum6")

        self.snum8 = QtWidgets.QLineEdit(self.centralwidget)
        self.snum8.setGeometry(QtCore.QRect(30, 680, 71, 31))
        self.snum8.setStyleSheet("background-color: white; font-size: 15px;")
        self.snum8.setObjectName("snum8")

        self.snum7 = QtWidgets.QLineEdit(self.centralwidget)
        self.snum7.setGeometry(QtCore.QRect(30, 640, 71, 31))
        self.snum7.setStyleSheet("background-color: white; font-size: 15px;")
        self.snum7.setObjectName("snum7")

        self.snum9 = QtWidgets.QLineEdit(self.centralwidget)
        self.snum9.setGeometry(QtCore.QRect(30, 720, 71, 31))
        self.snum9.setStyleSheet("background-color: white; font-size: 15px;")
        self.snum9.setObjectName("snum9")

        self.snum10 = QtWidgets.QLineEdit(self.centralwidget)
        self.snum10.setGeometry(QtCore.QRect(30, 760, 71, 31))
        self.snum10.setStyleSheet("background-color: white; font-size: 15px;")
        self.snum10.setObjectName("snum10")

        self.p1 = QtWidgets.QLineEdit(self.centralwidget)
        self.p1.setGeometry(QtCore.QRect(120, 400, 831, 31))
        self.p1.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.p1.setText("")
        self.p1.setObjectName("p1")

        self.q1 = QtWidgets.QLineEdit(self.centralwidget)
        self.q1.setGeometry(QtCore.QRect(970, 400, 101, 31))
        self.q1.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.q1.setText("")
        self.q1.setObjectName("q1")

        self.r1 = QtWidgets.QLineEdit(self.centralwidget)
        self.r1.setGeometry(QtCore.QRect(1090, 400, 101, 31))
        self.r1.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.r1.setText("")
        self.r1.setObjectName("r1")

        self.p2 = QtWidgets.QLineEdit(self.centralwidget)
        self.p2.setGeometry(QtCore.QRect(120, 440, 831, 31))
        self.p2.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.p2.setText("")
        self.p2.setObjectName("p2")

        self.q2 = QtWidgets.QLineEdit(self.centralwidget)
        self.q2.setGeometry(QtCore.QRect(970, 440, 101, 31))
        self.q2.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.q2.setObjectName("q2")

        self.r2 = QtWidgets.QLineEdit(self.centralwidget)
        self.r2.setGeometry(QtCore.QRect(1090, 440, 101, 31))
        self.r2.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.r2.setObjectName("r2")

        self.p3 = QtWidgets.QLineEdit(self.centralwidget)
        self.p3.setGeometry(QtCore.QRect(120, 480, 831, 31))
        self.p3.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.p3.setText("")
        self.p3.setObjectName("p3")

        self.q3 = QtWidgets.QLineEdit(self.centralwidget)
        self.q3.setGeometry(QtCore.QRect(970, 480, 101, 31))
        self.q3.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.q3.setObjectName("q3")

        self.r3 = QtWidgets.QLineEdit(self.centralwidget)
        self.r3.setGeometry(QtCore.QRect(1090, 480, 101, 31))
        self.r3.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.r3.setObjectName("r3")

        self.p4 = QtWidgets.QLineEdit(self.centralwidget)
        self.p4.setGeometry(QtCore.QRect(120, 520, 831, 31))
        self.p4.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.p4.setObjectName("p4")

        self.q4 = QtWidgets.QLineEdit(self.centralwidget)
        self.q4.setGeometry(QtCore.QRect(970, 520, 101, 31))
        self.q4.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.q4.setObjectName("q4")

        self.r4 = QtWidgets.QLineEdit(self.centralwidget)
        self.r4.setGeometry(QtCore.QRect(1090, 520, 101, 31))
        self.r4.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.r4.setObjectName("r4")

        self.p5 = QtWidgets.QLineEdit(self.centralwidget)
        self.p5.setGeometry(QtCore.QRect(120, 560, 831, 31))
        self.p5.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.p5.setObjectName("p5")

        self.q5 = QtWidgets.QLineEdit(self.centralwidget)
        self.q5.setGeometry(QtCore.QRect(970, 560, 101, 31))
        self.q5.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.q5.setObjectName("q5")

        self.r5 = QtWidgets.QLineEdit(self.centralwidget)
        self.r5.setGeometry(QtCore.QRect(1090, 560, 101, 31))
        self.r5.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.r5.setObjectName("r5")

        self.p6 = QtWidgets.QLineEdit(self.centralwidget)
        self.p6.setGeometry(QtCore.QRect(120, 600, 831, 31))
        self.p6.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.p6.setObjectName("p6")

        self.q6 = QtWidgets.QLineEdit(self.centralwidget)
        self.q6.setGeometry(QtCore.QRect(970, 600, 101, 31))
        self.q6.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.q6.setObjectName("q6")

        self.r6 = QtWidgets.QLineEdit(self.centralwidget)
        self.r6.setGeometry(QtCore.QRect(1090, 600, 101, 31))
        self.r6.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.r6.setObjectName("r6")

        self.p7 = QtWidgets.QLineEdit(self.centralwidget)
        self.p7.setGeometry(QtCore.QRect(120, 640, 831, 31))
        self.p7.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.p7.setObjectName("p7")

        self.q7 = QtWidgets.QLineEdit(self.centralwidget)
        self.q7.setGeometry(QtCore.QRect(970, 640, 101, 31))
        self.q7.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.q7.setObjectName("q7")

        self.r7 = QtWidgets.QLineEdit(self.centralwidget)
        self.r7.setGeometry(QtCore.QRect(1090, 640, 101, 31))
        self.r7.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.r7.setObjectName("r7")

        self.p8 = QtWidgets.QLineEdit(self.centralwidget)
        self.p8.setGeometry(QtCore.QRect(120, 680, 831, 31))
        self.p8.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.p8.setObjectName("p8")

        self.q8 = QtWidgets.QLineEdit(self.centralwidget)
        self.q8.setGeometry(QtCore.QRect(970, 680, 101, 31))
        self.q8.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.q8.setObjectName("q8")

        self.r8 = QtWidgets.QLineEdit(self.centralwidget)
        self.r8.setGeometry(QtCore.QRect(1090, 680, 101, 31))
        self.r8.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.r8.setObjectName("r8")

        self.p9 = QtWidgets.QLineEdit(self.centralwidget)
        self.p9.setGeometry(QtCore.QRect(120, 720, 831, 31))
        self.p9.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.p9.setObjectName("p9")

        self.q9 = QtWidgets.QLineEdit(self.centralwidget)
        self.q9.setGeometry(QtCore.QRect(970, 720, 101, 31))
        self.q9.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.q9.setText("")
        self.q9.setObjectName("q9") 

        self.r9 = QtWidgets.QLineEdit(self.centralwidget)
        self.r9.setGeometry(QtCore.QRect(1090, 720, 101, 31))
        self.r9.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.r9.setObjectName("r9")

        self.p10 = QtWidgets.QLineEdit(self.centralwidget)
        self.p10.setGeometry(QtCore.QRect(120, 760, 831, 31))
        self.p10.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.p10.setObjectName("p10")

        self.q10 = QtWidgets.QLineEdit(self.centralwidget)
        self.q10.setGeometry(QtCore.QRect(970, 760, 101, 31))
        self.q10.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.q10.setObjectName("q10")

        self.r10 = QtWidgets.QLineEdit(self.centralwidget)
        self.r10.setGeometry(QtCore.QRect(1090, 760, 101, 31))
        self.r10.setStyleSheet("background-color: white; font-size: 15px;margin-left: 2px;")
        self.r10.setObjectName("r10")

        self.a1 = QtWidgets.QLabel(self.centralwidget)
        self.a1.setGeometry(QtCore.QRect(1210, 400, 181, 31))
        self.a1.setStyleSheet("background-color: white; font-size: 18px;margin-left: 2px;border: 1px solid black;")
        self.a1.setObjectName("a1")
        
        self.a2 = QtWidgets.QLabel(self.centralwidget)
        self.a2.setGeometry(QtCore.QRect(1210, 440, 181, 31))
        self.a2.setStyleSheet("background-color: white; font-size: 18px;margin-left: 2px;border: 1px solid black;")
        self.a2.setObjectName("a2")

        self.a3 = QtWidgets.QLabel(self.centralwidget)
        self.a3.setGeometry(QtCore.QRect(1210, 480, 181, 31))
        self.a3.setStyleSheet("background-color: white; font-size: 18px;margin-left: 2px;border: 1px solid black;")
        self.a3.setObjectName("a3")

        self.a4 = QtWidgets.QLabel(self.centralwidget)
        self.a4.setGeometry(QtCore.QRect(1210, 520, 181, 31))
        self.a4.setStyleSheet("background-color: white; font-size: 18px;margin-left: 2px;border: 1px solid black;")
        self.a4.setObjectName("a4")

        self.a7 = QtWidgets.QLabel(self.centralwidget)
        self.a7.setGeometry(QtCore.QRect(1210, 640, 181, 31))
        self.a7.setStyleSheet("background-color: white; font-size: 18px;margin-left: 2px;border: 1px solid black;")
        self.a7.setObjectName("a7")

        self.a6 = QtWidgets.QLabel(self.centralwidget)
        self.a6.setGeometry(QtCore.QRect(1210, 600, 181, 31))
        self.a6.setStyleSheet("background-color: white; font-size: 18px;margin-left: 2px;border: 1px solid black;")
        self.a6.setObjectName("a6")

        self.a5 = QtWidgets.QLabel(self.centralwidget)
        self.a5.setGeometry(QtCore.QRect(1210, 560, 181, 31))
        self.a5.setStyleSheet("background-color: white; font-size: 18px;margin-left: 2px;border: 1px solid black;")
        self.a5.setObjectName("a5")

        self.a10 = QtWidgets.QLabel(self.centralwidget)
        self.a10.setGeometry(QtCore.QRect(1210, 760, 181, 31))
        self.a10.setStyleSheet("background-color: white; font-size: 18px;margin-left: 2px;border: 1px solid black;")
        self.a10.setObjectName("a10")

        self.a9 = QtWidgets.QLabel(self.centralwidget)
        self.a9.setGeometry(QtCore.QRect(1210, 720, 181, 31))
        self.a9.setStyleSheet("background-color: white; font-size: 18px;margin-left: 2px;border: 1px solid black;")
        self.a9.setObjectName("a9")

        self.a8 = QtWidgets.QLabel(self.centralwidget)
        self.a8.setGeometry(QtCore.QRect(1210, 680, 181, 31))
        self.a8.setStyleSheet("background-color: white; font-size: 18px;margin-left: 2px;border: 1px solid black;")
        self.a8.setObjectName("a8")

        self.calButton = QtWidgets.QPushButton(self.centralwidget)
        self.calButton.setGeometry(QtCore.QRect(40, 830, 151, 41))
        self.calButton.setStyleSheet("font-family: impact; font-size: 20px")
        self.calButton.setObjectName("calButton")
        self.calButton.clicked.connect(self.calculate)

        self.totLabel = QtWidgets.QLabel(self.centralwidget)
        self.totLabel.setGeometry(QtCore.QRect(1060, 830, 200, 31))
        self.totLabel.setStyleSheet("font-size: 20px; font-family: Stencil;")
        self.totLabel.setObjectName("totLabel")

        self.cgstLabel = QtWidgets.QLabel(self.centralwidget)
        self.cgstLabel.setGeometry(QtCore.QRect(330, 830, 131, 31))
        self.cgstLabel.setStyleSheet("font-size: 20px; font-family: Stencil;")
        self.cgstLabel.setObjectName("cgstLabel")

        self.sgstLabel = QtWidgets.QLabel(self.centralwidget)
        self.sgstLabel.setGeometry(QtCore.QRect(690, 830, 131, 31))
        self.sgstLabel.setStyleSheet("font-size: 20px; font-family: Stencil;")
        self.sgstLabel.setObjectName("sgstLabel")

        self.total = QtWidgets.QLabel(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(1210, 830, 181, 31))
        self.total.setStyleSheet("background-color: white; font-size: 18px; margin-left: 2px;border: 1px solid black;")
        self.total.setObjectName("total")

        self.cgst = QtWidgets.QLabel(self.centralwidget)
        self.cgst.setGeometry(QtCore.QRect(450, 830, 181, 31))
        self.cgst.setStyleSheet("background-color: white; font-size: 18px; margin-left: 2px;border: 1px solid black;")
        self.cgst.setObjectName("cgst")

        self.sgst = QtWidgets.QLabel(self.centralwidget)
        self.sgst.setGeometry(QtCore.QRect(810, 830, 181, 31))
        self.sgst.setStyleSheet("background-color: white; font-size: 18px; margin-left: 2px;border: 1px solid black;")
        self.sgst.setObjectName("sgst")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 800, 1331, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.gtotalLabel = QtWidgets.QLabel(self.centralwidget)
        self.gtotalLabel.setGeometry(QtCore.QRect(1060, 880, 141, 31))
        self.gtotalLabel.setStyleSheet("font-size: 20px; font-family: Stencil;")
        self.gtotalLabel.setObjectName("gtotalLabel")

        self.gtotal = QtWidgets.QLabel(self.centralwidget)
        self.gtotal.setGeometry(QtCore.QRect(1210, 880, 181, 31))
        self.gtotal.setStyleSheet("background-color: white; font-size: 18px; margin-left: 2px;border: 1px solid black;")
        self.gtotal.setObjectName("gtotal")

        self.printButton = QtWidgets.QPushButton(self.centralwidget)
        self.printButton.setGeometry(QtCore.QRect(40, 930, 151, 41))
        self.printButton.setStyleSheet("font-family: impact; font-size: 20px")
        self.printButton.setObjectName("printButton")
        self.printButton.clicked.connect(self.printInvoice)

        self.due = QtWidgets.QLabel(self.centralwidget)
        self.due.setGeometry(QtCore.QRect(810, 920, 181, 31))
        self.due.setStyleSheet("background-color: white; font-size: 18px; margin-left: 2px;border: 1px solid black;")
        self.due.setObjectName("due")

        self.advanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.advanceLabel.setGeometry(QtCore.QRect(330, 920, 111, 31))
        self.advanceLabel.setStyleSheet("font-size: 20px; font-family: Stencil;")
        self.advanceLabel.setObjectName("advanceLabel")

        self.dueLabel = QtWidgets.QLabel(self.centralwidget)
        self.dueLabel.setGeometry(QtCore.QRect(690, 920, 41, 31))
        self.dueLabel.setStyleSheet("font-size: 20px; font-family: Stencil;")
        self.dueLabel.setObjectName("dueLabel")

        self.advance = QtWidgets.QLineEdit(self.centralwidget)
        self.advance.setGeometry(QtCore.QRect(450, 920, 181, 31))
        self.advance.setStyleSheet("background-color: white; font-size: 15px; margin-left: 2px;")
        self.advance.setObjectName("advance")

        self.caldueButton = QtWidgets.QPushButton(self.centralwidget)
        self.caldueButton.setGeometry(QtCore.QRect(40, 880, 151, 41))
        self.caldueButton.setStyleSheet("font-family: impact; font-size: 20px")
        self.caldueButton.setObjectName("caldueButton")
        self.caldueButton.clicked.connect(self.calculateDue)

        self.devLabel = QtWidgets.QLabel(self.centralwidget)
        self.devLabel.setGeometry(QtCore.QRect(1090, 950, 281, 31))
        self.devLabel.setStyleSheet("font-family: Comic Sans MS; font-size: 15px;")
        self.devLabel.setObjectName("devLabel")

        self.mailButton = QtWidgets.QToolButton(self.centralwidget)
        self.mailButton.setGeometry(QtCore.QRect(1364, 950, 31, 31))
        self.mailButton.setStyleSheet("border:none;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/gmail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mailButton.setIcon(icon)
        self.mailButton.setObjectName("mailButton")

        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(580, 100, 311, 31))
        self.heading.setStyleSheet("font-family: Bodoni MT black; font-size: 30px")
        self.heading.setObjectName("heading")

        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(1290, 220, 101, 31))
        self.resetButton.setStyleSheet("font-family: impact; font-size: 20px")
        self.resetButton.setObjectName("resetButton")
        self.resetButton.clicked.connect(self.reset)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.amount = [self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8, self.a9, self.a10]
        self.quantity = [self.q1, self.q2, self.q3, self.q4, self.q5, self.q6, self.q7, self.q8, self.q9, self.q10]
        self.rate = [self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7, self.r8, self.r9, self.r10]
        self.aggregates = [self.total, self.cgst, self.sgst, self.advance, self.due, self.gtotal]
        self.serial = [self.snum1, self.snum2, self.snum3, self.snum4, self.snum5, self.snum6, self.snum7, self.snum8, self.snum9, self.snum10]
        self.particular = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8, self.p9, self.p10]
        self.valid = False
        self.calculated = False
        self.saved = False

        for i in range(10):
            self.serial[i].setText(str(i + 1))

        self.date.setDate(date.today())

        self.rightAlign()
        self.validateDBlogin()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sms_heading.setText(_translate("MainWindow", "SHRI MURLI SERVICES"))
        self.billNumLabel.setText(_translate("MainWindow", "Bill No."))
        self.billNum.setText(_translate("MainWindow", "1"))
        self.dateLabel.setText(_translate("MainWindow", "DATE"))
        self.pNameLabel.setText(_translate("MainWindow", "Party name:"))
        self.adddressLabel.setText(_translate("MainWindow", "Address:"))
        self.pGstinLabel.setText(_translate("MainWindow", "Party GSTIN:"))
        self.mobLabel.setText(_translate("MainWindow", "Mob. No.:"))
        self.snumLabel.setText(_translate("MainWindow", "S.No."))
        self.partiLabel.setText(_translate("MainWindow", "PARTICULARS"))
        self.qtyLabel.setText(_translate("MainWindow", "qty"))
        self.rateLabel.setText(_translate("MainWindow", "rate"))
        self.amtLabel.setText(_translate("MainWindow", "AMOUNT (in ₹)"))
        self.a1.setText(_translate("MainWindow", ""))
        self.a2.setText(_translate("MainWindow", ""))
        self.a3.setText(_translate("MainWindow", ""))
        self.a4.setText(_translate("MainWindow", ""))
        self.a7.setText(_translate("MainWindow", ""))
        self.a6.setText(_translate("MainWindow", ""))
        self.a5.setText(_translate("MainWindow", ""))
        self.a10.setText(_translate("MainWindow", ""))
        self.a9.setText(_translate("MainWindow", ""))
        self.a8.setText(_translate("MainWindow", ""))
        self.calButton.setText(_translate("MainWindow", "CALCULATE"))
        self.totLabel.setText(_translate("MainWindow", "GROSS TOTAL"))
        self.cgstLabel.setText(_translate("MainWindow", "CGST (14%)"))
        self.sgstLabel.setText(_translate("MainWindow", "SGST (14%)"))
        self.total.setText(_translate("MainWindow", "0.0"))
        self.cgst.setText(_translate("MainWindow", "0.0"))
        self.sgst.setText(_translate("MainWindow", "0.0"))
        self.gtotalLabel.setText(_translate("MainWindow", "GRAND TOTAL"))
        self.gtotal.setText(_translate("MainWindow", "0.0"))
        self.printButton.setText(_translate("MainWindow", "PRINT"))
        self.due.setText(_translate("MainWindow", "0.0"))
        self.advanceLabel.setText(_translate("MainWindow", "Advance"))
        self.dueLabel.setText(_translate("MainWindow", "Due"))
        self.advance.setText(_translate("MainWindow", "0.0"))
        self.caldueButton.setText(_translate("MainWindow", "CALCULATE DUE"))
        self.devLabel.setText(_translate("MainWindow", "Developed by AKASH KUMAR SINGH"))
        self.mailButton.setText(_translate("MainWindow", "..."))
        self.heading.setText(_translate("MainWindow", "BILLING DETAILS"))
        self.resetButton.setText(_translate("MainWindow", "RESET"))

    def validateDBlogin(self):
        self.DBname = None
        self.loginToDB()
        # To validate login credentials.
        try:
            self.mydb = sql.connect(host = self.host, user = self.DBuser, password = self.DBpswd)
            self.cur = self.mydb.cursor()
        except:
            self.messageBox(["You entered wrong credentials.", "ERROR"], "w")
            sys.exit()
        if not self.DBname:
            self.connectToDB()
        # To validate database exists or not
        try:
            self.mydb = sql.connect(host = self.host, user = self.DBuser, password = self.DBpswd, database = self.DBname)
            with open("recordsDB.key", "w") as f:
                    f.write(f"{self.host} {self.DBuser} {self.DBpswd} {self.DBname}")
            self.cur = self.mydb.cursor()
        except:
            ok = self.messageBox(["No database with specified name exists. Do you want to create one?", "NO DATABASE"], "w")
            if ok ==  QMessageBox.Ok:
                self.cur.execute(f"CREATE DATABASE {self.DBname}")
                with open("recordsDB.key", "w") as f:
                    f.write(f"{self.host} {self.DBuser} {self.DBpswd} {self.DBname}")
                self.messageBox(["Database created successfully", "SUCCESS"], "i")
                self.mydb.commit()
                self.mydb = sql.connect(host = self.host, user = self.DBuser, password = self.DBpswd, database = self.DBname)
                self.cur = self.mydb.cursor()
                self.createTables()
            else:
                sys.exit()
        self.loadBillNum()

    def loginToDB(self):
        try:
            with open("recordsDB.key", "r") as f:
                temp = f.read()
            self.host, self.DBuser, self.DBpswd, self.DBname = temp.split()
            return
        except:
            self.host, ok1 = QtWidgets.QInputDialog.getText(MainWindow, "HOST", "Enter the hostname (localhost/IP address): ")
            if ok1:
                self.DBuser, ok2 = QtWidgets.QInputDialog.getText(MainWindow, "DB USER", "Enter the username of MySQL database: ")
                if ok2:
                    self.DBpswd, ok3 = QtWidgets.QInputDialog.getText(MainWindow, "PASSWORD", "Enter your password for database: ")
                    if ok3:
                        return
        sys.exit()

    def connectToDB(self):
        self.DBname, ok = QtWidgets.QInputDialog.getText(MainWindow, "DB NAME", "Enter the name of MySQL database: ")
        if ok:
            return

    def createTables(self):
        self.cur.execute("CREATE TABLE customer (GSTIN varchar(15), party_name varchar(50), Address varchar(150), Mobile varchar(10), CONSTRAINT gstin PRIMARY KEY (GSTIN));")
        self.cur.execute("CREATE TABLE sales (GSTIN varchar(15), Bill_num int, product varchar(100), quantity int, rate double, amount double,  Date date);")
        self.cur.execute("CREATE TABLE bills (Bill_num int, Date date, gross_total double, cgst double, sgst double, grand_total double)")

    def messageBox(self, msg, flag):
        msgBox = QMessageBox()
        if flag == "i":
            msgBox.setIcon(QMessageBox.Information)
        else:
            msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(msg[0])
        msgBox.setWindowTitle(msg[1])
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return msgBox.exec()

    def reset(self):
        if not self.saved:
            ok = self.messageBox(["Bill not saved. Do you really want to reset.","NOT SAVED"],"w")
            if ok != QMessageBox.Ok:
                return
        else:
            self.billNum.setText(str(int(self.billNum.text()) + 1).zfill(3))
        for i in range(10):
            self.quantity[i].setText("")
            self.rate[i].setText("")
            self.amount[i].setText("")
            self.particular[i].setText("")
        
        for i in self.aggregates:
            i.setText("0.0")

        self.pName.setText("")
        self.pGstn.setText("")
        self.address.setText("")
        self.mob.setText("")
        self.saved = False

    def rightAlign(self):
        for i in range(10):
            self.amount[i].setAlignment(QtCore.Qt.AlignRight)
            self.quantity[i].setAlignment(QtCore.Qt.AlignRight)
            self.rate[i].setAlignment(QtCore.Qt.AlignRight)
            self.serial[i].setAlignment(QtCore.Qt.AlignRight)

        for i in self.aggregates:
            i.setAlignment(QtCore.Qt.AlignRight)

    def calculate(self):
        self.validateBill()
        if not self.valid:
            return
        self.valid = False
        total = 0
        for i in range(10):
            if self.quantity[i].text() and self.rate[i].text():
                self.amount[i].setText(str(round(float(self.quantity[i].text()) * (float(self.rate[i].text())/1.28), 2)))
                total += float(self.amount[i].text())

        self.total.setText(str(total))
        gst = round(total * 0.14, 2)
        self.cgst.setText(str(gst))
        self.sgst.setText(str(gst))
        self.gtotal.setText(str(round(total + (gst * 2),2)))
        self.calculated = True

    def calculateDue(self):
        self.due.setText(str(round(float(self.gtotal.text()) - float(self.advance.text()),2)))

    def printInvoice(self):
        if not self.calculated:
            self.messageBox(["Press calculate first.","ERROR"],"w")
            return
        self.calculated = False
        self.save()
        if not self.saved:
            return
        ganesh = Image("ganesh.png", height=30, width=50)
        sign = Image("sign.jpg", height=50, width=100,hAlign='RIGHT')

        doc = SimpleDocTemplate(f"{self.billNum.text()}.pdf", pagesize=A4)
        styles = getSampleStyleSheet()
        style_right = ParagraphStyle(name='right', parent=styles['Heading3'], alignment=TA_RIGHT)
        style_rt_text = ParagraphStyle(name='right_text', parent=styles['Normal'], alignment=TA_RIGHT)
        style_center = ParagraphStyle(name='center', parent=styles['Heading3'], alignment=TA_CENTER)
        style_center_h = ParagraphStyle(name='center', parent=styles['Heading1'], alignment=TA_CENTER)

        data1 = [
            [Paragraph("GSTIN: 23EIBPS0088H1Z9", styles["Heading3"]),"", "", Paragraph("Mob: 8109919607", style_right), ""],
            ["","",ganesh,"",""],
            ["","",Paragraph("<u>INVOICE</u>", style_center),"",""],
            [Paragraph("SHRI MURLI SERVICES", style_center_h),"","","",""],
            [Paragraph(f"<b>Bill No:</b> {self.billNum.text()}"), "","","",Paragraph("<b>Date:</b>{}".format(self.date.date().toString("dd-MM-yyyy")), style_rt_text)],
            ["",Paragraph("Party Name:", style_right), Paragraph(self.pName.text())],
            ["",Paragraph("Address: ", style_right), Paragraph(self.address.text())],
            ["",Paragraph("Party GSTIN:", style_right),  Paragraph(self.pGstn.text())],
            ["", Paragraph(f"Mob. No.:", style_right), Paragraph(self.mob.text())]
        ]
        tbl1 = Table(data1, colWidths=90)
        styleTable1 = TableStyle([
            ('SPAN',(0,0),(1,0)),
            ('SPAN',(0,3),(-1,3)),
            ('SPAN',(3,0),(4,0)),
            ('SPAN',(2,5),(-1,5)),
            ('SPAN',(2,6),(-1,6)),
            ('SPAN',(2,7),(-1,7)),
            ('SPAN',(2,8),(-1,8)),
            ('LEFTPADDING',(2,1),(2,1), 10),
            ('ALIGN', (0,0), (-1,-1), 'CENTER')
            ])
        tbl1.setStyle(styleTable1)
        
        data2 = [
            [Paragraph("S.No." , style_center), Paragraph("Particulars" , style_center),"","", Paragraph("Quantity (in bags)", styles["Heading4"]), Paragraph("Rate (per bag)", styles["Heading4"]), Paragraph("Amount" , style_center)],
        ]
        for i in range(10):
            if self.amount[i].text() == "":
                data2.append(["","","","","","",""])
                continue
            data2.append([self.serial[i].text(), self.particular[i].text(),"","", self.quantity[i].text(), self.rate[i].text(), self.amount[i].text()])
        data2.append(["","","","","","Gross Total",self.total.text()])
        data2.append(["","","","","","CGST 14%",self.cgst.text()])
        data2.append(["","","","","","SGST 14%",self.sgst.text()])
        data2.append(["","","","","","Grand Total",self.gtotal.text()])

        tbl2 = Table(data2, colWidths=60)
        
        span = []
        for i in range(10):
            span.append(('SPAN', (1,i), (3,i)))
        span.append(('ALIGN', (0,0), (-1,0), 'CENTER'))
        span.append(('VALIGN', (0,0), (-1,0), 'MIDDLE'))
        span.append(('ALIGN', (0,1), (0,-1), 'CENTER'))
        span.append(('ALIGN', (4,1), (5,10), 'CENTER'))
        span.append(('ALIGN', (6,1), (6,-1), 'RIGHT'))
        span.append(('GRID', (0,0), (-1,0),1, colors.black))
        span.append(('BOX', (0,1), (-1,-1),1, colors.black))
        span.append(('LINEAFTER', (0,1), (0,-1),1, colors.black))
        span.append(('LINEAFTER', (3,1), (3,-1),1, colors.black))
        span.append(('LINEAFTER', (4,1), (4,-1),1, colors.black))
        span.append(('LINEAFTER', (5,1), (5,-1),1, colors.black))
        span.append(('GRID', (5,11), (-1,-1),1, colors.black))

        styleTable = TableStyle(span)
        tbl2.setStyle(styleTable)

        sign_head = Paragraph("Proprietor Signature", style_right)
        doc.build([tbl1, Spacer(1,50), tbl2, Spacer(1,70), sign,sign_head])

        self.messageBox(["Invoice saved successfully.","SUCCESS"],"i")

    def save(self):
        self.cur.execute("SELECT party_name, GSTIN FROM customer WHERE party_name = '{}' and GSTIN = '{}';".format(self.pName.text(), self.pGstn.text()))
        temp = self.cur.fetchall()
        if not temp:
            try:
                self.cur.execute("INSERT INTO customer VALUES ('{}', '{}', '{}', '{}');".format(self.pGstn.text(),self.pName.text(),self.address.text(),self.mob.text()))
            except: 
                self.messageBox(["GSTIN number is already associated to other party.", "DUPLICATE GSTIN"],"w")
                return
        for i in range(10):
            if self.amount[i].text() == "":
                break
            self.cur.execute("INSERT INTO sales VALUES ('{}', {}, '{}', {}, {}, {}, '{}');".format(self.pGstn.text(),self.billNum.text(),self.particular[i].text(),
                                                                                            self.quantity[i].text(),self.rate[i].text(),self.amount[i].text(),
                                                                                            self.date.date().toString("yyyy-MM-dd")))
        self.cur.execute("INSERT INTO bills VALUES ({}, '{}', {}, {}, {}, {});".format(self.billNum.text(),self.date.date().toString("yyyy-MM-dd"),
                                                                                        self.total.text(),self.cgst.text(),self.sgst.text(),
                                                                                        self.gtotal.text()))
        self.mydb.commit()
        self.saved = True

    def loadBillNum(self):
        self.cur.execute("SELECT MAX(Bill_num) FROM bills;")
        num = self.cur.fetchall()
        if num[0][0] == None:
            self.billNum.setText("001")
        else:
            self.billNum.setText(str(num[0][0] + 1).zfill(3))

    def validateBill(self):
        if self.pName.text() == "" and self.address.text() == "" and self.pGstn.text() == "" and self.mob.text() == "":
            self.messageBox(["Incomplete data.","INCOMPLETE"],"w")
            return
        elif not (len(self.mob.text()) == 10 and self.mob.text().isnumeric()):
            self.messageBox(["Invalid mobile number.", "INVALID"],"w")
            return
        elif not (len(self.pGstn.text()) == 15):
            self.messageBox(["Invalid GSTIN number.", "INVALID"],"w")
            return
        
        for i in range(10):
            if self.amount[i].text() == "":
                break
            elif not (self.quantity[i].text().isnumeric() and self.rate[i].text().isnumeric() and self.serial[i].text().isnumeric()):
                self.messageBox(["You entered an invalid data.", "INVALID"],"w")
                return
        self.valid = True
                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
