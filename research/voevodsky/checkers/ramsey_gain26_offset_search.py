"""Targeted structured inverse construction; no archived endpoint, edge count or successful distances as input. Assume 8 neighbors are 4 opposite offset pairs. Use 26 surviving coordinates modulo 26+1+8. Construct induced core first, test legality, deduplicate, apply blind seven-demand packing test. Independently test the canonical completion by offsets and verify successes by clique search. Scoped family, NOT unrestricted selection."""
import itertools,json,subprocess,sys,collections,igraph as ig
from ramsey_retention_slice import D,check
n,d=26,8;m=n+1+d;F=(1<<n)-1;P=D.parent;stats=collections.Counter();cand={}
for ds in itertools.combinations(range(1,(m+1)//2),d//2):
 J=set(ds)|{m-v for v in ds};C=sorted(set(range(m))-{0}-J);assert len(C)==n;stats['offset_sets']+=1
 a=[sum(1<<i for i,y in enumerate(C) if (y-x)%m in J) for x in C];
 if not check(a,F,3,8):continue
 stats['legal_offset_sets']+=1;G=ig.Graph(n,[(i,j) for i in range(n) for j in range(i) if a[i]>>j&1]);key=sum(1<<(max(i,j)*(max(i,j)-1)//2+min(i,j)) for i,j in G.permute_vertices(G.canonical_permutation()).get_edgelist());cand.setdefault(key,(a,[]))[1].append(ds)
keys=sorted(cand);rows=[' '.join(map(str,cand[key][0])) for key in keys];vs=list(map(int,subprocess.check_output([sys.argv[1],'7','8'],input='\n'.join(rows)+'\n',text=True).splitlines()));assert len(vs)==len(keys);rec=[]
for key,v in zip(keys,vs):
 a,dslist=cand[key];ok=[];tight=[]
 for ds in dslist:
  J=set(ds)|{m-x for x in ds};C=sorted(set(range(m))-{0}-J);targets=sorted(J);ss=[sum(1<<i for i,y in enumerate(C) if (y-x)%m in J) for x in targets];b=[sum(1<<i for i,y in enumerate(C) if (y-x)%m in J) for x in C]+[0]*(d+1)
  for j,s in enumerate(ss,n):
   b[j]=s|1<<(m-1);b[-1]|=1<<j
   for i in range(n):b[i]|=(s>>i&1)<<j
  if check(b,(1<<m)-1,3,9):assert v;ok.append(ds);tight.append(ss)
 rec.append(dict(key=hex(key),edges=key.bit_count(),offsets=dslist,packing=bool(v),successful=ok,supports=tight))
print(stats,'types',len(keys),'packing',sum(vs),'full',sum(bool(r['successful']) for r in rec));print([(r['edges'],r['successful'][:1]) for r in rec if r['packing']]);(P/'ramsey_gain26_offset_search.json').write_text(json.dumps(dict(stats=stats,rows=rec))+'\n')
