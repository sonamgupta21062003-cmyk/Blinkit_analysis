-- 3. Step 4: Build the Analytical Master View (Joins all clean tables + Feature Engineering)


CREATE OR REPLACE VIEW vw_blinkit_master AS
SELECT 
    o.order_id,
    o.order_date,
    HOUR(o.order_date) AS order_hour,
    DAYNAME(o.order_date) AS order_day,
    o.customer_id,
    COALESCE(c.customer_segment, 'Unknown') AS customer_segment,
    COALESCE(c.area, 'Unknown') AS area,
    c.pincode,
    oi.product_id,
    COALESCE(p.product_name, CONCAT('Unknown Product (', oi.product_id, ')')) AS product_name,
    COALESCE(p.category, 'Uncategorized') AS category,
    COALESCE(p.brand, 'Unknown') AS brand,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * oi.unit_price) AS line_revenue,
    d.delivery_time_minutes AS delivery_variance_mins,
    CASE WHEN d.delivery_time_minutes > 0 THEN 1 ELSE 0 END AS is_delayed,
    d.delivery_status,
    d.reasons_if_delayed,
    f.rating,
    f.sentiment,
    f.feedback_category
FROM clean_orders o
INNER JOIN clean_order_items oi ON o.order_id = oi.order_id
LEFT JOIN clean_products p ON oi.product_id = p.product_id
LEFT JOIN clean_customers c ON o.customer_id = c.customer_id
LEFT JOIN clean_delivery d ON o.order_id = d.order_id
LEFT JOIN clean_feedback f ON o.order_id = f.order_id;

SELECT * FROM vw_blinkit_master LIMIT 10;
