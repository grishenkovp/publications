SELECT s3.date,
	s3.user_id,
	s3.date - s2.first_date AS delta_days,
	ceil((s3.date - s2.first_date)::real/30::real)*30 AS cohort_days,
	to_char(s2.first_date,'YYYY-MM') AS first_transaction
	s3.amount
FROM public.sales AS s3
LEFT JOIN
				(SELECT s1.user_id,
						MIN(s1.date) AS first_date
					FROM public.sales AS s1
					GROUP BY s1.user_id) AS s2 ON s3.user_id = s2.user_id
ORDER BY s3.user_id,
	s3.date



SELECT  s.date,
		s.user_id,
		s.date - FIRST_VALUE(s.date) OVER(PARTITION BY s.user_id ORDER BY s.date) AS delta_days,
		ceil((s.date - FIRST_VALUE(s.date) OVER(PARTITION BY s.user_id ORDER BY s.date))::real/30::real)*30 AS cohort_days,
		to_char(FIRST_VALUE(s.date) OVER(PARTITION BY s.user_id ORDER BY s.date),'YYYY-MM') AS first_transaction,
		s.amount
FROM public.sales AS s
ORDER BY s.user_id,
	s.date




SELECT r2.first_transaction,
		r2.cohort_days,
		--r2.total_amount,
		--sum(r2.total_amount) OVER (PARTITION BY r2.first_transaction ORDER BY r2.first_transaction, r2.cohort_days) as cumsum_amount,
		--first_value(r2.total_amount) OVER (PARTITION BY r2.first_transaction ORDER BY r2.first_transaction, r2.cohort_days) as first_total_amount,
		round((sum(r2.total_amount) OVER (PARTITION BY r2.first_transaction ORDER BY r2.first_transaction, r2.cohort_days)/ 
		first_value(r2.total_amount) OVER (PARTITION BY r2.first_transaction ORDER BY r2.first_transaction, r2.cohort_days)-1),3) as percent_cumsum_amount
FROM 
		(SELECT r.first_transaction, r.cohort_days, sum(r.amount) AS total_amount		
		FROM public.report_cohort_analysis AS r
		GROUP BY r.first_transaction, r.cohort_days
		ORDER BY r.first_transaction, r.cohort_days) as r2
		
SELECT *
FROM public.report_cohort_analysis
LIMIT 10

SELECT *
FROM public.report_cohort_analysis_percent
LIMIT 10
