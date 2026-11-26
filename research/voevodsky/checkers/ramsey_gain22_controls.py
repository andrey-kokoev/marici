"""All 22-core controls: fixed four-neighborhood feasibility via ordered clique intersections, allowing repeats. Check a full endpoint for every positive. Rank by the prior individually red-addable edge score, without labels or endpoints."""
import json,itertools,collections
from ramsey_retention_slice import CAT,D,decode,check
P=D.parent;out=[]
for idx,line in enumerate((CAT/'r37_22.g6').read_text().splitlines()):
 a=decode(line);n=len(a);I=[0]
 for i,v in enumerate(a):I.extend([q|1<<i for q in I if not q&v])
 S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];Q=[[q for q in I if q.bit_count()==k] for k in (4,5,6)];m4,m5,m6=[[sum(1<<j for j,q in enumerate(qs) if not q&s) for s in S] for qs in Q];G=[sum(1<<j for j in range(i,len(S)) if not m&m6[j]) for i,m in enumerate(m6)];counts=[0]*3;w=None
 def ids(mask):
  while mask:b=mask&-mask;mask^=b;yield b.bit_length()-1
 for i,adj in enumerate(G):
  for j in ids(adj):
   ij=adj&G[j];p=m5[i]&m5[j]
   for k in ids(ij):
    cand=ij&G[k];counts[0]+=cand.bit_count()
    if not cand or p&m5[k]:continue
    ban=p|((m5[i]|m5[j])&m5[k]);four=m4[i]&m4[j]&m4[k]
    for l in ids(cand):
     if ban&m5[l]:continue
     counts[1]+=1
     if four&m4[l]:continue
     counts[2]+=1
     if w is None:w=[S[t] for t in (i,j,k,l)]
 if w:
  g=a.copy()+[0]*5
  for j,t in enumerate(w,n):
   g[j]=t|1<<26;g[26]|=1<<j
   for i in ids(t):g[i]|=1<<j
  assert check(g,(1<<27)-1,3,8)
 sc=sum(not(a[i]>>j&1 or a[i]&a[j]) for i in range(n) for j in range(i));out.append(dict(row=idx,score=sc,counts=counts,witness=w))
print(sorted(collections.Counter((r['score'],bool(r['witness'])) for r in out).items()));print('survivors',*[sum(r['counts'][k]>0 for r in out) for k in range(3)]);(P/'ramsey_gain22_controls.json').write_text(json.dumps(out)+'\n')
