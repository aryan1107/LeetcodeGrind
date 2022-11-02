# Write your MySQL query statement below
SELECT player_id, min(event_date) as 'first_login'
FROM Activity A
Group by A.player_id;