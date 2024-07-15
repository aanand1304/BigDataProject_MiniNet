show_table = '''
SHOW TABLES;
'''

create_sub_table = '''
CREATE TABLE Subscription (
    PlanName VARCHAR(10) PRIMARY KEY,
    Price DECIMAL(5, 2) NOT NULL,
    Duration INT NOT NULL
);
'''

create_user_table = '''
CREATE TABLE Users (
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

create_movie_table = '''
CREATE TABLE Movies (
    Title VARCHAR(100) PRIMARY KEY,
    Genre VARCHAR(50) NOT NULL,
    ReleaseDate DATE NOT NULL
);
'''

create_actor_table = '''
CREATE TABLE Actors (
    Name VARCHAR(50) PRIMARY KEY,
    City VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL
);
'''

create_review_table = '''
CREATE TABLE Reviews (
    Username VARCHAR(50),
    MovieTitle VARCHAR(100),
    Score INT NOT NULL,
    Comment TEXT,
    PRIMARY KEY (Username, MovieTitle),
    FOREIGN KEY (Username) REFERENCES Users(Username) ON DELETE CASCADE,
    FOREIGN KEY (MovieTitle) REFERENCES Movies(Title) ON DELETE CASCADE
);
'''

create_favmovie_table = '''
CREATE TABLE FavoriteMovies (
    Username VARCHAR(50),
    MovieTitle VARCHAR(100),
    Score INT NOT NULL,
    PRIMARY KEY (Username, MovieTitle),
    FOREIGN KEY (Username) REFERENCES Users(Username) ON DELETE CASCADE,
    FOREIGN KEY (MovieTitle) REFERENCES Movies(Title) ON DELETE CASCADE
);
'''

create_movieActor_table = '''
CREATE TABLE MovieActors (
    MovieTitle VARCHAR(100),
    ActorName VARCHAR(50),
    Role VARCHAR(50),
    PRIMARY KEY (MovieTitle, ActorName),
    FOREIGN KEY (MovieTitle) REFERENCES Movies(Title) ON DELETE CASCADE,
    FOREIGN KEY (ActorName) REFERENCES Actors(Name) ON DELETE CASCADE
);
'''
create_watchHistory_table = '''
CREATE TABLE WatchHistory (
    Username VARCHAR(50),
    MovieTitle VARCHAR(100),
    WatchDate DATE NOT NULL,
    PRIMARY KEY (Username, MovieTitle),
    FOREIGN KEY (Username) REFERENCES Users(Username) ON DELETE CASCADE,
    FOREIGN KEY (MovieTitle) REFERENCES Movies(Title) ON DELETE CASCADE
);
'''

