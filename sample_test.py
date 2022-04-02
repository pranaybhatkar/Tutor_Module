import pandas as pd
from sqlalchemy import create_engine
import mysql.connector

# connector = mysql.connector.connect(host='localhost', database='Test_2', user='root', password='root')
# print(connector) # Acknowledgement
# cursor = connector.cursor()
# print("Done!") # Acknowledgement


def importing_data_into_db():
    df = pd.read_excel('Fynd_Batch3.xlsx')
    engine = create_engine("mysql://up2ocb1hrji2ux0d:KEuBHlyXcanciLh2Dtgz@bncm4psrmotblosp6jbg-mysql.services.clever-cloud.com:3306/bncm4psrmotblosp6jbg")
    df.to_sql('test_3', con=engine, if_exists='append', index=False)
    print("Executed!")

# importing_data_into_db() # to be run only once
