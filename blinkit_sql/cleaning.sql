CREATE OR REPLACE VIEW vw_blinkit_master AS
SELECT 
    o.order_id,
    o.customer_id,
    o.order_date,
    oi.product_id,
    p.product_name,
    p.category,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * oi.unit_price) AS line_total,
    dp.delivery_time_minutes,
    dp.delivery_status,
    cf.rating,
    cf.feedback_category
FROM blinkit_orders o
INNER JOIN blinkit_order_items oi ON o.order_id = oi.order_id
LEFT JOIN blinkit_products p ON oi.product_id = p.product_id
LEFT JOIN blinkit_delivery_performance dp ON o.order_id = dp.order_id
LEFT JOIN blinkit_customer_feedback cf ON o.order_id = cf.order_id;

-- Clean Orders (keeps 1 row per order_id)
CREATE TABLE clean_orders AS
WITH ranked_orders AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY order_date ASC) AS rn
    FROM blinkit_orders
)
SELECT * FROM ranked_orders WHERE rn = 1;

-- Clean Order Items (keeps 1 row per order_id + product_id pair)
CREATE TABLE clean_order_items AS
WITH ranked_items AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY order_id, product_id ORDER BY order_id) AS rn
    FROM blinkit_order_items
)
SELECT * FROM ranked_items WHERE rn = 1;


-- Clean Orders (keeps 1 row per order_id)
CREATE TABLE clean_orders AS
WITH ranked_orders AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY order_date ASC) AS rn
    FROM blinkit_orders
)
SELECT * FROM ranked_orders WHERE rn = 1;

-- Clean Order Items (keeps 1 row per order_id + product_id pair)
CREATE TABLE clean_order_item AS
WITH ranked_items AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY order_id, product_id ORDER BY order_id) AS rn
    FROM blinkit_order_items
)
SELECT * FROM ranked_items WHERE rn = 1;

-- Clean Products table: trim spaces and standardize casing
CREATE TABLE clean_products AS
SELECT DISTINCT
    product_id,
    TRIM(product_name) AS product_name,
    CONCAT(UPPER(LEFT(TRIM(category), 1)), LOWER(SUBSTRING(TRIM(category), 2))) AS category,
    brand,
    COALESCE(price, 0) AS price,
    COALESCE(mrp, price, 0) AS mrp
FROM blinkit_products
WHERE product_id IS NOT NULL;


-- Clean Delivery Performance: filter out impossible negative times and standardize status
CREATE TABLE clean_delivery AS
SELECT 
    order_id,
    delivery_partner_id,
    promised_time,
    actual_time,
    ABS(delivery_time_minutes) AS delivery_time_minutes,
    COALESCE(NULLIF(TRIM(delivery_status), ''), 'Unknown') AS delivery_status,
    COALESCE(reasons_if_delayed, 'No Delay') AS reasons_if_delayed
FROM blinkit_delivery_performance
WHERE order_id IS NOT NULL;

-- Clean Customer Feedback: replace NULL text with 'No Comment' and filter invalid ratings
CREATE TABLE clean_feedback AS
SELECT 
    feedback_id,
    order_id,
    customer_id,
    rating,
    COALESCE(NULLIF(TRIM(feedback_text), ''), 'No Comment') AS feedback_text,
    COALESCE(NULLIF(TRIM(feedback_category), ''), 'General') AS feedback_category,
    sentiment,
    feedback_date
FROM blinkit_customer_feedback
WHERE rating BETWEEN 1 AND 5;
