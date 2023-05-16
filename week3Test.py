import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock
import mysql.connector as con
from unittest.mock import patch
from PyQt5.QtWidgets import QApplication, QMessageBox
import test


########## Test for Mental Health Management System ##########
class TestMentalHealthManagementSystem(unittest.TestCase):

    def setUp(self):
       
        self.app = test.MainApp()

    def tearDown(self):
        pass

    @patch('mindmed.mysql.connector') # patch is mock object
    def test_anxiety(self, mock_connector):
        self.app.tb800.setText("1")
        self.app.tb801.setText("")
        self.app.tb802.setText("")
        self.app.tb803.setText("")
        
        cursor_mock = MagicMock()
        cursor_mock.fetchone.return_value = ('Hannah', 'Clark', 'Southville')
        self.app.mydb.cursor.return_value = cursor_mock

        self.app.anxiety()

        self.assertEqual(self.app.tb801.text(), 'Hannah')
        self.assertEqual(self.app.tb802.text(), 'Clark')
        self.assertEqual(self.app.tb803.text(), 'Southville')
        
        
    @patch('mindmed.mysql.connector')
    def test_saveanxiety(self, mock_connector):
    
        self.app.tb801.setText("John")
        self.app.tb802.setText("Doe")
        self.app.tb803.setText("Department")
        self.app.tb811.setText("Answer1")
        self.app.tb812.setText("Answer2")
        self.app.tb813.setText("Answer3")
        self.app.tb814.setText("Answer4")
        self.app.tb815.setText("Answer5")
        self.app.tb816.setText("Answer6")
        self.app.tb817.setText("Answer7")
  
        cursor_mock = MagicMock()
        self.app.mydb.cursor.return_value = cursor_mock
 
        self.app.saveanxiety()

        self.assertTrue(cursor_mock.execute.called)
        self.assertTrue(self.app.mydb.commit.called)
        self.assertEqual(self.app.tb801.text(), "")
        self.assertEqual(self.app.tb802.text(), "")
        self.assertEqual(self.app.tb803.text(), "")
        self.assertEqual(self.app.tb811.text(), "")
        self.assertEqual(self.app.tb812.text(), "")
        self.assertEqual(self.app.tb813.text(), "")
        self.assertEqual(self.app.tb814.text(), "")
        self.assertEqual(self.app.tb815.text(), "")
        self.assertEqual(self.app.tb816.text(), "")
        self.assertEqual(self.app.tb817.text(), "")
        
    @patch('mindmed.mysql.connector')
    def test_wellbeing(self, mock_connector):
        
        self.app.tb900.setText("1")
        self.app.tb901.setText("")
        self.app.tb902.setText("")
        self.app.tb903.setText("")
        
        cursor_mock = MagicMock()
        cursor_mock.fetchone.return_value = ('Jane', 'Smith', 'Southville')
        self.app.mydb.cursor.return_value = cursor_mock

        self.app.wellbeing()

        self.assertEqual(self.app.tb901.text(), 'Jane')
        self.assertEqual(self.app.tb902.text(), 'Smith')
        self.assertEqual(self.app.tb903.text(), 'Answer9')

    @patch('mindmed.mysql.connector')
    def test_savewellbeing(self,mock_connector):
        
        self.app.tb901.setText("Jane")
        self.app.tb902.setText("Smith")
        self.app.tb903.setText("Department")
        self.app.tb911.setText("Answer1")
        self.app.tb912.setText("Answer2")
        self.app.tb913.setText("Answer3")
        self.app.tb914.setText("Answer4")
        self.app.tb915.setText("Answer5")

        cursor_mock = MagicMock()
        self.app.mydb.cursor.return_value = cursor_mock

        self.app.savewellbeing()

        self.assertTrue(cursor_mock.execute.called)
        self.assertTrue(self.app.mydb.commit.called)
        self.assertEqual(self.app.tb901.text(), "")
        self.assertEqual(self.app.tb902.text(), "")
        self.assertEqual(self.app.tb903.text(), "")
        self.assertEqual(self.app.tb911.text(), "")
        self.assertEqual(self.app.tb912.text(), "")
        self.assertEqual(self.app.tb913.text(), "")
        self.assertEqual(self.app.tb914.text(), "")
        self.assertEqual(self.app.tb915.text(), "")

if __name__ == '__main__':
    unittest.main()
