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
                skip = False
                continue
            data = line.split(',')
            try:
                x.execute("""INSERT INTO problemanswered VALUES (
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s)""",
                      (data[12], data[13], data[14], data[15], data[16],
                       data[17], data[18], data[19], data[20], data[21],
                       data[22], data[23], data[24], data[25], data[26],
                       data[27], data[28], data[29], data[30], data[31],
               