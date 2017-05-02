# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pihue.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from phue import Bridge
import sys
import requests
import time
import json
import logging
from threading import Thread

#-----------------

counter = 1

MAX = 254

CUR = MAX

data = {'id': 1, "on": "false"}

JSON_ON = json.loads("""{"id":1,"on":"true"}""")

headers = {'content-type': 'application/json'}

# bridge setup----------

logging.basicConfig()

b = Bridge('192.168.2.3')

b.connect()

b.get_api()

#--url---------
url_on = 'https://maker.ifttt.com/trigger/Light_1_on/with/key/pRHIYK4v_9ZkyIZjD-vhFE_SlQTPVgiZtSFGcxeMfUV'

url_off = 'https://maker.ifttt.com/trigger/Light_1_off/with/key/pRHIYK4v_9ZkyIZjD-vhFE_SlQTPVgiZtSFGcxeMfUV'

###########------------------------------
url_blink = 'http://905be250.ngrok.io/posts/1'

#light on or off-----------------------
on_command = {'on' : True, 'bri' : MAX}

off_command = {'on' : False}

on_r = {'transitiontime': 1,'on' : True, 'bri' : MAX}

off_r = {'transitiontime': 1, 'on' : False}


#----------------------------------------

class Ui_pihue(object):
    def setupUi(self, pihue):
        pihue.setObjectName("pihue")
        pihue.resize(544, 469)
        self.centralWidget = QtWidgets.QWidget(pihue)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton_On = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_On.setGeometry(QtCore.QRect(60, 160, 221, 91))
        self.pushButton_On.setObjectName("pushButton_On")
        #
        self.pushButton_On.clicked.connect(on_clicked)
        self.pushButton_On.clicked.connect(self.light_status_on)
        self.pushButton_On.clicked.connect(self.light_bri)
        
        self.pushButton_Off = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Off.setGeometry(QtCore.QRect(280, 160, 211, 91))
        self.pushButton_Off.setObjectName("pushButton_Off")
        #
        self.pushButton_Off.clicked.connect(off_clicked)
        self.pushButton_Off.clicked.connect(self.light_status_off)
        self.pushButton_Off.clicked.connect(self.light_bri_0)

        
        self.pushButton_Blink = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Blink.setGeometry(QtCore.QRect(350, 260, 141, 101))
        self.pushButton_Blink.setObjectName("pushButton_Blink")
        #
        self.pushButton_Blink.clicked.connect(blink_clicked)
        
        self.label_bri = QtWidgets.QLabel(self.centralWidget)
        self.label_bri.setGeometry(QtCore.QRect(290, 50, 191, 61))
        self.label_bri.setObjectName("label_bri")
        
        self.label_status = QtWidgets.QLabel(self.centralWidget)
        self.label_status.setGeometry(QtCore.QRect(70, 50, 201, 61))
        self.label_status.setObjectName("label_status")
        #

        #----Up----
        self.pushButton_Up = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Up.setGeometry(QtCore.QRect(60, 260, 151, 101))
        self.pushButton_Up.setObjectName("pushButton_Up")
        self.pushButton_Up.clicked.connect(up_clicked)
        self.pushButton_Up.clicked.connect(self.light_bri)
        self.pushButton_Up.clicked.connect(self.light_status_on)

        #----Down---
        self.pushButton_Down = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Down.setGeometry(QtCore.QRect(210, 260, 141, 101))
        self.pushButton_Down.setObjectName("pushButton_Down")
        self.pushButton_Down.clicked.connect(down_clicked)
        self.pushButton_Down.clicked.connect(self.light_bri)        


        pihue.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(pihue)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 544, 22))
        self.menuBar.setObjectName("menuBar")
        pihue.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(pihue)
        self.mainToolBar.setObjectName("mainToolBar")
        pihue.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(pihue)
        self.statusBar.setObjectName("statusBar")
        pihue.setStatusBar(self.statusBar)

        self.retranslateUi(pihue)
        QtCore.QMetaObject.connectSlotsByName(pihue)

    def retranslateUi(self, pihue):
        _translate = QtCore.QCoreApplication.translate
        pihue.setWindowTitle(_translate("pihue", "pihue"))
        self.pushButton_On.setText(_translate("pihue", "On"))
        self.pushButton_Off.setText(_translate("pihue", "Off"))
        self.pushButton_Blink.setText(_translate("pihue", "Blink"))
        self.label_bri.setText(_translate("pihue", ""))
        self.label_status.setText(_translate("pihue", ""))
        #
        self.pushButton_Up.setText(_translate("pihue", "Up"))
        self.pushButton_Down.setText(_translate("pihue", "Down"))

    def light_status_on(self):
        self.label_status.setText("Lights On")

    def light_status_off(self):
        self.label_status.setText("Lights Off")

    def light_bri(self):
        if b.get_light(1, 'on') is True:
            cur_bri = b.get_light(1, 'bri')
            per = 100 * cur_bri / 254 
            self.label_bri.setText(str(int(per)) + "%")
        else:
            self.label_bri.setText(str(0) + "%")
            self.label_status.setText("Lights Off")
           
    def light_bri_0(self):
        self.label_bri.setText(str(0) + "%")
        
        
#--------------------------------

def on_clicked(self):
    print("On clicked")
    cur_bri = 254
    b.set_light(1, on_command)
    r = requests.post(url_on)

def off_clicked():
    print("Off clicked")
    cur_bri = 0
    b.set_light(1, off_command)
    r = requests.post(url_off)    

def blink_clicked():
    print("Blink clicked")
    var = b.get_light(1, 'on')
    cur_bri = b.get_light(1, 'bri')    
    for counter in range(1, 4):
        b.set_light(1, on_r)
        time.sleep(0.3)
        b.set_light(1, off_r)
        time.sleep(0.3)
        counter += 1
    if var is True:
        on_command_3 = {'on': True, 'bri': cur_bri}
        b.set_light(1, on_command_3)        
    else:
        b.set_light(1, off_command)

def down_clicked():
    cur_bri = b.get_light(1, 'bri')
    if cur_bri > 25:
        cur_bri = cur_bri -25
        b.set_light(1, 'bri', cur_bri)
    else:
        cur_bri = 0
        b.set_light(1, off_command)
        r = requests.post(url_off)        

def up_clicked():
    cur_bri = b.get_light(1, 'bri')
    cur_on = b.get_light(1, 'on')
    if cur_on is True:
        if cur_bri < 229:
            cur_bri = cur_bri + 25        
            on_command_2 = {'on': True, 'bri': cur_bri}
            b.set_light(1, on_command_2)
        else:
            b.set_light(1, on_command)
            r = requests.post(url_on)     
    else:
        cur_bri = 25
        on_command_4 = {'on': True, 'bri': cur_bri}
        b.set_light(1, on_command_4)
#------------------------
def update():
    while True:
        time.sleep(4)          
        r = requests.get(url_blink)   
        if r.json() == JSON_ON:
            var = b.get_light(1, 'on')
            cur_bri = b.get_light(1, 'bri')  
            print("Blink On")
            for counter in range(1, 5):
                b.set_light(1, on_r)
                time.sleep(0.3)
                b.set_light(1, off_r)
                time.sleep(0.3)
                counter += 1
            if var is True:
                on_command_5 = {'on': True, 'bri': cur_bri}     
                b.set_light(1, on_command_5)
            else:
                b.set_light(1, 'on', False)
            r = requests.put(url_blink, data = json.dumps(data), headers = headers)
        else:
            print("Blink Off")
        
if __name__ == "__main__":
    import sys
    back = Thread(target = update)
    back.start()
    app = QtWidgets.QApplication(sys.argv)
    pihue = QtWidgets.QMainWindow()
    ui = Ui_pihue()
    ui.setupUi(pihue)
    pihue.show()
    sys.exit(app.exec_())
