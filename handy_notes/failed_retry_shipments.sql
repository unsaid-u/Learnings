SHatter failed retry crons
- query 

WITH cte AS (
    SELECT
        t.integration_id AS integration_id,
        status,
        primary_identifier, 
        state,
        ROW_NUMBER() OVER (PARTITION BY t.primary_identifier, t.state ORDER BY t.updated_on DESC) AS row_data
    FROM
        task t 
    WHERE
        t.status IN ('failed', 'retry')
        AND t.integration_id IN  (5,9,26,40,47,54,57,60,66,71,84,97,98,102,106)
        AND t.updated_on between CURRENT_DATE - INTERVAL '3' DAY and CURRENT_DATE
    GROUP BY
        t.integration_id,
        status,state,
        t.primary_identifier,
        t.updated_on
)
SELECT
    integration_id,
    integration_name,
    status,
    COUNT(primary_identifier) AS shipment_count
FROM
    cte JOIN integration i ON integration_id = i.id
WHERE
    row_data = 1
group by 
 integration_id, i.integration_name, status
ORDER BY
    integration_id,
    shipment_count DESC;


! - never fully understood the query