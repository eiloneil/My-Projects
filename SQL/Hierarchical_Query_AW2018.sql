

WITH T AS (
SELECT	e.BusinessEntityID
	,	e.NationalIDNumber
	,	e.JobTitle
	,	e.OrganizationNode
	,	Isnull(e.OrganizationLevel, 0) as OrganizationLevel
	,	(select Max(e.NationalIDNumber) as id from HumanResources.Employee e where OrganizationLevel is null) as PID
	,	(select Max(e.JobTitle) as id from HumanResources.Employee e where OrganizationLevel is null) as P_JDesc
	,	(select Max(e.BusinessEntityID) as id from HumanResources.Employee e where OrganizationLevel is null) as P_BusinessEntityID
FROM	AdventureWorks2019.HumanResources.Employee e
WHERE	1=1
	AND	hierarchyid::GetRoot() = Isnull(OrganizationNode.GetAncestor(1), hierarchyid::GetRoot() )

UNION ALL 

SELECT	e.BusinessEntityID
	,	e.NationalIDNumber
	,	e.JobTitle
	,	e.OrganizationNode
	,	e.OrganizationLevel
	,	t.NationalIDNumber as PID
	,	t.JobTitle
	,	t.BusinessEntityID as P_BusinessEntityID
FROM	AdventureWorks2019.HumanResources.Employee e
JOIN	t 
	ON	e.OrganizationNode.GetAncestor(1) = t.OrganizationNode


 )


SELECT	t.BusinessEntityID as EmployeeBusinessEntityID 
	,	t.NationalIDNumber as EmployeeID
	,	pe.FirstName + ' ' + pe.LastName as Employee_Full_Name 
	,	t.JobTitle as EmployeeJobTitle
	,	t.OrganizationLevel
	,	t.P_BusinessEntityID as ParentBusinessEntityID 
	,	t.PID	as ParentID
	,	pp.FirstName + ' ' + pp.LastName as Parent_Full_Name 
	,	t.P_JDesc as ParentJobTitle

FROM t
LEFT JOIN Person.Person pe
	ON	pe.BusinessEntityID = t.BusinessEntityID
LEFT JOIN Person.Person pp
	ON	pp.BusinessEntityID = t.P_BusinessEntityID
ORDER BY OrganizationLevel ASC, 1 ASC

;


