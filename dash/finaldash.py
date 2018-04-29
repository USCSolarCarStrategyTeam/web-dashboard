#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, 
    QColorDialog, QApplication, QLabel, QDesktopWidget)
from PyQt5.QtGui import QColor, QPainter, QFont, QPixmap
from PyQt5.QtCore import Qt, QTime, QTimer
import sys
import math
from random import randint


class Dashboard(QWidget):
    
    def __init__(self):
        super(Dashboard, self).__init__()
        
        self.initUI()
        self.timer = QTimer()

        self.timer.timeout.connect(self.getSpeed)
        self.timer.timeout.connect(self.getRange)
        self.timer.timeout.connect(self.getBatt)
        self.timer.timeout.connect(self.getTemp)
        self.timer.timeout.connect(self.getCurrent)
        self.timer.timeout.connect(self.getPower)       
        self.timer.timeout.connect(self.adjustScaling)

        self.timer.start(1000)
        
        
    def initUI(self):    

        #Labels
        self.lbl1 = QLabel("Current Speed", self)
        self.lbl1.move(25, 25)

        self.lbl2 = QLabel("Estimated Range", self)
        self.lbl2.move(25, 270)

        self.lbl3 = QLabel("Battery Level", self)
        self.lbl3.move(320, 230)

        self.lbl4 = QLabel("Cabin Temperature", self)
        self.lbl4.move(540, 25)

        self.lbl5 = QLabel("Motor Current", self)
        self.lbl5.move(595, 175)

        self.lbl6 = QLabel("Power", self)
        self.lbl6.move(680, 320)


        #Values
        #Note: extra spaces prevent cutoff upon update
        self.currSpeed = QLabel("0   ", self)
        self.currSpeed.move(25, 55)

        self.currRange = QLabel("0   ", self)
        self.currRange.move(25, 300)

        self.currBatt = QLabel("0   ", self)
        self.currBatt.move(290, 240)

        self.currTemp = QLabel("0   ", self)
        self.currTemp.move(660, 55)

        self.currCurrent = QLabel("0   ", self)
        self.currCurrent.move(660, 205)

        self.currPower = QLabel("0   ", self)
        self.currPower.move(660, 350)


        #Units
        self.speedUnit = QLabel("mph", self)
        self.speedUnit.move(175, 150)
        
        self.rangeUnit = QLabel("mi.", self)
        self.rangeUnit.move(175, 395)

        self.battUnit = QLabel("%", self)
        self.battUnit.move(505, 278)

        self.tempUnit = QLabel("°F", self)
        self.tempUnit.move(740, 92)

        self.currentUnit = QLabel("A", self)
        self.currentUnit.move(740, 242)

        self.powerUnit = QLabel("W", self)
        self.powerUnit.move(740, 387)


        #Configure fonts
        textFont = QFont("Arial", 20)
        self.lbl1.setFont(textFont)
        self.lbl2.setFont(textFont)
        self.lbl3.setFont(textFont)
        self.lbl4.setFont(textFont)
        self.lbl5.setFont(textFont)
        self.lbl6.setFont(textFont)

        valueFontS = QFont("Arial", 50)
        valueFontM = QFont("Arial", 100)
        valueFontL = QFont("Arial", 150)
        self.currSpeed.setFont(valueFontM)
        self.currRange.setFont(valueFontM)
        self.currBatt.setFont(valueFontL)
        self.currTemp.setFont(valueFontS)
        self.currCurrent.setFont(valueFontS)
        self.currPower.setFont(valueFontS)

        unitFont = QFont("Arial", 20)
        self.speedUnit.setFont(unitFont)
        self.rangeUnit.setFont(unitFont)
        self.battUnit.setFont(unitFont)
        self.tempUnit.setFont(unitFont)
        self.currentUnit.setFont(unitFont)
        self.powerUnit.setFont(unitFont)


        #Configure colors
        textSS = "QLabel { color: white; }"
        self.lbl1.setStyleSheet(textSS)
        self.lbl2.setStyleSheet(textSS)
        self.lbl3.setStyleSheet(textSS)
        self.lbl4.setStyleSheet(textSS)
        self.lbl5.setStyleSheet(textSS)
        self.lbl6.setStyleSheet(textSS)

        valueSS = "QLabel { color: white; }"
        self.currSpeed.setStyleSheet(valueSS)
        self.currRange.setStyleSheet(valueSS)
        self.currBatt.setStyleSheet(valueSS)
        self.currTemp.setStyleSheet(valueSS)
        self.currCurrent.setStyleSheet(valueSS)
        self.currPower.setStyleSheet(valueSS)

        unitSS = "QLabel { color: white; }"
        self.speedUnit.setStyleSheet(valueSS)
        self.rangeUnit.setStyleSheet(valueSS)
        self.battUnit.setStyleSheet(valueSS)
        self.tempUnit.setStyleSheet(valueSS)
        self.currentUnit.setStyleSheet(valueSS)
        self.powerUnit.setStyleSheet(valueSS)


        #Battery image
        battMap = QPixmap("batteries/battery24.png")
        battMap = battMap.scaledToHeight(96)
        self.batteryImage = QLabel(self)
        self.batteryImage.setPixmap(battMap)
        self.batteryImage.move(300, 115)


        #Configure dash color
        col = QColor(0, 0, 0)   #black
        # col = QColor(189, 32, 49)   #cardinal
        # col = QColor(169,169,169)   #grey
        p = self.palette()
        p.setColor(self.backgroundRole(), col)
        self.setPalette(p)


        #Dimensions
        self.setGeometry(300, 300, 800, 480)    #as opposed to 720x480
        self.prevH = self.height()
        self.prevW = self.width()
        self.battScale = 96


        #Display!
        self.setWindowTitle('Solar Car Dash')
        self.center()
        self.show()
      
    def keyPressEvent(self, e):
        
        if e.key() == Qt.Key_Escape:
            self.close()
            
    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())    

    def getSpeed(self):

        newSpeed = randint(50, 59)
        self.currSpeed.setText(str(newSpeed))

    def getRange(self):

        newRange = randint(40, 49)
        self.currRange.setText(str(newRange))

    def getBatt(self):

        newBatt = randint(0, 99)
        self.currBatt.setText(str(newBatt))

        newMapName = "batteries/battery"
        if (newBatt <= 0):
            newMapName += "0.png"
        elif (newBatt >= 96):
            newMapName += "24.png"
        else:
            newMapName += str(int(newBatt / 100.0 * 24) + 1) + ".png"

        newBattMap = QPixmap(newMapName)
        newBattMap = newBattMap.scaledToHeight(self.battScale)
        self.batteryImage.setPixmap(newBattMap)

    def getTemp(self):

        newTemp = randint(60, 69)
        self.currTemp.setText(str(newTemp))

    def getCurrent(self):

        newCurrent = randint(80, 89)
        self.currCurrent.setText(str(newCurrent))

    def getPower(self):

        newPower = randint(90, 99)
        self.currPower.setText(str(newPower))

    def adjustScaling(self):
        w = self.width()
        h = self.height()
        prevW = self.prevW
        prevH = self.prevH

        #only update scaling if window size has changed recently
        if (w != prevW or h != prevH):
            
            #VALUES spacings & sizings
            self.currSpeed.move(25 * w / 800, 55 * h / 480)
            self.currRange.move(25 * w / 800, 300 * h / 480)
            self.currBatt.move(290 * w / 800, 240 * h / 480)
            self.currTemp.move(660 * w / 800, 55 * h / 480)
            self.currCurrent.move(660 * w / 800, 205 * h / 480)
            self.currPower.move(660 * w / 800, 350 * h / 480)

            #LABELS spacings & sizings
            self.lbl1.move(25 * w / 800, 25 * h / 480)
            self.lbl2.move(25 * w / 800, 270 * h / 480)
            self.lbl3.move(320 * w / 800, 230 * h / 480)
            self.lbl4.move(540 * w / 800, 25 * h / 480)
            self.lbl5.move(595 * w / 800, 175 * h / 480)
            self.lbl6.move(680 * w / 800, 320 * h / 480)

            #UNITS spacings & sizings
            self.speedUnit.move(175 * w / 800, 150 * h / 480)
            self.rangeUnit.move(175 * w / 800, 395 * h / 480)
            self.battUnit.move(505 * w / 800, 278 * h / 480)
            self.tempUnit.move(740 * w / 800, 92 * h / 480)
            self.currentUnit.move(740 * w / 800, 242 * h / 480)
            self.powerUnit.move(740 * w / 800, 387 * h / 480)
            
            #BATTERY spacing & sizing
            self.batteryImage.move(300 * w / 800, 115 * h / 480)
            
            #keep track of new dimensions
            self.prevH = h
            self.prevW = w
                
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    dash = Dashboard()
    sys.exit(app.exec_())