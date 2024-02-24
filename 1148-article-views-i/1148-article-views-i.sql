# Write your MySQL query statement below
select distinct author_id as id
from Views
where author_id = viewer_id
group by author_id, viewer_id
having count(*) >= 1
order by id asc