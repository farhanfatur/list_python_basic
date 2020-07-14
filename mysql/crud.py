import pymysql.cursors

db = pymysql.connect("localhost", "root", "", "nyobaksocket")
#############################
# select version
#############################
# cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print("Database version %s" %data)
# connection.close()
#############################
# end
#############################
# cursor = db.cursor()
# sql = """INSERT INTO pegawai(name)
#         VALUES('Farhan Fatur')"""

# sql = "INSERT INTO pegawai(name) \
#     VALUES('%s')" %\
#     ('John Wick')

# try:
#     cursor.execute(sql)
#     db.commit()
#     print("Insert is success")
# except:
#     db.rollback()
#     print("Insert is error")

#####################################
#  SELECT 
#####################################
cursor = db.cursor()
sql = "SELECT * FROM pegawai"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for each in results:
        id = each[0]
        name = each[1]
        print("id = %d, name = %s" %\
            (id, name))
except:
    print("Error: unable to fetch data")
    db.rollback()
#####################################
# end
#####################################

#####################################
#  UPDATE 
#####################################
# cursor = db.cursor()
# sql = "UPDATE pegawai SET name='Johnny Blaze' WHERE id='1'"
# try:
#     cursor.execute(sql)
#     db.commit()
#     print("Update pegawai is success")
# except:
#     print("Error: unable to fetch data")
#     db.rollback()
#####################################
#  end
#####################################

#####################################
#  DELETE 
#####################################
# cursor = db.cursor()
# sql = "DELETE FROM pegawai WHERE id='1'"
# try:
#     cursor.execute(sql)
#     db.commit()
#     print("Delete pegawai is success")
# except:
#     print("Error: unable to fetch data")
#     db.rollback()
#####################################
#  end
#####################################
db.close()