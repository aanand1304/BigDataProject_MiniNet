show_table ='''
SHOW TABLES
'''

create_sub_table='''
CREATE TABLE Subscription (
    PlanName VARCHAR(10) PRIMARY KEY,
    Price DECIMAL(5, 2) NOT NULL,
    Duration INT NOT NULL
);
'''

#Username, Email, Password, SubscriptionType, City, Country, Age
create_user_table='''
CREATE TABLE User (
    Username VARCHAR(50) PRIMARY KEY,
    Email VARCHAR(100) NOT NULL,
    Password VARCHAR(50) NOT NULL,
    SubscriptionType VARCHAR(10),
    City VARCHAR(50) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    Age INT NOT NULL,
    FOREIGN KEY (SubscriptionType) REFERENCES Subscription(PlanName) ON DELETE RESTRICT
);

'''
create_movie_table='''
CREATE TABLE Movie (
    MovieID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Genre VARCHAR(50) NOT NULL,
    ReleaseDate DATE NOT NULL
);
'''
create_actor_table='''
CREATE TABLE Actor (
    ActorID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    City VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL
);
'''
create_review_table='''
CREATE TABLE Review (
    Username VARCHAR(50) NOT NULL,
    MovieTitle VARCHAR(100) NOT NULL,
    Score INT NOT NULL,
    Comment TEXT,
    PRIMARY KEY (Username, MovieTitle),
    FOREIGN KEY (Username) REFERENCES User(Username),
    FOREIGN KEY (MovieTitle) REFERENCES Movie(Title) ON DELETE CASCADE
);
'''

create_favmovie_table ='''
CREATE TABLE FavoriteMovie (
    FavoriteID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    MovieID INT,
    Score INT NOT NULL,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (MovieID) REFERENCES Movie(MovieID)
    ON DELETE CASCADE
);
'''

create_movieActor_table='''
CREATE TABLE MovieActor (
    MovieID INT,
    ActorID INT,
    Role VARCHAR(50),
    PRIMARY KEY (MovieID, ActorID),
    FOREIGN KEY (MovieID) REFERENCES Movie(MovieID),
    FOREIGN KEY (ActorID) REFERENCES Actor(ActorID)
);
'''

delete_table='''

'''