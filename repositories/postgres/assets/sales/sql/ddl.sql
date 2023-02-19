CREATE TABLE IF NOT EXISTS sales (
	sales_id int8 PRIMARY KEY,
	salesperson_id int8 NOT NULL,
	customer_id int8 NOT NULL,
	product_id int8 NOT NULL,
	quantity int8 NOT NULL,
	CONSTRAINT sales_ibfk_1 FOREIGN KEY (salesperson_id) REFERENCES employees (employee_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT sales_ibfk_2 FOREIGN KEY (customer_id) REFERENCES customers (customer_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT sales_ibfk_3 FOREIGN KEY (product_id) REFERENCES products (product_id) ON DELETE CASCADE ON UPDATE CASCADE
);