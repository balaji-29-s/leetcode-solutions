# Write your MySQL query statement below
select round(count(a.player_id)/(select count(distinct player_id) from Activity),2) as fraction
from Activity a
join(
    select player_id,min(event_date) as first_date
    from Activity
    group by player_id
) f
on a.player_id=f.player_id
and datediff(a.event_date,f.first_date)=1