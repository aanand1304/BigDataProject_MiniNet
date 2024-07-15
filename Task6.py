from cassandra.cluster import Cluster

#Connect to  Cassandra cluster
cluster=Cluster(['172.17.0.2', '172.17.0.3', '172.17.0.4'],port=9042)

# Connect to MiniNet keyspace
session=cluster.connect('mininet')

# 6.2 Export all users
export_all_users="SELECT * FROM users;"

# 6.3 Export all users from a specific country
export_users_by_country='SELECT * FROM users WHERE country = %s ALLOW FILTERING;'

# 6.4 Export data to find users between 22-30 years old (including 22 and 30)
export_users_by_age_range="SELECT * FROM users WHERE age >= %s AND age <= %s ALLOW FILT>"

# 6.5 Count how many users exist per specific city
count_users_per_city="SELECT city, COUNT(*) AS user_count FROM users GROUP BY city;"

# Function to fetch and print results
def fetch_and_print_results(query,param=None):
    if param:
        rows = session.execute(query, param)
    else:
        rows = session.execute(query)
    for row in rows:
        print(row)


# Export all users
print("Export all users:")
fetch_and_print_results(export_all_users)

# Export all users from a specific country.

country = input("\n Enter the country to export users from: ")
print(f"\nExport users from {country}: ")
fetch_and_print_results(export_users_by_country, (country,))

# Export data to find users between 22-30 year old
print(" \nExport users aged 22 to 30 :")
fetch_and_print_results(export_users_by_age_range, (22, 30))


print()
print("Count users per city:")
fetch_and_print_results(count_users_per_city)


session.shutdown()