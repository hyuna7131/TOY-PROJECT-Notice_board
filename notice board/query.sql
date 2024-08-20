# db docker container에 접속해서 쿼리문 실행
# docker exec -it noticeboard-db-1 bash
# mysql -u root -p 

# table  생성
CREATE DATABASE IF NOT EXISTS board;

USE board;

CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


# id 재정렬
USE board;
SET @count = 0;
UPDATE posts SET id = @count:=(@count + 1) ORDER BY id;
ALTER TABLE posts AUTO_INCREMENT = 1;
