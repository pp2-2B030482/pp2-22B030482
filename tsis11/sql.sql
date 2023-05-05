CREATE OR REPLACE  FUNCTION find(patt VARCHAR)
RETURNS TABLE(
    first_name VARCHAR(20) ,
    phone_number VARCHAR(20)
) AS
$$
declare
    finde varchar :=CONCAT('%',patt,'%');
BEGIN
  RETURN QUERY
  SELECT m.first_name,m.phone_number from phonebook m
  WHERE m.first_name LIKE finde or m.phone_number LIKE finde;
END;
$$
LANGUAGE plpgsql;
DROP FUNCTION find;
SELECT find('d');

######################################################################################;


CREATE PROCEDURE create_contact(namer VARCHAR,phone_numb VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO phonebook(first_name,phone_number)
    VALUES(namer,phone_numb);
END;
$$;
CALL create_contact('klnlln','23234');
DROP Procedure create_contact;


######################################################################################;


CREATE PROCEDURE update_contact(namer VARCHAR,phone_numb VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE phonebook set phone_number=phone_numb WHERE first_name=namer;
END;
$$;
CALL update_contact('qwer','1');
SELECT * FROM phonebook;


######################################################################################;



CREATE PROCEDURE create_contacts(list_in TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
  item VARCHAR;
  i INTEGER;
BEGIN
    FOREACH item IN ARRAY list_in LOOP
        SELECT count(*) INTO i from phonebook WHERE first_name = split_part(item,' ',1);
        IF i = 0 THEN
            INSERT INTO phonebook(first_name,phone_number)
            VALUES( split_part(item,' ',1),split_part(item,' ',2));
        ELSE 
            UPDATE phonebook set phone_number=split_part(item,' ',2) WHERE first_name=split_part(item,' ',1);
            i:=0;
        END IF;
    END LOOP;
END;
$$;
CALL create_contacts(array['sgs 1','rrgerg 456454545']);
SELECT * from phonebook;
DROP Procedure create_contacts;



######################################################################################;


CREATE FUNCTION get_sorting_desc(modee text,pagination_limit INTEGER,pagination_offset INTEGER)
RETURNS TABLE(
    first_name2 VARCHAR(20) ,
    phone_number VARCHAR(20)
) AS
$$
DECLARE
   
BEGIN
  RETURN QUERY
  SELECT m.first_name,m.phone_number from phonebook m 
  ORDER BY m.first_name DESC
  OFFSET pagination_offset
  LIMIT pagination_limit;
END;
$$
LANGUAGE plpgsql;

DROP FUNCTION get_sorting_desk;

SELECT * FROM phonebook ORDER BY first_name DESC;
SELECT * from get_sorting_desk('DESK',4,0);


######################################################################################;


CREATE FUNCTION get_sorting_asc(modee text,pagination_limit INTEGER,pagination_offset INTEGER)
RETURNS TABLE(
    first_name2 VARCHAR(20) ,
    phone_number VARCHAR(20)
) AS
$$
DECLARE
   
BEGIN
  RETURN QUERY
  SELECT m.first_name,m.phone_number from phonebook m 
  ORDER BY m.first_name ASC
  OFFSET pagination_offset
  LIMIT pagination_limit;
END;
$$
LANGUAGE plpgsql;


######################################################################################;


CREATE PROCEDURE delete_contact(something VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = something OR phone_number = something;
END
$$;
CALL delete_contact('3333333333');
SELECT * FROM phonebook;