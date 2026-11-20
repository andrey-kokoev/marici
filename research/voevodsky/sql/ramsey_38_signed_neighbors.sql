-- nb(v,plus,minus): one row per vertex; vertex 0 uses bit 0. :a,:b is
-- an unassigned edge of a legal partial coloring. Return blocking rule masks.
WITH RECURSIVE
ends(p,m,e) AS (
 SELECT a.plus & b.plus, a.minus & b.minus, (1<<a.v)|(1<<b.v)
 FROM nb a, nb b WHERE a.v=:a AND b.v=:b
),
c(k,s,avail) AS (
 SELECT 0,0,m FROM ends
 UNION ALL
 SELECT k+1,s|(1<<v),avail & minus & ~((1<<v)|((1<<v)-1))
 FROM c JOIN nb ON (avail & (1<<v))<>0 WHERE k<6
)
SELECT '+' AS blocked_sign, e|(1<<v) AS rule_mask FROM ends JOIN nb ON (p&(1<<v))<>0
UNION ALL
SELECT '-', e|s FROM ends JOIN c ON k=6;
