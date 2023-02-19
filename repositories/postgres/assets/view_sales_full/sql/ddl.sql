CREATE OR REPLACE VIEW view_sales_full AS
SELECT 
	sales.sales_id, 
	
	employees.employee_id,
	concat(employees.first_name, ' ', employees.middle_initial, '. ', employees.last_name) AS employee_full_name,
	
	customers.customer_id,
	concat(customers.first_name, ' ', customers.middle_initial, '. ', customers.last_name) AS customer_full_name,
	
	products.product_id,
	products."name" AS product_name,
	products.price  AS product_price,
	sales.quantity  AS product_quantity
FROM 
	sales INNER JOIN employees ON 
		sales.salesperson_id = employees.employee_id 
	INNER JOIN products ON 
		sales.product_id = products.product_id 
	INNER JOIN customers ON 
		sales.customer_id = customers.customer_id