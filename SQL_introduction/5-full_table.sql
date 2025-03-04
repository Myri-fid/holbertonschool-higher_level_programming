-- prints description of the table first_table
SELECT TABLE_NAME, CREATE_TABLE
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
