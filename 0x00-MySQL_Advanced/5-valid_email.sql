-- Script to creates trigger to resets the attribute
-- valid_email only when the email has changed

DELIMITER $$ ;
CREATE TRIGGER validate BEFORE UPDATE ON users
FOR EACH ROW

BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;$$
DELIMITER ;
