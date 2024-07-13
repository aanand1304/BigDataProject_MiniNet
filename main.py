import mysql.connector
from mysql.connector import Error
from create_queries import *
from insert_queries import *
from select_queries import *
""" ****************************************Database Connection **********************************************"""
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
host = "34.28.114.133" # Add here your host IP address from the GCP
user = "root"
password = "Welcome@12345#" # Add here your password
database = "Mininet_DB"

connection = create_db_connection(host, user, password,database)




cursor = connection.cursor()



"""************************************************Table Create queries work***************************************************"""

#create sub table 
#cursor.execute(create_sub_table)

#create user table 
#cursor.execute(create_user_table)

#Create movie table
#cursor.execute(create_movie_table)

#----create actor table
#cursor.execute(create_actor_table)

#----create review table
#cursor.execute(create_review_table)

#----create_favmovie_table table
#cursor.execute(create_favmovie_table)

##---- create_watch_history_table
#cursor.execute(create_watchHistory_table)


##---- Movie actor table
#cursor.execute(create_movieActor_table)

#cursor.execute("DROP TABLE User;")



"""****************************************Insert querie work********************************************"""


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")



#insert subscription 
#execute_query(connection,insert_subscription)


#insert Users 
#execute_query(connection,insert_users)

#insert Movies 
#execute_query(connection,insert_movies)

#insert  Actors
#execute_query(connection,insert_actors)

#insert reviews 
#execute_query(connection,insert_reviews)

#insert favoriteMovies 
#execute_query(connection,insert_favoriteMovies)

#insert favoriteMovies 
#execute_query(connection,insert_movieActors)

#insert movieactors 
#execute_query(connection,insert_movieActors)

#insert watchhistory 
#execute_query(connection,insert_watchHistory)


'''*********************************************Show Table **************************************'''
'''
cursor.execute(show_table)
for (databases) in cursor:
     print(databases[0])

'''


"""**********************************Export Work(Select)**************************************"""

#4.1 Export all data about users in the HD subscriptions.
cursor.execute(hd_subscriptions)

results = cursor.fetchall()
print("Users in the HD subscriptions: ")
'''
for result in results:
  print(result)
'''
print()

#4.2 Export all data about actors and their associated movies."""
cursor.execute(actor_movies)

results = cursor.fetchall()
print("Actors and their associated movies: ")
for result in results:
  print(result)
print()
#4.3 Export all data to group actors from a specific city, showing also the average age (per city).
cursor.execute(actors_city)
results = cursor.fetchall()

print("Actors from a specific city & the average age /per city: ")
for result in results:
  print(result)

print()


#4.4 Export all data to show the favourite comedy movies for a specific user.

specific_user = input("Enter the username to fetch favorite comedy movie: ")

cursor.execute(fav_comedy_movie, (specific_user,))

results = cursor.fetchall()

print("Favourite comedy movies for ",specific_user)
for result in results:
  print(result)
print()


# 4.5 Export all data to count how many subscriptions are in the database per country.
cursor.execute(sub_byCountry)
results = cursor.fetchall()

print("Count subscriptions  per country: ")
for result in results:
  print(result)

print()

#4.6 Export all  data to find the movies that start with the keyword The .
cursor.execute(movie_nameThe)
results = cursor.fetchall()

print("Movies that start with the keyword 'The': ")
for result in results:
  print(result)

print()
#4.7 Export data to find the number of subscriptions per movie category.

