-- SQLite, one fixed legal and fully signed prefix, vertices numbered 0..61.
-- vertex(id); edge(u,v,sign), exactly one +/- row per unordered pair, u<v.
CREATE TABLE blocker (
    kind TEXT NOT NULL CHECK(kind IN ('contains','misses')),
    mask INTEGER NOT NULL,
    PRIMARY KEY(kind,mask)
) WITHOUT ROWID;
INSERT INTO blocker
SELECT 'contains', (1 << u) | (1 << v) FROM edge WHERE sign='+';

-- n.forward is the set of higher-numbered minus neighbors. Intersection
-- keeps exactly the vertices that extend the whole clique. No trial stars.
WITH RECURSIVE
n(id,bit,forward) AS (
  SELECT v.id, 1 << v.id, coalesce(sum(1 << e.v),0)
  FROM vertex v LEFT JOIN edge e ON e.u=v.id AND e.sign='-'
  GROUP BY v.id
),
clique(k,mask,available) AS (
  SELECT 1,bit,forward FROM n
  UNION ALL
  SELECT k+1, mask | bit, available & forward
  FROM clique JOIN n ON (available & bit)<>0
  WHERE k<9
)
INSERT INTO blocker SELECT 'misses',mask FROM clique WHERE k=9;
