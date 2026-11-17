-- Clean Customers
CREATE TABLE clean_customers AS
SELECT DISTINCT
    customer_id,
    TRIM(customer_name) AS customer_name,
    LOWER(TRIM(email)) AS email,
    TRIM(area) AS area,
    pincode,
    STR_TO_DATE(registration_date, '%Y-%m-%d') AS registration_date,
    COALESCE(customer_segment, 'Regular') AS customer_segment
FROM blinkit_customers
WHERE customer_id IS NOT NULL;
