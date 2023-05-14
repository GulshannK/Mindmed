from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import mysql.connector as con
import datetime


ui, _ = loadUiType('00-02-03-00-mindmed-P_M-R.ui')



class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
        self.menubar.setVisible(False)
        self.b01.clicked.connect(self.login)
        
        self.menu11.triggered.connect(self.show_add_new_employee_tab)
        self.b111.clicked.connect(self.save_employee_id_informatom)
        self.menu12.triggered.connect(self.show_edit_employee_tab)
        self.b400.clicked.connect(self.fill_information_of_the_selected_employee)
        self.b121.clicked.connect(self.edit_employee_information)
        self.b122.clicked.connect(self.delete_employee_information)
      
        self.menu21.triggered.connect(self.show_add_new_member_tab)
        self.b211.clicked.connect(self.save_member_informatom)
        self.menu22.triggered.connect(self.show_edit_member_tab)
        self.b500.clicked.connect(self.fill_information_of_the_selected_member)
        self.b221.clicked.connect(self.edit_member_information)
        self.b222.clicked.connect(self.delete_member_information)     

####################################333

        self.menu31.triggered.connect(self.show_pomodoro_tab)
        self.b510.clicked.connect(self.fill_student)
        self.b520.clicked.connect(self.save_pomodoro_information
)

####################### MT ###################
        self.menu51.triggered.connect(self.show_anxiety_disorder_tab)
        self.b510_2.clicked.connect(self.anxiety)
        self.b520_2.clicked.connect(self.saveanxiety)
        self.menu52.triggered.connect(self.show_Wellbeing_Index_tab)
        self.b510_3.clicked.connect(self.wellbeing)
        self.b520_3.clicked.connect(self.savewellbeing)



################# Pomodoro ###########
        self.menu31.triggered.connect(self.show_pomodoro_tab)


# ################### Pomodoro
        self.start_button.clicked.connect(self.start_timer)
        self.stop_button.clicked.connect(self.stop_timer)
        self.reset_button.clicked.connect(self.reset_timer)

        self.work_time_initial = QTime(0, 1, 0)  # set initial work time back to 25 minute. Dont forget!!
        self.break_time_initial = QTime(0, 1, 0)  # set initial break time back to 5 minute. Dont forget!!
    
        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.is_working = True

        # Number of Sessions
        self.reps_completed = 0

        # Number of sessions Qlabel
        self.reps_label = self.findChild(QLabel, 'reps_label')
        
        ######## Report tab #########
        self.imr1.triggered.connect(self.show_Report_tab)
        self.bttn99.clicked.connect(self.show_details)


####### Login 

    def login(self):
        un = self.tb01.text()
        pw = self.tb02.text()
        if(un=="" and pw==""):
            self.menubar.setVisible(True)
            self.tabWidget.setCurrentIndex(1)
        else:
            QMessageBox.information(self,"Mental Health Management System", "Invalid admin login details, Try again !")
            self.l01.setText("Invalid admin login details, Try again !")


############## Add New Employee ###########

    def show_add_new_employee_tab(self):
        self.tabWidget.setCurrentIndex(2)
        self.fill_next_employee_id()


    def fill_next_employee_id(self):
        try:
            employee_id = 0
            mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
            cursor = mydb.cursor()
            cursor.execute("select * from employee")
            result = cursor.fetchall()
            if result:
                for employee in result:
                    employee_id += 1
                self.l111.setText(str(employee_id + 1))
        except con.Error as e:
            print("Error occured in select employee ID" + e)
        finally:
            cursor.close()
            mydb.close()           
     

    def save_employee_id_informatom(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
            cursor = mydb.cursor()
            employee_id =self.l111.text()
            first_name =self.tb112.text()
            last_name = self.tb113.text()
            gender = self.cb114.currentText()
            date_of_birth = "-".join([self.tb115_1.text(), self.tb115_2.text(), self.tb115_3.text()])
            mobail_num= self.tb116.text()
            email = self.tb117.text()
            address = self.tb118.text()
            city= self.tb119.text()
            department = self.cb120.currentText()
            comment = self.tb121.text()
         
            sql_insert_employee = "insert into employee (employeeID,first_name,last_name,gender,date_of_birth,mobail_number,email,address,city,department,comment) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            value = (employee_id,first_name,last_name,gender,date_of_birth, mobail_num,email,address,city,department,comment)
            
            if(first_name!="" and last_name!="" and gender!="" and date_of_birth!="" and mobail_num!="" and address!="" and city!="" and department!="" and comment!=""):
                cursor.execute(sql_insert_employee ,value)
                mydb.commit()
                self.l1100.setText("Employee information saved successfully")
                QMessageBox.information(self, "Mental health management system","Employee information added successfully!")
            else:
                QMessageBox.information(self,"Mental Health Management System", "Missing Employee information, Try again !")
                self.l1100.setText("IMissing Member information, Try again !")

            self.l1100.setText("Add New Employee")
            self.tb112.setText("")
            self.tb113.setText("")
            self.cb114.setCurrentText("")
            self.tb115_1.setText("")
            self.tb115_2.setText("")
            self.tb115_3.setText("")
            self.tb116.setText("")
            self.tb117.setText("")
            self.tb118.setText("")
            self.tb119.setText("")
            self.cb120.setCurrentText("")
            self.tb121.setText("")
            self.tabWidget.setCurrentIndex(1)
    
        except con.Error as e:
            self.l210.setText("Error occured in save employeeID information" + e)
        finally:
            cursor.close()
            mydb.close()


################### Edit Employee ###################

    def show_edit_employee_tab(self):
        self.tabWidget.setCurrentIndex(3)
        self.choose_employee_id_from_textbox()

    def choose_employee_id_from_textbox(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
            cursor = mydb.cursor()
            employee_id = self.l5000.text()  

            cursor.execute("select * from employee where employeeID ='"+ employee_id +"'")

            result = cursor.fetchall()
            if result:
                self.tb401.clear()
                for emp in result:
                    self.tb401.addItem(str(emp[0]))

        except con.Error as e:
            print("Error occurred for the selected employee ID in the combobox" + e)
        finally:
            cursor.close()
            mydb.close()
           

    def fill_information_of_the_selected_employee(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db="MindMed")
            cursor = mydb.cursor()

            cursor.execute("SELECT * FROM employee WHERE employeeID = %s", (self.tb401.text(),))
            result = cursor.fetchone()
            if result:
                self.tb122.setText(str(result[1]))
                self.tb123.setText(str(result[2]))
                self.cb124.setCurrentText(str(result[3]))
                self.tb125_1.setText(str(result[4][0:4]))
                self.tb125_2.setText(str(result[4][5:7]))
                self.tb125_3.setText(str(result[4][-2:]))
                self.tb126.setText(str(result[5]))
                self.tb127.setText(str(result[6]))
                self.tb128.setText(str(result[7]))
                self.tb129.setText(str(result[8]))
                self.cb130.setCurrentText(str(result[9]))
                self.tb131.setText(str(result[10]))
            else:
                QMessageBox.information(self,"Mental Health Management System", "No employee found with this ID")


        except con.Error as e:
            print("Error occurred while filling the selected employee ID:", e)
        finally:
            cursor.close()
            mydb.close()


    def edit_employee_information(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
            cursor = mydb.cursor()
            employee_id =self.tb401.text()
            first_name =self.tb122.text()
            last_name = self.tb123.text()
            gender = self.cb124.currentText()
            date_of_birth = "-".join([self.tb125_1.text(), self.tb125_2.text(), self.tb125_3.text()])
            mobail_num= self.tb126.text()
            email = self.tb127.text()
            address = self.tb128.text()
            city= self.tb129.text()
            department = self.cb130.currentText()
            comment = self.tb131.text()
            
            sql_insert_member = "update employee set first_name ='"+ first_name +"',last_name ='"+ last_name +"',gender ='"+ gender +"',date_of_birth ='"+ date_of_birth +"',mobail_number ='"+ mobail_num +"',email ='"+ email +"',address ='"+ address +"',city ='"+ city +"',department ='"+ department +"',comment ='"+ comment +"' where employeeID = '"+ employee_id +"'"

            if(first_name!="" and last_name!="" and gender!="" and date_of_birth!="" and mobail_num!="" and address!="" and city!="" and department!="" and comment!=""):
                cursor.execute(sql_insert_member)
                mydb.commit()
                self.l1200.setText("Employee information edit successfully")# I need to check later
                QMessageBox.information(self, "Mental health management system","Employee information edit successfully!")
            else:
                QMessageBox.information(self,"Mental Health Management System", "Missing Employee information, Try again !")
                self.l1200.setText("Missing Employee information, Try again !")                  
            
            self.tb401.setText("")
            self.tb122.setText("")
            self.tb123.setText("")
            self.cb124.setCurrentText("")
            self.tb125_1.setText("")
            self.tb125_2.setText("")
            self.tb125_3.setText("")
            self.tb126.setText("")
            self.tb127.setText("")
            self.tb128.setText("")
            self.tb129.setText("")
            self.cb130.setCurrentText("")
            self.tb131.setText("")
            self.tabWidget.setCurrentIndex(1)
            
        except con.Error as e:
            self.l1200.setText("Error occured in edit selected Employee" + e)
        finally:
            cursor.close()
            mydb.close()
            
            
    def delete_employee_information(self):
        delete_message = QMessageBox.question(self,"Delete", "Are you sure you want to delete this employee",QMessageBox.Yes|QMessageBox.No )
        if delete_message == QMessageBox.Yes:
            try:
                mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
                cursor = mydb.cursor()
                employee_id =self.tb401.text()
                sql_delete_employee = "update employee set first_name='Deleted', last_name='Deleted', gender='', date_of_birth='', mobail_number='', email='', address='', city='', department='', comment='Deleted by Admin' where employeeID = '"+ employee_id +"'"
                cursor.execute(sql_delete_employee)
                mydb.commit()
                self.l1200.setText("Employee information deleted successfully")
                QMessageBox.information(self, "Mental health management system","Employee information deleted successfully!")

                self.tb401.setText("")
                self.tb122.setText("")
                self.tb123.setText("")
                self.cb124.setCurrentText("")
                self.tb125_1.setText("")
                self.tb125_2.setText("")
                self.tb125_3.setText("")
                self.tb126.setText("")
                self.tb127.setText("")
                self.tb128.setText("")
                self.tb129.setText("")
                self.cb130.setCurrentText("")
                self.tb131.setText("")
                self.tabWidget.setCurrentIndex(1)
            
            except con.Error as e:
                self.l220.setText("Error occured in delete selected employee" + e)
            finally:
                cursor.close()
                mydb.close()           
       

############## Add New Member ###########

    def show_add_new_member_tab(self):
        self.tabWidget.setCurrentIndex(4)
        self.fill_next_member_id()


    def fill_next_member_id(self):
        try:
            member_id = 0
            mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
            cursor = mydb.cursor()
            cursor.execute("select * from member")
            result = cursor.fetchall()
            if result:
                for member in result:
                    member_id += 1
                self.l211.setText(str(member_id + 1))
        except con.Error as e:
            print(f"Error occured in select member ID {e}")
        finally:
            cursor.close()
            mydb.close()           
     

    def save_member_informatom(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
            cursor = mydb.cursor()
            member_id =self.l211.text()
            first_name =self.tb212.text()
            last_name = self.tb213.text()
            gender = self.cb214.currentText()
            date_of_birth = "-".join([self.tb215_1.text(), self.tb215_2.text(), self.tb215_3.text()])
            mobail_num= self.tb216.text()
            email = self.tb217.text()
            address = self.tb218.text()
            city= self.tb219.text()
            department = self.cb220.currentText()
            comments = self.tb221.text()
         
            sql_insert_member = "insert into member (memberID,first_name,last_name,gender,date_of_birth,mobail_number,email,address,city,department,comments) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            value = (member_id,first_name,last_name,gender,date_of_birth, mobail_num,email,address,city,department,comments)
            
            if(first_name!="" and last_name!="" and gender!="" and date_of_birth!="" and mobail_num!="" and address!="" and city!="" and department!="" and comments!=""):
                cursor.execute(sql_insert_member ,value)
                mydb.commit()
                self.l210.setText("Member information saved successfully")
                QMessageBox.information(self, "Mental health management system","Member information added successfully!")
            else:
                QMessageBox.information(self,"Mental Health Management System", "Missing Member information, Try again !")
                self.l210.setText("IMissing Member information, Try again !")

            self.l210.setText("Add New Member")
            self.tb212.setText("")
            self.tb213.setText("")
            self.cb214.setCurrentText("")
            self.tb215_1.setText("")
            self.tb215_2.setText("")
            self.tb215_3.setText("")
            self.tb216.setText("")
            self.tb217.setText("")
            self.tb218.setText("")
            self.tb219.setText("")
            self.cb220.setCurrentText("")
            self.tb221.setText("")
            self.tabWidget.setCurrentIndex(1)
    
        except con.Error as e:
            self.l210.setText(f"Error occured in save memberID information {e}")
        finally:
            cursor.close()
            mydb.close()


################### Edit Member ###################

    def show_edit_member_tab(self):
        self.tabWidget.setCurrentIndex(5)
        self.choose_member_from_textbox()

    def choose_member_from_textbox(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
            cursor = mydb.cursor()
            member_id = self.l5000.text()  

            cursor.execute("select * from member where memberID ='"+ member_id +"'")

            result = cursor.fetchall()
            if result:
                self.tb501.clear()
                for mem in result:
                    self.tb501.addItem(str(mem[0]))

        except con.Error as e:
            print("Error occurred for the selected employee ID in the combobox" + e)
        finally:
            cursor.close()
            mydb.close()
           

    def fill_information_of_the_selected_member(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db="MindMed")
            cursor = mydb.cursor()

            cursor.execute("SELECT * FROM member WHERE memberID = %s", (self.tb501.text(),))
            result = cursor.fetchone()
            if result:
                self.tb222.setText(str(result[1]))
                self.tb223.setText(str(result[2]))
                self.cb224.setCurrentText(str(result[3]))
                self.tb225_1.setText(str(result[4][0:4]))
                self.tb225_2.setText(str(result[4][5:7]))
                self.tb225_3.setText(str(result[4][-2:]))
                self.tb226.setText(str(result[5]))
                self.tb227.setText(str(result[6]))
                self.tb228.setText(str(result[7]))
                self.tb229.setText(str(result[8]))
                self.cb230.setCurrentText(str(result[9]))
                self.tb231.setText(str(result[10]))
            else:
                QMessageBox.information(self,"Mental Health Management System", "No member found with this ID")


        except con.Error as e:
            print("Error occurred while filling the selected member ID:", e)
        finally:
            cursor.close()
            mydb.close()

    def edit_member_information(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
            cursor = mydb.cursor()
            member_id =self.tb501.text()
            first_name =self.tb222.text()
            last_name = self.tb223.text()
            gender = self.cb224.currentText()
            date_of_birth = "-".join([self.tb225_1.text(), self.tb225_2.text(), self.tb225_3.text()])
            mobail_num= self.tb226.text()
            email = self.tb227.text()
            address = self.tb228.text()
            city= self.tb229.text()
            department = self.cb230.currentText()
            comment = self.tb231.text()
            
            sql_insert_member = "update member set first_name ='"+ first_name +"',last_name ='"+ last_name +"',gender ='"+ gender +"',date_of_birth ='"+ date_of_birth +"',mobail_number ='"+ mobail_num +"',email ='"+ email +"',address ='"+ address +"',city ='"+ city +"',department ='"+ department +"',comment ='"+ comment +"' where memberID = '"+ member_id +"'"

            if(first_name!="" and last_name!="" and gender!="" and date_of_birth!="" and mobail_num!="" and address!="" and city!="" and department!="" and comment!=""):
                cursor.execute(sql_insert_member)
                mydb.commit()
                self.l220.setText("Member information edit successfully")
                QMessageBox.information(self, "Mental health management system","Member information edit successfully!")
            else:
                QMessageBox.information(self,"Mental Health Management System", "Missing Member information, Try again !")
                self.l220.setText("Missing Member information, Try again !")                  
            
            self.tb501.setText("")
            self.tb222.setText("")
            self.tb223.setText("")
            self.cb224.setCurrentText("")
            self.tb225_1.setText("")
            self.tb225_2.setText("")
            self.tb225_3.setText("")
            self.tb226.setText("")
            self.tb227.setText("")
            self.tb228.setText("")
            self.tb229.setText("")
            self.cb230.setCurrentText("")
            self.tb231.setText("")
            self.tabWidget.setCurrentIndex(1)
            
        except con.Error as e:
            self.l220.setText("Error occured in edit selected member" + e)
        finally:
            cursor.close()
            mydb.close()


    def delete_member_information(self):
        delete_message = QMessageBox.question(self,"Delete", "Are you sure you want to delete this member",QMessageBox.Yes|QMessageBox.No )
        if delete_message == QMessageBox.Yes:
            try:
                mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
                cursor = mydb.cursor()
                member_id =self.tb501.text()
                sql_delete_member = "update member set first_name='Deleted', last_name='Deleted', gender='', date_of_birth='', mobail_number='', email='', address='', city='', department='', comment='Deleted by Admin' where memberID = '"+ member_id +"'"
                cursor.execute(sql_delete_member)
                mydb.commit()
                self.l220.setText("Member information deleted successfully")
                QMessageBox.information(self, "Mental health management system","Member information deleted successfully!")

                self.tb501.setText("")
                self.tb222.setText("")
                self.tb223.setText("")
                self.cb224.setCurrentText("")
                self.tb225_1.setText("")
                self.tb225_2.setText("")
                self.tb225_3.setText("")
                self.tb226.setText("")
                self.tb227.setText("")
                self.tb228.setText("")
                self.tb229.setText("")
                self.cb230.setCurrentText("")
                self.tb231.setText("")
                self.tabWidget.setCurrentIndex(1)
            
            except con.Error as e:
                self.l220.setText("Error occured in delete selected member" + e)
            finally:
                cursor.close()
                mydb.close()           

############## Add New Member ###########

    def show_pomodoro_tab(self):
        self.tabWidget.setCurrentIndex(6)

############### Pomodoro Timer ################

    def start_timer(self):
            # Start timer
            self.timer.start(1000)
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)


    def stop_timer(self):
            # Stop timer
            self.timer.stop()
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)


    def reset_timer(self):
            # Reset timer
            self.timer.stop()

            self.work_time_initial = QTime(0, 1, 0)  # set initial work time back to 25 minutes
            self.break_time_initial = QTime(0, 1, 0) # Set initial break time back to 5 minutes

            self.lcd1.display(self.work_time_initial.toString('mm:ss'))
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            self.is_working = True

            self.reps_completed = 0
            self.reps_label.setText("Sessions: 0")     
        

    def tick(self):
        # Updates the timer display
            if self.is_working:
                self.work_time_initial = self.work_time_initial.addSecs(-1)
                self.lcd1.display(self.work_time_initial.toString('mm:ss'))
                if self.work_time_initial == QTime(0, 0):
                    self.is_working = False

                    self.reps_completed += 1
                    self.reps_label.setText(f"Sessions: {self.reps_completed}")

                    self.break_time_initial = QTime(0, 1, 0) # Set back to 5 minutes
                    self.lcd1.display(self.break_time_initial.toString('mm:ss'))
            else:
                self.break_time_initial = self.break_time_initial.addSecs(-1)
                self.lcd1.display(self.break_time_initial.toString('mm:ss'))
                if self.break_time_initial == QTime(0, 0):
                    self.is_working = True

                    self.work_time_initial = QTime(0, 1, 0) # set back to 25 minutes
                    self.lcd1.display(self.work_time_initial.toString('mm:ss'))   


      
########################################



########################################
    def show_pomodoro_tab(self):
        self.tabWidget.setCurrentIndex(6)
        self.choose_student_textbox()


    def save_pomodoro_information(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
            cursor = mydb.cursor()
            
            first_name =self.tb602.text()
            last_name = self.tb603.text()
            department =  self.tb604.text()
            num_pomodoro_session = self.tb605.text()
            date_of_adding_session = QDate.currentDate().toString(Qt.ISODate)

            # self.date_label.setText(date_of_adding_session) # Displays current date in label

            sql_insert_student = "insert into pomodoro (first_name,last_name,department,num_pomodoro_session,date_of_adding_session) values(%s,%s,%s,%s,%s)"
            values = (first_name, last_name, department, num_pomodoro_session, date_of_adding_session)

            if first_name != "" and last_name != "" and num_pomodoro_session.isnumeric():
                cursor.execute(sql_insert_student, values)
                mydb.commit()
                QMessageBox.information(self, "Mental health management system", "Student session added successfully!")
            else:
                QMessageBox.information(self,"Mental Health Management System", "Missing or invalid input, please try again.")

            self.tb602.setText("")
            self.tb603.setText("")
            self.tb604.setText("")
            self.tb605.setText("")

        except con.Error as e:
            print(f"Error occurred in save_pomodoro_information: {e}")
            mydb.rollback()

        finally:
            cursor.close()
            mydb.close()
            
                
    def choose_student_textbox(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
            cursor = mydb.cursor()
            employee_id = self.tb601.text()  

            cursor.execute("select * from member where memberID ='"+ employee_id +"'")

            result = cursor.fetchall()
            if result:
                self.tb601.clear()
                for emp in result:
                    self.tb601.addItem(str(emp[0]))

        except con.Error as e:
            print("Error occurred for the selected member ID in the combobox" + e)
        finally:
            cursor.close()
            mydb.close()
            

    def fill_student(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db="MindMed")
            cursor = mydb.cursor()

            cursor.execute("SELECT * FROM member WHERE memberID = %s", (self.tb601.text(),))
            result = cursor.fetchone()
            if result:
                self.tb602.setText(str(result[1]))
                self.tb603.setText(str(result[2]))
                self.tb604.setText(str(result[9]))

            else:
                QMessageBox.information(self,"Mental Health Management System", "No student found with this ID")


        except con.Error as e:
            print("Error occurred while filling the selected student ID:", e)
        finally:
            cursor.close()
            mydb.close()         

         
 ############################################### MT ######################################
 
    def show_anxiety_disorder_tab(self):
        self.tabWidget.setCurrentIndex(7)
        
 
    def anxiety(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
            cursor = mydb.cursor()
            
            cursor.execute("SELECT * FROM member WHERE memberID = %s", (self.tb800.text(),))
            result = cursor.fetchone()
            if result:
                self.tb801.setText(str(result[1]))
                self.tb802.setText(str(result[2]))
                self.tb803.setText(str(result[9]))

            else:
                QMessageBox.information(self,"Mental Health Management System", "No student found with this ID")
        
        except con.Error as e:
            print(f"Error occurred in save_pomodoro_information: {e}")
            mydb.rollback()

        finally:
            cursor.close()
            mydb.close()
    
    def saveanxiety(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
            cursor = mydb.cursor()
            first_name = self.tb801.text()
            last_name = self.tb802.text()
            department = self.tb803.text()         
            answer1 = self.tb811.text()
            answer2 = self.tb812.text()
            answer3 = self.tb813.text()
            answer4 = self.tb814.text()
            answer5 = self.tb815.text()
            answer6 = self.tb816.text()
            answer7 = self.tb817.text()
            # date_of_adding_session = QDate.currentDate().toString(Qt.ISODate)

            # self.date_label.setText(date_of_adding_session) # Displays current date in label

            sql_insert_student = "insert into moodtracker (first_name,last_name,department,answer1,answer2,answer3,answer4,answer5,answer6,answer7) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (first_name, last_name, department, answer1, answer2, answer3, answer4, answer5, answer6, answer7)

            if first_name != "" and last_name != "":
                cursor.execute(sql_insert_student, values)
                mydb.commit()
                QMessageBox.information(self, "Mental health management system", "User record added successfully!")
            else:
                QMessageBox.information(self,"Mental Health Management System", "Missing or invalid input, please try again.")

            self.tb801.setText("")
            self.tb802.setText("")
            self.tb803.setText("")
            self.tb811.setText("")
            self.tb812.setText("")
            self.tb813.setText("")
            self.tb814.setText("")
            self.tb815.setText("")
            self.tb816.setText("")
            self.tb817.setText("")
        except con.Error as e:
            print(f"Error occurred in moodtracker_information: {e}")
            mydb.rollback()

        finally:
            cursor.close()
            mydb.close()

    def show_Wellbeing_Index_tab(self):
        self.tabWidget.setCurrentIndex(8)
        
    def wellbeing(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
            cursor = mydb.cursor()
            
            cursor.execute("SELECT * FROM member WHERE memberID = %s", (self.tb900.text(),))
            result = cursor.fetchone()
            if result:
                self.tb901.setText(str(result[1]))
                self.tb902.setText(str(result[2]))
                self.tb903.setText(str(result[9]))

            else:
                QMessageBox.information(self,"Mental Health Management System", "No student found with this ID")
        
        except con.Error as e:
            print(f"Error occurred in mood_tracker_information: {e}")
            mydb.rollback()

        finally:
            cursor.close()
            mydb.close()
            
    def savewellbeing(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db = "MindMed")
            cursor = mydb.cursor()
            first_name = self.tb901.text()
            last_name = self.tb902.text()
            department = self.tb903.text()         
            answer1 = self.tb911.text()
            answer2 = self.tb912.text()
            answer3 = self.tb913.text()
            answer4 = self.tb914.text()
            answer5 = self.tb915.text()

            # date_of_adding_session = QDate.currentDate().toString(Qt.ISODate)

            # self.date_label.setText(date_of_adding_session) # Displays current date in label

            sql_insert_student = "insert into moodtrackerwho (first_name,last_name,department,answer1,answer2,answer3,answer4,answer5) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (first_name, last_name, department, answer1, answer2, answer3, answer4, answer5)

            if first_name != "" and last_name != "" and answer1 != " " and answer2 != " "and answer3 != " " and answer4 != " " and answer5 != " ":
                cursor.execute(sql_insert_student, values)
                mydb.commit()
                QMessageBox.information(self, "Mental health management system", "User record added successfully!")
            else:
                QMessageBox.information(self,"Mental Health Management System", "Missing or invalid input, please try again.")

            self.tb901.setText("")
            self.tb902.setText("")
            self.tb903.setText("")
            self.tb911.setText("")
            self.tb912.setText("")
            self.tb913.setText("")
            self.tb914.setText("")
            self.tb915.setText("")

        except con.Error as e:
            print(f"Error occurred in moodtracker inforamation: {e}")
            mydb.rollback()

        finally:
            cursor.close()
            mydb.close()


############################################## Report ###################################


    def show_Report_tab(self):
        self.tabWidget.setCurrentIndex(9)
 
    def show_details(self):
        try:
            mydb = con.connect(host="localhost", user="root", password="gulshan", db="MindMed")
            cursor = mydb.cursor()

            cursor.execute("SELECT * FROM pomodoro WHERE first_name = %s", (self.line99.text(),))
            result = cursor.fetchone()
            if result:
                self.lineEdit.setText(str(result[0]))
                self.lineEdit_2.setText(str(result[1]))
                self.lineEdit_3.setText(str(result[2]))
                self.lineEdit_4.setText(str(result[3]))
                self.lineEdit_5.setText(str(result[4]))

            else:
                QMessageBox.information(self,"Mental Health Management System", "No student found with this ID")
        
        except con.Error as e:
            print("Error occurred while filling the selected student ID:", e)
        finally:
            cursor.close()
            mydb.close()         
 ##############################################
 
 
        
def main():

    app = QApplication(sys.argv)

    window = MainApp()

    window.show()

    app.exec_()



if __name__ == '__main__':

    main()
