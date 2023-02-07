import psycopg2.extras
import matplotlib 
import matplotlib.pyplot as plt
matplotlib.use('Agg')

connectionString = "dbname='ialaed20_db' user = 'ialaed20'"
print("Connecting to database\n ->" +  connectionString)
connection = psycopg2.connect(connectionString)
print("connected!\n")

dict_cursor=connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
dict_cursor.execute("SELECT * FROM Product")
product_dict = dict_cursor.fetchall()
for row in product_dict:
    print(row['maker'])
                    