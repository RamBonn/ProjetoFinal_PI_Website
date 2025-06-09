CREATE DATABASE IF NOT EXISTS mysql_db;

CREATE USER IF NOT EXISTS 'flask_user'@'%' IDENTIFIED BY 'flask_password';

GRANT ALL PRIVILEGES ON mysql_db.* TO 'flask_user'@'%';

FLUSH PRIVILEGES;
