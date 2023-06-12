import pyodbc

cnxn = pyodbc.connect(
    "DRIVER={Devart ODBC Driver for PostgreSQL};Server=localhost;Port=5432;Database=postgres;User ID=postgres;Password=Harut.2001;Schema=postgres;String Types=Unicode"
)

cursor = cnxn.cursor()


cursor.execute(
    """
CREATE TABLE public.departments_0 (
  department_id SERIAL PRIMARY KEY,
  department_name VARCHAR(50) NOT NULL
);
"""
)
cursor.execute(
    """INSERT INTO public.departments_0 (department_name) VALUES
  ('HR'),
  ('Finance'),
  ('Marketing'),
  ('Engineering');"""
)

cursor.execute("SELECT * FROM public.departments_0")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
print()

cursor.execute(
    """
CREATE TABLE public.employees_0 (
  employee_id SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  department_id INT REFERENCES public.departments_0(department_id),
  manager_id INT REFERENCES public.employees_0(employee_id),
  hire_date DATE NOT NULL,
  salary NUMERIC(10,2) NOT NULL
);"""
)

cursor.execute(
    """INSERT INTO public.employees_0 (first_name, last_name, department_id, hire_date, salary, email) VALUES
  ('John', 'Doe', 1, '2022-01-15', 50000, 'johndoe@gmail.com'),
  ('Jane', 'Smith', 2, '2021-05-10', 60000, 'janesmith@gmail.com'),
  ('Michael', 'Johnson', 1, '2020-08-20', 55000, 'michaeljohnson@gmail.com'),
  ('Sarah', 'Williams', 3, '2023-02-01', 45000,'sarahwilliams@gmail.com'),
  ('David', 'Brown', 4, '2019-12-01', 70000,'davidbrown@gmail.com');"""
)

cursor.execute("SELECT * FROM public.employees_0")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
print()

cursor.execute(
    """SELECT CONCAT (first_name, ' ', last_name) as full_name, public.departments_0.department_name,public.employees_0.salary
FROM public.employees_0
INNER JOIN public.departments_0
ON public.employees_0.department_id = public.departments_0.department_id;"""
)
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
print()

cursor.execute(
    """SELECT public.departments_0.department_name,AVG(salary) AS average_salary
FROM public.employees_0
INNER JOIN public.departments_0
ON public.employees_0.department_id = public.departments_0.department_id
GROUP BY
department_name;"""
)
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
print()

cursor.execute(
    """SELECT
  CONCAT(public.employees_0.first_name, ' ', public.employees_0.last_name) AS employee_name,
  CONCAT(public.employees_0.first_name, ' ', public.employees_0.last_name) AS manager_name,
  department_name
FROM
  public.employees_0
JOIN
  public.departments_0 ON public.departments_0.department_id = public.employees_0.department_id
LEFT JOIN
  public.employees_0 m ON public.employees_0.manager_id = public.employees_0.employee_id;"""
)
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
print()

cursor.execute(
    """SELECT
  CONCAT(public.employees_0.first_name, ' ', public.employees_0.last_name) AS full_name,
  email
FROM
  public.employees_0
WHERE
  salary > 50000;"""
)
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
print()

cursor.execute(
    """UPDATE public.employees_0
SET salary = 60000
WHERE employee_id = 1;
SELECT * FROM public.employees_0;"""
)
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
print()

cursor.execute(
    """DELETE FROM public.employees_0
WHERE employee_id = 2;
SELECT * FROM public.employees_0;"""
)
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
print()
