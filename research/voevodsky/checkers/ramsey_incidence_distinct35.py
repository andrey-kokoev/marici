"""Orbit-cover enumeration for the simple 22-pair / 4-triple balanced template. No singleton masks, no repeated masks, fixed-point-free involution on labels and vertices. Classify up to commuting label relabelings; test both equivariant and unrestricted red completions."""
from ramsey_incidence_first35 import P,solve,swap
import itertools,json,collections
orbit=lambda n:sorted([s for s in range(256) if s.bit_count()==n and s<swap(s)])
perms=[[2*p[i//2]+((i&1)^((f>>(i//2))&1)) for i in range(8)] for p in itertools.permutations(range(4)) for f in range(16)];lookup=[[sum(1<<t[i] for i in range(8) if s>>i&1) for s in range(256)] for t in perms];groups={};raw=0
for skip in orbit(2):
 for x,y in itertools.combinations(orbit(3),2):
  m=[j for s in [s for s in orbit(2) if s!=skip]+[x,y] for j in [s,swap(s)]]
  if any(sum(s>>i&1 for s in m)!=7 for i in range(8)):continue
  raw+=1;k=min(tuple(sorted(t[s] for s in (skip,swap(skip))))+tuple(sorted(t[s] for s in (x,swap(x),y,swap(y)))) for t in lookup);groups.setdefault(k,m)
out=[]
for m in groups.values():
 z=solve(m);y=solve(m,False) if z['status']!='forced_blue' else z;out.append(dict(masks=m,symmetric=z,unrestricted=y))
(P/'ramsey_incidence_distinct35.json').write_text(json.dumps(dict(raw=raw,cases=out))+'\n');print(raw,len(groups),collections.Counter((z['symmetric']['status'],z['unrestricted']['status']) for z in out));print([(z['symmetric'].get('models'),z['unrestricted'].get('models')) for z in out])
