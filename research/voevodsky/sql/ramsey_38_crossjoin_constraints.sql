WITH RECURSIVE
vertex(id) AS (
    SELECT u FROM rels UNION SELECT v FROM rels
),
subsets(ids, last, k) AS (
    SELECT json_array(id), id, 1 FROM vertex
    UNION ALL
    SELECT json_insert(s.ids, '$[#]', v.id), v.id, s.k + 1
    FROM subsets AS s JOIN vertex AS v ON v.id > s.last
    WHERE s.k < 8
)
SELECT ids AS vertices,
       CASE k WHEN 3 THEN '+' WHEN 8 THEN '-' END AS forbidden_uniform_sign
FROM subsets
WHERE k IN (3, 8);
