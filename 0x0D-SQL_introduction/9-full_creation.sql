-- Create second_table table in hbtn_0c_0 db.
CREATE TABLE IF NOT EXIST second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table VALUES 
    ('1', 'John', '10'),
    ('2', 'Alex', '3'),
    ('3', 'Bob', '14'),
    ('4', 'George', '8');
