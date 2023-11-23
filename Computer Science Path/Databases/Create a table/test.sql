-- 0. Drop table to reset
-- DROP TABLE IF EXISTS test;

-- 1. Create Table
CREATE TABLE test(
  id INTEGER,
  name TEXT,
  birthday DATE
);

-- 2. Insert Values
INSERT INTO test (id, name, birthday) 
VALUES (1, 'Ororo Munroe', '1940-05-30');

INSERT INTO test (id, name, birthday) 
VALUES (2, 'Bob Smith', '1999-07-1');

INSERT INTO test (id, name, birthday) 
VALUES (3, 'Dave Jordan', '1700-01-12');

-- 3. View Table
SELECT * FROM test;

-- 4. Update table
UPDATE test
SET name = 'Storm'
WHERE id = 1;

-- 5. View Table
SELECT * FROM test;

-- 6. Add a new column
ALTER TABLE test
ADD COLUMN email TEXT;

-- 7. View Table
SELECT * FROM test;

-- 8. Add emails
UPDATE test
SET email = 'storm@codecademy.com'
WHERE id = 1;

UPDATE test
SET email = 'bob@codecademy.com'
WHERE id = 2;

UPDATE test
SET email = 'dave@codecademy.com'
WHERE id = 3;
