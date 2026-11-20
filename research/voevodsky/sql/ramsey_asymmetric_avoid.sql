-- SQLite fixed-order decision query. Bind :n (2..62), :red and :blue (>=2).
-- Returns one avoiding coloring (bits in colex edge order), or no rows if
-- exhaustion proves none exists. Cancellation is NOT exhaustion.
WITH RECURSIVE
v(i) AS (VALUES(0) UNION ALL SELECT i+1 FROM v WHERE i+1<:n),
color(bit,target) AS (VALUES('1',:red),('0',:blue)),
search(a,b,s) AS (
  VALUES(0,1,'')
  UNION ALL
  SELECT CASE WHEN a+1=b THEN 0 ELSE a+1 END,
         b+(a+1=b), s||bit
  FROM search CROSS JOIN color
  WHERE b<:n AND NOT EXISTS (
    -- A newly completed forbidden clique must contain the new edge (a,b).
    -- Its other vertices must be <a: edges (i,b) with i>a are not set yet.
    WITH RECURSIVE clique(lo,used,k) AS (
      VALUES(0,0,0) UNION ALL
      SELECT x.i+1, used|(1<<x.i), k+1 FROM clique CROSS JOIN v x
      WHERE k<target-2 AND x.i>=lo AND x.i+target-2-k<=a
        AND substr(s,1+a*(a-1)/2+x.i,1)=bit
        AND substr(s,1+b*(b-1)/2+x.i,1)=bit
        AND NOT EXISTS (SELECT 1 FROM v y WHERE (used & (1<<y.i))!=0
             AND substr(s,1+x.i*(x.i-1)/2+y.i,1)!=bit)
    ) SELECT 1 FROM clique WHERE k=target-2
  ) ORDER BY 2 DESC,1 DESC
)
SELECT s AS avoiding_coloring FROM search WHERE b=:n LIMIT 1;
