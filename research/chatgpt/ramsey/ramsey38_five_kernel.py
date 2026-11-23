"""Derive (not seed) all size <=5 inclusion-minimal supports: branch only on vertices of a shortest still-unhit independent seven, pruning red conflicts in either graph. After finding forced anchors, independently project the original rows and count by exact small transversals. Repeat at both deletions and all starts."""
from ramsey38_matching_continuations import data,C,J,ls,V,D,json
from functools import reduce
from operator import and_
from itertools import combinations

def solve(i,j,x):
 H=data[i][0];h,_,T=data[j];m=1<<x|1<<7;T=[t for t in T if not t&m];ban=[a|b for a,b in zip(H,h)];seen=set();hits=set()
 def visit(s,avail):
  if s in seen:return
  seen.add(s);openrows=[q&avail for q in T if not q&s];
  if not openrows:hits.add(s);return
  if s.bit_count()==5:return
  for k in ls(min(openrows,key=lambda r:(r.bit_count(),r))):visit(s|1<<k,avail&~(1<<k|ban[k]))
 visit(0,((1<<27)-1)&~m);M=sorted(v for v in hits if not any(w!=v and w&v==w for w in hits));p=reduce(and_,M);U=((1<<27)-1)&~(m|p)
 for k in ls(p):U&=~ban[k]
 R={t&U for t in T if not t&p};R=sorted(r for r in R if not any(q!=r and q&r==q for q in R));ext={};F=set();
 for s in M:
  ext[s]=[k for k in V if not ((s|m)>>k&1 or ban[k]&s)];assert s.bit_count() in (4,5);F.update([s] if s.bit_count()==5 else [s|1<<k for k in ext[s]])
 chk=set()
 for a in combinations(ls(U),5-p.bit_count()):
  s=p|sum(1<<k for k in a)
  if all(s&r for r in R) and not any(s&ban[k] for k in a):chk.add(s)
 assert chk==F and not F.intersection([h[x]&~m,h[7]&~m]);return dict(original_rows=len(T),anchors=ls(p),projected_minimal_rows=list(map(ls,R)),kernels=[dict(support=ls(s),fifth_choices=ext[s] if s.bit_count()==4 else None) for s in M],total=len(F))
if __name__=='__main__':
 run=[dict(start=i,deleted=[x,7],outputs=[solve(i,j,x) for j in (C[i],J[i])]) for i in range(8) for x in (1,2)];assert all(sorted(o['total'] for o in z['outputs'])==[3,5] for z in run);print(run[0]);(D/'ramsey38_five_kernel.json').write_text(json.dumps(run,indent=2)+'\n')
