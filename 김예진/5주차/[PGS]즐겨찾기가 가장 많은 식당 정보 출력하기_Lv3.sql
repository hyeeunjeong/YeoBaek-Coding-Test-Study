SELECT R.FOOD_TYPE, R.REST_ID, R.REST_NAME, R.FAVORITES
FROM REST_INFO R
WHERE R.FAVORITES = (
    SELECT MAX(F.FAVORITES)
    FROM REST_INFO F
    WHERE F.FOOD_TYPE = R.FOOD_TYPE
)
ORDER BY R.FOOD_TYPE DESC;
