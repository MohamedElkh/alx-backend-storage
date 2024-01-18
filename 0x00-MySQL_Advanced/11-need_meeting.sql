-- Script to creates view need_meeting to lists all students
-- have a score under 80 (strict) and no last_meeting or more than one

CREATE VIEW need_meeting AS SELECT name from students WHERE score < 80

AND (last_meeting IS NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH));