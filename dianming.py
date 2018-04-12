# -*- coding: utf-8 -*-

import os
from typing import Union

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
import DianmingWin
from datastore import Students
from datastore import SRecords


def updateui():
    pass

def initdata():
    pass

if __name__ == '__main__':
    import sys

    # open data file
    datafile: Union[bytes, str] = os.path.join(os.path.abspath('.'), 'Datas/JH1501.xlsx')
    studentslist = pd.read_excel(datafile)
    SS = pd.read_excel(datafile)

    # init the UIs
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = DianmingWin.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()


    # this section is for image showing test
    sface = QPixmap('Datas/Face/2014012329.jpg')
    ui.graphicsView.setPixmap(sface)
    sface.load(os.path.join(os.path.abspath('.'), 'Datas/Face/2014012390.jpg'))

    ui.graphicsView.setPixmap(sface)
    sys.exit(app.exec())
