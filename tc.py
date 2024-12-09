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

def Insert_TC():
  """Inserts a new TC record into the TC table and updates the corresponding Admn record."""
  print("- - - - -Enter student details- - - - --")
  try:
    conn, cursor = connect_to_db()
    if not conn:
      return

    Tcno = int(input("TC Number:"))
    TcD = input("TC Date:")
    AN = int(input("Admission Number:"))
    Reason = input("Reason:")
    Remark = input("Remark:")

    # Fetch student name from Admn table
    q = "SELECT Name FROM Admin WHERE Admn_no = %s"
    cursor.execute(q, (AN,))
    data = cursor.fetchone()
    Name = data[0] if data else None

    if Name:
      q = "INSERT INTO TC VALUES (%s, %s, %s,  %s, %s, %s)"
      values = (Tcno, TcD, AN, Name, Reason, Remark)
      cursor.execute(q, values)

      q = "UPDATE Admin SET TC_no = %s, TC_date = %s WHERE Admn_no = %s"
      values = (Tcno, TcD, AN)
      cursor.execute(q, values)

      conn.commit()
      print("Record Inserted successfully")
    else:
      print("Student not found in Admn table.")
  except mysql.connector.Error as err:
    print(f"Error inserting TC record: {err}")
  finally:
    close_connection(conn)

def Update_TC():
  """Updates an existing TC record in the TC table and the corresponding Admn record."""
  print("Enter the following details of the TC:")
  try:
    conn, cursor = connect_to_db()
    if not conn:
      return

    Tcno = int(input("TC Number:"))
    TcD = input("TC Date:")
    AN = int(input("Admission Number:"))
    Reason = input("Reason:")
    Remark = input("Remark:")

    # Fetch student name from Admn table
    q = "SELECT Name FROM Admin WHERE Admn_no = %s"
    cursor.execute(q, (AN,))
    data = cursor.fetchone()
    Name = data[0] if data else None

    if Name:
      q = "UPDATE TC SET TC_date = %s, Admn_no = %s, Name = %s, Reason = %s, Remark = %s WHERE TC_no = %s"
      values = (TcD, AN, Name, Reason, Remark, Tcno)
      cursor.execute(q, values)

      q = "UPDATE Admin SET TC_no = %s, TC_date = %s WHERE Admn_no = %s"
      values = (Tcno, TcD, AN)
      cursor.execute(q, values)

      conn.commit()
      print("Record successfully updated.")
    else:
      print("Student not found in Admn table.")
  except mysql.connector.Error as err:
    print(f"Error updating TC record: {err}")
  finally:
    close_connection(conn)

def Delete_TC():
  """Deletes a TC record from the TC table and updates the corresponding Admn record."""
  print("Enter the TC Number:")
  try:
    conn, cursor = connect_to_db()
    if not conn:
      return

    Tcno = int(input("TC Number:"))

    q = "DELETE FROM TC WHERE TC_no = %s"
    cursor.execute(q, (Tcno,))

    q = "UPDATE Admin SET TC_no = NULL, TC_date = NULL WHERE Admn_no = (SELECT Admn_no FROM TC WHERE TC_no = %s)"
    cursor.execute(q, (Tcno,))

    conn.commit()
    print("Record successfully deleted.")
  except mysql.connector.Error as err:
    print(f"Error deleting TC record: {err}")
  finally:
    close_connection(conn)

def Search_TC():
  """Searches for a specific TC record in the TC table."""
  print("Enter the TC Number:")
  try:
    conn, cursor = connect_to_db()
    if not conn:
      return

    Tcno = int(input("TC Number:"))

    q = "SELECT * FROM TC WHERE TC_no = %s"
    cursor.execute(q, (Tcno,))
    data = cursor.fetchone()

    if data:
      print("------------------------------------")
      print("TC number:", data[0])
      print("TC Date:", data[1])
      print("Admission Number:", data[2])
      print("Name:", data[3])
      print("Reason:", data[4])
      print("Remark:", data[5])
      print("------------------------------------")
    else:
      print("Record not found.")
  except mysql.connector.Error as err:
    print(f"Error searching TC record: {err}")
  finally:
    close_connection(conn)

def SearchAll_TC():
  """Retrieves and displays all TC records from the TC table."""
  try:
    conn, cursor = connect_to_db()
    if not conn:
      return

    q = "SELECT * FROM TC"
    cursor.execute(q)
    data = cursor.fetchall()

    heading = ("TC NO.", "TC_Date", "ADMISSION NO.", "Name", "Reason", "Remark")
    print(heading)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    for row in data:
      print(row)
  except mysql.connector.Error as err:
    print(f"Error retrieving TC records: {err}")
  finally:
    close_connection(conn)

def Menu_TC():
  while True:
    print("----------------TC Register----------------")
    print("\t\t1. Insert TC Details.")
    print("\t\t2. Update TC Details.")
    print("\t\t3. Delete TC Details.")
    print("\t\t4. Search Individual TC Details.")
    print("\t\t5. Search All TC Details.")
    print("\t\t6. Exit")

    choice = int(input("Enter your choice :"))
    if choice==1:
      Insert_TC()
    elif choice==2:
      Update_TC()
    elif choice==3:
      Delete_TC()
    elif choice==4:
      Search_TC()
    elif choice==5:
      SearchAll_TC()
    elif choice==6:
      print("Thanks for using")
      input("Going back to STAR. Press enter to exit.")
      break
    else:
      input("Wrong Entry. Press enter to continue and re-enter:")