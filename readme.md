*Total sales amount per day*

SELECT  DATE(created_at) AS sale_day, COUNT(*) AS total_transactions, SUM(s.quantity * p.selling_price) AS total_units_sold FROM sales GROUP BY DATE;

*Profit per day*
SELECT DATE(s.created_at) AS sale_day,SUM((p.selling_price - p.buying_price) * s.quantity) AS daily_profit FROM sales s JOIN products p ON s.pid = p.id GROUP BY DAT (s.created_at) ORDER BY sale_day DESC;

*Sales per product*
SELECT p.name AS product_name, SUM(s.quantity) AS total_units_sold, COUNT(*) AS total_transactions FROM sales s JOIN products p ON s.pid = p.id
GROUP BY p.name ORDER BY total_units_sold DESC;

*Profit per product*
SELECT p.name AS product_name,SUM((p.selling_price - p.buying_price) * s.quantity) AS total_profit, SUM(s.quantity) AS total_units_sold FROM sales s JOIN products p ON s.pid = p.id GROUP BY p.name ORDER BY total_profit DESC;


class student:
identity : student
state : roles, responsibilities, duties
behavior: enforce rules, communicate, coordinate, assist, resolve

class car:
Identity : car
State : brand, color, type, model year, engine
bahavior : moves, transports, accelerate,reverse 