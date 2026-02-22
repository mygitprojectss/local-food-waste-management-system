-- Query 1 — Providers Per City
SELECT City,
COUNT(*) AS Total_Providers
FROM providers
GROUP BY City;

-- Query 2 — Receivers Per City
SELECT City,
COUNT(*) AS Total_Receivers
FROM receivers
GROUP BY City;

-- Query 3 — Provider Type Contribution
SELECT Provider_Type,
COUNT(*) AS Food_Count
FROM food_listings
GROUP BY Provider_Type;

-- Query 4 — Total Food Quantity
SELECT SUM(Quantity) AS Total_Food
FROM food_listings;

--  Query 5 — Highest Listings City
SELECT Location,
COUNT(*) AS Listings
FROM food_listings
GROUP BY Location
ORDER BY Listings DESC;

-- Query 6 — Most Available Food Type
SELECT Food_Type,
COUNT(*) AS Total
FROM food_listings
GROUP BY Food_Type
ORDER BY Total DESC;

-- Query 7 — Claims Per Food Item
SELECT Food_ID,
COUNT(*) AS Total_Claims
FROM claims
GROUP BY Food_ID;

-- Query 8 — Provider Highest Claims
SELECT p.Name,
COUNT(c.Claim_ID) AS Successful_Claims

FROM providers p

JOIN food_listings f

ON p.Provider_ID = f.Provider_ID

JOIN claims c

ON f.Food_ID = c.Food_ID

GROUP BY p.Name

ORDER BY Successful_Claims DESC;

-- Query 9 — Claim Status %
SELECT Status,
COUNT(*)*100.0/
(SELECT COUNT(*) FROM claims) AS Percentage
FROM claims
GROUP BY Status;

-- Query 10 — Meal Type Most Claimed
SELECT f.Meal_Type,
COUNT(c.Claim_ID) AS Claims

FROM food_listings f

JOIN claims c

ON f.Food_ID = c.Food_ID

GROUP BY f.Meal_Type

ORDER BY Claims DESC;

-- Query 11 — Avg Food Claimed Receiver
SELECT r.Name,
AVG(f.Quantity) AS Avg_Claimed

FROM receivers r

JOIN claims c

ON r.Receiver_ID=c.Receiver_ID

JOIN food_listings f

ON f.Food_ID=c.Food_ID

GROUP BY r.Name;

-- Query 12 — Total Donation Per Provider
SELECT p.Name,
SUM(f.Quantity) AS Total_Donated

FROM providers p

JOIN food_listings f

ON p.Provider_ID=f.Provider_ID

GROUP BY p.Name

ORDER BY Total_Donated DESC;