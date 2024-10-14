WITH typeform AS (
    SELECT *
    FROM {{ source('dwblackfriday', 'typeform_responses') }}
)

SELECT * FROM typeform