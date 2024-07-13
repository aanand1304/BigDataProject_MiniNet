import mysql.connector
from mysql.connector import Error
from select_queries import *


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

host = "34.28.114.133"  # Add here your host IP address from the GCP
user = "root"
password = "Welcome@12345#"  # Add here your password
database = "Mininet_DB"

connection = create_db_connection(host, user, password, database)

def fetch_results(connection, query, params=None):
    """Fetches results and prints them in a basic format."""
    cursor = connection.cursor(dictionary=True) 
    try:
        if params is not None:
            cursor.execute(query, params)
        else:
            cursor.execute(query) 

        results = cursor.fetchall()
        for row in results:
            print(row)

    except Error as err:
        print(f"Error executing query: '{err}'")

    finally:
        cursor.close()

def query_hd_subscriptions():
    fetch_results(connection, hd_subscriptions)

def query_actor_movies():
    fetch_results(connection, actor_movies)

def query_actors_city():
    fetch_results(connection, actors_city)

def query_fav_comedy_movie(username):
    fetch_results(connection, fav_comedy_movie, (username,))

def query_sub_by_country():
    fetch_results(connection, sub_byCountry)

if __name__=="__main__":
    while True:
        print("\n  Select a query to run:")
        print("1. Export all data about users in the HD subscription ")
        print("2. Export all data about actors and their part movies.")
        print("3. Export all data to group actors from a particular city, average age per/city) .")
        print("4. Export all data to show the favourite comedy movies for a specific user. ")
        print("5. Export all data to count how many subscriptions are in the database per country . ")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            query_hd_subscriptions()
        elif choice == '2':
            query_actor_movies()
        elif choice == '3':
            query_actors_city()
        elif choice == '4':
            username = input("Enter the username: ")
            query_fav_comedy_movie(username)
        elif choice == '5':
            query_sub_by_country()
        elif choice == '6':
            connection.close()
            break
        else:
            print("Invalid choice. Please enter  number between 1 and 6.")
