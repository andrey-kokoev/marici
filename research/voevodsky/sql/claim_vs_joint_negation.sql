-- Fully answered claims only. 1 = confirmed; 0 = negated.
WITH sign(v) AS (VALUES (1),(0)),
pair(a,b) AS (SELECT x.v,y.v FROM sign x CROSS JOIN sign y),
r AS (
 SELECT a,b, ((a OR NOT b) AND (b OR NOT a)) AS false_forces_other_false,
        NOT (a AND b) AS exclusion_ok, a=b AS agree, a AND b AS joint_success
 FROM pair
)
SELECT a,b,false_forces_other_false,exclusion_ok,agree,
       false_forces_other_false AND exclusion_ok AND agree AS claims_allowed,
       joint_success FROM r ORDER BY a DESC,b DESC;
