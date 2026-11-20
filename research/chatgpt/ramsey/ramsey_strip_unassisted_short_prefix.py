"""Infer all candidate cyclic frames from actual growing short-route flags, without preselecting the source matching's symmetric orbit. Measure residual information still needed."""
from itertools import combinations
from ramsey_strip_intrinsic_fivefold_transport import records,groups,action,moved
from ramsey_strip_minimal_shared_constraints import allms
from ramsey_strip_matching_restart import r
base=[0,16,13,19,7,29];GS=list(groups)
allflags=set().union(*(m for _,_,m,_,_,_ in records));closure={(G,e):frozenset().union(*(moved({e},action(p)) for p in G)) for G in GS for e in allflags}
def infer(obs):
 result=[]
 for G in GS:
    u=frozenset().union(*(closure[G,e] for e in obs))
    if len(u)==len({i for i,j in u})==len({j for i,j in u}):result.append(G)
 return result
for n,o,m,true,_,_ in records:
 p=base if o==0 else [r[v] for v in base];obs=set();trace=[]
 for i,(a,b) in enumerate(zip(p,p[1:])):
    if i%2:a,b=r[a],r[b]
    obs.add(tuple(sorted((a,b))));trace.append((len(infer(obs)),sum(obs<=M for M in allms)))
 for k in range(11):
    cert=[extra for extra in combinations(sorted(m-obs),k) if infer(obs|set(extra))==[true] and sum(obs|set(extra)<=M for M in allms)==1]
    if cert:break
 print('source',n,o,'(candidate groups, perfect matchings) by route step',trace,'minimum additional residual flags',k,'certificates',len(cert))
