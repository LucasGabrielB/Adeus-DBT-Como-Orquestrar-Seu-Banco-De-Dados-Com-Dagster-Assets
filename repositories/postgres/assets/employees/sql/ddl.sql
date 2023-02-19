CREATE TABLE IF NOT EXISTS public.employees (
	employee_id int8 PRIMARY KEY,
	first_name varchar(40) NOT NULL,
	middle_initial varchar(40) NULL,
	last_name varchar(40) NOT NULL
);