select 
      p3.proj_group, 
      min(p3.proj_start) as date_start,
      max(p3.proj_end) as date_end,
      julianday(max(p3.proj_end))-julianday( min(p3.proj_end))+1 as delta
from
    (select 
	     p2.*,
	     sum(p2.flag)over(order by p2.proj_id) as proj_group
	from 
		(select 
		      p.proj_id , 
		      p.proj_start, 
		      p.proj_end, 
		      case 
		      when lag(p.proj_end)over(order by p.proj_id) = p.proj_start then 0 else 1 
		      end as flag
		from projects as p) as p2) as p3
group by p3.proj_group