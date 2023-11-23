-- Part 1: Create a table
CREATE TABLE films(
    name TEXT,
    year INTEGER
);


-- -- Part 2: Insert data into the table
INSERT INTO films (name, year)
VALUES ('The Matrix', 1999);

INSERT INTO films (name, year)
VALUES ('Napolean', 2023);

INSERT INTO films (name, year)
VALUES ('The Marvels', 2023);

INSERT INTO films (name, year)
VALUES ('The Avengers', 2012);


-- Part 3: Query the table
SELECT * FROM films;


-- Part 4: Adding Supplementary Information
ALTER TABLE films ADD COLUMN runtime INTEGER;
ALTER TABLE films ADD COLUMN category TEXT;
ALTER TABLE films ADD COLUMN rating REAL;
ALTER TABLE films ADD COLUMN box_office BIGINT;

SELECT * FROM films;


-- Part 5: Backfilling Data
UPDATE films
SET runtime = 150,
    category = 'sci-fi',
    rating = 8.7,
    box_office = 465300000   
WHERE name = 'The Matrix';

UPDATE films
SET runtime = 158,
    category = 'historical',
    rating = 6,
    box_office = 3000000
WHERE name = 'Napolean';

UPDATE films
SET runtime = 105,
    category = 'superhero',
    rating = 5,
    box_office = 162600000
WHERE name = 'The Marvels';

UPDATE films
SET runtime = 143,
    category = 'superhero',
    rating = 9,
    box_office = 1519000000   
WHERE name = 'The Avengers';

SELECT * FROM films;


-- Part 6: Adding Constraints
ALTER TABLE films
ADD CONSTRAINT unique_name UNIQUE (name);

-- This fails
INSERT INTO films (name, year)
VALUES ('The Avengers', 2012);
SELECT * FROM films;