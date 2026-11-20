"""Distinguish containing the four shared incidences from having precisely them shared. Classify identical cores and possible extra agreements across the two rooted Hall orbits."""
from ramsey_strip_witness_orbits import orbits,r,acts,transform,D,M,Counter
from collections import defaultdict
sw=lambda u:frozenset((r[i],r[15+j]-15) for i,j in u);cores={u:u&sw(u) for u in orbits};targets={c for c in cores.values() if len(c)==4};central=[(a,b) for p,a,b in acts if all(a[r[i]]==r[a[i]] for i in range(15))];hist=Counter();seen=set()
for c in sorted(targets,key=lambda v:tuple(sorted(v))):
    options=Counter((orbits[u],len(cores[u])) for u in orbits if c<=u);hist[tuple(sorted(options.items()))]+=1
    if c in seen:continue
    orb={transform(c,a,b) for a,b in central};seen|=orb;assert orb<=targets;fixed=sum(r[i]==i for i,j in c);print('orbit of cores',len(orb),'fixed flags',fixed,'representative',sorted(c),'completions',options)
print('distinct exact cores',len(targets),'containment profiles',hist);assert seen==targets
from itertools import combinations
for c in sorted(targets,key=lambda v:tuple(sorted(v)))[:1]:
 by={k:[cores[u]-c for u in orbits if orbits[u]==k and c<=u] for k in (1,2)};extra=by[2];possible=set.union(*(set(x) for x in extra));hits=[]
 for n in range(1,8):
    hits=[p for p in combinations(sorted(possible),n) if all(set(p)&x for x in extra)]
    if hits:break
 print('example core as pair:partition',[(D[i],M[j]) for i,j in sorted(c)],'137 universally extra',set.intersection(*(set(x) for x in extra)),'least tests hitting every 137 extension',n)
for c in targets:
 us=[u for u in orbits if c==cores[u]];assert len(us)==2 and sw(us[0])==us[1];assert all(cores[u]-c for u in orbits if c<=u and orbits[u]==2)
