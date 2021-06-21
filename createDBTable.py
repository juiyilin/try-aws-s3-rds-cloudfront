import mysql.connector 
import sys
sys.path.append(r"C:\Users\arthu\Desktop\j2\engineer_project\juiyilin.github.io\homework\section2\flaskvenv\taipei-day-trip-website")
print(*sys.path,sep='\n')
def createDB(cursor,DBname):
    try:
        cursor.execute(f"create database {DBname}")
        
    except mysql.connector.errors.DatabaseError:
        print('already exist db',DBname)
    else:
        print(DBname+' created')   
