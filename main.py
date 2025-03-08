import mysql.connector as sq

def connect():
    db = sq.connect(
        host='localhost',
        user='root',
        password='kiddo',
        database='schoolmgt'
    )
    if not db.is_connected():
        print("Database connection failed")
    return db


def student_management():
    print("a. NEW ADMISSION")
    print("b. UPDATE DETAILS")
    print("c. ISSUE TC")
    print("d. DISPLAY STUDENTS")
    choice = input("Enter your choice (a-d): ").lower()

    if choice == 'a':
        def insert_student():
            name = input("Enter name: ")
            admno = int(input("Enter admission number: "))
            clas = input("Enter class: ")
            city = input("Enter city: ")
            dob = input("Enter DOB (YYYY-MM-DD): ")
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("INSERT INTO st (admno, name, class, city, dob) VALUES (%s, %s, %s, %s, %s)",
                            (admno, name, clas, city, dob))
                con.commit()
                con.close()
                print("Student record inserted successfully.")
        insert_student()

    elif choice == 'b':
        def update_student():
            admno = int(input("Enter admission number: "))
            clas = input("Enter new class: ")
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("UPDATE st SET class = %s WHERE admno = %s", (clas, admno))
                con.commit()
                con.close()
                print("Student record updated successfully.")
        update_student()

    elif choice == 'c':
        def delete_student():
            admno = int(input("Enter admission number to delete: "))
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("DELETE FROM st WHERE admno = %s", (admno,))
                con.commit()
                con.close()
                print("Student record deleted successfully.")
        delete_student()

    elif choice == 'd':
        def display_students():
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("SELECT * FROM st")
                for i in cur.fetchall():
                    print(i)
                con.close()
        display_students()

    else:
        print("Invalid choice.")

def employee_management():
    print("a. NEW EMPLOYEE")
    print("b. UPDATE EMPLOYEE")
    print("c. DELETE EMPLOYEE")
    print("d. DISPLAY EMPLOYEES")
    choice = input("Enter your choice (a-d): ").lower()

    if choice == 'a':
        def insert_employee():
            empno = int(input("Enter employee number: "))
            name = input("Enter name: ")
            job = input("Enter job: ")
            hiredate = input("Enter hire date (YYYY-MM-DD): ")
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("INSERT INTO emp (empno, name, job, hiredate) VALUES (%s, %s, %s, %s)",
                            (empno, name, job, hiredate))
                con.commit()
                con.close()
                print("Employee record inserted successfully.")
        insert_employee()

    elif choice == 'b':
        def update_employee():
            empno = int(input("Enter employee number: "))
            job = input("Enter new job: ")
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("UPDATE emp SET job = %s WHERE empno = %s", (job, empno))
                con.commit()
                con.close()
                print("Employee record updated successfully.")
        update_employee()

    elif choice == 'c':
        def delete_employee():
            empno = int(input("Enter employee number to delete: "))
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("DELETE FROM emp WHERE empno = %s", (empno,))
                con.commit()
                con.close()
                print("Employee record deleted successfully.")
        delete_employee()

    elif choice == 'd':
        def display_employees():
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("SELECT * FROM emp")
                for i in cur.fetchall():
                    print(i)
                con.close()
        display_employees()

    else:
        print("Invalid choice.")


def fee_management():
    print("a. INSERT FEE RECORD")
    print("b. UPDATE FEE RECORD")
    print("c. DELETE FEE RECORD")
    print("d. DISPLAY FEE RECORDS")
    choice = input("Enter your choice (a-d): ").lower()

    if choice == 'a':
        def insert_fee():
            admno = int(input("Enter admission number: "))
            fees = float(input("Enter fee amount: "))
            monthunpaid = input("Enter month unpaid (if any): ")
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("INSERT INTO fees (admno, fees, monthunpaid) VALUES (%s, %s, %s)",
                            (admno, fees, monthunpaid))
                con.commit()
                con.close()
                print("Fee record inserted successfully.")
        insert_fee()

    elif choice == 'b':
        def update_fee():
            admno = int(input("Enter admission number: "))
            monthunpaid = input("Enter new month unpaid: ")
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("UPDATE fees SET monthunpaid = %s WHERE admno = %s", (monthunpaid, admno))
                con.commit()
                con.close()
                print("Fee record updated successfully.")
        update_fee()

    elif choice == 'c':
        def delete_fee():
            admno = int(input("Enter admission number to delete fee record: "))
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("DELETE FROM fees WHERE admno = %s", (admno,))
                con.commit()
                con.close()
                print("Fee record deleted successfully.")
        delete_fee()

    elif choice == 'd':
        def display_fee():
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("SELECT * FROM fees")
                for i in cur.fetchall():
                    print(i)
                con.close()
        display_fee()

    else:
        print("Invalid choice.")

def attendance_management():
    print("a. INSERT ATTENDANCE")
    print("b. UPDATE ATTENDANCE")
    print("c. DELETE ATTENDANCE")
    print("d. DISPLAY ATTENDANCE RECORDS")
    choice = input("Enter your choice (a-d): ").lower()

    if choice == 'a':
        def insert_attendance():
            admno = int(input("Enter admission number: "))
            present = int(input("Enter number of classes attended: "))
            totalpresent = int(input("Enter total number of classes: "))
            per = (present / totalpresent) * 100
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("INSERT INTO attendance (admno, present, totalpresent, per) VALUES (%s, %s, %s, %s)",
                            (admno, present, totalpresent, per))
                con.commit()
                con.close()
                print("Attendance record inserted successfully.")
        insert_attendance()

    elif choice == 'b':
        def update_attendance():
            admno = int(input("Enter admission number: "))
            present = int(input("Enter new number of classes attended: "))
            totalpresent = int(input("Enter new total number of classes: "))
            per = (present / totalpresent) * 100
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("UPDATE attendance SET present = %s, totalpresent = %s, per = %s WHERE admno = %s",
                            (present, totalpresent, per, admno))
                con.commit()
                con.close()
                print("Attendance record updated successfully.")
        update_attendance()

    elif choice == 'c':
        def delete_attendance():
            admno = int(input("Enter admission number to delete attendance record: "))
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("DELETE FROM attendance WHERE admno = %s", (admno,))
                con.commit()
                con.close()
                print("Attendance record deleted successfully.")
        delete_attendance()

    elif choice == 'd':
        def display_attendance():
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("SELECT * FROM attendance")
                for i in cur.fetchall():
                    print(i)
                con.close()
        display_attendance()

    else:
        print("Invalid choice.")


def school_management():
    print("a. INSERT SCHOOL DETAILS")
    print("b. UPDATE SCHOOL DETAILS")
    print("c. DELETE SCHOOL DETAILS")
    print("d. DISPLAY SCHOOL DETAILS")
    choice = input("Enter your choice (a-d): ").lower()

    if choice == 'a':
        def insert_school():
            id = int(input("Enter School Code:  "))
            sname = input("Enter school name: ")
            noofstudent = int(input("Enter number of students: "))
            noofemployee = int(input("Enter number of employees: "))
            nooflabs = int(input("Enter number of labs: "))
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("INSERT INTO school (id,sname, noofstudent, noofemployee, nooflabs) VALUES (%s, %s, %s, %s, %s)",
                            (id, sname, noofstudent, noofemployee, nooflabs))
                con.commit()
                con.close()
                print("School record inserted successfully.")
        insert_school()

    elif choice == 'b':
        def update_school():
            sname = input("Enter new school name: ")
            noofstudent = int(input("Enter new number of students: "))
            noofemployee = int(input("Enter new number of employees: "))
            nooflabs = int(input("Enter new number of labs: "))
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("UPDATE school SET sname = %s, noofstudent = %s, noofemployee = %s, nooflabs = %s WHERE id = 1",
                            (sname, noofstudent, noofemployee, nooflabs))  # Assuming id=1 for simplicity
                con.commit()
                con.close()
                print("School record updated successfully.")
        update_school()

    elif choice == 'c':
        def delete_school():
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("DELETE FROM school WHERE id = 1")
                con.commit()
                con.close()
                print("School record deleted successfully.")
        delete_school()

    elif choice == 'd':
        def display_school():
            con = connect()
            if con:
                cur = con.cursor()
                cur.execute("SELECT * FROM school")
                for i in cur.fetchall():
                    print(i)
                con.close()
        display_school()

    else:
        print("Invalid choice.")

def main_menu():
    print("1. STUDENT MANAGEMENT")
    print("2. EMPLOYEE MANAGEMENT")
    print("3. FEE MANAGEMENT")
    print("4. ATTENDANCE MANAGEMENT")
    print("5. SCHOOL MANAGEMENT")
    print("6. EXIT")
    try:
        choice = int(input("Enter your choice (1-6): "))
        if choice == 1:
            student_management()
        elif choice == 2:
            employee_management()
        elif choice == 3:
            fee_management()
        elif choice == 4:
            attendance_management()
        elif choice == 5:
            school_management()
        elif choice == 6:
            print("Exiting...")
        else:
            print("Invalid choice.")
            main_menu()
    except ValueError:
        print("Invalid input. Please enter a number.")
        main_menu()


main_menu()
