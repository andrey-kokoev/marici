"""All seven-compatible five-panels on the blind walk pool. Count survivors at each lower demand. For rejected panels record smallest total forbidden core-clique/newcomer-subset count for the core, with witness. Inclusion-maximal red supports suffice by monotonicity."""
import itertools,json,collections,math
import igraph as ig
from ramsey_retention_slice import D,check
P=D.parent;rows=json.loads((P/'ramsey_gain26_rewire.json').read_text())['records'];out=[]
for idx,r in enumerate(rows):
 if r['packing_at_least']<5:continue
 a=r['adj'];I=[0]
 for j,v in enumerate(a):I.extend([t|1<<j for t in I if not t&v]);
 S=[t for t in I if all(t&(1<<i|v) for i,v in enumerate(a))];Q={k:[q for q in I if q.bit_count()==k] for k in range(4,8)};M={k:[sum(1<<j for j,q in enumerate(qs) if not q&s) for s in S] for k,qs in Q.items()};assert all(M[7]);g=ig.Graph(len(S),[(i,j) for i,m in enumerate(M[7]) for j in range(i) if not m&M[7][j]]);panels=g.cliques(min=5,max=5);counts=[len(panels),0,0,0];best=None;wb=None;profile=None
 for p in panels:
  bad=[]
  for k in (6,5,4):
   total=0
   for sub in itertools.combinations(p,9-k):
    m=M[k][sub[0]]
    for j in sub[1:]:m&=M[k][j]
    total+=m.bit_count()
   bad.append(total)
   if not any(bad):counts[7-k]+=1
  if best is None or sum(bad)<best:best=sum(bad);wb=[S[i] for i in p];profile=bad
 assert wb
 b=a[:]+[0]*6
 for j,s in enumerate(wb,26):
  b[j]=s|1<<31;b[31]|=1<<j
  for i in range(26):b[i]|=(s>>i&1)<<j
 assert check(b,(1<<32)-1,3,9)==(best==0);out.append(dict(idx=idx,seed=r['seed'],step=r['step'],edges=r['edges'],seven_score=r['packing_at_least'],counts=counts,min_nines=best,best_profile=profile,rows=wb))
print('counts',list(map(sum,zip(*(r['counts'] for r in out)))),'cores',list(map(sum,zip(*([bool(x) for x in r['counts']] for r in out)))),'best histogram',collections.Counter(r['min_nines'] for r in out));(P/'ramsey_gain26_verify_five.json').write_text(json.dumps(out)+'\n')
