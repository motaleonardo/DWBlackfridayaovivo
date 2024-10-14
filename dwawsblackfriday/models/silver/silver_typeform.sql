WITH typeform AS (
    SELECT *
    FROM {{ ref('bronze_typeform_responses') }}
)

SELECT
    submitted_at,
    response_id
FROM typeform