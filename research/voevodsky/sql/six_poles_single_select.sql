SELECT s.key AS src, d.key AS dst,
       CASE WHEN (s.value ->> 0) = -(d.value ->> 0)
             AND (s.value ->> 1) = -(d.value ->> 1)
             AND (s.value ->> 2) = -(d.value ->> 2)
            THEN 'join' ELSE 'antijoin' END AS relation
FROM product p CROSS JOIN customer c CROSS JOIN approved a
CROSS JOIN blocked b CROSS JOIN interested i CROSS JOIN explicitly_ignoring e
CROSS JOIN json_each(json_object(
    'product', json_array(p.x,p.y,p.z), 'customer', json_array(c.x,c.y,c.z),
    'approved', json_array(a.x,a.y,a.z), 'blocked', json_array(b.x,b.y,b.z),
    'interested', json_array(i.x,i.y,i.z), 'explicitly_ignoring', json_array(e.x,e.y,e.z)
)) s
CROSS JOIN json_each(json_object(
    'product', json_array(p.x,p.y,p.z), 'customer', json_array(c.x,c.y,c.z),
    'approved', json_array(a.x,a.y,a.z), 'blocked', json_array(b.x,b.y,b.z),
    'interested', json_array(i.x,i.y,i.z), 'explicitly_ignoring', json_array(e.x,e.y,e.z)
)) d
ORDER BY src, dst;
