import psycopg2
import matplotlib 
import matplotlib.pyplot as plt
matplotlib.use('Agg')

connectionString = "dbname='ialaed20_db' user = 'ialaed20'"
print("Connecting to database\n ->" +  connectionString)
connection = psycopg2.connect(connectionString)
print("connected!\n")
cursor = connection.cursor()
sqlStatement = 'SELECT Rating,Count(rating) FROM Netflix_Dataset_Rating Natural JOIN Netflix_Dataset_Movie GROUP BY (Rating) ORDER BY Rating;'
cursor.execute(sqlStatement)
records = cursor.fetchall()
for row in records:
    print(row)
next_record = cursor.fetchone()

Rating = []
Name =[]

for row in records:
    Name.append(row[0])
    Rating.append(row[1])
    
plt.bar(Name, Rating, width = 0.4)
matplotlib.pyplot.xticks(fontsize=8)
plt.title('Top 5 Worst Rated Movies')
plt.xlabel('Movie') 
plt.ylabel('Average Rating') 
plt.savefig("Sample_Graph5.png")



#SELECT SELECT User_ID,MAX(rating) FROM Netflix_Dataset_Rating GROUP BY (User_ID);
#SELECT Movie_ID,AVG(rating) FROM Netflix_Dataset_Rating GROUP BY (Movie_ID);
#SELECT * FROM Netflix_Dataset_Movie NATURAL JOIN Netflix_Dataset_Rating;
