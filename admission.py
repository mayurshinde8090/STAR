import mysql.connector
def connect_to_db():
  """Connects to the MySQL database and returns a connection object and cursor."""
  try:
    conn = mysql.connector.connect(
      host='localhost',
      user='root',
      password='1234',
      database='STAR'
    )
    cursor = conn.cursor()
    return conn, cursor
  except mysql.connector.Error as err:
    print(f"Error connecting to database: {err}")
    return None, None

def close_connection(conn):
  """Closes the database connection if it exists."""
  if conn:
    conn.close()

def Insert_Admn():
  try:
    conn, cursor = connect_to_db()
    if not conn:
      return
    
    print(" Enter the following details of student")
    AN=int(input("Admission number="))
    DOA=input("Date of admission=")
    N=input("Name=")
    FA=input("Father's name=")
    MA=input("Mother's name=")
    DOB=input("Date of birth=")
    AC=input("Admission category=")
    C=input("Class=")
    Cst=input("Cast=")
    q = "INSERT INTO Admin (Admn_no, Date_of_Admission, Name, Father_name, Mothers_name, DOB, Admin_category, Class, Cast, TC_no, TC_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (AN, DOA, N, FA, MA, DOB, AC, C, Cst, None, None)
    cursor.execute(q, values)
    conn.commit()
    print("Record successfully saved")
  except mysql.connector.Error as err:
    print(f"Error inserting record: {err}")
  finally:
    close_connection(conn)

def Update_Admn():
  """Updates an existing student record in the Admin table."""
  print("Enter the following details of the student:")
  try:
    conn, cursor = connect_to_db()
    if not conn:
      return

    AN = int(input("Admission number="))
    DOA = input("Date of admission=")
    N = input("Name=")
    FA = input("Father's name=")
    MA = input("Mother's name=")
    DOB = input("Date of birth=")
    AC = input("Admission category=")
    C = input("Class=")
    Cst = input("Cast=")

    q = "UPDATE Admin SET Date_of_Admission = %s, Name = %s, Father_name = %s, Mothers_name = %s, DOB = %s, Admin_category = %s, Class = %s, Cast = %s WHERE Admn_no = %s"
    values = (DOA, N, FA, MA, DOB, AC, C, Cst, AN)
    cursor.execute(q, values)
    conn.commit()
    print("Record successfully updated.")
  except mysql.connector.Error as err:
    print(f"Error updating record: {err}")
  finally:
    close_connection(conn)

def Delete_Admn():
  """Deletes a student record from the Admn table."""
  print("Enter the following details of the student:")
  try:
    conn, cursor = connect_to_db()
    if not conn:
      return

    AN = int(input("Admission number="))

    q = "DELETE FROM Admin WHERE Admn_no = %s"
    cursor.execute(q, (AN,))
    conn.commit()
    print("Record successfully deleted.")
  except mysql.connector.Error as err:
    print(f"Error deleting record: {err}")
  finally:
    close_connection(conn)

def Select_Admn():
  """Searches for a specific student record in the Admn table."""
  print("Enter the following details of the student:")
  try:
    conn, cursor = connect_to_db()
    if not conn:
      return

    AN = int(input("Admission number="))

    q = "SELECT * FROM Admin WHERE Admn_no = %s"
    cursor.execute(q, (AN,))
    data = cursor.fetchone()

    if data:
      print("Admission no=", data[0])
      print("Date of admission=", data[1])
      print("Name=", data[2])
      print("Father's name=", data[3])
      print("Mother's name=", data[4])
      print("DOB=", data[5])
      print("Admiossion category=", data[6])
      print("Class=", data[7])
      print("Caste=", data[8])
      print("TC no.=", data[9])
      print("TC date=", data[10])
    else:
      print("Record not found.")
  except mysql.connector.Error as err:
    print(f"Error searching record: {err}")
  finally:
    close_connection(conn)

def SelectAll_Admn():
  """Retrieves and displays all student records from the Admn table."""
  try:
    conn, cursor = connect_to_db()
    if not conn:
      return

    q = "SELECT * FROM Admin"
    cursor.execute(q)
    data = cursor.fetchall()

    heading = ("ADMN NO", "Date of Admn", "Name", "Father's Name", "Mother's Name", "DOB", "Admn Cat", "Class", "Caste", "TC No", "TC Date")
    print(heading)
    print("----------------------------------------------------------------------------------------------------------------------------------")
    for row in data:
      print(row)
  except mysql.connector.Error as err:
    print(f"Error retrieving records: {err}")
  finally:
    close_connection(conn)

def MenuAdmn():
  while True:
    print("--------------------Admission Register--------------------")
    print("\t\t1. Insert Student Details.")
    print("\t\t2. Update Student Details.")
    print("\t\t3. Delete Student Details.")
    print("\t\t4. Search Student Details.")
    print("\t\t5. Search ALL Student Details.")
    print("\t\t6.Exit")

    choice = int(input("Enter Your Choice(1-6) = "))
    if choice == 1:
      Insert_Admn()
    elif choice == 2:
      Update_Admn()
    elif choice == 3:
      Delete_Admn()
    elif choice == 4:
      Select_Admn()
    elif choice == 5:
      SelectAll_Admn()
    elif choice == 6:
      print("Thanks For Using")
      input("Going back to STAR. press enter")
      break
    else:
      input("Wrong Entery. Press any key to continue and Re-enter.")








