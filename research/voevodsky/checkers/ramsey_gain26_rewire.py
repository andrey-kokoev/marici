"""Two-vertex block resampling at fixed order 26. No endpoint data or symmetry. Remove both rows and redraw all incident edges, not monotonically augmenting a sparse parent. Sample one uniform legal replacement other than current conditional on chosen pair. Pool checkpoints by canonical graph. Rank via exact largest-blue-clique screen."""
import sys,json,random,itertools,subprocess,collections
import igraph as ig
from ramsey_retention_slice import D,decode,check
P=D.parent;rng=random.Random(260081);F=(1<<26)-1;seeds=[decode(s) for s in (P/'ramsey38_26_e73_hog.g6').read_text().splitlines()];pool={};moves=0
for i,a in enumerate(seeds):
 a=a[:]
 for step in range(1,25):
  u,v=rng.sample(range(26),2);keep=F^(1<<u|1<<v);I=[0]
  for j,g in enumerate(a):
   if keep>>j&1:I.extend([t|1<<j for t in I if not t&g]);
  seven=[s for s in I if s.bit_count()==7];six=[s for s in I if s.bit_count()==6];H=[s for s in I if all(s&q for q in seven)];miss=[sum(1<<j for j,q in enumerate(six) if not q&s) for s in H];old=(a[u]&keep,a[v]&keep,(a[u]>>v)&1);opts=[(s,t,b) for j,s in enumerate(H) for k,t in enumerate(H) for b in (0,1) if (not (s&t) if b else not (miss[j]&miss[k])) and (s,t,b)!=old]
  if not opts:continue
  s,t,b=rng.choice(opts);moves+=1;a[u]=s|b<<v;a[v]=t|b<<u
  for j in range(26):
   if keep>>j&1:a[j]=(a[j]&keep)|((s>>j&1)<<u)|((t>>j&1)<<v)
  if step%4==0:
   assert check(a,F,3,8);g=ig.Graph(26,[(x,y) for x in range(26) for y in range(x) if a[x]>>y&1]);key=tuple(sorted(tuple(sorted(e)) for e in g.permute_vertices(g.canonical_permutation()).get_edgelist()));pool.setdefault(key,dict(seed=i,step=step,adj=a[:],edges=len(key)))
rs=list(pool.values());pending=rs
for k in range(4,9):
 if not pending:break
 vals=subprocess.check_output([sys.argv[1],'7',str(k)],input=''.join(' '.join(map(str,r['adj']))+'\n' for r in pending),text=True).splitlines();surv=[]
 for r,b in zip(pending,vals,strict=True):
  if int(b):r['packing_at_least']=k;surv.append(r)
 pending=surv
print('moves',moves,'types',len(rs),'edges vs packing',collections.Counter((r['edges'],r.get('packing_at_least',0)) for r in rs));(P/'ramsey_gain26_rewire.json').write_text(json.dumps(dict(moves=moves,records=rs))+'\n')
