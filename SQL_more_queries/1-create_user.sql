-- le mot de passe de user_0d_1 doit être défini sur user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT SELECT ON *.* TO 'user_0d_1'@'localhost';
