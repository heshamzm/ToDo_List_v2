BEGIN TRANSACTION;
DROP TABLE IF EXISTS "taskslist";
CREATE TABLE IF NOT EXISTS "taskslist" (
	"id"	INTEGER ,
	"name"	TEXT NOT NULL ,
    "last_updated"	TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"created_at"	TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS "tasks";
CREATE TABLE IF NOT EXISTS "tasks" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL UNIQUE,
	"last_updated"	TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"created_at"	TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"status"	TEXT,
	"priority"	TEXT,
    "description" TEXT,
	"taskslist_id"	INTEGER NOT NULL,
	FOREIGN KEY("taskslist_id") REFERENCES "taskslist"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);


DROP TABLE IF EXISTS "users";
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER,
	"username"	TEXT NOT NULL UNIQUE,
	"password" TEXT NOT NULL,
	"firstname" TEXT NOT NULL,
	"lastname" TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

INSERT INTO "taskslist" VALUES (1,"Python List","2012-04-23 18:25:43.511000","2012-04-23 18:25:43.511000");
INSERT INTO "taskslist" VALUES (2,"Home List","2012-04-23 18:25:43.511000","2012-04-23 18:25:43.511000");

INSERT INTO "tasks" VALUES (1,"Learn Flask Blueprints","2012-04-23 18:25:43.511000","2012-04-23 18:25:43.511000","Done","Medium","Remember to check the documentation.",1);
INSERT INTO "tasks" VALUES (2,"Learn Python Enums","2012-04-23 18:25:43.511000","2012-04-23 18:25:43.511000","In progress","High","Use the link sent by teacher.",1);
INSERT INTO "tasks" VALUES (3,"Revise OOP Concepts","2012-04-23 18:25:43.511000","2012-04-23 18:25:43.511000","Done","Low","By solving more exercise.",1);
INSERT INTO "tasks" VALUES (4,"Clean Keyboard","2012-04-23 18:25:43.511000","2012-04-23 18:25:43.511000","New","High","Buy the cleaning solution first.",2);
INSERT INTO "tasks" VALUES (5,"Water Plants","2012-04-23 18:25:43.511000","2012-04-23 18:25:43.511000","Done","Medium","Half a cup for the little one only.",2);

INSERT INTO "users" VALUES (1,"reema_95","1234","Reema", "Eilouti");
INSERT INTO "users" VALUES (2,"hesham_94","1234","Hesham", "Marei");
INSERT INTO "users" VALUES (3,"hamza_96","1234","Hamza", "Rdaideh");

COMMIT;