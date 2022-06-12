import MySQLdb
conn = MySQLdb.connect(host="localhost",
                       user="root",
                       passwd="1234",
                       db="testdb")
x = conn.cursor()

for i in range(1, 11):

        file = open("F:/DataMining/anonymized_dataset_for_ADM2017/student_log_{}.csv".format(i), "r")
        skip = True
        for line in file:
            if (skip):
                s