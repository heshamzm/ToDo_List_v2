BEGIN TRANSACTION;
DROP TABLE IF EXISTS "tasklists";
CREATE TABLE IF NOT EXISTS "tasklists" (
	"id"	INTEGER,
    "author_id"	INTEGER NOT NULL,
    "last_updated"	TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"created_at"	TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"tasks"	INTEGER NOT NULL,
    FOREIGN KEY("author_id") REFERENCES "tasks"("id"),
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
	PRIMARY KEY("id" AUTOINCREMENT)
);