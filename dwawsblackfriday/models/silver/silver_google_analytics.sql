WITH google_analytics_view AS (
    SELECT *
    FROM {{ ref('bronze_google_analytics') }}
)

SELECT
    CAST("date" as date) as "date",
    CAST("city" as varchar) as "city",
    CAST("country" as varchar) as "country",
    CAST("deviceCategory" as varchar) as "device_category",
    CAST("sessionSource" as varchar) as "session_source",
    CAST("sessionMedium" as varchar) as "session_medium",
    CAST("totalUsers" as integer) as "total_users",
    CAST("newUsers" as integer) as "new-users",
    CAST("activeUsers" as integer) as "active_users",
    CAST("sessions" as integer) as "sessions",
    CAST("engagedSessions" as integer) as "engaged_sessions",
    CAST("averageSessionDuration" as float) as "average_session_duration",
    CAST("screenPageViews" as integer) as "screen_page_views"
from google_analytics_view