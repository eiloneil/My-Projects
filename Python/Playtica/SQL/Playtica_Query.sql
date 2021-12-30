if 1=1
begin
WITH LastOrder as (
	SELECT s.salesperson_id
	 , MAX(s.order_date) as LastOrderDate
	FROM PlayticaSales s
	GROUP BY s.salesperson_id	   
)

SELECT
	  s.salesperson_id
	, sp.Age as [salesperson_age]
	, COUNT(DISTINCT CASE 
			WHEN s.Amount > 1000
			THEN s.Number END) as [CNT_Sales_Above_1000]
	, MAX(CASE 
			WHEN s.Amount > 500
			THEN 1
			ELSE 0 END) as [has_above_500_sale]
	, COUNT(DISTINCT s.cust_id) as [CNT_Costumers]
	, DATEDIFF(DD, MAX(s.order_date), GETDATE()) as [DaysSinceLastOrder]
	, MAX(CASE 
			WHEN LastOrder.salesperson_id IS NOT NULL
			THEN s.Amount END) as [LastOrderAmount]
FROM PlayticaSales s
LEFT JOIN  LastOrder
	ON s.salesperson_id = LastOrder.salesperson_id
   AND s.order_date		= LastOrder.LastOrderDate
LEFT JOIN PlayticaSalesPerson sp
	on sp.ID = s.salesperson_id
GROUP BY s.salesperson_id
	  , sp.Age
end
	  ;

SELECT 
	  UserId	
	, Time_stamp	
	, platform_id	
	, install_source	
	, Country	
	, Gender	
	, Age

FROM (
	SELECT *
		, ROW_NUMBER() OVER (PARTITION BY i.UserId ORDER BY Time_stamp ASC) as rn
	FROM PlayticaInstalls i
	) irn
WHERE irn.rn = 1




/*
UserId	Time_stamp	platform_id	install_source	Country	Gender	Age

*/