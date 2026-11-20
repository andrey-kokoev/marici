"""Infer C5 from partial flags by requiring its orbit closure to remain a partial matching, not to agree with a known completion. Minimum certificate sizes are measured on known matchings only afterward."""
from itertools import combinations
from ramsey_strip_intrinsic_fivefold_transport import records,groups,action,moved
GS=list(groups);closures={}
for G in GS:
 for e in {(i,j) for _,_,m,_,_,_ in records for i,j in m}:
    closures[G,e]=frozenset().union(*(moved({e},action(p)) for p in G))
def infer(obs):
 ans=[]
 for G in GS:
    forced=frozenset().union(*(closures[G,e] for e in obs))
    if len(forced)==len({x for x,y in forced})==len({y for x,y in forced}):ans.append(G)
 return ans
certificate_records=[]
for n,o,m,true,candidates,correct in records:
 for k in range(1,9):
    cert=[c for c in combinations(sorted(m),k) if infer(c)==[true]]
    if cert:break
 assert cert
 certificate_records.append((n,o,m,true,cert))
 boundary=tuple(e for e in m if 0 in e or 29 in e)
 print('source',n,o,'minimum flags identifying subgroup',k,'certificates',len(cert),'boundary-only groups',len(infer(boundary)),'example',cert[0])
