SELECT
    ORDER_ID,
    PRODUCT_ID,
    QUANTITY
FROM {{ source('raw', 'ORDER_ITEMS') }}