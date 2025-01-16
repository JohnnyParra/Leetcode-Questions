SELECT EU.unique_id, E.name
FROM EmployeeUNI EU
RIGHT JOIN Employees E on EU.id = E.id;