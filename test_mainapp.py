import unittest
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
ui, _ = loadUiType('mindmed.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
        self.menubar.setVisible(False)
        self.b01.clicked.connect(self.login)

    def login(self):
        un = self.tb01.text()
        pw = self.tb02.text()
        if (un == "admin" and pw == "1979"):
            self.menubar.setVisible(True)
            self.tabWidget.setCurrentIndex(1)
        else:
            QMessageBox.information(self,"Mental Health Management System", "Invalid admin login details, Try again !")
            self.l01.setText("Invalid admin login details, Try again !")

class TestMainApp(unittest.TestCase):

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = MainApp()

    def tearDown(self):
        self.window.close()

    def test_login_success(self):
        self.window.tb01.setText("admin")
        self.window.tb02.setText("1979")
        self.window.login()
        self.assertTrue(self.window.menubar.isVisible())
        self.assertEqual(self.window.tabWidget.currentIndex(), 1)

    def test_login_failure(self):
        self.window.tb01.setText("invalid")
        self.window.tb02.setText("password")
        self.window.login()
        self.assertFalse(self.window.menubar.isVisible())
        self.assertEqual(self.window.tabWidget.currentIndex(), 0)
        self.assertEqual(self.window.l01.text(), "Invalid admin login details, Try again !")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
