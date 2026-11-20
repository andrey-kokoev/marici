"""Remove row-mate constraints, then cube or cross-incidence constraints. Domains and boundary/nonreturn prescriptions unchanged. Unresolved domains are not counted as actual solutions."""
from collections import Counter
from ramsey_strip_mixed_cube_exchange import U,V,E,F,cross,r
vertices=U+V
for cube,crosslinks,row in ((True,True,False),(True,False,False),(False,True,False),(True,True,True)):
 def compatible(x,y,a,b):
    if (x==y)!=(a==b):return False
    if row and (r[x]==y)!=(r[a]==b):return False
    if (x in U)==(y in U):return not cube or bool(E(x,y) if x in U else F(x,y))==bool(E(a,b) if a in U else F(a,b))
    return not crosslinks or (cross(x,y) if x in U else cross(y,x))==(cross(a,b) if a in U else cross(b,a))
 D={x:set(V if x in U else U) for x in vertices};D[16]={7};D[7].discard(16);rounds=0
 while True:
    new={x:{a for a in D[x] if all(any(compatible(x,y,a,b) for b in D[y]) for y in vertices if y!=x)} for x in vertices};assert all(new.values())
    if new==D:break
    D=new;rounds+=1
 print('cube,cross,row',cube,crosslinks,row,'rounds',rounds,'domain histogram',dict(Counter(map(len,D.values()))))
 if cube and crosslinks:
    assert all(len(v)==1 for v in D.values());g={x:next(iter(d)) for x,d in D.items()};assert all(g[g[x]]==r[x] for x in vertices)
