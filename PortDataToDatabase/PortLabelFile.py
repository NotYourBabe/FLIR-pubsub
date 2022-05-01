import MySQLdb
conn = MySQLdb.connect(host="localhost",
                       user="root",
                       passwd="1234",
                       db="testdb")
x = conn.cursor()

file = open("F:/DataMining/anonymized_dataset_for_ADM2