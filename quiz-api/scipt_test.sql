DELETE FROM Reponse;
DELETE FROM Question;

delete from sqlite_sequence where name='Question';
delete from sqlite_sequence where name='Reponse';

UPDATE Question SET title = 'blblbl' WHERE id=1

SELECT COUNT(*) FROM Reponse WHERE idQuestion=1;

DELETE FROM Reponse WHERE id=(SELECT MAX(id) FROM Reponse WHERE idQuestion=2)

UPDATE Reponse SET text = 'bl', isCorrect='bl' WHERE id=(SELECT MIN(id)+1 FROM Reponse WHERE idQuestion=1)

UPDATE Question SET position=position+1  WHERE (position>=1 AND position<3)

UPDATE Question SET position=position-1  WHERE (position<=4 AND position>2)

UPDATE Question SET position=position-1  WHERE position >1

INSERT INTO Participants VALUES ("coco",2,1);

INSERT INTO Participants (name, answers) VALUES ('pmpm', 5)

DELETE FROM Participants

SELECT COUNT(*) FROM Question

INSERT INTO Administration (login, password) VALUES ('admin','testAdmin') 

SELECT * FROM Administration
