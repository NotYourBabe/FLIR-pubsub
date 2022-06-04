import MySQLdb
conn = MySQLdb.connect(host="localhost",
                       user="root",
                       passwd="1234",
                       db="testdb")
x = conn.cursor()

for i in range(1, 11):

        file = o