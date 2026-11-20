SELECT 'product' AS src, 'product' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM product AS a CROSS JOIN product AS b
UNION ALL
SELECT 'product' AS src, 'customer' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM product AS a CROSS JOIN customer AS b
UNION ALL
SELECT 'product' AS src, 'approved' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM product AS a CROSS JOIN approved AS b
UNION ALL
SELECT 'product' AS src, 'blocked' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM product AS a CROSS JOIN blocked AS b
UNION ALL
SELECT 'product' AS src, 'interested' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM product AS a CROSS JOIN interested AS b
UNION ALL
SELECT 'product' AS src, 'explicitly_ignoring' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM product AS a CROSS JOIN explicitly_ignoring AS b
UNION ALL
SELECT 'customer' AS src, 'product' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM customer AS a CROSS JOIN product AS b
UNION ALL
SELECT 'customer' AS src, 'customer' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM customer AS a CROSS JOIN customer AS b
UNION ALL
SELECT 'customer' AS src, 'approved' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM customer AS a CROSS JOIN approved AS b
UNION ALL
SELECT 'customer' AS src, 'blocked' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM customer AS a CROSS JOIN blocked AS b
UNION ALL
SELECT 'customer' AS src, 'interested' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM customer AS a CROSS JOIN interested AS b
UNION ALL
SELECT 'customer' AS src, 'explicitly_ignoring' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM customer AS a CROSS JOIN explicitly_ignoring AS b
UNION ALL
SELECT 'approved' AS src, 'product' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM approved AS a CROSS JOIN product AS b
UNION ALL
SELECT 'approved' AS src, 'customer' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM approved AS a CROSS JOIN customer AS b
UNION ALL
SELECT 'approved' AS src, 'approved' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM approved AS a CROSS JOIN approved AS b
UNION ALL
SELECT 'approved' AS src, 'blocked' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM approved AS a CROSS JOIN blocked AS b
UNION ALL
SELECT 'approved' AS src, 'interested' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM approved AS a CROSS JOIN interested AS b
UNION ALL
SELECT 'approved' AS src, 'explicitly_ignoring' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM approved AS a CROSS JOIN explicitly_ignoring AS b
UNION ALL
SELECT 'blocked' AS src, 'product' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM blocked AS a CROSS JOIN product AS b
UNION ALL
SELECT 'blocked' AS src, 'customer' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM blocked AS a CROSS JOIN customer AS b
UNION ALL
SELECT 'blocked' AS src, 'approved' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM blocked AS a CROSS JOIN approved AS b
UNION ALL
SELECT 'blocked' AS src, 'blocked' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM blocked AS a CROSS JOIN blocked AS b
UNION ALL
SELECT 'blocked' AS src, 'interested' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM blocked AS a CROSS JOIN interested AS b
UNION ALL
SELECT 'blocked' AS src, 'explicitly_ignoring' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM blocked AS a CROSS JOIN explicitly_ignoring AS b
UNION ALL
SELECT 'interested' AS src, 'product' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM interested AS a CROSS JOIN product AS b
UNION ALL
SELECT 'interested' AS src, 'customer' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM interested AS a CROSS JOIN customer AS b
UNION ALL
SELECT 'interested' AS src, 'approved' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM interested AS a CROSS JOIN approved AS b
UNION ALL
SELECT 'interested' AS src, 'blocked' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM interested AS a CROSS JOIN blocked AS b
UNION ALL
SELECT 'interested' AS src, 'interested' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM interested AS a CROSS JOIN interested AS b
UNION ALL
SELECT 'interested' AS src, 'explicitly_ignoring' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM interested AS a CROSS JOIN explicitly_ignoring AS b
UNION ALL
SELECT 'explicitly_ignoring' AS src, 'product' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM explicitly_ignoring AS a CROSS JOIN product AS b
UNION ALL
SELECT 'explicitly_ignoring' AS src, 'customer' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM explicitly_ignoring AS a CROSS JOIN customer AS b
UNION ALL
SELECT 'explicitly_ignoring' AS src, 'approved' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM explicitly_ignoring AS a CROSS JOIN approved AS b
UNION ALL
SELECT 'explicitly_ignoring' AS src, 'blocked' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM explicitly_ignoring AS a CROSS JOIN blocked AS b
UNION ALL
SELECT 'explicitly_ignoring' AS src, 'interested' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM explicitly_ignoring AS a CROSS JOIN interested AS b
UNION ALL
SELECT 'explicitly_ignoring' AS src, 'explicitly_ignoring' AS dst,
       CASE WHEN (b.x,b.y,b.z) = (-a.x,-a.y,-a.z) THEN 'join' ELSE 'antijoin' END AS relation
FROM explicitly_ignoring AS a CROSS JOIN explicitly_ignoring AS b
ORDER BY src, dst;
