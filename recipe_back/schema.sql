DROP TABLE IF EXISTS recipe;

CREATE TABLE recipe (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL,
    source TEXT,
    addedAt TEXT
);