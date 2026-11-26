"""Freeze one red header, transport an ordered red pair inside its red neighborhood. Never enumerate four-vertex subsets. Scope: SRG(16,6,2,2); blue-five exclusion follows by common-neighbor incidence."""
import itertools,json
from ramsey_retention_slice import D
V=list(itertools.product(range(4),repeat=2));out={}
for name in ('rook','Shrikhande'):
 nb={i:{j for j,(u,v) in enumerate(V) if i!=j and ((x==u or y==v) if name=='rook' else ((u-x)%4,(v-y)%4) in {(0,1),(0,3),(1,0),(3,0),(1,1),(3,3)})} for i,(x,y) in enumerate(V)};assert all(len(n)==6 for n in nb.values()) and all(len(nb[i]&nb[j])==2 for i,j in itertools.combinations(nb,2));hist={}
 for h,L in nb.items():
  unseen={(i,j) for i in L for j in nb[i]&L};periods=[]
  while unseen:
   start=min(unseen);p=start;n=0
   while p in unseen:
    unseen.remove(p);i,j=p;k,=(nb[j]&L)-{i};p=(j,k);n+=1
   assert p==start;periods.append(n)
  key=','.join(map(str,sorted(periods)));hist[key]=hist.get(key,0)+1
 out[name]=hist
assert 30**2>11*(30+2*20);print(out);(D.parent/'ramsey_marked_header_transport.json').write_text(json.dumps(out,indent=1)+'\n')
