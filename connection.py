import mysql.connector as msc
try:
    conn = msc.connect(host='localhost',user='root',passwd='1234')
    print("Connection Successful.")
except msc.Error as err:
    print("Some exception occur")
    print(f"Error :{err}")
