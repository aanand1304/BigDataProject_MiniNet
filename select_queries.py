"""4.1 Export all data about users in the HD subscriptions."""

hd_subscriptions='''
SELECT Username,Email,Password,SubscriptionType,City,Country, Age
FROM Users
JOIN Subscription ON Users.SubscriptionType = Subscription.PlanName
WHERE SubscriptionType ='HD';
'''

"""4.2 Export all data about actors and their associated movies."""
actor_movies='''
SELECT a.Name,a.City,a.DateOfBirth,m.Title,m.Genre,m.ReleaseDate
FROM Actors a
JOIN MovieActors ma ON a.Name= ma.ActorName
JOIN Movies m ON ma.MovieTitle=m.Title;
'''

"""4.3 Export all data to group actors from a specific city, showing also the average age (per city)."""
actors_city='''
SELECT City,COUNT(Name) AS NumberOfActors, 
    AVG(FLOOR(DATEDIFF(CURDATE(), DateOfBirth) / 365.25)) AS AverageAge
FROM Actors
GROUP BY City;

'''

#4.4 Export all data to show the favourite comedy movies for a specific user.
fav_comedy_movie='''
SELECT fm.Username,fm.MovieTitle,m.Genre,m.ReleaseDate
FROM FavoriteMovies fm
JOIN Movies m ON fm.MovieTitle= m.Title
WHERE fm.Username = %s AND m.Genre = 'Comedy';
'''


# 4.5 Export all data to count how many subscriptions are in the database per country.

sub_byCountry='''
SELECT Country,COUNT(Username) as SubscriptionCount
FROM Users
GROUP BY Country;
'''

#4.6 Export all  data to find the movies that start with the keyword The .

movie_nameThe='''
SELECT Title,Genre,ReleaseDate
FROM Movies
WHERE Title LIKE 'The%';
'''

#4.7 Export data to find the number of subscriptions per movie category.
subs_movieCat='''
SELECT m.Genre as Category,COUNT(u.Username) as SubscriptionCount
FROM Movies m
JOIN Reviews r ON m.Title = r.MovieTitle
JOIN Users u ON r.Username =u.Username
GROUP BY m.Genre;
'''

#4.8 Export data to find the username and the city of the youngest customer in the UHD subscription  category.
young_User='''
SELECT Username,Email,Password,SubscriptionType,City,Country,Age
FROM Users
WHERE SubscriptionType= 'UHD'
ORDER BY Age ASC
LIMIT 1;

'''

#4.9 Export data to find users between 22 - 30 years old (including 22 and 30 ).
user_22_30='''
SELECT Username,Email,City,Country,Age,SubscriptionType
FROM Users
WHERE Age BETWEEN 22 AND 30;
'''


#4.10 Export data to find the average age of users with low score reviews (less than 3). Group your data for users under 20, 21-40, and 41 and over.

averageAge_lowreview='''
SELECT 
    CASE
        WHEN Age < 20 THEN 'Under 20'
        WHEN Age BETWEEN 21 AND 40 THEN '21-40'
        ELSE '41 and over'
    END as AgeGroup,
    AVG(Age) as AverageAge
FROM  Users u
JOIN Reviews r ON u.Username= r.Username
WHERE r.Score < 3
GROUP BY AgeGroup;
'''