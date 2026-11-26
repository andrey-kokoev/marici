"""Predecessor-only predictors in increasing combinatorial order. No score fitted. Compare blind calls to saved verdicts only after computing them."""
import json,itertools,collections
from pathlib import Path
from fractions import Fraction
P=Path(__file__).resolve().parents[1]/'results';out=[]
for i,r in enumerate(json.loads((P/'ramsey_anchor_release36.json').read_text())[1:]):
 a=r['core'];I=[0]
 for j,v in enumerate(a):I.extend([s|1<<j for s in I if not s&v])
 S=[s for s in I if all(s&(v|1<<j) for j,v in enumerate(a))];Q=[q for q in I if q.bit_count()==4];M=[sum(1<<j for j,q in enumerate(Q) if not q&s) for s in S];N=len(S);margin=4*max(len(Q)-m.bit_count() for m in M)-3*len(Q);G=[{j for j in range(i,N) if not m&M[j]} for i,m in enumerate(M)];w=[]
 for u,gu in enumerate(G):
  for v in gu:
   both=gu&G[v]
   for t in both:
    for l in both&G[t]:w.append([S[j] for j in (u,v,t,l)])
 free=[(u,v) for u in range(len(a)) for v in range(u) if not(a[u]>>v&1 or a[u]&a[v])];out.append(dict(row=i,addable_edges=free,edges=sum(v.bit_count() for v in a)//2,fours=len(Q),margin=margin,compatible_fours=len(w),example=w[:1],legal=r['best'] is not None));
print([(r['edges'],r['fours'],r['margin'],r['compatible_fours'],r['legal']) for r in out]);(P/'ramsey_rank12.json').write_text(json.dumps(out)+'\n')
# Post-hoc separator on order 12; freeze at four for the neighboring order, same thresholds and four support rows.
other=[r for r in json.loads((P/'ramsey_frontier_transfer.json').read_text()) if r['n']==11 and r['d']==4];tab=collections.Counter()
for r in other:
 a=r['core'];f=sum(not(a[i]>>j&1 or a[i]&a[j]) for i in range(len(a)) for j in range(i));tab[f>=4,r['full']]+=1
print('order11',tab);(P/'ramsey_rank12_transfer.json').write_text(json.dumps([dict(predicted=x,actual=y,count=c) for (x,y),c in sorted(tab.items())])+'\n')
