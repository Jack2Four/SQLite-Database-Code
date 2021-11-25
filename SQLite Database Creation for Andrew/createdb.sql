CREATE TABLE "User_Table" (
	"UserID"	INTEGER NOT NULL,
	"Username"	TEXT,
	"Password"	TEXT,
	"Forename"	TEXT,
	"Surname"	TEXT,
	"Email"	TEXT,
	"DateOfBirth"	TEXT,
	PRIMARY KEY("UserID" AUTOINCREMENT)
);

CREATE TABLE "User_Notes" (
	"NoteID"	INTEGER NOT NULL,
	"NoteNameTXT"	TEXT,
	"NoteMessage"	TEXT,
	"UserID"	INTEGER,
	FOREIGN KEY("UserID") REFERENCES "User_Table"("UserID"),
	PRIMARY KEY("NoteID" AUTOINCREMENT)
);

