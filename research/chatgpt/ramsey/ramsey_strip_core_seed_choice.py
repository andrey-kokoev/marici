"""Locate the free core bit in local seed data. Generate the full quarter-turn orbit of each link and inspect the two maximal cores' active half routes."""
from ramsey_strip_rotation_retained_core import best,cores,image,f,allms
from ramsey_strip_matching_restart import turn,P,T
for n,m in enumerate(best,1):
    c=cores[m];anchor={(9,15)};assert anchor<=c and image(anchor,f)==anchor
    for e in c-anchor:
        orbit=frozenset({e});step=frozenset({e})
        for _ in range(3):step=image(step,f);orbit|=step
        assert len(orbit)==4 and orbit|anchor==c
    diff=m^turn(m);adj={}
    for x,y in diff:adj.setdefault(x,set()).add(y);adj.setdefault(y,set()).add(x)
    p=[0,16]
    while True:
        x,=adj[p[-1]]-{p[-2]}
        if x==p[0]:break
        p.append(x)
    print('candidate',n,'cycle through entry',p,'seed-link orbit',sorted(c-anchor))
    print('entries of both cycle vertex sets include exit pole?',29 in p)
