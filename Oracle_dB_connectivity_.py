# Connectivity with Oracle database:

# Importing the Oracle package for connectivity.
import cx_Oracle
# Create a table in Oracle database
con = cx_Oracle.connect('hr/hr@localhost:1521/xe')
print(con.version)

# Now execute the sql query
cursor = con.cursor()  # Object which carries data --> for passing and receiving sql queries
print("Cursor Object created successfully")

# Sql queries to be passed in execute method

# cursor.execute("create table Test_1(Serial_No integer, Name varchar2(30), Latest_Qualification varchar2(100), "
#               "Courses_Certifications varchar2(100))")
# con.commit()
# print("Table Created successfully")


# cursor.execute("insert into Test_1 values('1','Pranay Bhatkar','PG-DBDA','Python,SQL,PowerBi')")
# con.commit()
# print("Updated successfully")

cursor.execute("select * from Test_1")
print(cursor)

test_list = []

for data in cursor:
    print(data)
    test_list.append(data)

print(test_list)
# con.commit() # used for pushing the data into the database.
# execute --> common method
















































































































