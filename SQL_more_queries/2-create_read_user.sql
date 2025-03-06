-- user_0d_2 password should be set to user_0d_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- privilege
GRANT ALL PRIVILEGES
ON *.* TO 'user_0d_2'@'localhost'
WITH GRANT OPTION;

-- privilege
FLUSH PRIVILEGES;
