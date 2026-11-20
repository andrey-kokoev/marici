"""Identify exposed leaves from ONLY the fixed half. A leaf whose two already occupied neighbors are eight steps apart is the stitch guard. Test all eligible oriented pairs as a separate sufficiency control."""
from ramsey_strip_local_stitch import flips,ps,N,s,t,full,fill,Counter

def leaves(p):
    path=(s,)+p+(t,);used=set(path);out=[]
    for v in full-used:
        touched=[i for i,x in enumerate(path) if x in N[v]]
        if len(touched)==2:
            w,=N[v]-used;out.append((touched[1]-touched[0],v,w))
    return sorted(out)
for _,idx,good,bad,_,__,isol,p in flips:
    L=leaves(p);assert [z[0] for z in L]==[6,6,8];_,v,w=L[-1];assert isol==[v] and v not in set(good)|set(bad) and w in bad and w not in good
C=Counter()
for p in ps:
    gs=[(v,w) for d,v,w in leaves(p) if d==8];
    if len(gs)!=1:continue
    v,w=gs[0]
    for q in ps:
        if set(q)&set(p):continue
        ok=fill(frozenset(full-set(p)-set(q)-{s,t}));C[(v not in q and w in q,ok)]+=1
print('8/8 local stitches; wider oriented (strands guard, closes):',C)
