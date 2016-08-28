CREATE TABLE Categories (
   ID int NOT NULL,
   Name varchar(50) NOT NULL,
   PRIMARY KEY(ID)
);

CREATE TABLE CatVolMap (
	CatID int NOT NULL,
    VolID int NOT NULL,
    PRIMARY KEY(CatID, VolID)
);

CREATE TABLE Volunteers (
	ID int NOT NULL,
    Name varchar(100) NOT NULL,
    Email varchar(100) NOT NULL,
    PhoneNumber char(10) NOT NULL,
    PRIMARY KEY(ID)
);

