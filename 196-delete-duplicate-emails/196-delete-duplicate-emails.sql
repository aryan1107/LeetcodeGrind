# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE p2 From Person p1, Person p2 WHERE p1.email = p2.email
AND p2.id > p1.id;