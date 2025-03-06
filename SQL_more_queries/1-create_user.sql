-- user_0d_1 password should be set to user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'uSer_0d_1_pwd';

-- privilege
GRANT ALL PRIVILEGES
ON *.* TO 'user_0d_1'@'localhost'
WITH GRANT OPTION;
