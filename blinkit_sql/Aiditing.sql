use blinkitdb;


USE blinkitdb;

-- 1. Check row counts across all 9 tables
SELECT 'blinkit_orders' AS table_name, COUNT(*) AS row_count FROM blinkit_orders
UNION ALL
SELECT 'blinkit_order_items', COUNT(*) FROM blinkit_order_items
UNION ALL
SELECT 'blinkit_products', COUNT(*) FROM blinkit_products
UNION ALL
SELECT 'blinkit_customers', COUNT(*) FROM blinkit_customers
UNION ALL
SELECT 'blinkit_customer_feedback', COUNT(*) FROM blinkit_customer_feedback
UNION ALL
SELECT 'blinkit_delivery_performance', COUNT(*) FROM blinkit_delivery_performance
UNION ALL
SELECT 'blinkit_inventory', COUNT(*) FROM blinkit_inventory
UNION ALL
SELECT 'blinkit_inventorynew', COUNT(*) FROM blinkit_inventorynew
UNION ALL
SELECT 'blinkit_marketing_performance', COUNT(*) FROM blinkit_marketing_performance;

-- 2. Inspect column names and data types across your schema
SELECT table_name, column_name, data_type 
FROM information_schema.columns 
WHERE table_schema = 'blinkitdb'
ORDER BY table_name, ordinal_position;


-- 1. Check unique customers
SELECT customer_id, COUNT(*) 
FROM blinkit_customers 
GROUP BY customer_id 
HAVING COUNT(*) > 1;

-- 2. Check duplicate product lines inside the same order
SELECT order_id, product_id, COUNT(*) 
FROM blinkit_order_items 
GROUP BY order_id, product_id 
HAVING COUNT(*) > 1;

-- 3. Check duplicate delivery records for the same order
SELECT order_id, COUNT(*) 
FROM blinkit_delivery_performance 
GROUP BY order_id 
HAVING COUNT(*) > 1;

-- 2. Check for orphan order items (items pointing to an order_id that doesn't exist)
SELECT COUNT(*) AS orphan_items
FROM blinkit_order_items oi
LEFT JOIN blinkit_orders o ON oi.order_id = o.order_id
WHERE o.order_id IS NULL;

