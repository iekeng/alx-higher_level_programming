-- Create hbtn_0d_2 db and user_0d_2 user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2
IDENTIFY BY 'user_0d_2_pwd';
-- Grant SELECT privilege to user_0d_2 on hbtn_0d_2 db
GRANT SELECT ON hbtn_0d_2.*
TO user_0d_2@localhost;
