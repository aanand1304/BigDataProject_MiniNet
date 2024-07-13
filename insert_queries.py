insert_subscription='''
INSERT INTO Subscription (PlanName, Price, Duration) VALUES
('HD', 9.99, 1),
('UHD', 14.99, 1);
'''


insert_users = '''
INSERT INTO Users (Username, Email, Password, City, Country, Age, SubscriptionType) VALUES
('john_doe', 'john@example.com', 'password1', 'New York', 'USA', 28, 'HD'),
('Ashit Anand', 'ashit@example.com', 'password5123', 'Patna', 'India', 28, 'HD'),
('Khalid', 'khaild@example.com', 'password01', 'SAGA', 'UK', 25, 'HD'),
('alice_smith', 'alice@example.com', 'password2', 'Los Angeles', 'USA', 34, 'HD'),
('jane_doe', 'jane@example.com', 'password3', 'Chicago', 'USA', 21, 'UHD'),
('bob_jones', 'bob@example.com', 'password4', 'Boston', 'USA', 30, 'UHD'),
('emma_johnson', 'emma@example.com', 'password5', 'San Francisco', 'USA', 25, 'HD');
'''
insert_movies = '''
INSERT INTO Movies (Title, Genre, ReleaseDate) VALUES
('Stranger Things', 'Sci-Fi', '2016-07-15'),
('Breaking Bad', 'Drama', '2008-01-20'),
('The Office', 'Comedy', '2005-03-24'),
('Parks and Recreation', 'Comedy', '2009-04-09'),
('The Godfather', 'Crime', '1972-03-24');
'''

insert_actors = '''
INSERT INTO Actors (Name, City, DateOfBirth) VALUES
('Millie Bobby Brown', 'Los Angeles', '2004-02-19'),
('Tom Holland', 'Los Angeles', '2001-01-19')
('Bryan Cranston', 'Hollywood', '1956-03-07'),
('Winona Ryder', 'New York', '1971-10-29'),
('Aaron Paul', 'Boise', '1979-08-27'),
('David Harbour', 'White Plains', '1975-04-10');
'''

insert_reviews = '''
INSERT INTO Reviews (Username, MovieTitle, Score, Comment) VALUES
('john_doe', 'Stranger Things', 5, 'Amazing show!'),
('alice_smith', 'Breaking Bad', 3, 'Good show'),
('jane_doe', 'The Office', 4, 'Funny and smart'),
('bob_jones', 'Parks and Recreation', 2, 'Not my taste'),
('emma_johnson', 'The Godfather', 5, 'A classic!');
'''

insert_favoriteMovies = '''
INSERT INTO FavoriteMovies (Username, MovieTitle, Score) VALUES
('john_doe', 'The Office', 5),
('john_doe', 'Parks and Recreation', 4),
('alice_smith', 'The Godfather', 3),
('jane_doe', 'Stranger Things', 5),
('bob_jones', 'Breaking Bad', 4);
'''


insert_movieActors = '''
 INSERT INTO MovieActors (MovieTitle, ActorName, Role) VALUES
('Stranger Things', 'Millie Bobby Brown', 'Eleven'),
('Breaking Bad', 'Bryan Cranston', 'Walter White'),
('Stranger Things', 'Winona Ryder', 'Joyce Byers'),
('Breaking Bad', 'Aaron Paul', 'Jesse Pinkman'),
('Stranger Things', 'David Harbour', 'Jim Hopper');
'''

insert_watchHistory = '''
INSERT INTO WatchHistory (Username, MovieTitle, WatchDate) VALUES
('john_doe','Stranger Things','2023-06-10'),
('alice_smith','Breaking Bad', '2023-06-11'),
('jane_doe','The Office','2023-06-12'),
('bob_jones','Parks and Recreation','2023-06-13'),
('emma_johnson','The Godfather', '2023-06-14');
'''

