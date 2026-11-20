-- SQLite. R(red triangle, blue K4): paired lower and upper certificates.
-- Lower: on Z/8 color the cycle edges and opposite pairs red, all others blue.
-- Upper: in an avoiding K9 a red neighborhood is blue-complete (so size <=3).
-- A blue neighborhood avoids both red and blue triangles (so size <=5 by the
-- independent exhaustive six-vertex check below). Hence every red degree is 3,
-- impossible since the sum of degrees in an undirected graph is even.
WITH RECURSIVE
v(i) AS (VALUES(0) UNION ALL SELECT i+1 FROM v WHERE i<7),
e(a,b,r) AS (SELECT a.i,b.i,(b.i-a.i IN(1,4,7)) FROM v a JOIN v b ON a.i<b.i),
tri8(a,b,c,red) AS (SELECT x.a,x.b,y.b,x.r+y.r+z.r AS red FROM e x JOIN e y ON x.b=y.a
         JOIN e z ON z.a=x.a AND z.b=y.b),
lower_ok(ok) AS (SELECT NOT EXISTS(SELECT 1 FROM tri8 WHERE red=3) AND NOT EXISTS(
  SELECT 1 FROM tri8 t JOIN e x ON x.a=t.a JOIN e y ON y.a=t.b AND y.b=x.b
  JOIN e z ON z.a=t.c AND z.b=x.b WHERE t.red=0 AND x.r+y.r+z.r=0)),
-- Assign one bit to each edge of K6; enumerate every red edge mask.
f(a,b,bit) AS (SELECT a,b,1<<(b*(b-1)/2+a) FROM e WHERE b<6),
tri6(mask) AS (SELECT x.bit|y.bit|z.bit FROM f x JOIN f y ON x.b=y.a
               JOIN f z ON z.a=x.a AND z.b=y.b),
colors(m) AS (VALUES(0) UNION ALL SELECT m+1 FROM colors WHERE m<32767),
local_ok(ok) AS (SELECT NOT EXISTS(SELECT 1 FROM colors WHERE NOT EXISTS(
    SELECT 1 FROM tri6 WHERE (m&mask) IN (0,mask)))),
degrees(d) AS (SELECT i FROM v UNION ALL SELECT 8),
possible(d) AS (SELECT d FROM degrees WHERE d<4 AND (8-d<6 OR NOT (SELECT ok FROM local_ok))),
upper_ok(ok) AS (SELECT count(*)=1 AND (9*min(d))%2=1 FROM possible)
SELECT lower_ok.ok AS avoiding_K8_verified,local_ok.ok AS K6_neighborhood_bound_verified,
       upper_ok.ok AS K9_impossible,CASE WHEN lower_ok.ok AND upper_ok.ok THEN 9 END AS R_3_4
FROM lower_ok,local_ok,upper_ok;
