USE TrojanScheduler;

ALTER TABLE courses
ADD course_id_string varchar(255);


ALTER TABLE courses
ADD course_name_long varchar(2000);

DELETE FROM professors;
DELETE FROM courses;

SELECT * FROM professors;
SELECT * FROM courses;



