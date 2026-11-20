"""Compare affine flag types of all three short fillings, including the previously omitted accumulated filling. Test inverse-ring reflection as an actual matching symmetry."""
from collections import Counter
from ramsey_strip_intrinsic_fivefold_transport import symmetry,action,moved,I,P,T
from ramsey_strip_unbiased_three_constraints import selected,allms,ms
for n,pair in enumerate(selected,1):
 m=allms[pair[0]];G,hub=symmetry(m);g=min(p for p in G if p!=I);ring=[min(set(I)-{hub})]
 for _ in range(4):ring.append(g[ring[-1]])
 c={x:i for i,x in enumerate(ring)};hist=Counter();orient=[]
 for d,j in m:
  x,y=P[d]
  if hub in (x,y):hist['hub selected']+=1;continue
  block,=[p for p in T[j-15] if hub in p];z,=set(block)-{hub}
  if (c[x]+c[y]-2*c[z])%5==0:hist['midpoint']+=1
  else:
   hist['nonmidpoint']+=1
   if (2*c[y]-c[x]-c[z])%5:x,y=y,x
   orient.append((x,y))
 reflection=list(I)
 for x,i in c.items():reflection[x]=ring[-i%5]
 print('filling',n,'accumulated',set(ms)=={allms[j] for j in pair},'hub',hub,'flag types',dict(hist),'reflection preserves matching',moved(m,action(reflection))==m,'nonmidpoint step counts',dict(Counter((c[y]-c[x])%5 for x,y in orient)))
