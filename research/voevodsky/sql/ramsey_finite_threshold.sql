-- SQLite with JSON support. Bind integers 1<=r,n,mu and 0<=cap<=62.
WITH RECURSIVE
sizes(m) AS (SELECT 0 UNION ALL SELECT m+1 FROM sizes WHERE m<:cap),
colors(c) AS (SELECT 0 UNION ALL SELECT c+1 FROM colors WHERE c+1<:mu),
-- Enumerate subsets once by adding vertices in increasing order.
sub(mask,k,lo) AS (
  SELECT 0,0,0 UNION ALL
  SELECT mask | (1 << i.m), k+1, i.m+1 FROM sub JOIN sizes i
    ON i.m>=lo AND i.m<:cap WHERE k<max(:r,:n)
),
edges(e,j) AS (
  SELECT mask, row_number() OVER (ORDER BY mask)-1 FROM sub WHERE k=:r
),
-- Each path assigns exactly one color to each r-subset of [m].
paint(m,j,assignment) AS (
  SELECT m,0,'[]' FROM sizes WHERE m>=:n UNION ALL
  SELECT p.m,p.j+1,json_insert(p.assignment,'$[#]',c.c)
  FROM paint p JOIN edges e ON e.j=p.j AND e.e<(1 << p.m) CROSS JOIN colors c
),
bad(m) AS (
  SELECT p.m FROM paint p
  WHERE NOT EXISTS (SELECT 1 FROM edges e WHERE e.j=p.j AND e.e<(1 << p.m))
    AND NOT EXISTS (
      SELECT 1 FROM sub s WHERE s.k=:n AND s.mask<(1 << p.m)
        AND (SELECT count(DISTINCT json_extract(p.assignment,'$['||e.j||']'))
             FROM edges e WHERE (e.e & s.mask)=e.e)<=1
    )
)
SELECT min(m) AS least_forcing_size FROM sizes
WHERE m>=:n AND m NOT IN (SELECT m FROM bad);
