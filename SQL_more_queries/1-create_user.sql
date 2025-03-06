-- user_0d_1 password should be set to user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- privilege
GRANT SELECT
ON *.* TO 'user_0d_1'@'localhost'
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost'

-- privilege
FLUSH PRIVILEGES;
