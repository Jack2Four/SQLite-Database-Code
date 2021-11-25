import sqlite3
import os
import os.path

# This function deletes a database.
# It's just a file so all it does it 
#  delete the file
def delete_db(database_file):
    if os.path.exists(database_file):
        os.remove(database_file)

# This function initialises a database.
# The first parameter is the file containing 
#  the database
# The second parameter is a file containing 
#  SQL DDL to create the tables
def init_db(database_file, database_sql):   
    # open the sqlite database file
    conn = sqlite3.connect(database_file)

    # connect to it and get a cursor
    # this is like a placeholder in the database
    cursor = conn.cursor()                  
    
    # open the script file containing SQL
    script = open(database_sql, 'r')

    # read the contents of the script 
    # into a string called sql
    sql = script.read()                     
    
    # execute the SQL 
    cursor.executescript(sql)               
    
    # commit the changes to make them permanent
    conn.commit()                           
    
    # close the connection to the database
    conn.close()          
    


def insert_data(database_file, sql):
    # open the sqlite database file
    conn = sqlite3.connect(database_file)
    # this is like a placeholder in the database
    script = open(sql, 'r')
    sql = script.read()
    cursor = conn.cursor()
    # execute the SQL 
    cursor.executescript(sql)
    conn.commit()    
    conn.close() 


delete_db("Booking.db")
init_db("Booking.db", "createdb.sql")
insert_data("Booking.db", "newsql.sql")