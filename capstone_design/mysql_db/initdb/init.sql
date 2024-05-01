-- 사용자와의 대화 내용을 저장할 table
CREATE DATABASE IF NOT EXISTS consult_data CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE consult_data;

CREATE TABLE IF NOT EXISTS chats (
                                     id INT AUTO_INCREMENT,
                                     role VARCHAR(50),
    content TEXT CHARACTER SET utf8mb4,
    PRIMARY KEY(id)
    );

-- 추천 직업 카테코리와 고유번호를 저장할 table

CREATE TABLE IF NOT EXISTS jobs (
                                    id INT AUTO_INCREMENT,
                                    job_name TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
                                    category TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
                                    PRIMARY KEY(id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO jobs (job_name, category)
VALUES ('운동 관련직', '서비스계열'),
       ('무용 관련직', '서비스계열'),
       ('안전 관련직', '기술계열'),
       ('일반운전 관련직', '기술계열'),
       ('기능직', '기술계열'),
       ('의복제조 관련직', '생산계열'),
       ('조리 관련직', '서비스계열'),
       ('이미용 관련직', '서비스계열'),
       ('기타 게임·오락·스포츠 관련직', '서비스계열'),
       ('고급 운전 관련직', '기술계열'),
       ('공학 기술직', '기술계열'),
       ('공학 전문직', '기술계열'),
       ('음악 관련직', '서비스계열'),
       ('악기 관련직', '서비스계열'),
       ('연기 관련직', '서비스계열'),
       ('웹·게임·애니메이션 관련직', '사무계열'),
       ('미술 및 공예 관련직', '생산계열'),
       ('기타 특수 예술직', '생산계열'),
       ('사회서비스직', '서비스계열'),
       ('인문계 교육 관련직', '서비스계열'),
       ('이공계 교육 관련직', '서비스계열'),
       ('의료관련 전문직', '기술계열'),
       ('IT관련전문직', '기술계열'),
       ('금융 및 경영 관련직', '사무계열'),
       ('인문 및 사회과학 관련직', '사무계열'),
       ('회계 관련직', '사무계열'),
       ('언어 관련 전문직', '사무계열'),
       ('작가 관련직', '사무계열'),
       ('교육관련 서비스직', '서비스계열'),
       ('기획서비스직', '사무계열'),
       ('매니지먼트 관련직', '서비스계열'),
       ('보건의료 관련 서비스직', '서비스계열'),
       ('사무 관련직', '사무계열'),
       ('영업관련 서비스직', '사무계열'),
       ('일반 서비스직', '서비스계열'),
       ('디자인 관련직', '사무계열'),
       ('영상 관련직', '사무계열'),
       ('예술기획 관련직', '기술계열'),
       ('자연친화 관련직', '기술계열'),
       ('농생명산업 관련직', '기술계열'),
       ('환경관련 전문직', '기술계열'),
       ('법률 및 사회활동 관련직', '사무계열'),
       ('이학 전문직', '사무계열');
