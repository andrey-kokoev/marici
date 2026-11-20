"""Examine whole five-flag orbits directly, including their completions and induced directed generators. Avoid repeating the subset certificate search."""
from ramsey_strip_intrinsic_fivefold_transport import records,groups,moved,action
from ramsey_strip_asymmetric_generator import directed
from ramsey_strip_minimal_shared_constraints import allms
for n,o,m,G,candidates,correct in records:
    orbits={frozenset().union(*(moved({e},action(p)) for p in G)) for e in m};g,hub=directed(m)
    for orb in sorted(orbits,key=lambda s:sorted(s)):
        compatible=[]
        for H in groups:
            forced=frozenset().union(*(moved(orb,action(p)) for p in H))
            if len(forced)==len({i for i,j in forced})==len({j for i,j in forced}):compatible.append(H)
        completions=[M for M in allms if orb<=M]
        if len(compatible)!=1:continue
        assert len(completions)==2
        other,=[M for M in completions if M!=m];g2,h2=directed(other);assert hub==h2 and moved(other,action(g))==other
        power=tuple(range(6));exponent=None
        for k in range(1,5):
            power=tuple(g[x] for x in power)
            if power==g2:exponent=k
        print('source',n,o,'observed orbit',sorted(orb),'changed flags per completion',len(m-other),'other generator power',exponent)
