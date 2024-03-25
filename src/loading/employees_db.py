import sqlite3
from project_paths import EMPLOYEES_DB


# Connect to database (create if not exists)
con = sqlite3.connect(EMPLOYEES_DB)
cur = con.cursor()

# Create tables and insert data
cur.executescript("""
create table tEmployeeList(
    EmployeeId int,
    EmployeeName nvarchar(250),
    EmployeeTitle nvarchar(250),
    ManagerId int
);

create table tSalary(
    CalendarDate date,
    Employee nvarchar(250),
    Department nvarchar(250),
    Salary numeric(18, 2)
);

create table Dimension_Employee(
    EmployeeId int,
    EmployeeName nvarchar(250),
    EmployeeTitle nvarchar(250),
    ManagerId int,
    SalaryNumber int,
    date_from datetime default CURRENT_TIMESTAMP,
    date_to datetime default '9999-12-31 23:59:59'
);

insert into tEmployeeList(EmployeeId, EmployeeName, EmployeeTitle, ManagerId)
select 1 as EmployeeId, 'John T.' as EmployeeName, 'Director of American Office' as EmployeeTitle, null as ManagerId
union
select 2 as EmployeeId, 'George F.' as EmployeeName, 'Manager' as EmployeeTitle, 1 as ManagerId
union
select 3 as EmployeeId, 'Elliot S.' as EmployeeName, 'Driver' as EmployeeTitle, 2 as ManagerId
union
select 11 as EmployeeId, 'Anna K.' as EmployeeName, 'Director of European Office' as EmployeeTitle, null as ManagerId
union
select 12 as EmployeeId, 'Elsa F.' as EmployeeName, 'Senior Manager' as EmployeeTitle, 11 as ManagerId
union
select 13 as EmployeeId, 'Olaf S.' as EmployeeName, 'Snowma' as EmployeeTitle, 12 as ManagerId
union
select 21 as EmployeeId, 'Tom K.' as EmployeeName, 'Cat in European Office' as EmployeeTitle, 11 as ManagerId
union
select 22 as EmployeeId, 'Kristoff I.' as EmployeeName, 'Ice Manager' as EmployeeTitle, 21 as ManagerId
union
select 23 as EmployeeId, 'Troll K.' as EmployeeName, 'Stone Manager' as EmployeeTitle, 22 as ManagerId;

insert into tSalary(CalendarDate, Employee, Department, Salary)
select '20190101' as CalendarDate, 'Employee #1' as Employee, 'Sales' as Department, 1000 as Salary
union
select '20190201' as CalendarDate, 'Employee #1' as Employee, 'Sales' as Department, 1200 as Salary
union
select '20190301' as CalendarDate, 'Employee #1' as Employee, 'Sales' as Department, 1500 as Salary
union
select '20190401' as CalendarDate, 'Employee #1' as Employee, 'Sales' as Department, 1700 as Salary
union
select '20190101' as CalendarDate, 'Employee #2' as Employee, 'Sales' as Department, 2000 as Salary
union
select '20190201' as CalendarDate, 'Employee #2' as Employee, 'Sales' as Department, 2200 as Salary
union
select '20190301' as CalendarDate, 'Employee #2' as Employee, 'Sales' as Department, 2500 as Salary
union
select '20190401' as CalendarDate, 'Employee #2' as Employee, 'Sales' as Department, 2700 as Salary
union
select '20190101' as CalendarDate, 'Employee #3' as Employee, 'Marketing' as Department, 3000 as Salary
union
select '20190201' as CalendarDate, 'Employee #3' as Employee, 'Marketing' as Department, 3200 as Salary
union
select '20190301' as CalendarDate, 'Employee #3' as Employee, 'Marketing' as Department, 3500 as Salary
union
select '20190401' as CalendarDate, 'Employee #3' as Employee, 'Marketing' as Department, 3700 as Salary;
""")

# Commit and close connection
con.commit()
con.close()
