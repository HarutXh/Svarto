DROP TABLE departments_3;
DROP TABLE employees_3;
CREATE TABLE departments_3 (
  department_id SERIAL PRIMARY KEY,
  department_name VARCHAR(50) NOT NULL
);

CREATE TABLE employees_3 (
  employee_id SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  department_id INT REFERENCES departments_3(department_id),
  manager_id INT REFERENCES employees_3(employee_id),
  hire_date DATE NOT NULL,
  salary NUMERIC(10,2) NOT NULL
);

INSERT INTO departments_3 (department_name) VALUES
  ('HR'),
  ('Finance'),
  ('Marketing'),
  ('Engineering');

INSERT INTO employees_3 (first_name, last_name, department_id, hire_date, salary, email) VALUES
  ('John', 'Doe', 1, '2022-01-15', 50000, 'johndoe@gmail.com'),
  ('Jane', 'Smith', 2, '2021-05-10', 60000, 'janesmith@gmail.com'),
  ('Michael', 'Johnson', 1, '2020-08-20', 55000, 'michaeljohnson@gmail.com'),
  ('Sarah', 'Williams', 3, '2023-02-01', 45000,'sarahwilliams@gmail.com'),
  ('David', 'Brown', 4, '2019-12-01', 70000,'davidbrown@gmail.com');


SELECT CONCAT (first_name, ' ', last_name) as full_name, departments_3.department_name,employees_3.salary
FROM employees_3
INNER JOIN departments_3
ON employees_3.department_id = departments_3.department_id;

SELECT departments_3.department_name,AVG(salary) AS average_salary
FROM employees_3
INNER JOIN departments_3
ON employees_3.department_id = departments_3.department_id
GROUP BY
department_name;

SELECT
  CONCAT(employees_3.first_name, ' ', employees_3.last_name) AS employee_name,
  CONCAT(employees_3.first_name, ' ', employees_3.last_name) AS manager_name,
  department_name
FROM
  employees_3
JOIN
  departments_3 ON departments_3.department_id = employees_3.department_id
LEFT JOIN
  employees_3 m ON employees_3.manager_id = employees_3.employee_id;

SELECT
  CONCAT(employees_3.first_name, ' ', employees_3.last_name) AS full_name,
  email
FROM
  employees_3
WHERE
  salary > 50000;

UPDATE employees_3
SET salary = 60000
WHERE employee_id = 1;

Select * FROM employees_3;

DELETE FROM employees_3
WHERE employee_id = 2;

SELECT * FROM employees_3;

