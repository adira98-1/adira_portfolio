SELECT
    CUSTOMER_ID,
    FIRST_NAME,
    LAST_NAME,
    EMAIL,
    CITY,
    STATE,
    SIGNUP_DATE
FROM {{ ref('stg_customers') }}