

with EmployeeHr as 
	(
  SELECT e.EmployeeKey
		,e.FirstName + ' ' + e.LastName as FullName
		,isnull(e.ParentEmployeeKey, -999) as ParentKey
		,e.FirstName + ' ' + e.LastName as ParentFullName
		, 1 as [LEVEL]
		,e.Title
		,CAST(e.EmployeeKey AS VARCHAR)  as Hierarchy
  FROM dbo.DimEmployee e
  where e.ParentEmployeeKey is null
  
  UNION ALL

  SELECT ep.EmployeeKey
		,ep.FirstName + ' ' + ep.LastName as fname
		,ep.ParentEmployeeKey
		,hr.FullName as ParentFullName
		,hr.LEVEL + 1 as [LEVEL]
		,ep.Title
		,CAST(hr.Hierarchy + '>' + CAST(ep.EmployeeKey AS VARCHAR) AS VARCHAR) as HR
  FROM dbo.DimEmployee ep
  JOIN EmployeeHr hr on hr.EmployeeKey = ep.ParentEmployeeKey
	)

SELECT * FROM EmployeeHr
