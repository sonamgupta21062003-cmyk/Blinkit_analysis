USE blinkitdb;

-- 1. Check Delivery Performance & Feedback links to Orders
SELECT 'orphan_deliveries' AS check_name, COUNT(*) AS issue_count
FROM blinkit_delivery_performance dp
LEFT JOIN blinkit_orders o ON dp.order_id = o.order_id
WHERE o.order_id IS NULL

UNION ALL

SELECT 'orphan_feedback', COUNT(*)
FROM blinkit_customer_feedback cf
LEFT JOIN blinkit_orders o ON cf.order_id = o.order_id
WHERE o.order_id IS NULL

UNION ALL

-- 2. Check Feedback links to Customers
SELECT 'orphan_feedback_customers', COUNT(*)
FROM blinkit_customer_feedback cf
LEFT JOIN blinkit_customers c ON cf.customer_id = c.customer_id
WHERE c.customer_id IS NULL

UNION ALL

-- 3. Check BOTH Inventory tables links to Products
SELECT 'orphan_inventory_old', COUNT(*)
FROM blinkit_inventory i
LEFT JOIN blinkit_products p ON i.product_id = p.product_id
WHERE p.product_id IS NULL

UNION ALL

SELECT 'orphan_inventory_new', COUNT(*)
FROM blinkit_inventorynew inew
LEFT JOIN blinkit_products p ON inew.product_id = p.product_id
WHERE p.product_id IS NULL;

-- 4. Compare blinkit_inventory vs blinkit_inventorynew (to see which one to keep)
SELECT 'blinkit_inventory' AS tbl, COUNT(*) AS total_rows, MIN(date) AS start_date, MAX(date) AS end_date FROM blinkit_inventory
UNION ALL
SELECT 'blinkit_inventorynew', COUNT(*), MIN(date), MAX(date) FROM blinkit_inventorynew;

-- 5. Quick check on Marketing Performance (Standalone campaign table)
SELECT COUNT(*) AS total_campaigns, SUM(CASE WHEN spend < 0 OR revenue < 0 THEN 1 ELSE 0 END) AS negative_values
FROM blinkit_marketing_performance;
