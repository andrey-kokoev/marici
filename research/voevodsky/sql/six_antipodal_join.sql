-- SQLite. Run once in a fresh database. Coordinates encode role names, not business facts.
BEGIN;
CREATE TABLE pole (
  id TEXT PRIMARY KEY NOT NULL,
  x INTEGER NOT NULL, y INTEGER NOT NULL, z INTEGER NOT NULL,
  UNIQUE(x,y,z), CHECK(x IN (-1,0,1) AND y IN (-1,0,1) AND z IN (-1,0,1)
                        AND abs(x)+abs(y)+abs(z)=1)
) WITHOUT ROWID;
INSERT INTO pole VALUES ('product',1,0,0),('customer',-1,0,0),
  ('approved',0,1,0),('blocked',0,-1,0),
  ('interested',0,0,1),('explicitly_ignoring',0,0,-1);

-- Full directed pair domain, including the diagonal. Materialize both halves
-- of the coordinate join. The antijoin is relative to THIS pair domain:
-- anti(src,dst) means that dst is not the antipode of src.
CREATE TABLE pair_index (
  src TEXT NOT NULL, dst TEXT NOT NULL, is_antipode INTEGER NOT NULL CHECK(is_antipode IN (0,1)),
  PRIMARY KEY(src,dst)
) WITHOUT ROWID;
INSERT INTO pair_index
SELECT a.id,b.id,1 FROM pole a JOIN pole b
  ON (b.x,b.y,b.z)=(-a.x,-a.y,-a.z)
UNION ALL
SELECT a.id,b.id,0 FROM pole a CROSS JOIN pole b
WHERE NOT EXISTS (SELECT 1 FROM pole opp WHERE opp.id=b.id
                   AND (opp.x,opp.y,opp.z)=(-a.x,-a.y,-a.z));
CREATE INDEX pair_out ON pair_index(src,is_antipode,dst);
CREATE INDEX pair_in ON pair_index(dst,is_antipode,src);
CREATE VIEW antipodal_join AS SELECT src,dst FROM pair_index WHERE is_antipode=1;
CREATE VIEW antipodal_antijoin AS SELECT src,dst FROM pair_index WHERE is_antipode=0;
COMMIT;
