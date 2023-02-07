import psycopg2
import matplotlib 
import matplotlib.pyplot as plt
matplotlib.use('Agg')

connectionString = "dbname='ialaed20_db' user = 'ialaed20'"
print("Connecting to database\n ->" +  connectionString)
connection = psycopg2.connect(connectionString)
print("connected!\n")
cursor = connection.cursor()
sqlStatement = 'SELECT * FROM PC;'
cursor.execute(sqlStatement)
records = cursor.fetchall()
for row in records:
    print(row)
next_record = cursor.fetchone()

HD_sizes = []
RAM =[]
for row in records:
    HD_sizes.append(row[3])
    RAM.append(row[2])
plt.plot(HD_sizes, RAM,'ro')
plt.savefig("hd_ram_comparison.png")


