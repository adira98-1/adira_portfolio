SELECT
    o.ORDER_ID,
    o.CUSTOMER_ID,
    oi.PRODUCT_ID,
    o.ORDER_DATE,
    oi.QUANTITY,
    o.TOTAL_AMOUNT
FROM {{ ref('stg_orders') }} o
JOIN {{ ref('stg_order_items') }} oi
    ON o.ORDER_ID = oi.ORDER_ID