SELECT today.id as Id
FROM Weather as yesterday
JOIN Weather as today ON (today.recordDate::date - yesterday.recordDate::date) = 1
    AND today.temperature > yesterday.temperature;