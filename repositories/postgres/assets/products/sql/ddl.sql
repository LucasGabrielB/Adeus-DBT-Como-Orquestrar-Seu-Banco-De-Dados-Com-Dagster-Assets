CREATE TABLE IF NOT EXISTS public.products (
	product_id int8 PRIMARY KEY,
	"name" varchar(50) NOT NULL,
	price numeric(19, 4) NULL
);