import mysql.connector

connector = mysql.connector.connect(host='bncm4psrmotblosp6jbg-mysql.services.clever-cloud.com:3306', database='bncm4psrmotblosp6jbg', user='up2ocb1hrji2ux0d', password='KEuBHlyXcanciLh2Dtgz')
print(connector)

cursor = connector.cursor()
print("Done")


# Create a database separately.
# cursor.execute("create database Test_2")
# print("Database created successfully")

# Table Creation cursor.execute("create table TEST_SQL(Serial_No integer(10), Name varchar(30), Latest_Qualifications
# varchar(30), Courses_Certifications varchar(30))")
# connector.commit()
# print("Committed Successfully")

# cursor.execute("create table new_employee(empID integer(10), name varchar(30), salary integer(30))")
# print("Table created successfully")
# connector.commit()
# print("Committed successfully")


# Value Insertion
# cursor.execute("insert into TEST_SQL values('1','Pranay Bhatkar','PG-DBDA','Python,SQL,PowerBi')")
# connector.commit()
# print("Committed Successfully")


# cursor.execute("select * from TEST_SQL")
# print(cursor)

# test_list = []

# for data in cursor:
#    print(data)
#    test_list.append(data)

# print(test_list)

def Test_Function():
    cursor.execute("select * from TEST_SQL")
    print(cursor)

    test_list = []

    for data in cursor:
        print(data)
        test_list.append(list(data))

    print(test_list)


Test_Function()
