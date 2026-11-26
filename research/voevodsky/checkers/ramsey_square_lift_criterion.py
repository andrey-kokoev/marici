"""For two red diagonals, a cyclic square lift fails exactly if its untouched exterior contains an independent (k-3)-set. Exhaust local gadget table, directly cross-check actual endpoints on small layers and classify full 16 and 22 layers by criterion."""
import itertools,json,collections,gzip
from ramsey_retention_slice import CAT,D,decode,check,has
P=D.parent
red={tuple(sorted(e)) for e in [(0,2),(1,3)]+[(8,4+i) for i in range(4)]+[(4+i,(i-h)%4) for i in range(4) for h in (1,2)]};tab=[]
for m in range(16):
 corners=[i for i in range(4) if m>>i&1];vs=corners+[4+i for i in corners]+[8];best=max(len(s) for j in range(len(vs)+1) for s in itertools.combinations(vs,j) if not any(e in red for e in itertools.combinations(s,2)));base=len({i%2 for i in corners});assert best==base+1+(m==15);tab.append([base,best])
def audit(gs,k,direct):
 hist=collections.Counter();sample=None
 for a in gs:
  n=len(a);F=(1<<n)-1;g=[sum(1<<j for j in range(n) if j!=i and not(v>>j&1 or v&a[j])) for i,v in enumerate(a)]
  for u in range(n):
   for w in range(u+1,n):
    common=g[u]&g[w];ns=[i for i in range(u+1,n) if common>>i&1]
    for v,x in itertools.combinations(ns,2):
     c=(u,v,w,x)
     if not(a[u]>>w&1 and a[v]>>x&1):hist['other_diagonals']+=1;continue
     mask=sum(1<<i for i in c);U=F&~(mask|a[u]|a[w]|a[v]|a[x]);bad=has([~t for t in a],U,k-3);hist['fail' if bad else 'pass']+=1
     if bad and sample is None:sample=dict(core=a,cycle=c,exterior_mask=U)
     if direct:
      b=list(a)+[0]*5
      for i in range(4):
       h=n+i;t=a[c[(i+2)%4]]|1<<c[(i+1)%4];b[h]=t|1<<(n+4);b[-1]|=1<<h
       for j in range(n):b[j]|=(t>>j&1)<<h
      assert check(b,(1<<(n+5))-1,3,k+1)==(not bad)
 return dict(counts=hist,failed_example=sample)
small=json.loads((P/'ramsey_frontier_transfer.json').read_text());res={}
for n in (10,11,12):res[n]=audit([list(t) for t in {tuple(r['core']) for r in small if r['n']==n}],5,True)
res[16]=audit([decode(s.strip()) for s in gzip.open(CAT.parent/'r36_16.g6.gz','rt')],6,False);res[17]=audit([decode(s) for s in (CAT/'r36_17.g6').read_text().splitlines()],6,True);res[22]=audit([decode(s) for s in (CAT/'r37_22.g6').read_text().splitlines()],7,True);print({n:dict(q['counts']) for n,q in res.items()});(P/'ramsey_square_lift_criterion.json').write_text(json.dumps(dict(table=tab,layers=res))+'\n')
