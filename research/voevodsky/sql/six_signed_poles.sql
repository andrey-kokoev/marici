-- SQLite, fresh database. The signed axis code determines the antipode.
CREATE TABLE pole (
  role TEXT PRIMARY KEY NOT NULL,
  code INTEGER NOT NULL UNIQUE CHECK (code IN (-3,-2,-1,1,2,3))
);
INSERT INTO pole VALUES ('product',1), ('customer',-1), ('approved',2),
  ('blocked',-2), ('interested',3), ('explicitly_ignoring',-3);

SELECT a.role AS src, b.role AS dst,
       CASE WHEN b.code = -a.code THEN 'join' ELSE 'antijoin' END AS relation
FROM pole AS a CROSS JOIN pole AS b;

SELECT a.role AS src, b.role AS dst
FROM pole AS a JOIN pole AS b ON b.code = -a.code;
