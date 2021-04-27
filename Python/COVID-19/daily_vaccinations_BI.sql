-- Daily Vaccinated and Daily Healed by Dose

select 
	  p.vac_Date as [Date]
	, p.[1] as [Not_Healed_First Dose]
	, isnull(p.[2], 0) as [Not_Healed_Second Dose]
	, p.[1] + isnull(p.[2], 0) as [Not_Healed_Daily Total]
	, isnull(gp.CNT_valid_vacc, 0) as Not_Healed_Green_Passport
	, h.[First Dose] as Healed_First_Dose
	, h.[Second Dose] as Healed_Second_Dose
	, h.[Daily Total] as Healed_Daily_Total
	, p.[1] + h.[First Dose] as All_1st_Dose
	, isnull(p.[2],0) + h.[Second Dose] as All_2nd_Dose
	, isnull(gp.CNT_valid_vacc, 0) + h.[First Dose] as All_Green_Passport
	, p.[1] + h.[First Dose] + isnull(p.[2],0) + h.[Second Dose] as All_Daily_Total
from (

	--// Add Vaccinated by Dose - Not Healed
	select v.Dose_ind, CAST(v.Vaccination_Date_Time AS DATE) as vac_Date
			, count(distinct v.Person_Id) as CNT
	from dwh.Fact_Corona_Vaccination_Population v
	left join dwh.vw_Fact_Corona_Panel_Investigation_Model i
		on i.new_IdentityNumber = v.Person_Id
			and i.ind_active_heal = 1
			and i.date_recovery < v.Vaccination_Date_Time
	where v.Vaccination_Date_Time between '2020-12-19' and getdate()
		and i.new_IdentityNumber is null
		and v.Manufactor_Code = 22 --Tamar's addition according to Itamar's request (Pfizer)
	group by v.Dose_ind, CAST(v.Vaccination_Date_Time AS DATE)
	)a
PIVOT (
SUM(CNT) for Dose_ind in ([1], [2])
	)p
	
	--// Add Green Passports - Not Healed
left join (
	select CAST(v1.Vaccination_Date_Time AS DATE) as vac1_date
		, count(distinct v1.Person_Id) as CNT_valid_vacc
	from dwh.Fact_Corona_Vaccination_Population v1
	join dwh.Fact_Corona_Vaccination_Population v2
		on v1.Person_Id = v2.Person_Id
		and v1.Manufactor_Code = 22 --Tamar's addition according to Itamar's request (Moderna)
		and v1.Dose_ind = 1 and v2.Dose_ind = 2
	left join dwh.vw_Fact_Corona_Panel_Investigation_Model i
		on i.new_IdentityNumber = v1.Person_Id
			and i.ind_active_heal = 1
			and i.date_recovery < v1.Vaccination_Date_Time
	where DATEDIFF(DD, v2.Vaccination_Date_Time, GETDATE()) >= 7
		and i.new_IdentityNumber is null
		and DATEDIFF(DD, v1.Vaccination_Date_Time, GETDATE()) >= 25
	group by CAST(v1.Vaccination_Date_Time AS DATE)
	)gp on gp.vac1_date = p.vac_Date

	--// Add Healed and Vaccinated
left join (
	select 
		  p.vac_Date as Date
		, p.[1] as [First Dose]
		, isnull(p.[2], 0) as [Second Dose]
		, p.[1] + isnull(p.[2], 0) as [Daily Total]
	from (
		select v.Dose_ind, CAST(v.Vaccination_Date_Time AS DATE) as vac_Date
				, count(distinct v.Person_Id) as CNT
		from dwh.vw_Fact_Corona_Panel_Investigation_Model i
		join dwh.Fact_Corona_Vaccination_Population v
			on i.new_IdentityNumber = v.Person_Id
				and i.ind_active_heal = 1
				and i.date_recovery < v.Vaccination_Date_Time
				and v.Manufactor_Code = 22 --Tamar's addition according to Itamar's request (Moderna)
		group by v.Dose_ind, CAST(v.Vaccination_Date_Time AS DATE)
		)a
	PIVOT (
	SUM(CNT) for Dose_ind in ([1], [2])
		)p
	) h on h.Date = p.vac_Date

ORDER BY 1 ASC
