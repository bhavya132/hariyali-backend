import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import pyodbc
import psycopg2
from sqlalchemy import create_engine
from urllib import parse

connecting_string = 'Driver={ODBC Driver 17 for SQL Server};Server=tcp:hariyalidb.database.windows.net,1433;Database=users;Uid=bhavyta;Pwd=@hello1234;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
params = parse.quote_plus(connecting_string)
# conn = psycopg2.connect("dbname='tmfjryay' user='tmfjryay' host='john.db.elephantsql.com' password='veuXB04ZYzkqrLYgs5xGR417M_tt_Umu'")
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
# engine = create_engine("mariadb+mariadbconnector://DB00006300:y=uNldI3Xt09rtEaMmZIaLO@hariyali-db00006300.mdb0002418.db1.skysql.net:5001/hariyali")
connection = engine.connect()
result = connection.execute("select 1+1 as res")
print('connection is ok')
# print(engine.table_names())



# SQLALCHEMY_DATABASE_URL = os.environ['COCKROACH_DB_CONN_STR']

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
