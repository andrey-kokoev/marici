"""An interval-link obstruction independent of shellability and interior vertices."""
from ramsey38_global_shell import N,audit,fmt
from ramsey38_compare_support_fillings import boundary
from ramsey38_support_ball_completion import shelling

root=7
rows={v:frozenset(N[root]&n) for v,n in N.items() if v not in N[root]|{root}}
boundaries,_=audit(root)
assert len(boundaries)==2
edge=rows[18]; t=rows[23]; u=rows[4]
assert edge==t&u=={6,21}
# Positive controls: retaining row 4 alone works on each boundary.
controls=[[(6,11,13,27),(6,9,21,27),(3,6,11,21),(3,11,13,21),(6,13,21,27),(6,11,13,21)],
          [(6,9,11,21),(9,11,21,27),(3,6,11,13),(3,6,13,21),(11,13,21,27),(6,11,13,21)]]
seen=set()
for cells in controls:
    ts=set(map(frozenset,cells));assert u in ts and t not in ts and shelling(ts);seen.add(boundary(ts))
assert seen==boundaries
for bd in boundaries:
    # Cone from vertex 3 over the opposite boundary triangles: row 23 alone.
    ts={f|{3} for f in bd if 3 not in f};assert t in ts and u not in ts and boundary(ts)==bd and shelling(ts)
    ends=set.union(set(),*(f-edge for f in bd if edge<=f))
    assert ends==t-edge=={3,9} and (u-edge).isdisjoint(ends)
    print('boundary triangles at',sorted(edge),fmt(f for f in bd if edge<=f), 'forced link edges',fmt((t-edge,u-edge)))
