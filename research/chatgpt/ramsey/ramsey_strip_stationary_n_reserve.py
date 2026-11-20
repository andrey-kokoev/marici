"""Test whether the fixed N column names the moving residue before the route. Generate all ten strips directly on the folded prism, group by row-derived N fan, and measure first unique residue among all candidates sharing a visit prefix."""
from itertools import combinations
from collections import Counter
from ramsey_strip_prism_proof import X,P,T,ext,E,V
rows=('BRNN','BNRN');B=rows[0].index('B');R,S=(w.index('R') for w in rows);Q,=set(range(4))-{B,R,S};e=lambda x,y:X.index(tuple(sorted((x,y))));pair=lambda x,y:tuple(sorted((x,y)));fan=lambda x:P.index(pair(e(x,R),e(x,S)));qmid,=ext[fan(Q)];start,=ext[fan(B)];d0,d1=(pair(e(B,k),e(j,Q)) for k,j in [(R,S),(S,R)]);last=pair(*(set(range(6))-set(d0+d1)));pole=15+T.index(tuple(sorted((d0,d1,last))));end,=ext[pole];cand=[]
def grow(p):
 if p[-1]==end:
    if len(p)==10:
        rem=tuple(sorted(V-set(p)));cand.append((p,rem,rem in E))
    return
 if len(p)==10:return
 for x in sorted(V-set(p)):
    if tuple(sorted((p[-1],x))) in E:grow(p+(x,))
grow((start,));assert len(cand)==len({u for _,u,_ in cand})==10 and sum(ok for _,_,ok in cand)==6
assert not set.intersection(*(set(u) for _,u,ok in cand if ok));print('N fan',fan(Q),qmid,'contains N midpoint / closes',Counter((qmid in u,ok) for _,u,ok in cand));print('first uniquely predictive prefix length',Counter(min(i for i in range(11) if len({v for q,v,_ in cand if q[:i]==p[:i]})==1) for p,_,_ in cand));print('success residues:',[u for p,u,ok in cand if ok])
