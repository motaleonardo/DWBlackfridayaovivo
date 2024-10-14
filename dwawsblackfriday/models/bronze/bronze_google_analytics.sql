WITH google_analytics AS (
    SELECT *
    FROM {{ source('dwblackfriday', 'google_analytics_data') }}
)

SELECT * FROM google_analytics